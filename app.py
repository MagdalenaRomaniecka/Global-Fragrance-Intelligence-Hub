import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS - FORCED GOLD HIERARCHY & LUXURY DESIGN
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

    /* GLOBAL HEADERS AGGRESSIVE OVERRIDE (Forced Gold & Aesthetic) */
    h1 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        text-transform: uppercase !important; 
        letter-spacing: 4px !important; 
        text-align: center !important;
        border-bottom: 1px solid #D4AF37 !important;
        padding-bottom: 20px !important;
        font-size: 2.2rem !important;
        margin-bottom: 30px !important;
    }
    h2 { 
        color: #F0E68C !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        text-transform: uppercase !important; 
        letter-spacing: 2px !important; 
        text-align: center !important;
        font-size: 1.6rem !important;
        border-top: 1px solid #333 !important;
        padding-top: 25px !important;
        margin-top: 45px !important;
    }
    h3 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 1.25rem !important;
        border-left: 4px solid #D4AF37 !important;
        padding-left: 15px !important;
        margin-top: 35px !important;
        font-weight: 400 !important;
    }

    /* CENTERED GOLD HEADER FRAME */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 8px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 30px 60px; text-align: center; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title-text { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 6px; margin: 0; }
    
    /* STRATEGIC METRICS */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 25px 15px; text-align: center; transition: 0.3s; height: 100%; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); transform: translateY(-3px); }
    .metric-label { color: #666; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 10px; font-weight: 700; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2rem; margin: 0; }
    
    /* TRANSCRIPT CONTAINER */
    .report-frame { 
        background: #080808; 
        padding: 45px; 
        border: 1px solid #222; 
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        margin-bottom: 25px;
        color: #dfdfdf;
        line-height: 1.9;
        text-align: justify;
    }

    .btn-launch { display:block; width:100%; padding:14px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.8rem; text-decoration:none; letter-spacing: 1px; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.4rem; border-left: 4px solid #D4AF37; padding-left: 18px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 2px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 3px; text-transform: uppercase; }

    @media (max-width: 768px) {
        .main-title-text { font-size: 1.6rem; }
        h1 { font-size: 1.5rem !important; }
        .report-frame { padding: 25px; }
    }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <div class="main-title-text">Fragrance Intelligence</div>
                <div style="font-family: 'Lato'; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 12px;">Global Strategic Hub • Predictive Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Market", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Forecasting Precision", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

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
        
        # LOGIC: Force Report 2026 for Episode 2 and 3
        if "Ep. 1" in episode:
            current_t, current_a, report_f = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title, desc = "Notes_Gourmand", "The Gourmand 2.0 Movement", "Analyzing 'The Lipstick Effect' and Sol de Janeiro's dominance."
        else: # Ep 2 and Ep 3
            current_t = "podcast_transcript_2026.md" if "Ep. 2" in episode else "ep3_whisper_transcript_EN.md"
            current_a = "podcast_2026.mp3" if "Ep. 2" in episode else "ep3_europe_barbell.mp3"
            report_f = "macro_report_2026.md" # FIXED: Macro Report 2026 assigned to both
            f_type = "None" if "Ep. 2" in episode else "Barbell"
            v_title = "2026 Global Projections" if "Ep. 2" in episode else "The Barbell Market Structure 2026"
            desc = "Strategic deep dive into the macroeconomic shifts defining the 2026 landscape."

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
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read()) # Nested markdown for rendering
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
    with d2:
        report_label = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(report_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Strategic report '{report_f}' not found.")

# --- TAB 2: MARKET ANALYTICS ---
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment", hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark", size_max=45)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=600)
    st.plotly_chart(fig_b, use_container_width=True)
    st.markdown("""
        <div style="border: 1px solid #D4AF37; background: #080808; padding: 40px; margin-top: 30px; border-radius: 2px; text-align: center;">
            <div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.5rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 25px; border-bottom: 1px solid #222; padding-bottom: 20px;">Strategic Insight: The Trickle-Down Effect</div>
            <div style="color: #ccc; font-family: 'Lato'; font-size: 1.1rem; line-height: 1.9; text-align: justify;">
                Market data reveals a clear <strong>Trickle-Down Effect</strong>. Innovations typically originate in the <strong>Niche</strong> segment, prioritizing artistry and exotic molecules. Within 1-2 years, these profiles are commercialized by <strong>Prestige</strong> houses. Finally, the trend reaches the <strong>Mass-Market</strong>, driving massive volume through affordable alternatives.
            </div>
        </div>
    """, unsafe_allow_html=True)

# ... (Vault, Outlook, Ecosystem remain same but ensure naming consistency)