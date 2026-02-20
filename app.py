import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 0. CONFIGURATION & LUXURY THEME
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

    /* Elegant Golden Header */
    .header-wrapper { display: flex; justify-content: center; padding: 20px 0 10px 0; }
    .header-inner { 
        border: 1px solid #D4AF37; 
        padding: 25px 60px; 
        text-align: center; 
        background-color: #050505; 
    }
    .main-title { 
        font-family: 'Tenor Sans', sans-serif; 
        color: #D4AF37; 
        font-size: 2.2rem; 
        text-transform: uppercase; 
        letter-spacing: 5px; 
        margin: 0; 
    }
    
    /* Section Headers */
    .section-header { 
        color: #D4AF37; 
        font-family: 'Tenor Sans', sans-serif; 
        font-size: 1.1rem; 
        border-left: 3px solid #D4AF37; 
        padding-left: 15px; 
        margin-bottom: 20px; 
        text-transform: uppercase; 
        letter-spacing: 1px;
    }

    /* Intelligence Dossier Box - Centered & Elegant */
    .dossier-container {
        font-family: 'Lato', sans-serif;
        color: #cccccc;
        background: #080808;
        padding: 40px;
        border: 1px solid #222;
        max-width: 900px;
        margin: 0 auto;
        line-height: 1.8;
    }
    .dossier-container h1, .dossier-container h2 {
        text-align: center;
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 30px;
    }
    .dossier-container p {
        text-align: justify;
        margin-bottom: 20px;
    }
    .dossier-container strong {
        color: #F0E68C;
        font-weight: 700;
    }

    /* Project Cards */
    .project-card {
        border: 1px solid #222;
        background: #0a0a0a;
        padding: 20px;
        transition: 0.3s;
        height: 100%;
    }
    .project-card:hover { border-color: #D4AF37; }

    .footer { 
        text-align: center; 
        padding: 40px 0; 
        color: #444; 
        font-size: 0.65rem; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
    }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 1. TOP SECTION: BRANDING & EXECUTIVE SUMMARY
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-inner">
            <h1 class="main-title">Fragrance Intelligence</h1>
            <div style="color:#888; font-size:0.75rem; letter-spacing:3px; margin-top:5px;">
                ATELIER DATA TERMINAL • STRATEGIC FORECAST 2026
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Executive Summary for Clarity
st.markdown("""
    <div style="max-width: 800px; margin: 0 auto; text-align: center; padding: 20px 0 40px 0;">
        <p style="color: #666; font-size: 0.9rem; line-height: 1.6;">
            Welcome to the <b>Fragrance Intelligence Hub</b>. This terminal serves as a strategic bridge between macroeconomic data and the olfactory market. 
            By synthesizing AI-driven analytics, supply chain shifts, and consumer sentiment, we provide a high-fidelity forecast for the luxury fragrance ecosystem 
            through 2026 and beyond. Use the tabs below to explore briefings, datasets, and future radars.
        </p>
    </div>
""", unsafe_allow_html=True)

# Compact Metrics
m1, m2, m3, m4, m5, m6 = st.columns(6)
metrics = [
    ("Market Cap", "$593.2B"), ("CAGR", "+16.2%"), ("Local RU", "68%"),
    ("Poland PPP", "20th"), ("Scent Stacking", "+125%"), ("SdJ Share", "31.6%")
]
for col, (l, v) in zip([m1, m2, m3, m4, m5, m6], metrics):
    col.markdown(f'<div style="text-align:center;"><div style="color:#444; font-size:0.6rem; text-transform:uppercase;">{l}</div><div style="color:#D4AF37; font-size:1.1rem;">{v}</div></div>', unsafe_allow_html=True)

st.write("---")

# -----------------------------------------------------------------------------
# 2. NAVIGATION
# -----------------------------------------------------------------------------
tab_briefing, tab_analytics, tab_outlook, tab_ecosystem = st.tabs([
    "STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "2026 TREND RADAR", "ECOSYSTEM"
])

# Global Episode Choice
with tab_briefing:
    st.write("")
    selected_episode = st.radio(
        "Select Dossier Content:", 
        ["EPISODE 01: RECESSION GLAM", "EPISODE 02: 2026 MACRO OUTLOOK"],
        horizontal=True
    )
    st.write("")

    if "EPISODE 01" in selected_episode:
        audio_src = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"
        transcript_path = "podcast_transcript.md"
        viz_title = "2025 Market Dynamics"
        has_macro = False
    else:
        audio_src = "podcast_2026.mp3"
        transcript_path = "podcast_transcript_2026.md"
        viz_title = "2026 Macro Projections"
        has_macro = True

    c_left, c_right = st.columns([1, 1.5], gap="large")
    with c_left:
        st.markdown('<div class="section-header">Audio Briefing</div>', unsafe_allow_html=True)
        st.audio(audio_src)
        st.info("Listen to the expert analysis regarding current market shifts and consumer behavior.")

    with c_right:
        st.markdown(f'<div class="section-header">Live Data: {viz_title}</div>', unsafe_allow_html=True)
        if not df.empty:
            fig = px.scatter(df.head(100), x="year_clean", y="community_score", size="community_votes", color="segment", template="plotly_dark", color_discrete_sequence=['#D4AF37', '#666'])
            fig.update_layout(height=300, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    st.markdown('<div class="section-header">Intelligence Dossier</div>', unsafe_allow_html=True)
    
    # Elegant formatting for the text content
    if has_macro:
        d_tab1, d_tab2 = st.tabs(["📝 Full Transcript", "📈 2026 Macro Report"])
        with d_tab1:
            try:
                with open(transcript_path, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="dossier-container">{f.read()}</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
        with d_tab2:
            try:
                with open('macro_report_2026.md', 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="dossier-container">{f.read()}</div>', unsafe_allow_html=True)
            except: st.info("Macro Report file not found.")
    else:
        try:
            with open(transcript_path, 'r', encoding='utf-8') as f:
                st.markdown(f'<div class="dossier-container">{f.read()}</div>', unsafe_allow_html=True)
        except: st.error("Transcript file missing.")

# -----------------------------------------------------------------------------
# 3. FILLING THE EMPTY TABS
# -----------------------------------------------------------------------------
with tab_analytics:
    st.markdown('<div class="section-header">Market Clustering & Performance</div>', unsafe_allow_html=True)
    if not df.empty:
        st.write("Filter the global fragrance dataset to identify emerging clusters.")
        f_opt = st.selectbox("Market Lens:", ["All Data", "Focus: Gourmand", "Focus: Functional"])
        st.dataframe(df.head(100), use_container_width=True)
    else:
        st.info("Connect to data source to view analytics.")

with tab_outlook:
    st.markdown('<div class="section-header">Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    # 
    st.markdown("""
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px;">
        <div class="project-card">
            <h3 style="color:#D4AF37;">🧪 Functional Fragrance</h3>
            <p style="color:#888; font-size:0.9rem;">Scent as a neuro-modulator. 71% of consumers now expect fragrances to offer mood-enhancing benefits via biotech-derived molecules.</p>
        </div>
        <div class="project-card">
            <h3 style="color:#D4AF37;">🧛‍♀️ Vamp Romantic</h3>
            <p style="color:#888; font-size:0.9rem;">The rebellion against minimalism. Bold, dark profiles like black cherry, leather, and smoked plum dominate Gen Z preference.</p>
        </div>
        <div class="project-card">
            <h3 style="color:#D4AF37;">📈 Macro Forces</h3>
            <p style="color:#888; font-size:0.9rem;">Nvidia's $5T cap and trade protectionism (tariffs) are creating a pressure cooker for supply chain R&D.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab_ecosystem:
    st.markdown('<div class="section-header">Project Ecosystem</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
        <div class="project-card">
            <h4 style="color:#D4AF37;">🌍 Aromo Intelligence</h4>
            <p style="color:#666; font-size:0.8rem;">Global market scraping engine and strategic dashboard.</p>
            <a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" target="_blank" style="color:#D4AF37; text-decoration:none; font-weight:bold;">VIEW CODE</a>
        </div>
        <div class="project-card">
            <h4 style="color:#D4AF37;">🔍 Perfume Finder</h4>
            <p style="color:#666; font-size:0.8rem;">Personalized recommendation system based on olfactory notes.</p>
            <a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" target="_blank" style="color:#D4AF37; text-decoration:none; font-weight:bold;">VIEW CODE</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • MAGDALENA ROMANIECKA 2026</div>', unsafe_allow_html=True)