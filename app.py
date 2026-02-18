import streamlit as st
import plotly.express as px
import pandas as pd
import os
import re
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 0. CONFIGURATION
# -----------------------------------------------------------------------------
if not os.path.exists('.streamlit'):
    os.makedirs('.streamlit')

with open('.streamlit/config.toml', 'w') as f:
    f.write("""
[theme]
base="dark"
primaryColor="#D4AF37"
backgroundColor="#000000"
secondaryBackgroundColor="#0e0e0e"
textColor="#E0E0E0"
font="sans serif"
""")

# -----------------------------------------------------------------------------
# 1. UI & LUXURY CSS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%);
        font-family: 'Lato', sans-serif !important;
    }

    /* --- HEADER & METRICS --- */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 60px; text-align: center; background-color: #050505; min-width: 320px; }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 4px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 10px; font-weight: 300; }

    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: center; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.1); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Lato', sans-serif; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2.5rem; margin: 0; }

    /* --- TABS --- */
    div[data-baseweb="tab-list"] { justify-content: center !important; gap: 30px; margin-top: 20px; margin-bottom: 30px; border-bottom: 1px solid #222 !important; padding-bottom: 10px; }
    button[data-baseweb="tab"] { background-color: transparent !important; border: none !important; color: #666 !important; font-family: 'Lato', sans-serif !important; text-transform: uppercase !important; letter-spacing: 2px !important; font-size: 0.8rem !important; padding: 10px !important; }
    button[data-baseweb="tab"]:hover { color: #D4AF37 !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #D4AF37 !important; border-bottom: 2px solid #D4AF37 !important; font-weight: 700 !important; }

    /* --- HEADERS --- */
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; border-left: 3px solid #D4AF37; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }

    /* --- TRANSCRIPT --- */
    .transcript-box {
        max-width: 800px; margin: 0 auto; padding: 40px;
        background-color: #080808; border: 1px solid #222;
        color: #cccccc; font-family: 'Lato', sans-serif; font-size: 1rem; line-height: 1.8;
        text-align: justify; /* Justified text */
    }
    .transcript-box h3 { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; text-align: center; margin-top: 30px; border-bottom: 1px solid #333; padding-bottom: 10px; }
    .transcript-box b { color: #F0E68C; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }
    .transcript-box p { margin-bottom: 15px; }

    /* --- MOBILE --- */
    @media only screen and (max-width: 600px) {
        .header-inner { padding: 20px; min-width: auto; }
        .main-title { font-size: 1.5rem; letter-spacing: 2px; }
        .transcript-box { padding: 15px; text-align: left; }
    }

    /* --- FOOTER & CARDS --- */
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; letter-spacing: 1px; z-index: 999; text-transform: uppercase; font-family: 'Lato', sans-serif; }
    a { color: #D4AF37 !important; text-decoration: none !important; transition: 0.3s; }
    a:hover { color: #FFF !important; }
    
    .project-card { border:1px solid #222; background:#0a0a0a; padding:20px; transition:0.3s; display:flex; flex-direction:column; justify-content:space-between; height:100%; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:10px; background:#D4AF37; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; margin-bottom:10px; border-radius:2px; font-family:'Lato', sans-serif; }
    .btn-code { display:block; width:100%; padding:10px; border:1px solid #444; color:#888 !important; text-align:center; text-transform:uppercase; font-size:0.7rem; border-radius:2px; font-family:'Lato', sans-serif; }
    .btn-code:hover { border-color:#D4AF37; color:#D4AF37 !important; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DATA LOAD & CONFIG
# -----------------------------------------------------------------------------
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"

PODCAST_SCRIPT = {
    "I. INTRODUCTION: RECESSION GLAM": {
        "start_time": 0, "filter": "None",
        "desc": "Global market resilience ($593.2B). Analysis of 'The Lipstick Effect' evolving into 'The Fragrance Effect' as consumers seek affordable luxury."
    },
    "II. SCENT TREND: GOURMAND 2.0": {
        "start_time": 571, "filter": "Notes_Gourmand",
        "desc": "Case study: Sol de Janeiro. The shift from simple sugary scents to sophisticated, edible profiles (Scent-stacking strategy)."
    },
    "III. MARKET FOCUS: RUSSIA & DUHI": {
        "start_time": 1433, "filter": "Market_Russia",
        "desc": "Regional analysis: How import tariffs (35%) drove local production to 68% market share."
    }
}

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 3. HEADER & METRICS
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Fragrance Intelligence</h1>
                <div class="sub-title">Global Trends • Strategic Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.markdown('<div class="metric-box"><div class="metric-label">Global Beauty Market</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="metric-box"><div class="metric-label">Fragrance Growth</div><div class="metric-value">+16.2%</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="metric-box"><div class="metric-label">RU Local Production</div><div class="metric-value">68% Share</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 4. TABS
# -----------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "ECOSYSTEM"])

# --- TAB 1: BRIEFING ---
with tab1:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence</div>', unsafe_allow_html=True)
        selected_chapter = st.radio("Select Chapter:", list(PODCAST_SCRIPT.keys()))
        chapter_data = PODCAST_SCRIPT[selected_chapter]
        st.audio(AUDIO_URL, start_time=chapter_data["start_time"])
        st.markdown(f"""
            <div style="margin-top:20px; border-left:3px solid #D4AF37; padding:15px; background:rgba(212,175,55,0.05);">
                <p style="color:#D4AF37; font-size:0.6rem; text-transform:uppercase; margin-bottom:5px; font-weight:bold; letter-spacing:1px;">Key Narrative</p>
                <p style="color:#ccc; font-size:0.95rem; line-height:1.6; font-family:'Lato', sans-serif;">{chapter_data['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Data: {selected_chapter.split(':')[1]}</div>', unsafe_allow_html=True)
        if not df.empty:
            df_story = df.copy()
            if chapter_data["filter"] == "Notes_Gourmand" and 'top_notes' in df_story.columns:
                df_story = df_story[df_story['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar', case=False, na=False)]
            elif chapter_data["filter"] == "Market_Russia" and 'country' in df_story.columns:
                df_story = df_story[df_story['country'] == 'Russia']
            
            fig = px.scatter(
                df_story, x="year_clean", y="community_score", size="community_votes",
                color="segment", hover_name="name", template="plotly_dark",
                color_discrete_sequence=['#D4AF37', '#F0E68C', '#666']
            )
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=380, margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: ANALYTICS ---
with tab2:
    st.markdown('<div class="section-header">Market Clustering</div>', unsafe_allow_html=True)
    if not df.empty:
        filter_option = st.selectbox("Filter Data View:", ["Show All Global Data", "Focus: Gourmand 2.0 Notes", "Focus: Russian Market"])
        df_plot = df.copy()
        if filter_option == "Focus: Gourmand 2.0 Notes" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar', case=False, na=False)]
        elif filter_option == "Focus: Russian Market" and 'country' in df_plot.columns:
            df_plot = df_plot[df_plot['country'] == 'Russia']

        fig2 = px.scatter(
            df_plot, x="year_clean", y="community_score", size="community_votes",
            color="segment", hover_name="name", template="plotly_dark",
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#666']
        )
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450)
        st.plotly_chart(fig2, use_container_width=True)
        
        # --- FIX: USING GLOBAL 'df' TO ENSURE 50 ROWS APPEAR ---
        st.markdown('<div class="section-header" style="margin-top:30px;">Raw Data Inspection (50 Rows)</div>', unsafe_allow_html=True)
        st.markdown("<p style='color:#666; font-size:0.8rem;'>Displaying top 50 global records to demonstrate data structure.</p>", unsafe_allow_html=True)
        
        cols_to_show = ['name', 'segment', 'community_score']
        if 'top_notes' in df.columns: cols_to_show.append('top_notes')
        
        st.dataframe(
            df[cols_to_show].head(50), 
            height=400, 
            use_container_width=True,
            hide_index=True
        )

# --- TAB 3: ECOSYSTEM ---
with tab3:
    st.markdown('<div class="section-header">Project Ecosystem</div>', unsafe_allow_html=True)
    ecosystem_html = """
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
        <div class="project-card">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:10px;">🌍 Aromo Intelligence</div>
            <div style="color:#888; font-size:0.8rem; margin-bottom:20px; font-family:'Lato', sans-serif;">Global market scraping engine & forecasting dashboard.</div>
            <div style="margin-top:auto;">
                <a href="#" target="_blank" class="btn-launch">🚀 Launch App</a>
                <a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>
        <div class="project-card">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:10px;">🔍 Perfume Finder</div>
            <div style="color:#888; font-size:0.8rem; margin-bottom:20px; font-family:'Lato', sans-serif;">Consumer recommendation system for retail.</div>
            <div style="margin-top:auto;">
                <a href="#" target="_blank" class="btn-launch">🚀 Launch App</a>
                <a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>
        <div class="project-card">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:10px;">📊 Olfactory Insights</div>
            <div style="color:#888; font-size:0.8rem; margin-bottom:20px; font-family:'Lato', sans-serif;">Deep learning analysis of scent structures.</div>
            <div style="margin-top:auto;">
                <a href="https://github.com/MagdalenaRomaniecka/Olfactory-Insights" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>
        <div class="project-card">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:10px;">🧪 ScentSational LFS</div>
            <div style="color:#888; font-size:0.8rem; margin-bottom:20px; font-family:'Lato', sans-serif;">Backend engineering pipeline documentation.</div>
            <div style="margin-top:auto;">
                <a href="https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>
    </div>
    """
    st.markdown(ecosystem_html, unsafe_allow_html=True)
    st.write("")
    col_source, _ = st.columns([1,1])
    with col_source:
         st.markdown('<div class="section-header" style="margin-top:40px;">Intelligence Sources</div>', unsafe_allow_html=True)
         st.markdown("""
         * **[1] Euromonitor:** *Beauty and Personal Care 2025*
         * **[2] Givaudan:** *2023 Half Year Results*
         * **[3] Jutif:** *Academic Study on Men's Fragrances*
         * **[4] Russia Market Report:** *Forecast 2025-2035*
         """)
         st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/blob/main/Research_Whisper_AI.ipynb" class="btn-code" style="max-width:200px; margin-top:20px;">📄 Source Notebook</a>', unsafe_allow_html=True)

# --- FOOTER ---
st.write("")
st.write("")
st.markdown('<div class="section-header" style="text-align:center; border:none; margin-top:50px;">Strategic Transcript</div>', unsafe_allow_html=True)

try:
    with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
        # FIX: Clean bold markers from Markdown to HTML bold tags
        raw_text = f.read()
        clean_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', raw_text)
        
        # Split by empty lines to create paragraphs
        paragraphs = clean_text.split('\n\n')
        html_content = ""
        for p in paragraphs:
            if p.strip():
                if p.strip().startswith('#'):
                     html_content += f"<h3>{p.replace('#', '').strip()}</h3>"
                else:
                     html_content += f"<p>{p.strip()}</p>"
        
        st.markdown(f'<div class="transcript-box">{html_content}</div>', unsafe_allow_html=True)
except:
    st.info("Transcript unavailable.")

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • DEVELOPED BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)