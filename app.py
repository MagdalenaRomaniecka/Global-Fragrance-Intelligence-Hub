import streamlit as st
import plotly.express as px
import pandas as pd
import os
import re
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 0. CONFIGURATION: AUTO-GENERATE DARK THEME
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
# 1. UI & LUXURY CSS (MODERN EDITORIAL STYLE)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    /* IMPORT FONTS: Tenor Sans (Luxury Headers) & Lato (Clean Body) */
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* GLOBAL APP STYLING */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%);
        font-family: 'Lato', sans-serif !important;
    }

    /* --- HEADER --- */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 15px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 60px; text-align: center; background-color: #050505; min-width: 320px; }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 4px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 10px; font-weight: 300; }

    /* --- METRICS --- */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 15px; text-align: center; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.1); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Lato', sans-serif; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2.2rem; margin: 0; }

    /* --- TABS --- */
    div[data-baseweb="tab-list"] { justify-content: center !important; gap: 20px; margin-top: 10px; margin-bottom: 30px; border-bottom: 1px solid #222 !important; padding-bottom: 10px; flex-wrap: wrap; }
    button[data-baseweb="tab"] { background-color: transparent !important; border: none !important; color: #666 !important; font-family: 'Lato', sans-serif !important; text-transform: uppercase !important; letter-spacing: 1.5px !important; font-size: 0.75rem !important; padding: 10px !important; }
    button[data-baseweb="tab"]:hover { color: #D4AF37 !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #D4AF37 !important; border-bottom: 2px solid #D4AF37 !important; font-weight: 700 !important; }

    /* --- SECTION HEADERS --- */
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; border-left: 3px solid #D4AF37; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }

    /* --- TRANSCRIPT STYLING (EDITORIAL) --- */
    .transcript-box { font-family: 'Lato', sans-serif; font-size: 0.95rem; line-height: 1.8; text-align: justify; color: #cccccc; }
    .transcript-box h3 { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; text-align: center; margin-top: 20px; border-bottom: 1px solid #333; padding-bottom: 10px; font-weight: normal; }
    .transcript-box h2 { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; text-align: center; margin-top: 20px; border-bottom: 1px solid #D4AF37; padding-bottom: 10px; font-weight: normal; }
    .transcript-box b { color: #F0E68C; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; font-weight: 700; }
    .transcript-box p { margin-bottom: 15px; }

    /* --- MOBILE OPTIMIZATION --- */
    @media only screen and (max-width: 600px) {
        .header-inner { padding: 20px; min-width: auto; }
        .main-title { font-size: 1.5rem; letter-spacing: 2px; }
        .transcript-box { text-align: left; }
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
# 2. DATA LOAD & PODCAST SCRIPT
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

# ROW 1: General Market Metrics
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="metric-box"><div class="metric-label">Global Beauty Market</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="metric-box"><div class="metric-label">Fragrance Growth</div><div class="metric-value">+16.2%</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="metric-box"><div class="metric-label">RU Local Production</div><div class="metric-value">68% Share</div></div>', unsafe_allow_html=True)

# ROW 2: 2026 Outlook Metrics
c4, c5, c6 = st.columns(3)
c4.markdown('<div class="metric-box"><div class="metric-label">PL Global Econ Rank (PPP)</div><div class="metric-value">20th</div></div>', unsafe_allow_html=True)
c5.markdown('<div class="metric-box"><div class="metric-label">Scent-Stacking Boom</div><div class="metric-value">+125%</div></div>', unsafe_allow_html=True)
c6.markdown('<div class="metric-box"><div class="metric-label">Sol de Janeiro Share</div><div class="metric-value">31.6%</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 4. TABS
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "2026 OUTLOOK", "ECOSYSTEM"])

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
        # Analytics Filters including 2026 Trends
        filter_option = st.selectbox("Filter Data View:", [
            "Show All Global Data", 
            "Focus: Gourmand 2.0 Notes", 
            "Focus: Russian Market",
            "Focus: Functional Fragrance (2026 Trend)",
            "Focus: Vamp Romantic Notes (2026 Trend)"
        ])
        
        df_plot = df.copy()
        
        if filter_option == "Focus: Gourmand 2.0 Notes" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar', case=False, na=False)]
        elif filter_option == "Focus: Russian Market" and 'country' in df_plot.columns:
            df_plot = df_plot[df_plot['country'] == 'Russia']
        elif filter_option == "Focus: Functional Fragrance (2026 Trend)" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Water|Clean|Mineral|Musk|Green|Fresh', case=False, na=False)]
        elif filter_option == "Focus: Vamp Romantic Notes (2026 Trend)" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Plum|Cherry|Leather|Smoke|Incense|Dark', case=False, na=False)]

        fig2 = px.scatter(
            df_plot, x="year_clean", y="community_score", size="community_votes",
            color="segment", hover_name="name", template="plotly_dark",
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#666']
        )
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450)
        st.plotly_chart(fig2, use_container_width=True)
        
        st.write("")
        st.write("")
        with st.expander("🔎 INSPECT RAW DATA (TOP 50 GLOBAL RECORDS)"):
            st.markdown("<p style='color:#888; font-size:0.8rem; margin-bottom:10px;'>Displaying global dataset samples to ensure full visibility.</p>", unsafe_allow_html=True)
            cols_to_show = ['name', 'segment', 'community_score']
            if 'top_notes' in df.columns: cols_to_show.append('top_notes')
            
            st.dataframe(
                df[cols_to_show].head(50), 
                height=400, 
                use_container_width=True,
                hide_index=True
            )

# --- TAB 3: 2026 OUTLOOK ---
with tab3:
    st.markdown('<div class="section-header">Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    
    radar_html = """
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px; margin-bottom: 30px;">
        <div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #D4AF37;">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.2rem; margin-bottom:10px;">🧪 Functional Fragrance</div>
            <div style="color:#ccc; font-size:0.9rem; font-family:'Lato', sans-serif; line-height: 1.6;">
                Scent moves beyond aesthetics into neuroscience. Driven by post-pandemic wellness, 71% of consumers now expect fragrances to offer mood-enhancing benefits. Ingredients like <b>Givaudan's Cereboost</b> bridge the gap between perfumery and mental wellbeing.
            </div>
        </div>
        <div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #8B0000;">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.2rem; margin-bottom:10px;">🧛‍♀️ Vamp Romantic</div>
            <div style="color:#ccc; font-size:0.9rem; font-family:'Lato', sans-serif; line-height: 1.6;">
                A rebellion against 'Clean Girl' minimalism. Gen Z is driving a resurgence of dark, bold profiles. Key notes include <b>black cherry, smoked plum, incense, and leather</b>. This aesthetic blends gothic opulence with modern sensuality.
            </div>
        </div>
        <div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #F0E68C;">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.2rem; margin-bottom:10px;">📈 Macro Forces: Protectionism</div>
            <div style="color:#ccc; font-size:0.9rem; font-family:'Lato', sans-serif; line-height: 1.6;">
                Supply chains are adapting to aggressive US trade policies (tariffs). Capital is heavily concentrated in AI (Nvidia dominating S&P 500). Meanwhile, <b>Poland has advanced to the 20th largest global economy (PPP)</b>, creating a robust new market for luxury beauty.
            </div>
        </div>
    </div>
    """
    st.markdown(radar_html, unsafe_allow_html=True)


# --- TAB 4: ECOSYSTEM ---
with tab4:
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
         * **[1] Macro Update 2026:** *Market Analysis & Forecasts (2026 Update)*
         * **[2] Euromonitor:** *Beauty and Personal Care Report*
         * **[3] Givaudan:** *Half Year Results Transcript*
         * **[4] Russia Market Report:** *Forecast 2025-2035*
         """)
         st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/blob/main/Research_Whisper_AI.ipynb" class="btn-code" style="max-width:200px; margin-top:20px;">📄 Source Notebook</a>', unsafe_allow_html=True)

# --- FOOTER, TRANSCRIPT & MACRO REPORT (DUAL EXPANDERS) ---
st.write("")
st.write("")

col_doc1, col_doc2 = st.columns(2)

with col_doc1:
    with st.expander("📄 READ PODCAST TRANSCRIPT"):
        try:
            with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
                raw_text = f.read()
                clean_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', raw_text)
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
            st.info("Transcript unavailable. Please ensure 'podcast_transcript.md' is in the directory.")

with col_doc2:
    with st.expander("📈 READ 2026 MACRO REPORT"):
        try:
            with open('macro_report_2026.md', 'r', encoding='utf-8') as f:
                raw_macro = f.read()
                clean_macro = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', raw_macro)
                paragraphs_macro = clean_macro.split('\n\n')
                html_macro = ""
                for p in paragraphs_macro:
                    if p.strip():
                        if p.strip().startswith('## '):
                             html_macro += f"<h3 style='color:#D4AF37; margin-top:20px; border-bottom:1px solid #333; padding-bottom:10px;'>{p.replace('##', '').strip()}</h3>"
                        elif p.strip().startswith('# '):
                             html_macro += f"<h2 style='color:#F0E68C; text-align:center;'>{p.replace('#', '').strip()}</h2>"
                        else:
                             html_macro += f"<p style='margin-bottom:10px;'>{p.strip()}</p>"
                
                st.markdown(f'<div class="transcript-box">{html_macro}</div>', unsafe_allow_html=True)
        except:
            st.info("Macro report unavailable. Please ensure 'macro_report_2026.md' is in the directory.")

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • DEVELOPED BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)