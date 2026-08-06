import streamlit as st
import plotly.express as px
import pandas as pd
import os
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
    
    .section-header { 
        color: #D4AF37; 
        font-family: 'Tenor Sans'; 
        font-size: 1.4rem; 
        text-align: center !important; 
        border-bottom: 1px solid #D4AF37; 
        padding-bottom: 10px; 
        margin: 30px auto 20px auto; 
        text-transform: uppercase; 
        letter-spacing: 3px; 
        width: 100%;
    }
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 10px; background-color: #0E0E0E; }
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
        if filename in files:
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
metrics = [("Global Beauty Market", "$593B"), ("EU Trade Surplus", "€238B"), ("Poland PPP 2026", "> Japan"), ("Prestige Elasticity", "-1.81")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["STRATEGIC BRIEFINGS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_nav, col_viz = st.columns([1, 1.5], gap="large")
    with col_nav:
        st.markdown('<div class="section-header">Executive Selection</div>', unsafe_allow_html=True)
        episode = st.radio("Selection:", [
            "🏛️ Ep. 0: Global Foundation", 
            "🎧 Ep. 1: Recession Glam", 
            "📊 Ep. 2: Global Trade", 
            "🔮 Ep. 3: 2026 Outlook", 
            "🌍 Ep. 4: European Barbell", 
            "🎓 Ep. 5: Carto AI & Neuro-Tech",
            "🎓 Ep. 6: B2B Price Elasticity",
            "🎓 Ep. 7: EU Regulatory Shock",
            "🧬 Ep. 8: Master Synthesis"
        ], label_visibility="collapsed")
        
        if "Ep. 0" in episode:
            current_t, current_a, rep_file = None, None, "master_prologue.md"
            f_type, v_title, desc = "None", "Macroeconomic Foundations 2026", "The 5T Nvidia era, EU 2023/1545 shock, and Givaudan MoodScentz™+ integration."
        elif "Ep. 1" in episode:
            current_t, current_a, rep_file = "podcast_transcript.md", "podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title, desc = "Popularity", "Global Popularity Ranking", "Analyzing Lattafa viral surge and Givaudan MoodScentz™ neuro-active solutions."
        elif "Ep. 2" in episode:
            current_t, current_a, rep_file = "ep2_trade_transcript.md", "ep2_audio.mp3", "ep2_trade_report.md"
            f_type, v_title, desc = "None", "Global Trade Volume 2024", "Deep Research data on US Section 122 tariffs, EU surplus, and Russian autarky (93M units)."
        elif "Ep. 3" in episode:
            current_t, current_a, rep_file = "podcast_transcript_2026.md", "podcast_2026.mp3", "ep3_outlook_report.md"
            f_type, v_title, desc = "None", "2026 Global Projections", "Impact of the 5T Nvidia era, the 2025 Tariff Shock, and negative 1.81 price elasticity."
        elif "Ep. 4" in episode:
            current_t, current_a, rep_file = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "barbell_strategy_2026.md"
            f_type, v_title, desc = "Barbell", "The Barbell Market Structure 2026", "Mapping the European Barbell structure, Poland PPP breakthrough, and 0.28 digital correlation."
        elif "Ep. 5" in episode:
            current_t, current_a, rep_file = "ep5_summary_transcript.md", "ep5_How_AI_engineers_perfumes_for_your_brain.mp3", "master_prologue.md"
            f_type, v_title, desc = "Popularity", "Givaudan Carto AI Infrastructure", "Deep-dive technical breakdown: Algorithmic scent formulation and EEG brainwave mapping."
        elif "Ep. 6" in episode:
            current_t, current_a, rep_file = "ep2_trade_transcript.md", "ep6_The_High_Stakes_Economics_Of_Fragrance.mp3", "ep2_trade_report.md"
            f_type, v_title, desc = "None", "B2B Price Elasticity Vectors", "Advanced macroeconomic regression analyzing consumer behavior under severe inflation."
        elif "Ep. 7" in episode:
            current_t, current_a, rep_file = "ep3_whisper_transcript_EN.md", "ep7_The_Secret_Chemical_Battlefield_of_Luxury_Perfume.mp3", "barbell_strategy_2026.md"
            f_type, v_title, desc = "Barbell", "EU 2023/1545 Regulatory Compliance", "Strategic adaptation strategies for allergen restrictions and synthetic ingredient bans."
        else:
            current_t, current_a, rep_file = "master_synthesis_transcript.md", "ep8_master_synthesis.mp3", "master_synthesis.md"
            f_type, v_title, desc = "None", "Master Strategic Synthesis 2026", "Final dossier compiled via Deep Research and B2B technological architecture curated by Magdalena Romaniecka."

        if current_a:
            target_audio = find_file(current_a)
            if os.path.exists(target_audio):
                st.audio(target_audio)
            else:
                st.markdown(f'<div style="color: #888888; font-size: 0.8rem; font-style: italic;">[Audio file {current_a} pending upload]</div>', unsafe_allow_html=True)
        
        st.markdown(f'<p style="color:#D4AF37; font-size:0.95rem; font-style:italic; margin-top:20px; border-left: 3px solid #D4AF37; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data ✦ {v_title}</div>', unsafe_allow_html=True)
        
        if f_type == "Barbell" and 'market_structure' in df.columns:
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=18, color='#D4AF37'))
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="center", x=0.5))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, yaxis=dict(showgrid=False))
            st.plotly_chart(fig, use_container_width=True)
        
        elif f_type == "Popularity" and 'community_votes' in df.columns and 'name' in df.columns:
            df_t = df.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment" if 'segment' in df.columns else None, text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=15, color='#D4AF37'), cliponaxis=False)
            max_val = df_t['community_votes'].max()
            fig.update_xaxes(range=[0, max_val * 1.35], showgrid=False, showticklabels=False)
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.6, xanchor="center", x=0.5), margin=dict(r=100))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, yaxis=dict(showgrid=False))
            st.plotly_chart(fig, use_container_width=True)
            
        else:
            st.markdown("""
            <div style="height: 450px; display: flex; align-items: center; justify-content: center; border: 1px dashed #333333; border-radius: 4px; background: rgba(18,18,18,0.5);">
                <div style="text-align: center; color: #666666; font-family: 'Lato', sans-serif; letter-spacing: 2px; text-transform: uppercase; font-size: 0.9rem;">
                    ✦ Awaiting active dataset selection ✦<br><br>
                    <span style="font-size: 0.7rem; color: #444444;">Please refer to accompanying audio briefing</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    
    if "Ep. 0" in episode:
        st.markdown('<div class="section-header">Macroeconomic Foundations 2026</div>', unsafe_allow_html=True)
        try:
            with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                content_r = f.read()
                st.markdown(f'<div class="report-frame">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
        except: 
            st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Documentation indexing in progress...</div>', unsafe_allow_html=True)
    else:
        l_col, r_col = st.columns(2, gap="large")
        with l_col:
            st.markdown('<div class="section-header">Executive Audio Debrief</div>', unsafe_allow_html=True)
            if current_t:
                try:
                    with open(find_file(current_t), 'r', encoding='utf-8') as f:
                        content_t = f.read()
                        st.markdown(f'<div class="report-frame">\n\n{content_t}\n\n</div>', unsafe_allow_html=True)
                except: 
                    st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Debrief indexing in progress...</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Technical audio briefing selected. Please refer to the Master Dossier on the right for accompanying documentation.</div>', unsafe_allow_html=True)
        with r_col:
            st.markdown('<div class="section-header">Executive Master Dossier</div>', unsafe_allow_html=True)
            try:
                with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                    content_r = f.read()
                    st.markdown(f'<div class="report-frame">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
            except: 
                st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Dossier indexing in progress...</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="section-header">Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ INTELLIGENCE NOTE: 64% of analyzed Ultra-Niche segments utilize Jungle Essence™ CO2 extraction technologies to justify premium pricing above $350.</div>', unsafe_allow_html=True)

    if 'community_votes' in df.columns and 'segment' in df.columns:
        df_sun = df.sort_values('community_votes', ascending=False).groupby('segment').head(5).reset_index(drop=True)
        df_sun['Global Market'] = 'Global Market'
        
        fig_sun = px.sunburst(df_sun, path=['Global Market', 'segment', 'brand', 'name'], values='community_votes', color='segment', color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555', 'Mass Market':'#555'}, template="plotly_dark")
        fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
        st.plotly_chart(fig_sun, use_container_width=True)

with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    if 'name' in df.columns:
        f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
        f_data = df[df['name'] == f_choice].iloc[0]
        
        intel_note = ""
        if "Phantom" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ B2B CASE STUDY: Designed via Givaudan Carto AI and 45M EEG brainwave measurements to optimize confidence-boosting neuro-responses.</div>'
        elif "Idôle" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ ECO-INNOVATION: Features ultra-thin 15mm glass technology reducing carbon footprint by 63% via Givaudan sustainability stack.</div>'
        elif "Libre" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ MOLECULAR DESIGN: Features proprietary Diva Lavender and Vanilla Caviar molecular hybrids developed in Givaudan laboratories.</div>'

        score_val = f_data.get('community_score', 4.5)
        notes_val = f_data.get('top_notes', "Proprietary Accord Stack")
        brand_val = f_data.get('brand', "Global Brand")
        seg_val = f_data.get('segment', "Prestige")

        st.markdown(f"""
        <div style="background-color: #0E0E0E; border: 2px solid #D4AF37; border-radius: 4px; padding: 40px; margin: 20px auto; max-width: 850px; text-align: center; box-shadow: 0 0 25px rgba(212,175,55,0.15);">
            <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.6rem; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 8px;">{f_data['name']}</div>
            <div style="font-family: 'Lato', sans-serif; color: #888888; font-size: 0.85rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 35px;">{brand_val} ✦ {seg_val}</div>
            <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 20px; flex-wrap: wrap;">
                <div style="border: 1px solid rgba(212,175,55,0.4); background: #121212; padding: 20px 30px; flex: 1; min-width: 220px;">
                    <div style="color: #888888; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;">Quality Score</div>
                    <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 3rem; line-height: 1.1;">{score_val:.1f} / 5.0</div>
                </div>
                <div style="border: 1px solid rgba(212,175,55,0.4); background: #121212; padding: 20px 30px; flex: 1; min-width: 220px; display: flex; flex-direction: column; justify-content: center;">
                    <div style="color: #888888; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;">Key Notes</div>
                    <div style="font-family: 'Lato', sans-serif; color: #E0E0E0; font-size: 1.05rem; line-height: 1.5;">{notes_val}</div>
                </div>
            </div>
            {intel_note}
        </div>
        """, unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    apps = [
        ("🧬 ScentSational AI", "AI Concierge providing personalized signature scent recommendations.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("📊 Perfume Finder", "Interactive database for manual filtering and exploring fragrance profiles.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📡 Hugging Face LFS2", "Advanced machine learning models and datasets mapping social sentiment.", "https://huggingface.co/spaces/Baphomert/ScentSational-Fragrantica-LFS2"),
        ("🌍 Market Pulse Hub", "Dashboard integrating Deep Research data with live macro tracking.", "https://github.com/MagdalenaRomaniecka")
    ]
    for col, (name, dsc, link) in zip([e1, e2, e3, e4], apps):
        col.markdown(f"""<div class="project-card">
            <h4 style="color:#D4AF37; margin-top:0; font-size:0.9rem;">{name}</h4>
            <p style="color:#888888; font-size:0.7rem;">{dsc}</p>
            <a class="btn-launch" href="{link}" target="_blank">LAUNCH APP</a>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)