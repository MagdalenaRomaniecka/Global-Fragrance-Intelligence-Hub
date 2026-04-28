import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS ✦ MOBILE RESPONSIVE LUXURY
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence ✦ Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%);
        font-family: 'Lato', sans-serif !important;
    }
    
    @media (max-width: 768px) {
        .main-title { font-size: 1.2rem !important; letter-spacing: 2px !important; }
        .header-inner { padding: 15px 10px !important; }
        .metric-value { font-size: 1.2rem !important; }
        .metric-label { font-size: 0.55rem !important; letter-spacing: 1.5px !important; }
        .report-frame { padding: 15px !important; font-size: 0.9rem !important; text-align: left !important; line-height: 1.6 !important; }
        .section-header { font-size: 1.1rem !important; padding-left: 10px !important; margin: 20px 0 10px 0 !important; }
        h1 { font-size: 1.2rem !important; }
        h2 { font-size: 1.1rem !important; }
        .vault-main-title { font-size: 1.6rem !important; letter-spacing: 2px !important; }
        .vault-stats-container { gap: 15px !important; }
        .vault-stat-box { min-width: 100% !important; padding: 15px !important; }
        .strat-box-mobile { padding: 15px !important; }
    }

    [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2 {
        text-align: center !important; justify-content: center !important; display: flex !important; width: 100% !important;
    }

    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 20px 0 10px 0; }
    .header-outer { border: 1px solid #444; padding: 10px; display: inline-block; width: 100%; max-width: 750px; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 50px; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 5px; margin: 0; border: none !important; }
    
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; font-size: 1.8rem !important; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-transform: uppercase !important; border-top: 1px solid #333 !important; padding-top: 30px !important; margin-top: 45px !important; font-size: 1.4rem !important; }

    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; border-radius: 2px; margin-bottom: 10px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 8px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }

    .report-frame { background: #080808; padding: 45px; border: 1px solid #222; box-shadow: 0 15px 40px rgba(0,0,0,0.6); color: #dfdfdf; line-height: 1.9; text-align: justify; margin-bottom: 20px; font-size: 1.05rem; border-radius: 2px; width: 100%; overflow-wrap: break-word; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.4rem; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 3px; }
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 10px; }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p { text-align: center !important; font-family: 'Tenor Sans', sans-serif !important; letter-spacing: 1px; font-size: 0.8rem; }

    .project-card { border:1px solid #222; background:rgba(15,15,15,0.95); padding:20px; transition:0.3s; height:100%; display:flex; flex-direction:column; justify-content:space-between; margin-bottom: 20px; border-radius: 2px; }
    .project-card:hover { border-color:#D4AF37; box-shadow: 0 0 20px rgba(212, 175, 55, 0.15); }
    .btn-launch { display:block; width:100%; padding:12px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; text-decoration:none; letter-spacing: 2px; border-radius: 2px; }

    .footer { position: relative; width: 100%; background-color: #000; color: #444; text-align: center; padding: 30px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; margin-top: 50px; }
    
    .tab-intro { text-align: center; color: #888; font-size: 0.85rem; letter-spacing: 1px; margin-bottom: 30px; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# INTELLIGENT FILE LOCATOR
# -----------------------------------------------------------------------------
def find_file(filename):
    for root, dirs, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return filename

df = load_and_merge_data()
df['segment'] = df['segment'].str.replace('-', ' ')

# -----------------------------------------------------------------------------
# 2. HEADER WITH DATA ORIGIN
# -----------------------------------------------------------------------------
st.markdown("""
<div class="header-wrapper">
    <div class="header-outer">
        <div class="header-inner">
            <h1 class="main-title">Fragrance Intelligence</h1>
            <div style="font-family: 'Lato'; color: #888; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 10px;">
                Global Strategic Hub ✦ Predictive Forecast 2026
            </div>
            <div style="font-family: 'Lato'; color: #555; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 15px; border-top: 1px solid #222; padding-top: 10px;">
                Data Intelligence Google Deep Research ✦ Givaudan Neuro Tech ✦ Fragrantica Datasets ✦ Chestny ZNAK
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# GLOBAL EXECUTIVE SUMMARY (Przed KPI)
global_intro_html = """
<div style="background: rgba(212,175,55,0.05); border: 1px solid rgba(212,175,55,0.3); padding: 25px; margin-top: 10px; margin-bottom: 30px; border-radius: 2px; text-align: center;">
    <div style="color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.2rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px;">Strategic Intelligence Hub</div>
    <div style="color: #ccc; font-size: 0.95rem; line-height: 1.6; max-width: 900px; margin: 0 auto;">
        This application is an advanced data synthesis engine ✦ It processes millions of data points from Kaggle ✦ Chestny ZNAK ✦ and Givaudan neuro technology to map the 2026 global market ✦ It transforms raw empirical data into actionable predictive intelligence ✦ proving that the industry has shifted from traditional beauty into an economic survival and bio hacking sector
    </div>
</div>
"""
st.markdown(global_intro_html, unsafe_allow_html=True)

# KPI METRICS
m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Market", "$593B"), ("EU Trade Surplus", "€238B"), ("Poland PPP 2026", "> Japan"), ("Prestige Elasticity", "Minus 1.81")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. ANALYTICAL TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFINGS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    st.markdown('<div class="tab-intro">Audio intelligence and executive dossiers ✦ Select a briefing to load dynamic data and macroeconomic reports</div>', unsafe_allow_html=True)
    
    top_left, top_right = st.columns([1, 1.5], gap="large")
    
    with top_left:
        st.markdown('<div class="section-header" style="margin-top:0;">Executive Selection</div>', unsafe_allow_html=True)
        episode = st.radio("Select Audio Briefing", ["🏛️ 0 ✦ Global Foundation", "🎧 Episode 1 ✦ Recession Glam", "📊 Episode 2 ✦ Global Trade", "🔮 Episode 3 ✦ 2026 Outlook", "🌍 Episode 4 ✦ European Barbell", "🧬 Episode 5 ✦ Master Synthesis"], label_visibility="collapsed")
        
        if "0 ✦ Global" in episode:
            current_t, current_a, rep_file = None, None, "master_prologue.md"
            desc = "The 5T Nvidia era ✦ Hollowing Out ✦ and the Section 122 Tariff Shock"
        elif "Episode 1" in episode:
            current_t, current_a, rep_file = "podcast_transcript.md", "podcast_trends.mp3", "trend_report_2025.md"
            desc = "Analyzing Lattafa viral surge and Givaudan MoodScentz neuro active solutions"
        elif "Episode 2" in episode:
            current_t, current_a, rep_file = "ep2_trade_transcript.md", "ep2_audio.mp3", "ep2_trade_report.md"
            desc = "Deep Research data on US Section 122 tariffs ✦ EU surplus ✦ and Russian autarky"
        elif "Episode 3" in episode:
            current_t, current_a, rep_file = "podcast_transcript_2026.md", "podcast_2026.mp3", "macro_report_2026.md"
            desc = "Impact of the 5T Nvidia era ✦ the 2025 Tariff Shock ✦ and negative 1.81 price elasticity"
        elif "Episode 4" in episode:
            current_t, current_a, rep_file = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "barbell_strategy_2026.md"
            desc = "Mapping the European Barbell structure ✦ Poland PPP breakthrough ✦ and 0.28 digital correlation"
        else:
            current_t, current_a, rep_file = "ep5_summary_transcript.md", "ep5_audio.mp3", "ep5_summary_report.md"
            desc = "Final dossier compiled via Deep Research and Givaudan technological architecture"

        if current_a:
            st.audio(find_file(current_a))
        
        st.markdown(f'<p style="color:#D4AF37; font-size:0.95rem; font-style:italic; margin-top:15px; border-left: 3px solid #D4AF37; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    if "0 ✦ Global" in episode:
        with top_right:
            st.markdown('<div class="section-header" style="margin-top:0;">Macroeconomic Foundations 2026</div>', unsafe_allow_html=True)
            try:
                with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                    content_r = f.read().replace(':', ' ✦').replace('-', ' ').replace(';', ' ')
                    st.markdown(f'<div class="report-frame" style="margin-top: 15px;">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
            except:
                st.error("Dossier missing")
                
        st.write("---")
        st.markdown('<div class="section-header" style="text-align: center;">Live Market Data ✦ The Barbell Structure</div>', unsafe_allow_html=True)
        df_barbell = df.groupby('segment')['community_votes'].sum().reset_index()
        df_barbell['sort_order'] = df_barbell['segment'].map({'Mass Market': 0, 'Prestige': 1, 'Niche': 2})
        df_barbell = df_barbell.sort_values('sort_order')

        fig = px.bar(df_barbell, x="segment", y="community_votes", color="segment", text="community_votes",
                     color_discrete_map={'Niche':'#D4AF37', 'Prestige':'#1a1a1a', 'Mass Market':'#F0E68C'}, template="plotly_dark")
        fig.update_traces(textposition='outside', textfont=dict(size=18, family="Lato", color='#ffffff'), cliponaxis=False, hovertemplate="<b>Segment</b> %{x}<br><b>Votes</b> %{y}<extra></extra>")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=350, xaxis_title=None, yaxis_title=None, showlegend=False, margin=dict(t=20, b=10, l=0, r=0), xaxis=dict(showgrid=False, tickfont=dict(size=14, color='#aaaaaa')), yaxis=dict(showgrid=False, showticklabels=False))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    else:
        with top_right:
            if "Episode 4" in episode:
                st.markdown('<div class="section-header" style="margin-top:0;">Live Market Data ✦ The Barbell Structure</div>', unsafe_allow_html=True)
                df_barbell = df.groupby('segment')['community_votes'].sum().reset_index()
                df_barbell['sort_order'] = df_barbell['segment'].map({'Mass Market': 0, 'Prestige': 1, 'Niche': 2})
                df_barbell = df_barbell.sort_values('sort_order')

                fig = px.bar(df_barbell, x="segment", y="community_votes", color="segment", text="community_votes",
                             color_discrete_map={'Niche':'#D4AF37', 'Prestige':'#1a1a1a', 'Mass Market':'#F0E68C'}, template="plotly_dark")
                fig.update_traces(textposition='outside', textfont=dict(size=18, family="Lato", color='#ffffff'), cliponaxis=False, hovertemplate="<b>Segment</b> %{x}<br><b>Votes</b> %{y}<extra></extra>")
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=320, xaxis_title=None, yaxis_title=None, showlegend=False, margin=dict(t=20, b=10, l=0, r=0), xaxis=dict(showgrid=False, tickfont=dict(size=14, color='#aaaaaa')), yaxis=dict(showgrid=False, showticklabels=False))
                st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

            elif "Episode 1" in episode:
                st.markdown('<div class="section-header" style="margin-top:0;">Live Market Data ✦ Viral Popularity Ranking</div>', unsafe_allow_html=True)
                df_t = df.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
                
                fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", text="community_votes",
                             color_discrete_map={'Niche':'#D4AF37', 'Prestige':'#1a1a1a', 'Mass Market':'#F0E68C'}, template="plotly_dark")
                fig.update_traces(textposition='outside', textfont=dict(size=16, family="Lato", color='#ffffff'), cliponaxis=False, hovertemplate="<b>Brand</b> %{y}<br><b>Votes</b> %{x}<extra></extra>")
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=320, xaxis_title=None, yaxis_title=None, showlegend=False, margin=dict(t=20, b=10, l=0, r=0), xaxis=dict(range=[0, df_t['community_votes'].max() * 1.35], showgrid=False, showticklabels=False), yaxis=dict(showgrid=False, tickfont=dict(size=13, color='#aaaaaa')))
                st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
                
            else:
                st.markdown('<div class="section-header" style="margin-top:0;">Intelligence Architecture</div>', unsafe_allow_html=True)
                infographic_html = """<style>
.blueprint-container { border: 1px solid rgba(212,175,55,0.2); background: radial-gradient(circle at 50% -20%, #151515 0%, #000 100%); padding: 30px; border-radius: 2px; position: relative; overflow: hidden; box-shadow: inset 0 0 30px rgba(0,0,0,0.8); margin: 15px auto; max-width: 95%; }
.blueprint-container::before { content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 1px; background: linear-gradient(90deg, transparent, rgba(212,175,55,0.8), transparent); animation: scanline 4s linear infinite; }
@keyframes scanline { 100% { left: 200%; } }
.bp-title { color: #D4AF37; text-align: center; font-size: 1.1rem; letter-spacing: 4px; margin-bottom: 30px; font-weight: 400; font-family: 'Tenor Sans', sans-serif; text-transform: uppercase; }
.bp-grid { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }
.bp-card { background: rgba(10,10,10,0.8); border: 1px solid #1a1a1a; padding: 25px 15px; flex: 1; min-width: 180px; text-align: center; transition: all 0.4s ease; border-bottom: 2px solid #111; }
.bp-card:hover { border-color: rgba(212,175,55,0.4); background: rgba(15,15,15,1); transform: translateY(-5px); box-shadow: 0 10px 25px rgba(212,175,55,0.05); border-bottom: 2px solid #D4AF37; }
.bp-icon { font-size: 1.8rem; margin-bottom: 15px; filter: grayscale(100%) brightness(1.5) sepia(100%) hue-rotate(5deg) saturate(300%); }
.bp-header { color: #D4AF37; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; font-weight: bold; }
.bp-list { color: #999; font-size: 0.85rem; line-height: 1.8; list-style-type: none; padding: 0; margin: 0; }
</style>
<div class="blueprint-container">
<div class="bp-title">Givaudan Carto ✦ Data Ecosystem</div>
<div class="bp-grid">
<div class="bp-card">
<div class="bp-icon">📥</div>
<div class="bp-header">Raw Data Input</div>
<ul class="bp-list">
<li>Kaggle Global Sets</li>
<li>Chestny ZNAK Logs</li>
<li>Consumer Sentiment</li>
</ul>
</div>
<div class="bp-card">
<div class="bp-icon">⚙️</div>
<div class="bp-header">Processing Engine</div>
<ul class="bp-list">
<li>Carto AI Algorithms</li>
<li>Python Regressions</li>
<li>Neuro Mood Mapping</li>
</ul>
</div>
<div class="bp-card">
<div class="bp-icon">💎</div>
<div class="bp-header">Strategic Output</div>
<ul class="bp-list">
<li>Neuro Active Scents</li>
<li>Dopamine Hacking</li>
<li>Predictive Playbook</li>
</ul>
</div>
</div>
</div>"""
                st.markdown(infographic_html, unsafe_allow_html=True)

        st.write("---")
        
        l_col, r_col = st.columns(2, gap="large")
        with l_col:
            st.markdown('<div class="section-header">Executive Audio Debrief</div>', unsafe_allow_html=True)
            try:
                with open(find_file(current_t), 'r', encoding='utf-8') as f:
                    content_t = f.read().replace(':', ' ✦').replace('-', ' ').replace(';', ' ')
                    st.markdown(f'<div class="report-frame">\n\n{content_t}\n\n</div>', unsafe_allow_html=True)
            except:
                st.error("Debrief missing")
                
        with r_col:
            st.markdown('<div class="section-header">Executive Master Dossier</div>', unsafe_allow_html=True)
            try:
                with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                    content_r = f.read().replace(':', ' ✦').replace('-', ' ').replace(';', ' ')
                    st.markdown(f'<div class="report-frame">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
            except:
                st.error("Dossier missing")

with tabs[1]:
    st.markdown('<div class="tab-intro">Visualizing the 2026 market hierarchy ✦ Interactive sunburst chart mapping the flow of capital across segments</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    df_sun = df.sort_values('community_votes', ascending=False).groupby('segment').head(5).reset_index(drop=True)
    df_sun['Global Market'] = 'Global Market'
    
    fig_sun = px.sunburst(df_sun, path=['Global Market', 'segment', 'brand', 'name'], values='community_votes', color='segment', color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass Market':'#555'}, template="plotly_dark")
    fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
    st.plotly_chart(fig_sun, use_container_width=True)

with tabs[2]:
    st.markdown('<div class="tab-intro">Empirical evidence and strategic case studies ✦ Analyzing specific assets through the lens of the Barbell Strategy</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Empirical Evidence ✦ Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Case Study", sorted(df['name'].tolist()), label_visibility="collapsed")
    f_data = df[df['name'] == f_choice].iloc[0]
    
    if f_data['segment'] == 'Niche':
        strat_label = "Identity Shielding Asset"
        strat_desc = "Inelastic demand profile ✦ High cognitive value shielding consumers from digital noise ✦ Immune to Section 122 shocks"
    elif f_data['segment'] == 'Mass Market':
        strat_label = "Smart Efficiency ✦ Dopamine Hacking"
        strat_desc = "Capturing the squeezed middle class ✦ High performance to price ratio ✦ Beneficiary of the Minus 1.81 elasticity shift"
    else:
        strat_label = "The Squeezed Middle"
        strat_desc = "Highly sensitive to price elasticity ✦ Most impacted by Section 122 tariffs ✦ Requires urgent transition to biotech value"

    vault_html = f"""<div style="border: 2px solid #D4AF37; padding: 4px; background: #000; margin: 15px auto; max-width: 95%; box-shadow: 0 0 30px rgba(212,175,55,0.15);">
<div style="border: 1px solid rgba(212,175,55,0.4); background: radial-gradient(circle at 50% 50%, #0a0a0a 0%, #000000 100%); padding: 30px 15px; text-align: center;">
<div class="vault-main-title" style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 10px;">{f_data['name']}</div>
<div style="color: #D4AF37; font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 20px;">{f_data['brand']} ✦ {f_data['segment']}</div>
<div class="strat-box-mobile" style="background: rgba(212,175,55,0.05); border: 1px solid rgba(212,175,55,0.2); padding: 15px 30px; margin: 0 auto 30px auto; border-radius: 2px; max-width: 800px;">
<div style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; margin-bottom:8px; text-transform:uppercase; font-weight:bold;">Strategic Market Context ✦ {strat_label}</div>
<div style="color: #ccc; font-size: 0.85rem; font-style: italic; letter-spacing: 1px;">{strat_desc}</div>
</div>
<div class="vault-stats-container" style="display: flex; justify-content: center; gap: 20px; margin-bottom: 20px; flex-wrap: wrap;">
<div class="vault-stat-box" style="border: 2px solid #D4AF37; background: linear-gradient(145deg, #1a1500 0%, #050505 100%); padding: 4px; min-width: 200px; flex: 1;">
<div style="border: 1px solid rgba(212,175,55,0.3); padding: 15px 20px; height: 100%;">
<div style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; margin-bottom:10px; text-transform:uppercase;">Quality Score</div>
<div style="color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2.5rem; line-height: 1.2; margin: 0;">{f_data['community_score']:.1f} / 5.0</div>
</div>
</div>
<div class="vault-stat-box" style="border: 2px solid #D4AF37; background: linear-gradient(145deg, #1a1500 0%, #050505 100%); padding: 4px; min-width: 200px; flex: 1;">
<div style="border: 1px solid rgba(212,175,55,0.3); padding: 15px 20px; height: 100%; display: flex; flex-direction: column; justify-content: center;">
<div style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; margin-bottom:10px; text-transform:uppercase;">Key Notes</div>
<div style="color: #ccc; font-size: 0.95rem; line-height: 1.4; margin: 0;">{f_data['top_notes'].replace('-', ' ')}</div>
</div>
</div>
</div>
</div>
</div>"""
    st.markdown(vault_html, unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="tab-intro">The analytical infrastructure ✦ Connected applications powering the global predictive forecast</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    
    e1, e2, e3, e4 = st.columns(4)
    
    # Podpięcie Twoich linków pod najbardziej logiczne kategorie
    apps = [
        ("🌍 Aromo Intelligence", "Custom scraping engine for Eurasian markets tracking real-time price fluctuations.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"),
        ("🧬 Kaggle Prediction", "Regression models and viral trend analysis for market forecasting.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("📊 Market Pulse", "The main intelligence hub integrating all strategic research and metrics.", "https://global-fragrance-intelligence-app-fqjkvd9syohbhfpczxgnph.streamlit.app/"),
        ("📡 Deep Research AI", "Macroeconomic analysis engine and predictive asset discovery.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/")
    ]
    
    for col, (name, dsc, link) in zip([e1, e2, e3, e4], apps):
        col.markdown(f"""<div class="project-card">
            <h4 style="color:#D4AF37; margin-top:0; font-size:0.9rem;">{name}</h4>
            <p style="color:#888; font-size:0.7rem;">{dsc}</p>
            <a class="btn-launch" href="{link}" target="_blank">LAUNCH APP</a>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)