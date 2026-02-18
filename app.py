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
font="serif"
""")

# -----------------------------------------------------------------------------
# 1. UI & LUXURY ATELIER CSS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    /* IMPORT FONTS: Playfair Display (Italic support) & Montserrat */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Montserrat:wght@300;400;500;600&display=swap');

    /* GLOBAL APP STYLING */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000000 100%);
        font-family: 'Montserrat', sans-serif !important;
    }

    /* --- TYPOGRAPHY: ELEGANT & SLANTED --- */
    h1 {
        font-family: 'Playfair Display', serif !important;
        font-style: italic; /* <--- POCHYŁA ELEGANCJA */
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 4.2rem !important;
        font-weight: 400;
        margin-top: 10px;
        letter-spacing: 1px;
        padding-bottom: 15px;
        text-shadow: 0px 4px 20px rgba(0,0,0,0.8);
    }

    h3 {
        font-family: 'Playfair Display', serif !important;
        font-style: italic;
        color: #D4AF37 !important;
        font-weight: 400;
        letter-spacing: 1px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        padding-bottom: 5px;
        margin-top: 30px;
        display: inline-block;
    }

    .sub-header {
        color: #888;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.85rem !important;
        letter-spacing: 4px;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 60px;
        border-top: 1px solid rgba(212, 175, 55, 0.2);
        border-bottom: 1px solid rgba(212, 175, 55, 0.2);
        padding: 15px 0;
        width: 70%;
        margin-left: auto;
        margin-right: auto;
    }

    /* --- METRICS --- */
    .gold-metric {
        background-color: rgba(10, 10, 10, 0.6);
        border: 1px solid #222;
        padding: 30px;
        text-align: center;
        position: relative;
        transition: 0.3s;
    }
    .gold-metric:hover { border-color: #D4AF37; background-color: rgba(212, 175, 55, 0.05); }
    
    .metric-label { 
        color: #999; 
        font-family: 'Montserrat', sans-serif; 
        font-size: 0.7rem; 
        text-transform: uppercase; 
        letter-spacing: 3px; 
        margin-bottom: 10px; 
    }
    .metric-value { 
        font-family: 'Playfair Display', serif; 
        font-style: italic; /* <--- POCHYŁA LICZBA */
        font-size: 3rem; 
        color: #F0E68C; 
        background: linear-gradient(to bottom, #FCF6BA, #AA771C); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
    }

    /* --- TRANSCRIPT STYLING (EDITORIAL LOOK) --- */
    .transcript-box {
        font-family: 'Playfair Display', serif;
        font-size: 1.15rem;
        line-height: 1.8;
        color: #d0d0d0;
        text-align: justify;
        max-width: 800px;
        margin: 0 auto;
        padding: 50px;
        background-color: #050505;
        border: 1px solid #222;
        border-radius: 2px;
        box-shadow: 0 0 50px rgba(0,0,0,0.8);
    }
    .transcript-box h1, .transcript-box h2 {
        text-align: center;
        color: #D4AF37;
        font-style: italic;
        margin-top: 40px;
        margin-bottom: 25px;
        font-weight: 400;
    }
    .transcript-box p {
        margin-bottom: 20px;
        text-indent: 40px; /* Akapitowe wcięcie */
    }
    .transcript-box strong {
        color: #F0E68C;
        font-weight: normal;
    }

    /* --- TABLES & DROPDOWNS --- */
    .luxury-table { width: 100%; border-collapse: collapse; background-color: #0e0e0e; color: #ccc; font-family: 'Montserrat', sans-serif; font-size: 0.85rem; }
    .luxury-table th { background-color: #1a1a1a; color: #D4AF37; font-family: 'Playfair Display', serif; font-style: italic; padding: 15px; border-bottom: 1px solid #D4AF37; }
    .luxury-table td { padding: 12px; border-bottom: 1px solid #333; }
    .luxury-table tr:hover { background-color: rgba(212, 175, 55, 0.05); }

    div[data-baseweb="popover"], div[data-baseweb="popover"] > div { background-color: #000 !important; border: 1px solid #D4AF37 !important; }
    ul[data-baseweb="menu"] { background-color: #000 !important; }
    li[data-baseweb="option"] { color: #ccc !important; }
    li[data-baseweb="option"]:hover, li[aria-selected="true"] { background-color: #D4AF37 !important; color: #000 !important; }

    /* --- ECOSYSTEM CARDS --- */
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #555; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; letter-spacing: 2px; z-index: 999; text-transform: uppercase; }
    a { color: #D4AF37 !important; text-decoration: none !important; transition: 0.3s; }
    a:hover { color: #FFF !important; text-shadow: 0 0 10px #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DATA LOAD & PODCAST SCRIPT
# -----------------------------------------------------------------------------
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"

PODCAST_SCRIPT = {
    "I. INTRODUCTION: RECESSION GLAM": {
        "start_time": 0, "filter": "None",
        "desc": "Global beauty market resilience ($593B). Analysis of 'The Lipstick Effect' evolving into 'The Fragrance Effect' as consumers seek affordable luxury."
    },
    "II. SCENT TREND: GOURMAND 2.0": {
        "start_time": 571, "filter": "Notes_Gourmand",
        "desc": "Case study: Sol de Janeiro. The shift from simple sugary scents to sophisticated, edible profiles (Scent-stacking strategy)."
    },
    "III. MARKET FOCUS: RUSSIA & DUHI": {
        "start_time": 1433, "filter": "Market_Russia",
        "desc": "Regional analysis: How import tariffs (35%) drove local production to 68% market share. High-concentration preferences."
    }
}

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 3. HEADER & METRICS
# -----------------------------------------------------------------------------
st.markdown("<h1>Fragrance Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Global Trends • Market Sentiment • Strategic Forecast 2026</div>", unsafe_allow_html=True)

# UPDATED METRICS - PRECISE LABELS
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="gold-metric"><div class="metric-label">Global Beauty Market</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="gold-metric"><div class="metric-label">Fragrance Growth</div><div class="metric-value">+16.2%</div></div>', unsafe_allow_html=True) # Zmienione na 16.2% z raportu Givaudan LFL
c3.markdown('<div class="gold-metric"><div class="metric-label">RU Local Production</div><div class="metric-value">68% Share</div></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------------------------------
# 4. TABS
# -----------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🎙️ STRATEGIC BRIEFING", "📊 DEEP DIVE ANALYTICS", "🔗 METHODOLOGY & ECOSYSTEM"])

# --- TAB 1: STORY MODE ---
with tab1:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown("### 🎧 AI-Synthesized Market Report")
        selected_chapter = st.radio("Select Chapter to Navigate Audio:", list(PODCAST_SCRIPT.keys()))
        chapter_data = PODCAST_SCRIPT[selected_chapter]
        st.audio(AUDIO_URL, start_time=chapter_data["start_time"])
        st.markdown(f"""
            <div style="border-left: 2px solid #D4AF37; padding: 20px; background: rgba(20,20,20,0.5); margin-top: 20px;">
                <p style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; font-weight:bold; text-transform:uppercase;">Key Narrative</p>
                <p style="font-style:italic; color:#e0e0e0; font-size:1.1rem; line-height:1.6; font-family:'Playfair Display', serif;">"{chapter_data['desc']}"</p>
            </div>
        """, unsafe_allow_html=True)

    with col_viz:
        st.markdown(f"### 📉 Data Visualization: {selected_chapter.split(':')[1]}")
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
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Montserrat", height=450)
            st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: ANALYST MODE ---
with tab2:
    st.markdown("### 📈 Deep Dive Analytics")
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
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Montserrat", height=500)
        st.plotly_chart(fig2, use_container_width=True)
        
        with st.expander("🔎 INSPECT RAW DATA (TOP 50 ROWS)"):
            cols_to_show = ['name', 'segment', 'community_score']
            if 'top_notes' in df_plot.columns: cols_to_show.append('top_notes')
            html_table = df_plot[cols_to_show].head(50).to_html(classes='luxury-table', index=False, border=0)
            st.markdown(html_table, unsafe_allow_html=True)

# --- TAB 3: METHODOLOGY & ECOSYSTEM ---
with tab3:
    st.markdown("### 🧩 The Fragrance Data Ecosystem")
    st.markdown("This hub serves as the central command for my deployed applications:")
    
    # KARTY PROJEKTÓW
    ecosystem_html = """
    <style>
    .project-container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
    .project-card { background-color: #0e0e0e !important; border: 1px solid #333 !important; padding: 20px; border-radius: 4px; transition: 0.3s; }
    .project-card:hover { border-color: #D4AF37 !important; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1); }
    .project-title { color: #D4AF37 !important; font-family: 'Playfair Display', serif; font-style:italic; font-size: 1.3rem; margin-bottom: 5px; font-weight: 400; }
    .project-desc { color: #888 !important; font-size: 0.8rem; margin-bottom: 20px; min-height: 40px; font-family: 'Montserrat', sans-serif; }
    .btn-row { display: flex; gap: 10px; }
    .btn-launch { flex: 1; background-color: #D4AF37 !important; color: #000 !important; padding: 10px; text-align: center; font-weight: bold; text-transform: uppercase; font-size: 0.75rem; border-radius: 2px; text-decoration: none !important; font-family: 'Montserrat', sans-serif; }
    .btn-launch:hover { background-color: #F0E68C !important; }
    .btn-code { flex: 1; background-color: transparent !important; color: #D4AF37 !important; border: 1px solid #444 !important; padding: 10px; text-align: center; text-transform: uppercase; font-size: 0.75rem; border-radius: 2px; text-decoration: none !important; font-family: 'Montserrat', sans-serif;}
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
    
    # ŹRÓDŁA - FINALNA PRECYZJA (Z pliku DOCX)
    col_source, _ = st.columns([1,1])
    with col_source:
         st.markdown("### 📚 Primary Intelligence Sources")
         st.markdown("""
         * **[1] Euromonitor International:** *Beauty and Personal Care 2025 Edition* (Global Market Valuation: $593B).
         * **[2] Givaudan:** *2023 Half Year Results & Integrated Report* (Fine Fragrance Growth +16.2%, Myrissi AI).
         * **[3] Academic Study (Jutif):** *Unraveling Men's Fragrance Preferences on Online Marketplaces* (ML Analysis).
         * **[4] Russia Perfume Market Report:** *Size, Share & Forecast 2025-2035* (Local Production Share: 68%).
         * **[5] Sol de Janeiro:** *Best Selling Body Mists Analysis* (Gourmand 2.0 Trends).
         """)
         st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/blob/main/Research_Whisper_AI.ipynb" class="repo-btn" style="border: 1px solid #D4AF37; padding: 10px; display: block; text-align: center;"><b>📄 View Research Notebook (Colab)</b></a>', unsafe_allow_html=True)

# --- FOOTER & TRANSCRIPT ---
st.write("")
st.write("")

# TRANSKRYPCJA W STYLU "MAGAZINE" (Center + Justify)
with st.expander("📄 READ FULL STRATEGIC TRANSCRIPT"):
    try:
        with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
            content = f.read()
            # Wrap in the custom styled div
            st.markdown(f'<div class="transcript-box">{content}</div>', unsafe_allow_html=True)
    except:
        st.info("Transcript unavailable.")

st.markdown("""
    <div class="footer">
        DATA SOURCE: EUROMONITOR, GIVAUDAN, ACADEMIC STUDIES & NOTEBOOKLM INSIGHTS <br>
        © 2026 DEVELOPED BY <a href="https://github.com/MagdalenaRomaniecka" target="_blank">MAGDALENA ROMANIECKA</a>
    </div>
""", unsafe_allow_html=True)