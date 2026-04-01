import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS - MOBILE RESPONSIVE LUXURY
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
    
    @media (max-width: 768px) {
        .main-title { font-size: 1.5rem !important; letter-spacing: 2px !important; }
        .metric-value { font-size: 1.4rem !important; }
        .report-frame { padding: 20px !important; font-size: 0.95rem !important; }
        h1 { font-size: 1.4rem !important; }
    }

    [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2 {
        text-align: center !important; justify-content: center !important; display: flex !important; width: 100% !important;
    }

    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 40px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 10px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 50px; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 5px; margin: 0; border: none !important; }
    
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; font-size: 1.8rem !important; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-transform: uppercase !important; border-top: 1px solid #333 !important; padding-top: 30px !important; margin-top: 45px !important; font-size: 1.4rem !important; }

    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; border-radius: 2px; margin-bottom: 10px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 8px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }

    .report-frame { background: #080808; padding: 45px; border: 1px solid #222; box-shadow: 0 15px 40px rgba(0,0,0,0.6); color: #dfdfdf; line-height: 1.9; text-align: justify; margin-bottom: 20px; font-size: 1.05rem; border-radius: 2px; width: 100%; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.4rem; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 3px; }
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 20px; }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p { 
        text-align: center !important; font-family: 'Tenor Sans', sans-serif !important; letter-spacing: 2px; 
    }

    .project-card { border:1px solid #222; background:rgba(15,15,15,0.95); padding:25px; transition:0.3s; height:100%; display:flex; flex-direction:column; justify-content:space-between; margin-bottom: 20px; border-radius: 2px; }
    .project-card:hover { border-color:#D4AF37; box-shadow: 0 0 20px rgba(212, 175, 55, 0.15); }
    .btn-launch { display:block; width:100%; padding:12px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; text-decoration:none; letter-spacing: 2px; border-radius: 2px; }

    .footer { position: relative; width: 100%; background-color: #000; color: #444; text-align: center; padding: 30px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER WITH DATA ORIGIN
# -----------------------------------------------------------------------------
st.markdown("""
<div class="header-wrapper">
    <div class="header-outer">
        <div class="header-inner">
            <h1 class="main-title">Fragrance Intelligence</h1>
            <div style="font-family: 'Lato'; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 4px; margin-top: 10px;">
                Global Strategic Hub ✦ Predictive Forecast 2026
            </div>
            <div style="font-family: 'Lato'; color: #555; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; border-top: 1px solid #222; padding-top: 10px;">
                Data Intelligence Google Deep Research ✦ Aromo and Fragrantica Datasets ✦ Chestny ZNAK
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# UPDATED KPI METRICS
m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Market", "$593B"), ("EU Trade Surplus", "€238B"), ("Poland PPP 2026", "> Japan"), ("Prestige Elasticity", "-1.81")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. ANALYTICAL TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFINGS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Selection:", ["🎧 Ep. 1: Recession Glam", "📊 Ep. 2: Global Trade", "🔮 Ep. 3: 2026 Outlook", "🌍 Ep. 4: European Barbell", "🧬 Ep. 5: Master Synthesis"], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_t, current_a, rep_file = "podcast_transcript.md", "podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title, desc = "Popularity", "Global Popularity Ranking", "Analyzing Sol de Janeiro dominance Lattafa viral surge and Givaudan neuro active solutions."
        elif "Ep. 2" in episode:
            current_t, current_a, rep_file = "ep2_trade_transcript.md", "ep2_audio.mp3", "ep2_trade_report.md"
            f_type, v_title, desc = "None", "Global Trade Volume 2024", "Deep Research data on US Section 122 tariffs EU surplus and Russian autarky 93M units."
        elif "Ep. 3" in episode:
            current_t, current_a, rep_file = "podcast_transcript_2026.md", "podcast_2026.mp3", "ep3_outlook_report.md"
            f_type, v_title, desc = "None", "2026 Global Projections", "Impact of the 5T Nvidia era the 2025 Tariff Shock and negative 1.81 price elasticity."
        elif "Ep. 4" in episode:
            current_t, current_a, rep_file = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "barbell_strategy_2026.md"
            f_type, v_title, desc = "Barbell", "The Barbell Market Structure 2026", "Mapping the European Barbell structure Poland PPP breakthrough and 0.28 digital correlation."
        else:
            current_t, current_a, rep_file = "ep5_summary_transcript.md", "ep5_audio.mp3", "macro_report_2026.md"
            f_type, v_title, desc = "None", "Master Strategic Synthesis 2026", "Final dossier compiled via Deep Research and Kaggle datasets curated by Magdalena Romaniecka."

        st.audio(current_a)
        st.markdown(f'<p style="color:#D4AF37; font-size:0.95rem; font-style:italic; margin-top:20px; border-left: 3px solid #D4AF37; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data ✦ {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=18, color='#D4AF37'))
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="center", x=0.5))
        else:
            df_t = df.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=15, color='#D4AF37'), cliponaxis=False)
            max_val = df_t['community_votes'].max()
            fig.update_xaxes(range=[0, max_val * 1.35], showgrid=False, showticklabels=False)
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.6, xanchor="center", x=0.5), margin=dict(r=100))
        
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)

    # TWO-COLUMN LAYOUT: TRANSCRIPTION (LEFT) | DOSSIER (RIGHT)
    st.write("---")
    l_col, r_col = st.columns(2, gap="large")
    with l_col:
        st.markdown('<div class="section-header">Executive Audio Debrief</div>', unsafe_allow_html=True)
        try:
            with open(current_t, 'r', encoding='utf-8') as f:
                st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                st.markdown(f.read())
                st.markdown('</div>', unsafe_allow_html=True)
        except: st.error("Debrief missing.")
    with r_col:
        st.markdown('<div class="section-header">Executive Master Dossier</div>', unsafe_allow_html=True)
        try:
            with open(rep_file, 'r', encoding='utf-8') as f:
                st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                st.markdown(f.read())
                st.markdown('</div>', unsafe_allow_html=True)
        except: st.error("Dossier missing.")

with tabs[1]:
    st.markdown('<div class="section-header">Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    # BULLETPROOF FIX FOR SUNBURST
    df_sun = df.sort_values('community_votes', ascending=False).groupby('segment').head(5).reset_index(drop=True)
    df_sun['Global Market'] = 'Global Market'
    
    fig_sun = px.sunburst(df_sun, path=['Global Market', 'segment', 'brand', 'name'], values='community_votes', color='segment', color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555'}, template="plotly_dark")
    fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
    st.plotly_chart(fig_sun, use_container_width=True)

with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
    f_data = df[df['name'] == f_choice].iloc[0]
    vault_html = f"""
    <div style="border: 2px solid #D4AF37; padding: 6px; background: #000; margin: 30px auto; max-width: 900px; box-shadow: 0 0 30px rgba(212,175,55,0.15);">
        <div style="border: 1px solid rgba(212,175,55,0.4); background: radial-gradient(circle at 50% 50%, #0a0a0a 0%, #000000 100%); padding: 50px 30px; text-align: center;">
            <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.8rem; letter-spacing: 6px; text-transform: uppercase; margin-bottom: 10px;">{f_data['name']}</div>
            <div style="color: #D4AF37; font-size: 0.9rem; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 40px;">{f_data['brand']} ✦ {f_data['segment']}</div>
            <div style="display: flex; justify-content: center; gap: 40px; margin-bottom: 40px; flex-wrap: wrap;">
                <div style="border: 2px solid #D4AF37; background: linear-gradient(145deg, #1a1500 0%, #050505 100%); padding: 4px; min-width: 250px; border-radius: 2px;">
                    <div style="border: 1px solid rgba(212,175,55,0.3); padding: 20px 30px;">
                        <div style="color:#D4AF37; font-size:0.85rem; letter-spacing:3px; margin-bottom:10px; text-transform:uppercase;">Quality Score</div>
                        <div style="color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 3.5rem; line-height: 1.2; margin: 0;">{f_data['community_score']:.1f}/5.0</div>
                    </div>
                </div>
                <div style="border: 2px solid #D4AF37; background: linear-gradient(145deg, #1a1500 0%, #050505 100%); padding: 4px; min-width: 250px; border-radius: 2px;">
                    <div style="border: 1px solid rgba(212,175,55,0.3); padding: 20px 30px;">
                        <div style="color:#D4AF37; font-size:0.85rem; letter-spacing:3px; margin-bottom:10px; text-transform:uppercase;">Key Notes</div>
                        <div style="color: #ccc; font-size: 1.1rem; line-height: 1.5; margin: 0;">{f_data['top_notes']}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(vault_html, unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    apps = [
        ("🌍 Aromo Intelligence", "Custom scraping engine for Eurasian markets tracking real time price fluctuations.", "https://share.streamlit.io/"),
        ("🧬 Kaggle Prediction", "Regression models calculating price elasticity and viral candidates.", "https://share.streamlit.io/"),
        ("📊 Market Pulse", "Dashboard integrating Deep Research data with live import export tracking.", "https://share.streamlit.io/"),
        ("📡 Deep Research AI", "Macroeconomic analysis engine processing geopolitical shifts and 2035 trends.", "https://share.streamlit.io/")
    ]
    for col, (name, dsc, link) in zip([e1, e2, e3, e4], apps):
        col.markdown(f"""<div class="project-card">
            <h4 style="color:#D4AF37; margin-top:0; font-size:0.9rem;">{name}</h4>
            <p style="color:#888; font-size:0.75rem;">{dsc}</p>
            <a class="btn-launch" href="{link}" target="_blank">LAUNCH APP</a>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)