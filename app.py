import streamlit as st
import plotly.express as px
import pandas as pd
import os
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
# 1. UI & LUXURY ATELIER CSS (MODERN FASHION STYLE)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    /* IMPORT FONTS: Tenor Sans (Luxury Headers) & Lato (Clean Body) */
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* GLOBAL APP STYLING */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 100%);
        font-family: 'Lato', sans-serif !important;
    }

    /* --- 1. FRAMED HEADER (CLEAN & SHARP) --- */
    .main-header-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
        margin-bottom: 30px;
    }
    .main-header-box {
        border: 1px solid #D4AF37; 
        padding: 5px;
        display: inline-block;
        max-width: 95%;
    }
    .main-header-inner {
        border: 1px solid #D4AF37; 
        padding: 20px 50px;
        text-align: center;
        background-color: #050505;
    }
    .main-header-text {
        font-family: 'Tenor Sans', sans-serif; /* NOWA CZCIONKA */
        color: #D4AF37;
        font-size: 2.2rem;
        text-transform: uppercase;
        letter-spacing: 4px; /* Szerokie odstępy dla elegancji */
        margin: 0;
    }
    .sub-header-text {
        font-family: 'Lato', sans-serif;
        color: #888;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-top: 10px;
        font-weight: 300;
    }

    /* --- MOBILE OPTIMIZATION --- */
    @media only screen and (max-width: 600px) {
        .main-header-inner { padding: 15px 10px; }
        .main-header-text { font-size: 1.5rem; letter-spacing: 2px; }
        .sub-header-text { font-size: 0.6rem; letter-spacing: 1px; }
        .gold-metric { padding: 10px; }
        .metric-value { font-size: 1.8rem !important; }
    }

    /* --- 2. TABS (MINIMALIST) --- */
    div[data-baseweb="tab-list"] {
        justify-content: center !important;
        gap: 15px;
        margin-bottom: 25px;
        border-bottom: none !important;
    }
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        border: 1px solid #333 !important;
        color: #888 !important;
        border-radius: 0px !important;
        padding: 8px 25px !important;
        font-family: 'Lato', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-size: 0.75rem !important;
        transition: 0.3s;
    }
    button[data-baseweb="tab"]:hover {
        border-color: #D4AF37 !important;
        color: #D4AF37 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        color: #000 !important;
        font-weight: 700 !important;
    }

    /* --- 3. SECTION HEADERS --- */
    .section-header {
        border-left: 3px solid #D4AF37;
        padding-left: 15px;
        margin-bottom: 20px;
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif; /* SPÓJNOŚĆ */
        font-size: 1.4rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* --- METRICS --- */
    .gold-metric {
        background-color: rgba(20, 20, 20, 0.4);
        border: 1px solid #333;
        padding: 25px;
        text-align: center;
        transition: 0.3s;
    }
    .gold-metric:hover { border-color: #D4AF37; background-color: rgba(212, 175, 55, 0.05); }
    .metric-label { color: #888; font-family: 'Lato', sans-serif; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; }
    .metric-value { 
        font-family: 'Tenor Sans', sans-serif; 
        font-size: 2.5rem; 
        color: #F0E68C; 
    }

    /* --- OTHERS --- */
    .transcript-box {
        font-family: 'Lato', sans-serif; font-size: 0.95rem; line-height: 1.8; color: #ccc;
        text-align: justify; max-width: 800px; margin: 0 auto; padding: 30px;
        background-color: #080808; border: 1px solid #222;
    }
    
    /* Tables & Dropdowns */
    div[data-baseweb="popover"], div[data-baseweb="popover"] > div { background-color: #000 !important; border: 1px solid #444 !important; }
    ul[data-baseweb="menu"] { background-color: #000 !important; }
    li[data-baseweb="option"] { color: #ccc !important; font-family: 'Lato', sans-serif; }
    li[data-baseweb="option"]:hover, li[aria-selected="true"] { background-color: #D4AF37 !important; color: #000 !important; }
    
    .luxury-table { width: 100%; border-collapse: collapse; background-color: #0e0e0e; color: #ccc; font-family: 'Lato', sans-serif; font-size: 0.85rem; }
    .luxury-table th { background-color: #151515; color: #D4AF37; font-family: 'Tenor Sans', sans-serif; padding: 15px; border-bottom: 1px solid #444; letter-spacing: 1px;}
    .luxury-table td { padding: 12px; border-bottom: 1px solid #222; }
    
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; letter-spacing: 1px; z-index: 999; text-transform: uppercase; font-family: 'Lato', sans-serif; }
    a { color: #D4AF37 !important; text-decoration: none !important; transition: 0.3s; }
    a:hover { color: #FFF !important; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DATA LOAD & PODCAST SCRIPT
# -----------------------------------------------------------------------------
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"

PODCAST_SCRIPT = {
    "I. INTRODUCTION: RECESSION GLAM": {
        "start_time": 0, "filter": "None",
        "desc": "Global beauty market resilience ($593B). Analysis of 'The Lipstick Effect' evolving into 'The Fragrance Effect'."
    },
    "II. SCENT TREND: GOURMAND 2.0": {
        "start_time": 571, "filter": "Notes_Gourmand",
        "desc": "Case study: Sol de Janeiro. The shift from simple sugary scents to sophisticated, edible profiles (Scent-stacking)."
    },
    "III. MARKET FOCUS: RUSSIA & DUHI": {
        "start_time": 1433, "filter": "Market_Russia",
        "desc": "Regional analysis: How import tariffs (35%) drove local production to 68% market share."
    }
}

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 3. HEADER (TENOR SANS - CLEAN LUXURY)
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="main-header-container">
        <div class="main-header-box">
            <div class="main-header-inner">
                <h1 class="main-header-text">Fragrance Intelligence</h1>
                <div class="sub-header-text">Global Trends • Market Sentiment • Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# METRICS
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="gold-metric"><div class="metric-label">Global Beauty Market</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="gold-metric"><div class="metric-label">Fragrance Growth</div><div class="metric-value">+16.2%</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="gold-metric"><div class="metric-label">RU Local Production</div><div class="metric-value">68% Share</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 4. TABS
# -----------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "ECOSYSTEM"])

# --- TAB 1: STORY MODE ---
with tab1:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">🎧 AI-Synthesized Market Report</div>', unsafe_allow_html=True)
        
        selected_chapter = st.radio("Select Chapter to Navigate Audio:", list(PODCAST_SCRIPT.keys()))
        chapter_data = PODCAST_SCRIPT[selected_chapter]
        st.audio(AUDIO_URL, start_time=chapter_data["start_time"])
        
        st.markdown(f"""
            <div style="border: 1px solid #222; padding: 20px; background: #0a0a0a; margin-top: 15px; border-left: 3px solid #D4AF37;">
                <p style="color:#D4AF37; font-size:0.65rem; letter-spacing:2px; font-weight:700; text-transform:uppercase; margin-bottom:8px; font-family:'Lato', sans-serif;">Key Narrative</p>
                <p style="color:#ccc; font-size:0.95rem; line-height:1.6; font-family:'Lato', sans-serif;">{chapter_data['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">📉 Visualization: {selected_chapter.split(':')[1]}</div>', unsafe_allow_html=True)
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
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=400)
            st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: ANALYST MODE ---
with tab2:
    st.markdown('<div class="section-header">📈 Market Sentiment & Clustering</div>', unsafe_allow_html=True)
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
        
        with st.expander("🔎 INSPECT RAW DATA (TOP 50 ROWS)"):
            cols_to_show = ['name', 'segment', 'community_score']
            if 'top_notes' in df_plot.columns: cols_to_show.append('top_notes')
            html_table = df_plot[cols_to_show].head(50).to_html(classes='luxury-table', index=False, border=0)
            st.markdown(html_table, unsafe_allow_html=True)

# --- TAB 3: METHODOLOGY & ECOSYSTEM ---
with tab3:
    st.markdown('<div class="section-header">🧩 The Fragrance Data Ecosystem</div>', unsafe_allow_html=True)
    st.markdown("This hub serves as the central command for my deployed applications:")
    
    ecosystem_html = """
    <style>
    .project-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 20px; }
    .project-card { background-color: #0e0e0e !important; border: 1px solid #222 !important; padding: 20px; border-radius: 2px; transition: 0.3s; }
    .project-card:hover { border-color: #D4AF37 !important; }
    .project-title { color: #D4AF37 !important; font-family: 'Tenor Sans', sans-serif; font-size: 1.1rem; margin-bottom: 5px; font-weight: 400; text-transform: uppercase; letter-spacing: 1px; }
    .project-desc { color: #888 !important; font-size: 0.8rem; margin-bottom: 20px; min-height: 40px; font-family: 'Lato', sans-serif; line-height: 1.4; }
    .btn-row { display: flex; gap: 10px; }
    .btn-launch { flex: 1; background-color: #D4AF37 !important; color: #000 !important; padding: 8px; text-align: center; font-weight: 600; text-transform: uppercase; font-size: 0.7rem; border-radius: 2px; text-decoration: none !important; font-family: 'Lato', sans-serif; letter-spacing: 1px; }
    .btn-launch:hover { background-color: #F0E68C !important; }
    .btn-code { flex: 1; background-color: transparent !important; color: #888 !important; border: 1px solid #444 !important; padding: 8px; text-align: center; text-transform: uppercase; font-size: 0.7rem; border-radius: 2px; text-decoration: none !important; font-family: 'Lato', sans-serif; letter-spacing: 1px; }
    .btn-code:hover { border-color: #D4AF37 !important; color: #D4AF37 !important; }
    </style>
    
    <div class="project-container">
        <div class="project-card">
            <div class="project-title">🌍 Aromo Intelligence</div>
            <div class="project-desc">Global market scraping engine & trend forecasting dashboard covering 50k+ products.</div>
            <div class="btn-row">
                <a href="#" target="_blank" class="btn-launch">🚀 Launch App</a>
                <a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>
        <div class="project-card">
            <div class="project-title">🔍 Perfume Finder</div>
            <div class="project-desc">Consumer-facing recommendation system using similarity algorithms for retail.</div>
            <div class="btn-row">
                <a href="#" target="_blank" class="btn-launch">🚀 Launch App</a>
                <a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>
        <div class="project-card">
            <div class="project-title">📊 Olfactory Insights</div>
            <div class="project-desc">Deep learning analysis of scent structures and chemical composition mapping.</div>
            <div class="btn-row"><a href="https://github.com/MagdalenaRomaniecka/Olfactory-Insights" target="_blank" class="btn-code" style="flex:2">💻 View Code</a></div>
        </div>
        <div class="project-card">
            <div class="project-title">🧪 ScentSational LFS</div>
            <div class="project-desc">Backend engineering pipeline & Large File Storage documentation.</div>
            <div class="btn-row"><a href="https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS" target="_blank" class="btn-code" style="flex:2">💻 View Code</a></div>
        </div>
    </div>
    """
    st.markdown(ecosystem_html, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    col_source, _ = st.columns([1,1])
    with col_source:
         st.markdown('<div class="section-header">📚 Primary Intelligence Sources</div>', unsafe_allow_html=True)
         st.markdown("""
         * **[1] Euromonitor International:** *Beauty and Personal Care 2025 Edition* (Global Market Valuation: $593B).
         * **[2] Givaudan:** *2023 Half Year Results* (Fine Fragrance Growth +16.2%, Myrissi AI).
         * **[3] Academic Study (Jutif):** *Unraveling Men's Fragrance Preferences on Online Marketplaces* (ML Analysis).
         * **[4] Russia Perfume Market Report:** *Size, Share & Forecast 2025-2035* (Local Production Share: 68%).
         * **[5] Sol de Janeiro:** *Best Selling Body Mists Analysis* (Gourmand 2.0 Trends).
         """)
         st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/blob/main/Research_Whisper_AI.ipynb" class="repo-btn" style="border: 1px solid #444; color: #888; padding: 10px; display: block; text-align: center; font-size: 0.8rem;">📄 View Research Notebook (Colab)</a>', unsafe_allow_html=True)

# --- FOOTER & TRANSCRIPT ---
st.write("")
st.write("")

with st.expander("📄 READ FULL STRATEGIC TRANSCRIPT"):
    try:
        with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
            content = f.read()
            st.markdown(f'<div class="transcript-box">{content}</div>', unsafe_allow_html=True)
    except:
        st.info("Transcript unavailable.")

st.markdown("""
    <div class="footer">
        DATA SOURCE: EUROMONITOR, GIVAUDAN, ACADEMIC STUDIES & NOTEBOOKLM INSIGHTS <br>
        © 2026 DEVELOPED BY <a href="https://github.com/MagdalenaRomaniecka" target="_blank">MAGDALENA ROMANIECKA</a>
    </div>
""", unsafe_allow_html=True)