import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    .stApp { background-color: #000000; background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%); font-family: 'Lato', sans-serif !important; }
    [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2 { text-align: center !important; justify-content: center !important; display: flex !important; width: 100% !important; }
    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 40px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 10px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 50px; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 5px; margin: 0; border: none !important; }
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; font-size: 1.8rem !important; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-transform: uppercase !important; border-top: 1px solid #333 !important; padding-top: 30px !important; margin-top: 45px !important; font-size: 1.4rem !important; }
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 8px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }
    .report-frame { background: #080808; padding: 45px; border: 1px solid #222; box-shadow: 0 15px 40px rgba(0,0,0,0.6); color: #dfdfdf; line-height: 1.9; text-align: justify; margin-bottom: 30px; font-size: 1.05rem; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.4rem; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 3px; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 20px; }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p { text-align: center !important; font-family: 'Tenor Sans', sans-serif !important; letter-spacing: 2px; }
    .project-card { border:1px solid #222; background:rgba(15,15,15,0.95); padding:25px; transition:0.3s; height:100%; display:flex; flex-direction:column; justify-content:space-between; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:12px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.75rem; text-decoration:none; letter-spacing: 1px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

st.markdown("""<div class="header-wrapper"><div class="header-outer"><div class="header-inner"><h1 class="main-title">Fragrance Intelligence</h1>
<div style="font-family: 'Lato', color: #888, font-size: 0.8rem, text-transform: uppercase, letter-spacing: 4px, margin-top: 10px;">Global Strategic Hub ✦ Predictive Forecast 2026</div></div></div></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Market", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Intelligence Precision", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["STRATEGIC BRIEFINGS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Selection:", [
            "🎧 Ep. 1: Recession Glam and 2025 Market", 
            "📊 Ep. 2: Global Trade and Russian Autarky",
            "🔮 Ep. 3: 2026 Outlook and AI Architecture", 
            "🌍 Ep. 4: The European Barbell and Poland",
            "🧬 Ep. 5: Strategic Synthesis"
        ], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_t, current_a = "podcast_transcript.md", "podcast_trends.mp3"
            f_type, v_title = "Popularity", "Global Popularity Ranking"
            desc = "Analyzing Recession Glam and Sol de Janeiro dominance."
            rep_file, rep_title = "trend_report_2025.md", "📊 READ 2025 TREND REPORT: RECESSION GLAM"
        elif "Ep. 2" in episode:
            current_t, current_a = "ep2_trade_transcript.md", "ep2_audio.mp3"
            f_type, v_title = "None", "Global Trade Volume 2024"
            desc = "Hard data analysis of USA imports EU surplus and Russian domestic production records."
            rep_file, rep_title = "ep2_trade_report.md", "📊 READ GLOBAL TRADE AND AUTARKY REPORT"
        elif "Ep. 3" in episode:
            current_t, current_a = "podcast_transcript_2026.md", "podcast_2026.mp3"
            f_type, v_title = "None", "2026 Global Projections"
            desc = "Deep dive into the 5T AI era and the 2025 Tariff Shock."
            rep_file, rep_title = "macro_report_2026.md", "📈 READ 2026 MACROECONOMIC REPORT"
        elif "Ep. 4" in episode:
            current_t, current_a = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3"
            f_type, v_title = "Barbell", "The Barbell Market Structure 2026"
            desc = "Mapping the European Barbell structure and Poland rising PPP."
            rep_file, rep_title = "barbell_strategy_2026.md", "⚖️ READ 2026 EUROPEAN BARBELL STRATEGY"
        else:
            current_t, current_a = "ep5_summary_transcript.md", "ep5_audio.mp3"
            f_type, v_title = "None", "Strategic Synthesis 2025 to 2026"
            desc = "Final dossier powered by Google Deep Research and analysis by Magdalena Romaniecka."
            rep_file, rep_title = "ep5_summary_report.md", "🧬 READ MASTER STRATEGIC SYNTHESIS"

        st.audio(current_a)
        st.markdown(f'<p style="color:#888; font-size:0.9rem; font-style:italic; margin-top:20px; border-left: 3px solid #333; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data ✦ {v_title}</div>', unsafe_allow_html=True)
        
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            
            fig = px.bar(b_counts.sort_values('Tier'), x='Tier', y='Count', color='Tier', text='Count', 
                         color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=18, color='#D4AF37', family="Tenor Sans"))
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=False, xaxis=dict(showgrid=False, tickfont=dict(size=13, color='#bbb')), yaxis=dict(showgrid=False, showticklabels=False))
            fig.update_yaxes(range=[0, b_counts['Count'].max() * 1.3])
            
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, margin=dict(t=20, b=10, l=10, r=10))
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('<p style="color:#666; font-size:0.75rem; text-align:right; font-style:italic; letter-spacing:1px;">Data Origin: Macroeconomic Market Segmentation Forecast 2026</p>', unsafe_allow_html=True)
        else:
            # SORTOWANIE I LUXURY KOLORY DLA GŁÓWNEGO WYKRESU
            df_t = df.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", text="community_votes", 
                         color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=15, color='#D4AF37', family="Lato"))
            fig.update_layout(xaxis_title=None, yaxis_title=None, legend_title_text=None, xaxis=dict(showgrid=False, showticklabels=False), yaxis=dict(showgrid=False, tickfont=dict(size=13, color='#ddd')))
            fig.update_xaxes(range=[0, df_t['community_votes'].max() * 1.3])
            
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, margin=dict(t=20, b=10, l=10, r=10))
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('<p style="color:#666; font-size:0.75rem; text-align:right; font-style:italic; letter-spacing:1px;">Data Intelligence: Fragrantica and Aromo Sentiment Engines (Historical Aggregation 2020 to 2024)</p>', unsafe_allow_html=True)

    st.write("---")
    st.markdown('<div class="section-header">Intelligence Library</div>', unsafe_allow_html=True)
    c_left, c_right = st.columns(2, gap="large")
    with c_left:
        with st.expander("📄 READ EXECUTIVE AUDIO DEBRIEF"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Debrief missing.")
    with c_right:
        with st.expander(rep_title):
            try:
                with open(rep_file, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.info("Report missing.")

with tabs[1]:
    st.markdown('<div class="section-header">Market Segmentation Strategic Hierarchy</div>', unsafe_allow_html=True)
    df_sunburst = df.groupby('segment').apply(lambda x: x.nlargest(5, 'community_votes')).reset_index(drop=True)
    fig_sun = px.sunburst(df_sunburst, path=[px.Constant("Global Market"), 'segment', 'brand', 'name'], 
                          values='community_votes', color='segment',
                          color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555'},
                          template="plotly_dark")
    fig_sun.update_traces(textfont=dict(family="Lato, sans-serif", size=14), insidetextorientation='auto')
    fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700, font_family="Lato")
    st.plotly_chart(fig_sun, use_container_width=True)

with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
    f_data = df[df['name'] == f_choice].iloc[0]
    st.markdown(f"<div style='border: 2px solid #D4AF37; padding: 50px; background: #000; text-align: center;'><h1 style='color:#D4AF37; border:none;'>{f_data['name']}</h1><p style='color:#888;'>{f_data['brand']} ✦ {f_data['segment']}</p></div>", unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card"><h4 style="color:#D4AF37;">🌍 Aromo Intelligence</h4><p style="color:#888;">Russian market scraping engine.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)