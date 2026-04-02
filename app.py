import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS ✦ LUXURY & RESPONSIVE
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
    
    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 40px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 10px; display: inline-block; width: 100%; max-width: 750px; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 50px; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 5px; margin: 0; }
    
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; }
    
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 8px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }

    .report-frame { background: #080808; padding: 45px; border: 1px solid #222; color: #dfdfdf; line-height: 1.9; text-align: justify; font-size: 1.05rem; border-radius: 2px; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.4rem; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 3px; }
    
    .intelligence-badge { border: 1px solid #D4AF37; background: #1a1500; padding: 20px; margin-top: 25px; font-size: 0.85rem; color: #F0E68C; letter-spacing: 1px; line-height: 1.6; border-radius: 2px; }
    
    .project-card { border: 1px solid #222; background: rgba(15,15,15,0.95); padding: 25px; transition: 0.3s; height: 100%; border-radius: 2px; }
    .btn-launch { display: block; width: 100%; padding: 12px; background: #D4AF37 !important; color: #000 !important; text-align: center; font-weight: bold; text-transform: uppercase; font-size: 0.7rem; text-decoration: none; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# Helper function to find files in nested directories
def find_file(filename):
    for root, dirs, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return filename

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="header-wrapper">
    <div class="header-outer">
        <div class="header-inner">
            <h1 class="main-title">Fragrance Intelligence</h1>
            <div style="color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 4px; margin-top: 10px;">
                Global Strategic Hub ✦ Predictive Forecast 2026
            </div>
            <div style="color: #555; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; border-top: 1px solid #222; padding-top: 10px;">
                Data Intelligence Google Deep Research ✦ Givaudan Neuro-Tech ✦ Fragrantica Datasets ✦ Chestny ZNAK
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Market", "$593B"), ("EU Trade Surplus", "€238B"), ("Poland PPP 2026", "> Japan"), ("Prestige Elasticity", "-1.81")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. ANALYTICAL TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFINGS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_nav, col_viz = st.columns([1, 1.5], gap="large")
    with col_nav:
        st.markdown('<div class="section-header">Executive Selection</div>', unsafe_allow_html=True)
        episode = st.radio("Selection:", ["🏛️ 0. Global Foundation", "🎧 Ep. 1: Recession Glam", "📊 Ep. 2: Global Trade", "🔮 Ep. 3: 2026 Outlook", "🌍 Ep. 4: European Barbell", "🧬 Ep. 5: Master Synthesis"], label_visibility="collapsed")
        
        # MAPPING TO YOUR ACTUAL VS CODE FILENAMES
        if "0. Global" in episode:
            rep_file = "master_prologue.md"
            desc = "Macroeconomic Foundations 2026 ✦ The 5T Nvidia era ✦ EU 2023/1545 shock."
        elif "Ep. 1" in episode:
            rep_file = "trend_report_2025.md"
            desc = "Analyzing Lattafa viral surge and Givaudan MoodScentz™ neuro-active solutions."
        elif "Ep. 2" in episode:
            rep_file = "ep2_trade_report.md"
            desc = "Deep Research data on US Section 122 tariffs ✦ EU surplus ✦ Russian autarky."
        elif "Ep. 3" in episode:
            # FIXED: Matching your VS Code sidebar
            rep_file = "macro_report_2026.md" 
            desc = "Impact of the 5T Nvidia era ✦ 2025 Tariff Shock ✦ negative 1.81 elasticity."
        elif "Ep. 4" in episode:
            rep_file = "barbell_strategy_2026.md"
            desc = "Mapping the European Barbell structure ✦ Poland PPP breakthrough."
        else:
            # FIXED: Matching your VS Code sidebar
            rep_file = "ep5_summary_report.md"
            desc = "Final dossier compiled via Deep Research and B2B technological architecture."

        st.markdown(f'<p style="color:#D4AF37; font-size:0.95rem; font-style:italic; margin-top:20px; border-left: 3px solid #D4AF37; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Market Data Analysis</div>', unsafe_allow_html=True)
        df_t = df.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
        fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    
    # -------------------------------------------------------------------------
    # DYNAMIC FILE LOADER WITH DEEP SEARCH
    # -------------------------------------------------------------------------
    file_path = find_file(rep_file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            st.markdown(f'<div class="report-frame">\n\n{content}\n\n</div>', unsafe_allow_html=True)
    except:
        st.error(f"Dossier '{rep_file}' missing at path: {file_path}. Please check file location.")

with tabs[1]:
    st.markdown('<div class="section-header">Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ INTELLIGENCE NOTE ✦ 64% of analyzed Ultra-Niche segments utilize Jungle Essence™ CO2 extraction technologies to justify premium pricing above $350.</div>', unsafe_allow_html=True)
    df_sun = df.sort_values('community_votes', ascending=False).groupby('segment').head(5).reset_index(drop=True)
    fig_sun = px.sunburst(df_sun, path=['segment', 'brand', 'name'], values='community_votes', color='segment', color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555'}, template="plotly_dark")
    fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
    st.plotly_chart(fig_sun, use_container_width=True)

with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
    f_data = df[df['name'] == f_choice].iloc[0]
    
    intel_note = ""
    if "Phantom" in f_choice:
        intel_note = '<div class="intelligence-badge">✦ B2B CASE STUDY ✦ Designed via Givaudan Carto AI and 45M EEG brainwave measurements to optimize neuro-responses.</div>'
    elif "Idôle" in f_choice:
        intel_note = '<div class="intelligence-badge">✦ ECO-INNOVATION ✦ Features ultra-thin 15mm glass technology reducing carbon footprint by 63%.</div>'
    elif "Libre" in f_choice:
        intel_note = '<div class="intelligence-badge">✦ MOLECULAR DESIGN ✦ Features proprietary Diva Lavender and Vanilla Caviar molecular hybrids.</div>'

    vault_html = f"""
    <div style="border: 2px solid #D4AF37; padding: 40px; background: #050505; text-align: center; box-shadow: 0 0 30px rgba(212,175,55,0.1);">
        <div style="font-family: 'Tenor Sans'; color: #D4AF37; font-size: 2.5rem; letter-spacing: 5px; text-transform: uppercase;">{f_data['name']}</div>
        <div style="color: #D4AF37; font-size: 0.9rem; letter-spacing: 3px; margin-bottom: 30px;">{f_data['brand']} ✦ {f_data['segment']}</div>
        <div style="display: flex; justify-content: center; gap: 30px;">
            <div style="border: 1px solid #333; padding: 20px; min-width: 200px;">
                <div style="color: #666; font-size: 0.7rem; text-transform: uppercase;">Score</div>
                <div style="color: #F0E68C; font-size: 2rem;">{f_data['community_score']:.1f}</div>
            </div>
            <div style="border: 1px solid #333; padding: 20px; min-width: 200px;">
                <div style="color: #666; font-size: 0.7rem; text-transform: uppercase;">Key Notes</div>
                <div style="color: #ccc; font-size: 1rem;">{f_data['top_notes']}</div>
            </div>
        </div>
        {intel_note}
    </div>
    """
    st.markdown(vault_html, unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    apps = [
        ("🌍 Aromo Intelligence", "Custom scraping engine mapping social sentiment to B2B platforms like Myrissi™.", "https://share.streamlit.io/"),
        ("🧬 Kaggle Prediction", "Regression models calculating price elasticity and B2B tech adoption rates.", "https://share.streamlit.io/"),
        ("📊 Market Pulse", "Dashboard integrating Deep Research data with live tracking of EU 2023/1545 impact.", "https://share.streamlit.io/"),
        ("📡 Deep Research AI", "Macroeconomic engine processing Nvidia Class trends and Givaudan MoodScentz™+ data.", "https://share.streamlit.io/")
    ]
    for col, (name, dsc, link) in zip([e1, e2, e3, e4], apps):
        col.markdown(f"""<div class="project-card">
            <h4 style="color:#D4AF37; margin-top:0;">{name}</h4>
            <p style="color:#888; font-size:0.75rem;">{dsc}</p>
            <a class="btn-launch" href="{link}" target="_blank">LAUNCH APP</a>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)