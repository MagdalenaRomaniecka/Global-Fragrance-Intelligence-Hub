import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS (FORCED GOLD HIERARCHY & NO HASH MARKS)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%); 
        font-family: 'Lato', sans-serif !important; 
    }

    /* GLOBAL HEADERS AGGRESSIVE OVERRIDE */
    h1, h2, h3 { font-family: 'Tenor Sans', sans-serif !important; text-transform: uppercase !important; }
    
    h1 { 
        color: #D4AF37 !important; 
        font-size: 2.2rem !important; 
        text-align: center !important; 
        border-bottom: 1px solid #D4AF37 !important; 
        padding-bottom: 15px !important; 
        letter-spacing: 4px !important;
        margin-bottom: 25px !important;
    }
    
    h2 { 
        color: #F0E68C !important; 
        font-size: 1.6rem !important; 
        text-align: center !important; 
        letter-spacing: 2px !important; 
        border-top: 1px solid #333 !important;
        padding-top: 25px !important;
        margin-top: 40px !important;
    }
    
    h3 { 
        color: #D4AF37 !important; 
        font-size: 1.2rem !important; 
        border-left: 4px solid #D4AF37 !important; 
        padding-left: 15px !important; 
        margin-top: 30px !important;
    }

    /* HEADER FRAME */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 8px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 30px 60px; text-align: center; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title-text { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 6px; margin: 0; }
    
    /* REPORT CONTAINER */
    .report-frame { 
        background: #080808; 
        padding: 45px; 
        border: 1px solid #222; 
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        color: #dfdfdf;
        line-height: 1.9;
        text-align: justify;
    }

    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2rem; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <div class="main-title-text">Fragrance Intelligence</div>
                <div style="color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 10px;">Strategic Hub • 2026 Projections</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. LOGIC & TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.4], gap="large")
    with col_audio:
        episode = st.radio("Select Briefing:", [
            "🎧 Ep. 1: 2025 Market Trends", 
            "🔮 Ep. 2: 2026 Macro Outlook",
            "🌍 Ep. 3: The European Barbell"
        ])
        
        # DEFINITIVE LOGIC FOR 2026 MACRO REPORT
        if "Ep. 1" in episode:
            current_t, current_a, report_f = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md"
            r_label = "📈 READ 2025 TREND REPORT"
        elif "Ep. 2" in episode:
            current_t, current_a, report_f = "podcast_transcript_2026.md", "podcast_2026.mp3", "macro_report_2026.md"
            r_label = "📈 READ 2026 MACRO REPORT"
        else: # Ep 3
            current_t, current_a, report_f = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "macro_report_2026.md"
            r_label = "📈 READ 2026 MACRO REPORT"

        st.audio(current_a)

    with col_viz:
        # (Wykresy Barbell/Gourmand)
        st.write("Live Data Visualization Feed...")

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 READ TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
    with d2:
        with st.expander(r_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report '{report_f}' found in explorer but not loaded. Check spelling.")

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)