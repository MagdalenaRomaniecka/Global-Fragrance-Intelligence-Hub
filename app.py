import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS (MOBILE-FIRST LUXURY: SMALLER FONTS & RESPONSIVE FRAMES)
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

    /* NAGŁÓWEK GŁÓWNY - ZMNIEJSZONY I ELASTYCZNY */
    .header-wrapper { display: flex; justify-content: center; padding: 15px 0 10px 0; }
    .header-outer { border: 0.5px solid #444; padding: 5px; display: inline-block; width: auto; max-width: 500px; }
    .header-inner { border: 0.5px solid #D4AF37; padding: 15px 30px; text-align: center; background-color: #050505; box-shadow: inset 0 0 15px rgba(212,175,55,0.08); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 1.8rem; text-transform: uppercase; letter-spacing: 3px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 5px; font-weight: 300; }
    
    /* METRYKI KPI - ZMNIEJSZONE */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 10px; text-align: center; transition: 0.3s; height: 100%; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.15); transform: translateY(-1px); }
    .metric-label { color: #666; font-size: 0.55rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; font-weight: 700; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.4rem; margin: 0; }
    
    /* SEKCJE RAPORTÓW (TRANSCRIPT BOX) - ZMNIEJSZONE CZCIONKI & PADDING */
    .transcript-box { font-family: 'Lato', sans-serif; font-size: 0.9rem; line-height: 1.6; color: #dfdfdf; background: #080808; padding: 20px; border: 1px solid #222; box-shadow: 0 5px 15px rgba(0,0,0,0.4); text-align: justify; }
    .transcript-box h1 { color: #D4AF37 !important; font-family: 'Tenor Sans', sans-serif !important; font-size: 1.3rem !important; text-align: center; border-bottom: 0.5px solid #D4AF37; padding-bottom: 10px; margin-bottom: 15px; text-transform: uppercase; }
    .transcript-box h2 { color: #F0E68C !important; font-family: 'Tenor Sans', sans-serif !important; font-size: 1.1rem !important; border-top: 1px solid #333; padding-top: 15px; margin-top: 20px; text-align: center; }
    .transcript-box strong { color: #F0E68C; font-weight: 700; }

    /* MOBILE ADJUSTMENTS (< 768px) */
    @media (max-width: 768px) {
        .main-title { font-size: 1.3rem; letter-spacing: 1.5px; }
        .metric-value { font-size: 1.1rem; }
        .transcript-box { padding: 10px; font-size: 0.85rem; }
    }

    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.1rem; border-left: 3px solid #D4AF37; padding-left: 10px; margin: 20px 0 10px 0; text-transform: uppercase; letter-spacing: 1px; }
    .project-card { border:1px solid #222; background:rgba(15,15,15,0.9); padding:15px; transition:0.3s; height:100%; display:flex; flex-direction:column; justify-content:space-between; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:8px; background:#D4AF37; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.65rem; text-decoration:none; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 1px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. KPI
# -----------------------------------------------------------------------------
st.markdown("""<div class="header-wrapper"><div class="header-outer"><div class="header-inner"><h1 class="main-title">Fragrance Intelligence</h1><div class="sub-title">Atelier strategic hub • Predictive Forecast</div></div></div></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Beauty Market", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth", "+75.3%"), ("Precision", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "ANALYTICS", "VAULT", "OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.4], gap="medium")
    with col_audio:
        st.markdown('<div class="section-header">Audio Briefing Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Intelligence Briefing Series:", [
            "Ep. 1: 2025 Market Trends", 
            "Ep. 2: 2026 outlook",
            "Ep. 3: European Barbell"
        ], label_visibility="collapsed")
        
        # LOGIC: Force Report 2026 for Episode 2 and 3
        current_p = episode.split(': ')[0]
        
        if current_p == "Ep. 1":
            current_t, current_a, report_f = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title = "Notes_Gourmand", "Top Gourmand Trends"
        elif current_p == "Ep. 2":
            current_t, current_a, report_f = "podcast_transcript_2026.md", "podcast_2026.mp3", "macro_report_2026.md"
            f_type, v_title = "None", "2026 Global Projections"
        else: # Ep 3
            current_t, current_a, report_f = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "macro_report_2026.md"
            f_type, v_title = "Barbell", "The European Barbell Structure 2026"

        st.audio(current_a)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Feed: {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            fig = px.bar(b_counts.sort_values('Tier'), x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
        else:
            df_v = df.copy()
            if f_type == "Notes_Gourmand": 
                df_v = df_v[df_v['top_notes'].str.contains('Vanilla|Pistachio', case=False, na=False)]
            
            # POPRAWKA WIZUALNA: Top 5 najpopularniejszych gourmandów
            df_t = df_v.nlargest(5, 'community_votes').sort_values('community_votes', ascending=True)
            
            # Czysty styl bez segmentów, tylko czyste Atelier
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', text="community_votes", 
                         color_discrete_sequence=['#D4AF37'], # Czyste złoto
                         template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#000', marker_line_width=1)
            
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", showlegend=False, height=300)
        
        # POPRAWKA CZYTELNOŚCI: Usunięcie siatki
        fig.update_xaxes(showgrid=False, title="")
        fig.update_yaxes(showgrid=False, title="")
        
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 Executive Summary TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f: st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
    with d2:
        report_label = "📈 READ 2025 TREND REPORT" if current_p == "Ep. 1" else "📈 READ 2026 MACRO REPORT"
        with st.expander(report_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f: st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.info(f"Report file '{report_f}' not found in the directory.")

# ... (Analytics, Vault, Outlook, Ecosystem tabs remain logic-consistent, but now smaller fonts from global CSS)