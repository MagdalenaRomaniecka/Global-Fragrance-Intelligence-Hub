import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS (HIERARCHY, GOLD TYPOGRAPHY & CENTERING)
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

    /* NAGŁÓWEK GŁÓWNY */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 8px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 30px 60px; text-align: center; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 6px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 10px; font-weight: 300; }
    
    /* METRYKI */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; height: 100%; border-radius: 2px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2rem; margin: 0; }
    
    /* --- HIERARCHIA NAGŁÓWKÓW W RAPORTACH (FIX) --- */
    .transcript-box { 
        font-family: 'Lato', sans-serif; 
        font-size: 1.05rem; 
        line-height: 1.9; 
        color: #dfdfdf; 
        background: #080808; 
        padding: 45px; 
        border: 1px solid #222; 
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        margin-bottom: 25px;
        text-align: justify;
    }

    /* Agresywne wymuszanie stylu dla nagłówków Markdown */
    [data-testid="stMarkdownContainer"] h1 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 2.1rem !important; 
        text-align: center !important; 
        border-bottom: 1px solid #D4AF37 !important; 
        padding-bottom: 15px !important; 
        margin-bottom: 25px !important; 
        text-transform: uppercase !important; 
        letter-spacing: 3px !important;
    }

    [data-testid="stMarkdownContainer"] h2 { 
        color: #F0E68C !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 1.5rem !important; 
        margin-top: 35px !important; 
        text-align: center !important; 
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        border-top: 1px solid #333 !important;
        padding-top: 20px !important;
    }

    [data-testid="stMarkdownContainer"] h3 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 1.2rem !important; 
        margin-top: 25px !important; 
        border-left: 3px solid #D4AF37 !important; 
        padding-left: 15px !important; 
    }

    [data-testid="stMarkdownContainer"] strong { color: #F0E68C !important; font-weight: 700 !important; }

    /* VAULT CARD & OTHERS */
    .vault-card { border: 1px solid #D4AF37; background: #050505; padding: 45px 25px; text-align: center; border-radius: 2px; box-shadow: 0 0 30px rgba(212,175,55,0.15); }
    .vault-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.4rem; letter-spacing: 3px; }
    .btn-launch { display:block; width:100%; padding:12px; background:#D4AF37; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.75rem; text-decoration:none; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.4rem; border-left: 4px solid #D4AF37; padding-left: 18px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 2px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER & KPI
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Fragrance Intelligence</h1>
                <div class="sub-title">Global Strategic Hub • Predictive Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
metrics = [("Global Beauty Market", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Intelligence Precision", "91%")]
for col, (lab, val) in zip([c1, c2, c3, c4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAG_VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.4], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Intelligence Briefing Series:", [
            "🎧 Ep. 1: Recession Glam & 2025 Market", 
            "🔮 Ep. 2: 2026 Outlook & AI Architecture",
            "🌍 Ep. 3: The European Barbell & Poland"
        ], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_t, current_a, report_f = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title, desc = "Notes_Gourmand", "The Gourmand 2.0 Movement", "Analyzing 'The Lipstick Effect' and Sol de Janeiro's dominance."
        elif "Ep. 2" in episode:
            current_t, current_a, report_f = "podcast_transcript_2026.md", "podcast_2026.mp3", "macro_report_2026.md"
            f_type, v_title, desc = "None", "2026 Global Projections", "Deep dive into AI architecture and neuro-perfumery."
        else: # Ep 3
            current_t, current_a, report_f = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "macro_report_2026.md"
            f_type, v_title, desc = "Barbell", "The Barbell Market Structure 2026", "Bifurcation of the EU market: High-end vs. Extreme Budget."

        st.audio(current_a)
        st.markdown(f'<p style="color:#888; font-size:0.85rem; font-style:italic; margin-top:15px; border-left: 2px solid #333; padding-left: 15px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data: {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            b_counts = b_counts.sort_values('Tier')
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#D4AF37', marker_line_width=2)
        else:
            df_v = df.copy()
            if f_type == "Notes_Gourmand": df_v = df_v[df_v['top_notes'].str.contains('Vanilla|Pistachio', case=False, na=False)]
            df_t = df_v.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#D4AF37', marker_line_width=1.5)
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", showlegend=False, height=420)
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 READ EXECUTIVE SUMMARY TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="transcript-box">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
    with d2:
        report_label = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(report_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="transcript-box">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report file '{report_f}' not found.")

# ... (Reszta zakładek Market Analytics, Vault i Ecosystem pozostaje bez zmian)