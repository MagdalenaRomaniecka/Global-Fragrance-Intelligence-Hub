import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
import re
from data_loader import load_and_merge_data

st.set_page_config(page_title="Fragrance Intelligence ✦ Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0E0E0E;
        background-image: radial-gradient(circle at 50% 0%, #181818 0%, #0E0E0E 100%);
        color: #E0E0E0;
        font-family: 'Lato', sans-serif !important;
    }
    
    @media (max-width: 768px) {
        .main-title { font-size: 1.2rem !important; letter-spacing: 2px !important; }
        .header-inner { padding: 15px 10px !important; }
        .metric-value { font-size: 1.2rem !important; }
        .metric-label { font-size: 0.55rem !important; letter-spacing: 1.5px !important; }
        .report-frame { padding: 15px !important; font-size: 0.9rem !important; text-align: left !important; line-height: 1.6 !important; }
        .section-header { font-size: 1.1rem !important; margin: 20px 0 10px 0 !important; }
        h1 { font-size: 1.2rem !important; }
        h2 { font-size: 1.1rem !important; }
    }
    
    [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2 {
        text-align: center !important; justify-content: center !important; display: flex !important; width: 100% !important;
    }
    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 20px 0 10px 0; }
    .header-outer { border: 1px solid #333333; padding: 10px; display: inline-block; width: 100%; max-width: 750px; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 50px; background-color: #0E0E0E; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 5px; margin: 0; border: none !important; }
    
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; font-size: 1.8rem !important; }
    h2 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; text-transform: uppercase !important; border-top: 1px solid #262626 !important; padding-top: 30px !important; margin-top: 45px !important; font-size: 1.4rem !important; }
    
    .metric-box { border: 1px solid #262626; background-color: #121212; padding: 20px; text-align: center; transition: 0.3s; border-radius: 2px; margin-bottom: 10px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #888888; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 8px; }
    .metric-value { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }
    
    .report-frame {
        background: #121212;
        padding: 30px 40px;
        border: 1px solid #262626;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        color: #E0E0E0;
        line-height: 1.8;
        text-align: justify;
        margin-bottom: 20px;
        font-size: 0.95rem;
        border-radius: 2px;
        width: 100%;
        overflow-wrap: break-word;
    }
    
    .debrief-main-title, .dossier-main-title {
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        text-transform: uppercase;
        font-size: 1.4rem;
        margin-bottom: 5px;
        line-height: 1.3;
        text-align: left !important;
    }
    .debrief-sub-title, .dossier-sub-title {
        color: #E0E0E0;
        font-family: 'Lato', sans-serif;
        font-weight: 700;
        font-size: 0.85rem;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #333333;
        text-align: left !important;
    }
    .strategic-scope {
        color: #888888;
        font-family: 'Lato', sans-serif;
        font-size: 0.85rem;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    .part-heading, .dossier-topic-title {
        color: #E0E0E0;
        font-family: 'Lato', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .dossier-section-title {
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        text-transform: uppercase;
        font-size: 1.1rem;
        margin-top: 40px;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }
    .dialogue-text, .dossier-text {
        color: #E0E0E0;
        font-family: 'Lato', sans-serif;
        font-size: 0.95rem;
        line-height: 1.8;
        margin-bottom: 15px;
    }
    
    .section-header {
        color: #D4AF37;
        font-family: 'Tenor Sans';
        font-size: 1.4rem;
        text-align: center !important;
        display: block !important;
        border-bottom: 1px solid #D4AF37;
        padding-bottom: 10px;
        margin: 30px auto 20px auto;
        text-transform: uppercase;
        letter-spacing: 3px;
        width: 100%;
    }
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 10px; background-color: #0E0E0E; flex-wrap: wrap; }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p { text-align: center !important; font-family: 'Tenor Sans', sans-serif !important; letter-spacing: 1px; font-size: 0.8rem; color: #E0E0E0; }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #D4AF37 !important; }
    
    .project-card { border: 1px solid #262626; background: rgba(18,18,18,0.95); padding: 20px; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 20px; border-radius: 2px; }
    .project-card:hover { border-color: #D4AF37; box-shadow: 0 0 20px rgba(212, 175, 55, 0.15); }
    .btn-launch { display: block; width: 100%; padding: 12px; background: #D4AF37 !important; color: #0E0E0E !important; text-align: center; font-weight: bold; text-transform: uppercase; font-size: 0.7rem; text-decoration: none; letter-spacing: 2px; border-radius: 2px; }
    .footer { position: relative; width: 100%; background-color: #0E0E0E; color: #666666; text-align: center; padding: 30px; font-size: 0.65rem; border-top: 1px solid #1F1F1F; z-index: 999; letter-spacing: 2px; margin-top: 50px; }
    
    .intelligence-badge { text-align: center; color: #D4AF37; font-size: 0.85rem; font-style: italic; margin: 15px auto 25px auto; letter-spacing: 1px; border: 1px solid rgba(212,175,55,0.3); padding: 12px; background: rgba(212,175,55,0.05); max-width: 800px; }
    
    .stSelectbox label, .stSelectbox [data-testid="stMarkdownContainer"] p {
        font-family: 'Tenor Sans', sans-serif !important;
        font-size: 1.1rem !important;
        color: #D4AF37 !important;
        text-align: center !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        width: 100% !important;
        display: block !important;
    }
    
    div[data-testid="stSelectbox"] > div {
        margin: 0 auto !important;
        max-width: 400px !important;
    }
    </style>
""", unsafe_allow_html=True)

def find_file(filename):
    for root, _, files in os.walk("."):
        if filename and filename in files:
            return os.path.join(root, filename)
    return filename

df = load_and_merge_data()
if 'segment' in df.columns:
    df['segment'] = df['segment'].str.replace('-', ' ')

st.markdown("""
<div class="header-wrapper">
    <div class="header-outer">
        <div class="header-inner">
            <h1 class="main-title">Fragrance Intelligence</h1>
            <div style="font-family: 'Lato'; color: #888888; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 10px;">
                Global Strategic Hub ✦ Predictive Forecast 2026
            </div>
            <div style="font-family: 'Lato'; color: #666666; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 15px; border-top: 1px solid #262626; padding-top: 10px;">
                Data Intelligence Google Deep Research ✦ Givaudan Neuro Tech ✦ Fragrantica Datasets ✦ Chestny ZNAK
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Market", "$593B"), ("EU Trade Surplus", "€238B"), ("Poland PPP 2026", "> Japan"), ("Prestige Elasticity", "negative 1.81")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# Define briefings_content (Omitted large text blocks for brevity in processing, but keeping structure intact)
briefings_content = {
    "Ep. 0": {"dossier": "<div class='dossier-main-title'>🌐 2026 Global Architecture ✦ Master Prologue</div>"},
    "Ep. 1": {"debrief": "<div class='debrief-main-title'>🎙️ INTELLIGENCE BRIEFING ✦ RECESSION GLAM</div>", "dossier": "<div class='dossier-main-title'>🧠 2026 TREND REPORT ✦ NEURO RECESSION GLAM</div>"},
    "Ep. 2": {"dossier": "<div class='dossier-main-title'>📊 Global Trade Dynamics and the Russian Autarky Case</div>"},
    "Ep. 3": {"dossier": "<div class='dossier-main-title'>🧠 2026 TREND REPORT ✦ NEURO RECESSION GLAM</div>"},
    "Ep. 4": {"debrief": "<div class='debrief-main-title'>🎧 INTELLIGENCE BRIEFING ✦ THE EUROPEAN BARBELL & DATA VS CHEMISTRY</div>", "dossier": "<div class='dossier-main-title'>📊 MARKET POLARIZATION ✦ THE BARBELL EFFECT</div>"},
    "Ep. 5": {"debrief": "<div class='debrief-main-title'>🎙️ INTELLIGENCE BRIEFING ✦ CARTO AI & NEURO TECH</div>", "dossier": "<div class='dossier-main-title'>🧠 GIVAUDAN CARTO AI ✦ NEURO COGNITIVE ENGINEERING</div>"},
    "Ep. 6": {"debrief": "<div class='debrief-main-title'>🎙️ INTELLIGENCE BRIEFING ✦ B2B PRICE ELASTICITY</div>", "dossier": "<div class='dossier-main-title'>📊 MACROECONOMIC PRICE ELASTICITY ✦ B2B LOGISTICS</div>"},
    "Ep. 7": {"debrief": "<div class='debrief-main-title'>🎙️ INTELLIGENCE BRIEFING ✦ EU REGULATORY SHOCK</div>", "dossier": "<div class='dossier-main-title'>⚖️ INTELLECTUAL PROPERTY MOATS ✦ REGULATORY FORENSICS</div>"},
    "Ep. 8": {"debrief": "<div class='debrief-main-title'>🎙️ INTELLIGENCE BRIEFING ✦ THE BRUTAL ECONOMICS</div>", "dossier": "<div class='dossier-main-title'>📉 THE 2026 BARBELL & SUPPLY CHAIN PHYSICS</div>"},
    "Ep. 9": {"debrief": "<div class='debrief-main-title'>🎙️ INTELLIGENCE BRIEFING ✦ MASTER SYNTHESIS</div>", "dossier": "<div class='dossier-main-title'>🌐 2026 Global Architecture ✦ Master Synthesis</div>"}
}

tabs = st.tabs(["STRATEGIC BRIEFINGS", "MACRO & B2B SIMULATIONS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM", "M&A CAP TABLE"])

with tabs[0]:
    col_nav, col_viz = st.columns([1, 1.5], gap="large")
    with col_nav:
        st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Executive Selection</div>', unsafe_allow_html=True)
        episode = st.radio("Selection", [
            "🏛️ 0. Global Foundation", "🎧 Ep. 1 Recession Glam", "📊 Ep. 2 Global Trade", "🔮 Ep. 3 2026 Outlook",
            "🌍 Ep. 4 European Barbell", "🎓 Ep. 5 Carto AI & Neuro Tech", "🎓 Ep. 6 B2B Price Elasticity",
            "🎓 Ep. 7 EU Regulatory Shock", "📉 Ep. 8 The Brutal Economics", "🧬 Ep. 9 Master Synthesis"
        ], label_visibility="collapsed")
        
        match = re.search(r'(Ep\. \d+)', episode)
        ep_key = match.group(1) if match else "Ep. 0"
        content_dict = briefings_content.get(ep_key, {})

    with col_viz:
        st.markdown(f'<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Live Market Data</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">B2B Price Elasticity Simulator</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Market Strategic Hierarchy</div>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Fragrance Market Case Studies</div>', unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Analytical Project Ecosystem</div>', unsafe_allow_html=True)

with tabs[5]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Global M&A Capitalization</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ M&A FORENSICS Mapping corporate consolidation and the tactical shift towards minority investments in the global niche market</div>', unsafe_allow_html=True)
    
    ma_data = dict(
        character=["Global Niche Market", "L'Oréal", "ELC", "LVMH", "Puig", "Aesop", "Creed", "Tom Ford", "Le Labo", "MFK", "Byredo", "Penhaligon's"],
        parent=["", "Global Niche Market", "Global Niche Market", "Global Niche Market", "Global Niche Market", "L'Oréal", "L'Oréal", "ELC", "ELC", "LVMH", "Puig", "Puig"],
        value=[10.0, 4.0, 3.5, 1.5, 1.0, 2.5, 1.5, 2.8, 0.7, 1.5, 1.0, 0.5]
    )
    df_ma = pd.DataFrame(ma_data)
    
    fig_ma = px.sunburst(
        df_ma, 
        names='character', 
        parents='parent', 
        values='value',
        color_discrete_sequence=['#D4AF37', '#A67C00', '#594300', '#261D00']
    )
    
    fig_ma.update_layout(
        margin=dict(t=20, l=0, r=0, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E0E0E0', family="Lato"),
        height=550
    )
    st.plotly_chart(fig_ma, use_container_width=True)
    
    col_asian, col_exec = st.columns(2, gap="large")
    
    with col_asian:
        st.markdown('<div class="dossier-section-title" style="text-align: center;">The Asian Paradigm (K-Fragrance)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="report-frame" style="height: 100%;">
            <p><strong>Cultural Olfactory Barrier:</strong> The dominance of "Second Skin" profiles versus European projection requirements.</p>
            <p><strong>Regulatory Friction:</strong> Severe IFRA compliance protocols blocking indie brand imports to Western markets.</p>
            <p><strong>Strategic Resolution:</strong> Tactical minority investments bridging the gap (e.g., L'Oréal corporate venture funding in Borntostandout).</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_exec:
        st.markdown('<div class="dossier-section-title" style="text-align: center;">Executive Strategy Dashboard</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="report-frame" style="height: 100%;">
            <p><strong>Majority Buyouts:</strong> Legacy consolidation model (e.g., Aesop acquisition at $2.5B, Tom Ford at $2.8B). High risk of brand equity dilution and secondary market speculation.</p>
            <p><strong>The Amouage Protocol:</strong> Modern minority stake acquisitions securing global distribution infrastructure while preserving artisanal autonomy and market prestige.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)