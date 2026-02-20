import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 0. CONFIGURATION & LUXURY THEME
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

# Custom CSS for high-end boutique aesthetics
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* Main background with subtle gradient */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%);
        font-family: 'Lato', sans-serif !important; 
    }

    /* Elegant Golden Header */
    .header-wrapper { display: flex; justify-content: center; padding: 20px 0; }
    .header-inner { 
        border: 1px solid #D4AF37; 
        padding: 20px 50px; 
        text-align: center; 
        background-color: #050505; 
    }
    .main-title { 
        font-family: 'Tenor Sans', sans-serif; 
        color: #D4AF37; 
        font-size: 2rem; 
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

    /* Intelligence Dossier Box */
    .transcript-box { 
        font-family: 'Lato', sans-serif; 
        font-size: 0.95rem; 
        line-height: 1.7; 
        color: #cccccc; 
        background: #080808; 
        padding: 30px; 
        border: 1px solid #222; 
    }
    
    /* Metric styling */
    .metric-label { color: #666; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 1px; }
    .metric-value { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.3rem; }

    /* Centered Segmented Control for Episodes */
    div[data-testid="stRadio"] > label { display: none; } 
    div[data-testid="stRadio"] > div { 
        flex-direction: row !important; 
        justify-content: center !important; 
        gap: 40px !important; 
        padding: 20px 0;
    }
    
    .footer { 
        text-align: center; 
        padding: 40px 0 20px 0; 
        color: #444; 
        font-size: 0.65rem; 
        letter-spacing: 2px; 
        text-transform: uppercase; 
    }
    </style>
""", unsafe_allow_html=True)

# Load data using the project's data loader
df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 1. TOP NAVIGATION & METRICS
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-inner">
            <h1 class="main-title">Fragrance Intelligence</h1>
            <div style="color:#888; font-size:0.7rem; letter-spacing:2px; margin-top:5px;">
                ATELIER DATA TERMINAL • STRATEGIC FORECAST 2026
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# Compact horizontal metrics for a cleaner look
m1, m2, m3, m4, m5, m6 = st.columns(6)
metrics_data = [
    ("Global Market", "$593.2B"), ("Fragrance Growth", "+16.2%"), ("RU Local Share", "68%"),
    ("PL Econ Rank", "20th"), ("Scent Stacking", "+125%"), ("SdJ Market Share", "31.6%")
]
for col, (label, val) in zip([m1, m2, m3, m4, m5, m6], metrics_data):
    col.markdown(f'<div style="text-align:center;"><div class="metric-label">{label}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

st.write("---")

# -----------------------------------------------------------------------------
# 2. MAIN WORKSPACE
# -----------------------------------------------------------------------------
tab_briefing, tab_analytics, tab_outlook, tab_ecosystem = st.tabs([
    "STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "2026 TREND RADAR", "ECOSYSTEM"
])

with tab_briefing:
    # EPISODE SELECTOR (On-page for better UX)
    st.write("")
    selected_episode = st.radio(
        "Select Intelligence Episode:", 
        ["EPISODE 01: RECESSION GLAM", "EPISODE 02: 2026 MACRO OUTLOOK"],
        horizontal=True
    )
    st.write("")

    # Logic to switch content based on selection
    if "EPISODE 01" in selected_episode:
        audio_src = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"
        transcript_path = "podcast_transcript.md"
        viz_title = "2025 Market Dynamics"
        narrative_summary = "Analyzing 'The Lipstick Effect' and the rise of Gourmand 2.0 in the 2025 resilience phase."
        has_macro_report = False
    else:
        audio_src = "podcast_2026.mp3"
        transcript_path = "podcast_transcript_2026.md"
        viz_title = "2026 Macro Projections"
        narrative_summary = "An exclusive look at Nvidia's $5T cap, US trade tariffs, and Poland's economic leap over Japan."
        has_macro_report = True

    # Layout for Audio and Visualization
    col_left, col_right = st.columns([1, 1.5], gap="large")

    with col_left:
        st.markdown('<div class="section-header">Audio Intelligence</div>', unsafe_allow_html=True)
        st.audio(audio_src)
        st.markdown(f"""
            <div style="padding:20px; background:rgba(212,175,55,0.05); border:1px solid #333; font-size:0.9rem; color:#aaa; line-height:1.6;">
                <b style="color:#D4AF37;">NARRATIVE FOCUS:</b><br>{narrative_summary}
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown(f'<div class="section-header">Live Data: {viz_title}</div>', unsafe_allow_html=True)
        if not df.empty:
            # Display relevant chart
            fig = px.scatter(
                df.head(150), x="year_clean", y="community_score", size="community_votes",
                color="segment", template="plotly_dark", 
                color_discrete_sequence=['#D4AF37', '#666', '#F0E68C']
            )
            fig.update_layout(height=320, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

    # INTELLIGENCE DOSSIER (Consolidated Documents)
    st.write("---")
    st.markdown('<div class="section-header">Intelligence Dossier</div>', unsafe_allow_html=True)
    
    if has_macro_report:
        # Dual-document view for Episode 2
        doc_tab_text, doc_tab_macro = st.tabs(["📝 Full Transcript", "📈 2026 Macro Report"])
        with doc_tab_text:
            try:
                with open(transcript_path, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except FileNotFoundError:
                st.info(f"Transcript file ({transcript_path}) not found in directory.")
        
        with doc_tab_macro:
            try:
                with open('macro_report_2026.md', 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except FileNotFoundError:
                st.info("The 2026 Macro Report is currently being finalized in the terminal.")
    else:
        # Simple transcript view for Episode 1
        try:
            with open(transcript_path, 'r', encoding='utf-8') as f:
                st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
        except FileNotFoundError:
            st.info(f"Transcript file ({transcript_path}) not found.")

# -----------------------------------------------------------------------------
# 3. OTHER TABS (Placeholders for professional layout)
# -----------------------------------------------------------------------------
with tab_analytics:
    st.markdown('<div class="section-header">Market Clustering & Sentiment</div>', unsafe_allow_html=True)
    st.write("Deep dive data tables and clustering algorithms will be displayed here.")

with tab_outlook:
    st.markdown('<div class="section-header">Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    st.write("Analysis of Functional Fragrance, Neurocosmetics, and Vamp Romantic aesthetics.")

with tab_ecosystem:
    st.markdown('<div class="section-header">Project Ecosystem</div>', unsafe_allow_html=True)
    st.write("Links to Aromo Market Intelligence and Perfume Finder repositories.")

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • DEVELOPED BY MAGDALENA ROMANIECKA © 2026</div>', unsafe_allow_html=True)