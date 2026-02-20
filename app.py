import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 0. CONFIGURATION & FULL DARK THEME RECOVERY
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* Global styling */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%);
        font-family: 'Lato', sans-serif !important; 
    }

    /* Elegant Golden Header */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; }
    .header-inner { 
        border: 1px solid #D4AF37; 
        padding: 25px 60px; 
        text-align: center; 
        background-color: #050505; 
        min-width: 350px;
    }
    .main-title { 
        font-family: 'Tenor Sans', sans-serif; 
        color: #D4AF37; 
        font-size: 2.2rem; 
        text-transform: uppercase; 
        letter-spacing: 5px; 
        margin: 0; 
    }
    
    /* Luxury Section Headers */
    .section-header { 
        color: #D4AF37; 
        font-family: 'Tenor Sans', sans-serif; 
        font-size: 1.2rem; 
        border-left: 3px solid #D4AF37; 
        padding-left: 15px; 
        margin-bottom: 25px; 
        text-transform: uppercase; 
        letter-spacing: 1px;
    }

    /* Document Box (Used inside expanders) */
    .dossier-box {
        font-family: 'Lato', sans-serif;
        color: #cccccc;
        background: #080808;
        padding: 40px;
        border: 1px solid #222;
        line-height: 1.8;
    }
    .dossier-box h1 {
        text-align: center;
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        font-size: 1.6rem;
        border-bottom: 1px solid #D4AF37;
        padding-bottom: 15px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }
    .dossier-box h2 {
        text-align: center;
        color: #F0E68C;
        font-family: 'Tenor Sans', sans-serif;
        margin-top: 30px;
        font-weight: normal;
    }

    /* Ecosystem Grid Layout */
    .project-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
    .project-card { 
        border: 1px solid #222; 
        background: #0a0a0a; 
        padding: 25px; 
        transition: 0.3s; 
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .project-card:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.1); }
    .btn-launch { 
        display: block; width: 100%; padding: 10px; background: #D4AF37; 
        color: #000 !important; text-align: center; font-weight: bold; 
        text-transform: uppercase; font-size: 0.7rem; margin-top: 20px;
    }
    .btn-code { 
        display: block; width: 100%; padding: 10px; border: 1px solid #444; 
        color: #888 !important; text-align: center; text-transform: uppercase; 
        font-size: 0.7rem; margin-top: 10px;
    }
    .btn-code:hover { border-color: #D4AF37; color: #D4AF37 !important; }

    /* Force Dark Dataframes */
    [data-testid="stDataFrame"] { background-color: #000 !important; }

    .footer { text-align: center; padding: 50px 0; color: #444; font-size: 0.6rem; letter-spacing: 2px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 1. BRANDING & SUMMARY
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Fragrance Intelligence</h1>
                <div style="color:#888; font-size:0.75rem; letter-spacing:3px; margin-top:5px;">STRATEGIC DATA TERMINAL • FORECAST 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="max-width: 900px; margin: 0 auto; text-align: center; padding-bottom: 40px;">
        <p style="color: #777; font-size: 0.95rem; line-height: 1.6;">
            The <b>Atelier Terminal</b> provides a high-fidelity convergence of macroeconomic data and the luxury olfactory market. 
            By synthesizing AI-driven supply chain analytics and global consumer sentiment, we forecast the evolution of the 
            fragrance ecosystem through 2026.
        </p>
    </div>
""", unsafe_allow_html=True)

# Metrics
c1, c2, c3, c4, c5, c6 = st.columns(6)
m_data = [("Global Market", "$593.2B"), ("CAGR", "+16.2%"), ("Local RU", "68%"), ("Poland PPP", "20th"), ("Scent Stacking", "+125%"), ("SdJ Share", "31.6%")]
for col, (l, v) in zip([c1, c2, c3, c4, c5, c6], m_data):
    col.markdown(f'<div style="text-align:center;"><div style="color:#444; font-size:0.6rem; text-transform:uppercase;">{l}</div><div style="color:#D4AF37; font-size:1.2rem; font-family:Tenor Sans;">{v}</div></div>', unsafe_allow_html=True)

st.write("---")

# -----------------------------------------------------------------------------
# 2. MAIN WORKSPACE (TABS)
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "2026 OUTLOOK", "ECOSYSTEM"])

with tab1:
    st.write("")
    selected_ep = st.radio("Intelligence Dossier:", ["EPISODE 01: RECESSION GLAM", "EPISODE 02: 2026 MACRO OUTLOOK"], horizontal=True)
    st.write("")

    if "EPISODE 01" in selected_ep:
        audio_src = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"
        trans_path = "podcast_transcript.md"
        viz_title = "2025 Market Dynamics"
        is_ep2 = False
    else:
        audio_src = "podcast_2026.mp3"
        trans_path = "podcast_transcript_2026.md"
        viz_title = "2026 Forecast Model"
        is_ep2 = True

    c_left, c_right = st.columns([1, 1.5], gap="large")
    with c_left:
        st.markdown('<div class="section-header">Audio Briefing</div>', unsafe_allow_html=True)
        st.audio(audio_src)
        st.markdown('<div style="padding:15px; border-left:2px solid #D4AF37; background:#080808; color:#888; font-size:0.85rem;">Professional AI-generated briefing for executive review.</div>', unsafe_allow_html=True)

    with c_right:
        st.markdown(f'<div class="section-header">Live Data: {viz_title}</div>', unsafe_allow_html=True)
        if not df.empty:
            # FORCING TRANSPARENT CHART BACKGROUND
            fig = px.scatter(df.head(150), x="year_clean", y="community_score", size="community_votes", color="segment", template="plotly_dark", color_discrete_sequence=['#D4AF37', '#666', '#F0E68C'])
            fig.update_layout(height=320, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    st.markdown('<div class="section-header">Intelligence Dossier</div>', unsafe_allow_html=True)
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        with st.expander(f"📝 READ FULL TRANSCRIPT ({selected_ep.split(':')[0]})", expanded=False):
            try:
                with open(trans_path, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="dossier-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.error("Transcript missing.")
    
    with col_d2:
        if is_ep2:
            with st.expander("📈 READ 2026 MACRO REPORT", expanded=False):
                try:
                    with open('macro_report_2026.md', 'r', encoding='utf-8') as f:
                        st.markdown(f'<div class="dossier-box">{f.read()}</div>', unsafe_allow_html=True)
                except: st.info("Macro report file missing.")
        else:
            st.info("Additional macro reports are available in Episode 02.")

# --- ANALYTICS TAB ---
with tab2:
    st.markdown('<div class="section-header">Deep Dive Analytics</div>', unsafe_allow_html=True)
    if not df.empty:
        st.write("Exploration of global fragrance clusters and sentiment scoring.")
        st.dataframe(df.head(100), use_container_width=True)
    else:
        st.info("Data source connection pending.")

# --- OUTLOOK TAB ---
with tab3:
    st.markdown('<div class="section-header">2026 Trend Radar</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-grid">
        <div class="project-card"><h3 style="color:#D4AF37;">🧪 Functional Fragrance</h3><p style="color:#888; font-size:0.9rem;">Scent as a neuro-modulator. 71% of consumers expect mood-enhancing benefits via biotech ingredients.</p></div>
        <div class="project-card"><h3 style="color:#D4AF37;">🧛‍♀️ Vamp Romantic</h3><p style="color:#888; font-size:0.9rem;">Rebellion against minimalism. Bold, dark profiles like black cherry and leather dominate Gen Z preference.</p></div>
        <div class="project-card"><h3 style="color:#D4AF37;">📉 Macro Protectionism</h3><p style="color:#888; font-size:0.9rem;">US trade tariffs and Nvidia compute dominance are forcing a radical shift in luxury supply chains.</p></div>
    </div>
    """, unsafe_allow_html=True)

# --- ECOSYSTEM TAB ---
with tab4:
    st.markdown('<div class="section-header">Project Ecosystem</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-grid">
        <div class="project-card">
            <h4 style="color:#D4AF37;">🌍 Aromo Intelligence</h4>
            <p style="color:#666; font-size:0.8rem;">Global market scraping engine and strategic forecast dashboard.</p>
            <a href="#" class="btn-launch">🚀 Launch App</a>
            <a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" class="btn-code">💻 View Code</a>
        </div>
        <div class="project-card">
            <h4 style="color:#D4AF37;">🔍 Perfume Finder</h4>
            <p style="color:#666; font-size:0.8rem;">Personalized recommendation system based on olfactory chemical structures.</p>
            <a href="#" class="btn-launch">🚀 Launch App</a>
            <a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" class="btn-code">💻 View Code</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • MAGDALENA ROMANIECKA 2026</div>', unsafe_allow_html=True)