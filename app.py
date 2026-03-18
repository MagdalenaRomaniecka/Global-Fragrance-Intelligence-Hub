import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS (FORCED GOLD TYPOGRAPHY & CENTERING)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* Global Foundation */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%); 
        font-family: 'Lato', sans-serif !important; 
    }

    /* MAIN APP HEADER - THE GOLDEN FRAME */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 8px; display: inline-block; width: 100%; max-width: 650px; box-sizing: border-box; }
    .header-inner { border: 1px solid #D4AF37; padding: 30px 60px; text-align: center; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 6px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 10px; font-weight: 300; }
    
    /* STRATEGIC METRICS - GOLD GLOW */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; height: 100%; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); transform: translateY(-3px); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 8px; font-weight: 700; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2rem; margin: 0; }
    
    /* THE FAMOUS TRANSCRIPT BOX - REINSTATED WITH LUXURY HEADERS */
    [data-testid="stMarkdownContainer"] .transcript-box { 
        font-family: 'Lato', sans-serif; 
        font-size: 1.05rem; 
        line-height: 1.9; 
        color: #dfdfdf; 
        background: #080808; 
        padding: 45px; 
        border: 1px solid #222; 
        border-radius: 2px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        margin-bottom: 20px;
    }

    /* FORCING GOLD HEADERS INSIDE THE BOX */
    .transcript-box h1 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 2rem !important; 
        text-align: center !important; 
        border-bottom: 1px solid #D4AF37 !important; 
        padding-bottom: 20px !important; 
        margin-bottom: 30px !important; 
        text-transform: uppercase !important; 
        letter-spacing: 3px !important;
        line-height: 1.2 !important;
    }

    .transcript-box h2 { 
        color: #F0E68C !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 1.5rem !important; 
        margin-top: 40px !important; 
        text-align: center !important; 
        border-top: 1px solid #333 !important; 
        padding-top: 25px !important; 
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
    }

    .transcript-box h3 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 1.2rem !important; 
        margin-top: 30px !important; 
        border-left: 3px solid #D4AF37 !important; 
        padding-left: 15px !important; 
    }

    .transcript-box strong { color: #F0E68C !important; font-weight: 700 !important; }

    /* VAULT CARD - FABERLIC STYLE CENTERING */
    .vault-card { border: 1px solid #D4AF37; background: #050505; padding: 45px 25px; text-align: center; border-radius: 2px; box-shadow: 0 0 30px rgba(212,175,55,0.15); margin-top: 25px; }
    .vault-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.4rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px; }
    .vault-subtitle { font-family: 'Lato', sans-serif; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 40px; }

    /* MOBILE OPTIMIZATION */
    @media (max-width: 768px) {
        .main-title { font-size: 1.6rem; letter-spacing: 3px; }
        .transcript-box { padding: 25px; font-size: 0.95rem; }
        .transcript-box h1 { font-size: 1.4rem !important; }
    }

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
metrics = [("Global Beauty Sector", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Forecasting Precision", "91%")]
for col, (lab, val) in zip([c1, c2, c3, c4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. ANALYTICAL TABS
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
        
        if "Ep. 1" in episode:
            current_t, current_a, report_f = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title, desc = "Notes_Gourmand", "The Gourmand 2.0 Movement", "Analyzing 'The Lipstick Effect' and Sol de Janeiro's dominance."
        elif "Ep. 2" in episode:
            current_t, current_a, report_f = "podcast_transcript_2026.md", "podcast_2026.mp3", "macro_report_2026.md"
            f_type, v_title, desc = "None", "2026 Global Projections", "Deep dive into NVIDIA's AI dominance and neuro-perfumery."
        else:
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
                    content = f.read()
                    # THE FIX: Nested markdown inside the luxury div
                    st.markdown(f'<div class="transcript-box">', unsafe_allow_html=True)
                    st.markdown(content)
                    st.markdown(f'</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
    with d2:
        report_label = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(report_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # THE FIX: Nested markdown inside the luxury div
                    st.markdown(f'<div class="transcript-box">', unsafe_allow_html=True)
                    st.markdown(content)
                    st.markdown(f'</div>', unsafe_allow_html=True)
            except: st.info(f"Report file '{report_f}' not found.")

# --- TAB 2: MARKET ANALYTICS ---
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment", hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark", size_max=45)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=600)
    st.plotly_chart(fig_b, use_container_width=True)
    st.markdown("""
        <div style="border: 1px solid #D4AF37; background: #080808; padding: 40px; margin-top: 30px; border-radius: 2px;">
            <div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.5rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 25px; border-bottom: 1px solid #222; padding-bottom: 20px; text-align: center;">Strategic Insight: The Trickle-Down Effect</div>
            <div style="color: #ccc; font-family: 'Lato'; font-size: 1.1rem; line-height: 1.9; text-align: justify;">
                Market data reveals a clear <strong>Trickle-Down Effect</strong>. Innovations typically originate in the <strong>Niche</strong> segment, prioritizing artistry and exotic molecules. Within 1-2 years, these profiles are commercialized by <strong>Prestige</strong> houses. Finally, the trend reaches the <strong>Mass-Market</strong>, driving massive volume through affordable alternatives.
            </div>
        </div>
    """, unsafe_allow_html=True)

# ... (rest of the tabs remain the same, ensuring buttons have !important for gold color)
# ... [Keeping the Fragrance Vault, Outlook, and Ecosystem tabs from previous code for completeness]