import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS ✦ REMASTERED LUXURY 2026
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    
    /* Global Background */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000 100%); 
        font-family: 'Lato', sans-serif !important; 
    }

    /* Header Styling */
    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 60px 0 40px 0; }
    .header-outer { border: 1px solid #333; padding: 12px; display: inline-block; width: 100%; max-width: 850px; background: rgba(10,10,10,0.5); }
    .header-inner { border: 1px solid #D4AF37; padding: 35px 60px; background-color: #050505; box-shadow: inset 0 0 30px rgba(212,175,55,0.05); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.6rem; text-transform: uppercase; letter-spacing: 8px; margin: 0; }
    
    /* KPIs - Premium Glow */
    .metric-box { border: 1px solid #222; background: linear-gradient(145deg, #0a0a0a 0%, #111 100%); padding: 25px; text-align: center; transition: 0.4s; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 20px rgba(212, 175, 55, 0.15); transform: translateY(-2px); }
    .metric-label { color: #888; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 3px; font-weight: 700; margin-bottom: 12px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }

    /* Reports - Clean & Professional */
    .report-frame { background: #0c0c0c; padding: 50px; border: 1px solid #1a1a1a; color: #d0d0d0; line-height: 2; text-align: justify; font-size: 1.1rem; border-radius: 4px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.5rem; border-left: 4px solid #D4AF37; padding-left: 25px; margin: 40px 0 25px 0; text-transform: uppercase; letter-spacing: 4px; }
    
    /* Tabs & Radio Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 30px; border-bottom: 1px solid #222; }
    .stTabs [data-baseweb="tab-list"] button { font-family: 'Tenor Sans' !important; letter-spacing: 2px !important; color: #666 !important; }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] { color: #D4AF37 !important; border-bottom-color: #D4AF37 !important; }

    /* Intelligence Badges */
    .intelligence-badge { border: 1px solid rgba(212,175,55,0.3); background: rgba(212,175,55,0.03); padding: 20px; margin: 30px 0; font-size: 0.9rem; color: #F0E68C; border-left: 5px solid #D4AF37; }
    
    .footer { text-align: center; padding: 60px; color: #333; font-size: 0.7rem; letter-spacing: 3px; border-top: 1px solid #111; margin-top: 80px; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# LOGIC REMAINS - DESIGN EVOLVES
# -----------------------------------------------------------------------------
def find_file(filename):
    for root, dirs, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return filename

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="header-wrapper">
    <div class="header-outer">
        <div class="header-inner">
            <h1 class="main-title">Fragrance Intelligence</h1>
            <div style="color: #888; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 5px; margin-top: 15px;">
                Strategic Analysis Hub ✦ Forecast 2026-2035
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
# TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFINGS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_nav, col_viz = st.columns([1, 1.6], gap="large")
    with col_nav:
        st.markdown('<div class="section-header">Executive Selection</div>', unsafe_allow_html=True)
        episode = st.radio("Access Intelligence Folder:", ["🏛️ 0. Global Foundation", "🎧 Ep. 1: Recession Glam", "📊 Ep. 2: Global Trade", "🔮 Ep. 3: 2026 Outlook", "🌍 Ep. 4: European Barbell", "🧬 Ep. 5: Master Synthesis"], label_visibility="collapsed")
        
        # Mapping remains consistent for stability
        mapping = {
            "0. Global": ("master_prologue.md", None, None, "Foundation analysis of the 5T Nvidia era."),
            "Ep. 1": ("trend_report_2025.md", "podcast_trends.mp3", "podcast_transcript.md", "Lattafa surge & MoodScentz™ neuro-active solutions."),
            "Ep. 2": ("ep2_trade_report.md", "ep2_audio.mp3", "ep2_trade_transcript.md", "US Section 122 tariffs & Russian autarky metrics."),
            "Ep. 3": ("macro_report_2026.md", "podcast_2026.mp3", "podcast_transcript_2026.md", "Negative 1.81 price elasticity & Tariff Shock projections."),
            "Ep. 4": ("barbell_strategy_2026.md", "ep3_europe_barbell.mp3", "ep3_whisper_transcript_EN.md", "Poland PPP breakthrough & 0.28 digital correlation."),
            "Ep. 5": ("ep5_summary_report.md", "ep5_audio.mp3", "ep5_summary_transcript.md", "Final synthesis of chemistry, capital, and data.")
        }
        
        for key, (r, a, t, d) in mapping.items():
            if key in episode:
                rep_file, audio, trans, desc = r, a, t, d

        if audio: st.audio(find_file(audio))
        st.markdown(f'<div class="intelligence-badge">{desc}</div>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Data Visualization ✦ {episode[3:]}</div>', unsafe_allow_html=True)
        df_t = df.nlargest(12, 'community_votes').sort_values('community_votes', ascending=True)
        fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", 
                     color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, showlegend=True,
                          legend=dict(orientation="h", y=-0.2, x=0.5, xanchor="center"))
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    
    # Reports Layout - Unified for all
    l_col, r_col = st.columns(2, gap="large")
    with l_col:
        st.markdown('<div class="section-header">Intelligence Transcript</div>', unsafe_allow_html=True)
        try:
            with open(find_file(trans), 'r', encoding='utf-8') as f:
                st.markdown(f'<div class="report-frame">{f.read()}</div>', unsafe_allow_html=True)
        except: st.info("Foundation module: Transcript not applicable.")

    with r_col:
        st.markdown('<div class="section-header">Executive Dossier</div>', unsafe_allow_html=True)
        try:
            with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                st.markdown(f'<div class="report-frame">{f.read()}</div>', unsafe_allow_html=True)
        except: st.error("Strategic dossier missing.")

with tabs[1]:
    # Market Analytics logic remains
    st.markdown('<div class="section-header">Global Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    df_sun = df.sort_values('community_votes', ascending=False).groupby('segment').head(5).reset_index(drop=True)
    fig_sun = px.sunburst(df_sun, path=['segment', 'brand', 'name'], values='community_votes', color='segment', 
                          color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555'}, template="plotly_dark")
    fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
    st.plotly_chart(fig_sun, use_container_width=True)

# VAULT & ECOSYSTEM design also restored
with tabs[2]:
    st.markdown('<div class="section-header">Case Study Vault</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Intelligence Profile:", sorted(df['name'].tolist()))
    f_data = df[df['name'] == f_choice].iloc[0]
    st.markdown(f"""
    <div style="border: 1px solid #D4AF37; padding: 50px; background: rgba(5,5,5,0.8); text-align: center; border-radius: 4px;">
        <div style="font-family: 'Tenor Sans'; color: #D4AF37; font-size: 2.8rem; letter-spacing: 6px; text-transform: uppercase;">{f_data['name']}</div>
        <div style="color: #666; font-size: 1rem; letter-spacing: 4px; margin-bottom: 40px;">{f_data['brand']} ✦ {f_data['segment']}</div>
        <div style="display: flex; justify-content: center; gap: 50px;">
            <div><div style="color:#D4AF37; font-size:0.8rem; letter-spacing:2px;">SCORE</div><div style="font-size:2.5rem; color:#F0E68C;">{f_data['community_score']:.1f}</div></div>
            <div><div style="color:#D4AF37; font-size:0.8rem; letter-spacing:2px;">NOTES</div><div style="font-size:1.2rem; color:#ccc; max-width:400px;">{f_data['top_notes']}</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)