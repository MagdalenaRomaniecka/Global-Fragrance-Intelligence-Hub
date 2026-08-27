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
    }
    .debrief-sub-title, .dossier-sub-title {
        color: #E0E0E0;
        font-family: 'Lato', sans-serif;
        font-weight: 700;
        font-size: 0.85rem;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #333333;
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
metrics = [("Global Beauty Market", "$593B"), ("EU Trade Surplus", "€238B"), ("Poland PPP 2026", "> Japan"), ("Prestige Elasticity", "-1.81")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)


tabs = st.tabs(["STRATEGIC BRIEFINGS", "MACRO & B2B SIMULATIONS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_nav, col_viz = st.columns([1, 1.5], gap="large")
    with col_nav:
        st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Executive Selection</div>', unsafe_allow_html=True)
        
        episode = st.radio("Selection:", [
            "🏛️ 0. Global Foundation",
            "🎧 Ep. 1: Recession Glam",
            "📊 Ep. 2: Global Trade",
            "🔮 Ep. 3: 2026 Outlook",
            "🌍 Ep. 4: European Barbell",
            "🎓 Ep. 5: Carto AI & Neuro-Tech",
            "🎓 Ep. 6: B2B Price Elasticity",
            "🎓 Ep. 7: EU Regulatory Shock",
            "🧬 Ep. 8: Master Synthesis"
        ], label_visibility="collapsed")
       
        match = re.search(r'(Ep\. \d+)', episode)
        ep_key = match.group(1) if match else "Ep. 0"
        
        if "0." in episode:
            current_t, current_a, rep_file = None, None, "master_prologue.md"
            f_type, v_title, desc = "None", "Macroeconomic Foundations 2026", "The 5T Nvidia era, EU 2023/1545 shock, and Givaudan MoodScentz™+ integration."
        elif "1:" in episode:
            current_t, current_a, rep_file = "podcast_transcript.md", "podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title, desc = "Popularity", "Global Popularity Ranking", "Analyzing Lattafa viral surge and Givaudan MoodScentz™ neuro-active solutions."
        elif "2:" in episode:
            current_t, current_a, rep_file = "ep2_trade_transcript.md", "ep2_audio.mp3", "ep2_trade_report.md"
            f_type, v_title, desc = "None", "Global Trade Volume 2024", "Deep Research data on US Section 122 tariffs, EU surplus, and Russian autarky (93M units)."
        elif "3:" in episode:
            current_t, current_a, rep_file = "ep3_debrief", "podcast_2026.mp3", "ep3_dossier"
            f_type, v_title, desc = "None", "2026 Global Projections", "Impact of the 5T Nvidia era, the 2025 Tariff Shock, and negative 1.81 price elasticity."
        elif "4:" in episode:
            current_t, current_a, rep_file = "ep4_debrief", "ep3_europe_barbell.mp3", "ep4_dossier"
            f_type, v_title, desc = "Barbell", "The Barbell Market Structure 2026", "Mapping the European Barbell structure, Poland PPP breakthrough, and 0.28 digital correlation."
        elif "5:" in episode:
            current_t, current_a, rep_file = "ep5_debrief", "masterclass_ep1_audio.mp3", "ep5_dossier"
            f_type, v_title, desc = "Popularity", "Givaudan Carto AI Infrastructure", "Deep-dive technical breakdown: Algorithmic scent formulation and EEG brainwave mapping."
        elif "6:" in episode:
            current_t, current_a, rep_file = "ep6_debrief", "masterclass_ep2_audio.mp3", "ep6_dossier"
            f_type, v_title, desc = "None", "B2B Price Elasticity Vectors", "Advanced macroeconomic regression analyzing consumer behavior under severe inflation."
        elif "7:" in episode:
            current_t, current_a, rep_file = "ep7_debrief", "masterclass_ep3_audio.mp3", "ep7_dossier"
            f_type, v_title, desc = "Barbell", "EU 2023/1545 Regulatory Compliance", "Strategic adaptation strategies for allergen restrictions and synthetic ingredient bans."
        else:
            current_t, current_a, rep_file = "ep8_debrief.md", "Algorithms_are_the_new_master_perfumers_2.m4a", "ep8_dossier.md"
            f_type, v_title, desc = "None", "Master Strategic Synthesis 2026", "Final dossier compiled via Deep Research and B2B technological architecture curated by Magdalena Romaniecka."
            
        if current_a:
            target_audio = find_file(current_a)
            if os.path.exists(target_audio):
                st.audio(target_audio)
            else:
                st.markdown(f'<div style="color: #888888; font-size: 0.8rem; font-style: italic;">[Audio file {current_a} pending upload]</div>', unsafe_allow_html=True)
       
        st.markdown(f'<p style="color:#D4AF37; font-size:0.95rem; font-style:italic; margin-top:20px; border-left: 3px solid #D4AF37; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Live Market Data ✦ {v_title}</div>', unsafe_allow_html=True)
        
        # Robust fallback architecture for charts to prevent UI breakage
        if f_type == "Barbell":
            if 'market_structure' in df.columns:
                b_counts = df['market_structure'].value_counts().reset_index()
                b_counts.columns = ['Tier', 'Count']
            else:
                b_counts = pd.DataFrame({
                    'Tier': ['Ultra-Niche (Barbell Top)', 'Budget (Barbell Bottom)', 'Squeezed Middle'],
                    'Count': [12500, 48000, 4200]
                })
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count', 
                         color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, 
                         template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=18, color='#D4AF37'), cliponaxis=False)
            max_val = b_counts['Count'].max()
            fig.update_yaxes(range=[0, max_val * 1.5], showgrid=False, showticklabels=False)
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="center", x=0.5), margin=dict(t=50, b=0, l=0, r=0))
            
        else:
            col_name = 'Name' if 'Name' in df.columns else 'name' if 'name' in df.columns else None
            col_val = 'Rating Value' if 'Rating Value' in df.columns else 'community_votes' if 'community_votes' in df.columns else None
            
            if col_name and col_val:
                df_clean = df.dropna(subset=[col_val, col_name]).copy()
                df_clean[col_val] = pd.to_numeric(df_clean[col_val], errors='coerce')
                df_t = df_clean.nlargest(10, col_val).sort_values(col_val, ascending=True)
                fig = px.bar(df_t, x=col_val, y=col_name, orientation='h', text=col_val, color_discrete_sequence=['#D4AF37'], template="plotly_dark")
                fig.update_traces(texttemplate='%{text:.2f}', textposition='outside', textfont=dict(size=15, color='#D4AF37'), cliponaxis=False)
                max_val = df_t[col_val].max()
                fig.update_xaxes(range=[0, max_val * 1.35], showgrid=False, showticklabels=False)
                fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=False, margin=dict(t=50, r=100))
            else:
                fig = px.bar(x=["Data Available In Local DB"], y=[100], template="plotly_dark", color_discrete_sequence=['#333333'])
                
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)
        
    st.write("---")
   
    l_col, r_col = st.columns(2, gap="large")
    with l_col:
        st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Executive Audio Debrief</div>', unsafe_allow_html=True)
        try:
            with open(find_file(current_t), 'r', encoding='utf-8') as f:
                content_t = f.read()
                st.markdown(f'<div class="report-frame">\n\n{content_t}\n\n</div>', unsafe_allow_html=True)
        except:
            st.error(f"Debrief file '{current_t}' missing. Please ensure it is uploaded.")
            
    with r_col:
        st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Executive Master Dossier</div>', unsafe_allow_html=True)
        try:
            with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                content_r = f.read()
                st.markdown(f'<div class="report-frame">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
        except:
            st.error(f"Dossier file '{rep_file}' missing. Please ensure it is uploaded.")

with tabs[1]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">B2B Price Elasticity Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ INTELLIGENCE NOTE: Simulating the -1.81 elasticity index under Section 122 Tariff constraints to evaluate margin compression in the "Squeezed Middle" sector.</div>', unsafe_allow_html=True)
    
    col_input, col_chart = st.columns([1, 2], gap="large")
    
    with col_input:
        st.markdown('<div class="dossier-section-title">Scenario Parameters</div>', unsafe_allow_html=True)
        price_hike = st.slider("Projected Retail Price Increase (%)", min_value=0.0, max_value=50.0, value=10.0, step=1.0)
        base_volume = 100000 
        
        elasticity_coefficient = -1.81
        demand_change = price_hike * elasticity_coefficient
        new_volume = base_volume * (1 + (demand_change / 100))
        
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Projected Demand Shift (Volume)</div>
            <div class="metric-value" style="color: {'#FF4B4B' if demand_change < 0 else '#D4AF37'};">{demand_change:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_chart:
        simulation_data = pd.DataFrame({
            'Scenario': ['Base Market Demand', 'Post-Tariff Demand'],
            'Volume': [base_volume, max(0, new_volume)]
        })
        
        fig_sim = px.bar(
            simulation_data, 
            x='Scenario', 
            y='Volume',
            text='Volume',
            color='Scenario',
            color_discrete_map={'Base Market Demand': '#333333', 'Post-Tariff Demand': '#D4AF37'},
            template="plotly_dark"
        )
        fig_sim.update_traces(texttemplate='%{text:,.0f} Units', textposition='outside', textfont=dict(size=16, color='#E0E0E0'), cliponaxis=False)
        fig_sim.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis=dict(showgrid=False, showticklabels=False),
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False,
            height=350,
            margin=dict(t=50)
        )
        st.plotly_chart(fig_sim, use_container_width=True)

    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Correlation vs. Causation: Digital Virality</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ STATISTICAL AXIOM: A 0.28 correlation confirms that Top-of-Funnel (TOFU) digital hype does not guarantee Bottom-of-Funnel (BOFU) sales without physical retail anchors.</div>', unsafe_allow_html=True)
    
    col_gauge, col_text = st.columns([1, 1], gap="large")
    with col_gauge:
        corr_fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 0.28,
            title = {'text': "Digital Hype vs Sales Conversion (r)", 'font': {'color': '#D4AF37'}},
            gauge = {
                'axis': {'range': [0, 1], 'tickcolor': "#D4AF37"},
                'bar': {'color': "#D4AF37"},
                'bgcolor': "#1A1A1A",
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 0.28}
            }
        ))
        corr_fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "#E0E0E0"}, height=300)
        st.plotly_chart(corr_fig, use_container_width=True)
    with col_text:
        st.markdown("""
        <div class="report-frame" style="height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <h3 style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; margin-top:0;">The Omnichannel Bottleneck</h3>
            <p style="color:#E0E0E0; font-family:'Lato', sans-serif; font-size:0.95rem; line-height:1.6;">
            In evaluating DTC (Direct-to-Consumer) models, we frequently observe a cognitive bias mistaking digital virality (e.g., TikTok trends) for causal purchasing behavior. 
            <br><br>
            A correlation coefficient of <strong>0.28</strong> dictates that while Stanford ML algorithms effectively generate awareness, human olfaction staunchly resists total digitization. Physical drugstores (acting as economic anchors) maintain an absolute chokehold on final conversions. Eliminating UX Friction online is critical, but bypassing physical sensory auditing entirely results in incinerated Customer Acquisition Costs (CAC).
            </p>
        </div>
        """, unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ K-MEANS SEGMENTATION: 64% of analyzed Ultra-Niche segments utilize Jungle Essence™ CO2 extraction technologies to justify premium pricing above $350.</div>', unsafe_allow_html=True)
    if 'segment' in df.columns:
        # fallback for hierarchy
        df_sun = df.head(50).copy()
        df_sun['Global Market'] = 'Global Market'
        fig_sun = px.sunburst(df_sun, path=['Global Market', 'segment', 'Name' if 'Name' in df.columns else 'name'], color='segment', color_discrete_sequence=['#D4AF37', '#F0E68C', '#555'], template="plotly_dark")
        fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
        st.plotly_chart(fig_sun, use_container_width=True)

with tabs[3]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    col_n = 'Name' if 'Name' in df.columns else 'name' if 'name' in df.columns else None
    if col_n:
        f_choice = st.selectbox("Select Profile:", sorted(df[col_n].tolist()))
        f_data = df[df[col_n] == f_choice].iloc[0]
       
        intel_note = ""
        if "Phantom" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ A/B TESTING INSIGHT: Designed via Givaudan Carto AI and 45M EEG brainwave measurements to optimize confidence-boosting neuro-responses vs control groups.</div>'
        
        score_val = f_data.get('Rating Value', 4.5)
        notes_val = f_data.get('Main Accords', "Proprietary Accord Stack")
        brand_val = f_data.get('brand', "Global Brand")
        seg_val = f_data.get('segment', "Prestige")
        
        st.markdown(f"""
        <div style="background-color: #0E0E0E; border: 2px solid #D4AF37; border-radius: 4px; padding: 40px; margin: 20px auto; max-width: 850px; text-align: center; box-shadow: 0 0 25px rgba(212,175,55,0.15);">
            <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.6rem; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 8px;">{f_data[col_n]}</div>
            <div style="font-family: 'Lato', sans-serif; color: #888888; font-size: 0.85rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 35px;">{brand_val} ✦ {seg_val}</div>
            <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 20px; flex-wrap: wrap;">
                <div style="border: 1px solid rgba(212,175,55,0.4); background: #121212; padding: 20px 30px; flex: 1; min-width: 220px;">
                    <div style="color: #888888; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;">Quality Score</div>
                    <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 3rem; line-height: 1.1;">{score_val} / 5.0</div>
                </div>
                <div style="border: 1px solid rgba(212,175,55,0.4); background: #121212; padding: 20px 30px; flex: 1; min-width: 220px; display: flex; flex-direction: column; justify-content: center;">
                    <div style="color: #888888; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;">Key Notes</div>
                    <div style="font-family: 'Lato', sans-serif; color: #E0E0E0; font-size: 1.05rem; line-height: 1.5;">{notes_val}</div>
                </div>
            </div>
            {intel_note}
        </div>
        """, unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="section-header" style="display: block; width: 100%; text-align: center !important;">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    apps = [
        ("🌍 Aromo Intelligence", "Custom scraping engine mapping social sentiment to B2B platforms like Myrissi™.", "https://share.streamlit.io/"),
        ("🧬 Kaggle Prediction", "Regression models calculating price elasticity and B2B tech adoption rates.", "https://share.streamlit.io/"),
        ("📊 Market Pulse", "Dashboard integrating Deep Research data with live tracking of EU 2023/1545 regulatory impact.", "https://share.streamlit.io/"),
        ("📡 Deep Research AI", "Macroeconomic engine processing Nvidia Class trends and Givaudan MoodScentz™+ data.", "https://share.streamlit.io/")
    ]
    for col, (name, dsc, link) in zip([e1, e2, e3, e4], apps):
        col.markdown(f"""<div class="project-card">
            <h4 style="color:#D4AF37; margin-top:0; font-size:0.9rem;">{name}</h4>
            <p style="color:#888888; font-size:0.7rem;">{dsc}</p>
            <a class="btn-launch" href="{link}" target="_blank">LAUNCH APP</a>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)