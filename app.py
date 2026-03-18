import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS (LUXURY HIERARCHY & GLOBAL STYLES)
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

    /* NAGŁÓWKI W RAPORTACH - ZŁOTA HIERARCHIA */
    h1 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 2.2rem !important; 
        text-align: center !important; 
        border-bottom: 1px solid #D4AF37 !important; 
        padding-bottom: 20px !important; 
        letter-spacing: 4px !important;
        text-transform: uppercase !important;
    }
    h2 { 
        color: #F0E68C !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 1.6rem !important; 
        text-align: center !important; 
        border-top: 1px solid #333 !important;
        padding-top: 25px !important;
        margin-top: 40px !important;
        text-transform: uppercase !important;
    }
    h3 { 
        color: #D4AF37 !important; 
        font-family: 'Tenor Sans', sans-serif !important; 
        font-size: 1.25rem !important; 
        border-left: 4px solid #D4AF37 !important; 
        padding-left: 15px !important; 
        margin-top: 30px !important;
    }

    /* HEADER WRAPPER */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 8px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 30px 60px; text-align: center; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title-text { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 6px; margin: 0; }
    
    /* METRYKI */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 25px 15px; text-align: center; transition: 0.3s; height: 100%; border-radius: 2px; }
    .metric-label { color: #666; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2rem; margin: 0; }
    
    /* RAMKI RAPORTÓW */
    .report-frame { 
        background: #080808; 
        padding: 45px; 
        border: 1px solid #222; 
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        color: #dfdfdf;
        line-height: 1.9;
    }

    .project-card { border:1px solid #222; background:rgba(15,15,15,0.9); padding:25px; transition:0.3s; display:flex; flex-direction:column; justify-content:space-between; height:100%; }
    .btn-launch { display:block; width:100%; padding:12px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.75rem; text-decoration:none; }
    
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.4rem; border-left: 4px solid #D4AF37; padding-left: 18px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 2px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. NAGŁÓWEK I METRYKI (PRZYWRÓCONE)
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <div class="main-title-text">Fragrance Intelligence</div>
                <div style="color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 10px;">Global Strategic Hub • Predictive Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
metrics = [("Global Beauty Sector", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Intelligence Precision", "91%")]
for col, (lab, val) in zip([c1, c2, c3, c4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. ZAKŁADKI (PRZYWRÓCONE WSZYSTKIE 5)
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.4], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Select Intelligence Series:", [
            "🎧 Ep. 1: Recession Glam & 2025 Market", 
            "🔮 Ep. 2: 2026 Outlook & AI Architecture",
            "🌍 Ep. 3: The European Barbell & Poland"
        ], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_t, current_a, report_f = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title = "Notes_Gourmand", "The Gourmand 2.0 Movement"
            r_label = "📈 READ 2025 TREND REPORT"
        elif "Ep. 2" in episode:
            current_t, current_a, report_f = "podcast_transcript_2026.md", "podcast_2026.mp3", "macro_report_2026.md"
            f_type, v_title = "None", "2026 Global Projections"
            r_label = "📈 READ 2026 MACRO REPORT"
        else:
            current_t, current_a, report_f = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "macro_report_2026.md"
            f_type, v_title = "Barbell", "The Barbell Market Structure 2026"
            r_label = "📈 READ 2026 MACRO REPORT"

        st.audio(current_a)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data: {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            b_counts = b_counts.sort_values('Tier')
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
        else:
            df_v = df.copy()
            if f_type == "Notes_Gourmand": df_v = df_v[df_v['top_notes'].str.contains('Vanilla|Pistachio', case=False, na=False)]
            df_t = df_v.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
        
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 READ EXECUTIVE SUMMARY TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Transcript missing.")
    with d2:
        with st.expander(r_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report {report_f} not found.")

# --- TAB 2: MARKET ANALYTICS (PRZYWRÓCONE) ---
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment", hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark", size_max=45)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=600)
    st.plotly_chart(fig_b, use_container_width=True)
    st.markdown("""
        <div style="border: 1px solid #D4AF37; background: #080808; padding: 40px; margin-top: 30px; border-radius: 2px; text-align: center;">
            <div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.5rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 25px; border-bottom: 1px solid #222; padding-bottom: 20px;">Strategic Insight: The Trickle-Down Effect</div>
            <div style="color: #ccc; font-family: 'Lato'; font-size: 1.1rem; line-height: 1.9;">
                Market data reveals a clear <strong>Trickle-Down Effect</strong>. Innovations typically originate in the <strong>Niche</strong> segment. Within 1-2 years, these profiles are commercialized by <strong>Prestige</strong> houses. Finally, the trend reaches the <strong>Mass-Market</strong>.
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 3: VAULT (PRZYWRÓCONE) ---
with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Profile:", ["-- Choose a Profile --"] + sorted(df['name'].tolist()))
    if f_choice != "-- Choose a Profile --":
        f_data = df[df['name'] == f_choice].iloc[0]
        st.markdown(f"""
            <div style="border: 1px solid #D4AF37; background: #050505; padding: 45px 25px; text-align: center; border-radius: 2px; box-shadow: 0 0 30px rgba(212,175,55,0.15);">
                <div style="font-family: 'Tenor Sans'; color: #D4AF37; font-size: 2.4rem; letter-spacing: 3px; text-transform: uppercase;">{f_data['name']}</div>
                <div style="font-family: 'Lato'; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 40px;">{f_data['brand']} • {f_data['segment']}</div>
                <div style="display: flex; justify-content: center; gap: 70px; margin: 45px 0; flex-wrap: wrap;">
                    <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px; margin-bottom:12px;">QUALITY SCORE</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem;">{f_data['community_score']}/5.0</h3></div>
                    <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px; margin-bottom:12px;">GLOBAL VOTES</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem;">{f_data['community_votes']}</h3></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 4: OUTLOOK (PRZYWRÓCONE) ---
with tabs[3]:
    st.markdown('<div class="section-header">Strategic Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    t_list = [("🧪 Functional Scent", "AI-designed neuro-perfs."), ("🧛‍♀️ Vamp Romantic", "Gothic opulence."), ("📈 Macro Resilience", "Poland's rise.")]
    for col, (t_title, t_text) in zip([c1, c2, c3], t_list):
        col.markdown(f'<div style="border:1px solid #333; background:rgba(10,10,10,0.95); padding:35px; border-left: 4px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans; letter-spacing:1px; margin-bottom:15px;">{t_title}</h4><p style="color:#bbb; font-size:0.95rem; line-height:1.7;">{t_text}</p></div>', unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM (PRZYWRÓCONE) ---
with tabs[4]:
    st.markdown('<div class="section-header">Analytical Ecosystem</div>', unsafe_allow_html=True)
    ecosystem = [("🌍 Aromo Intelligence", "Russian market dashboard.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"), ("🔍 Perfume Finder", "Recommendation system.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/")]
    e_cols = st.columns(2)
    for i, (e_n, e_d, e_l) in enumerate(ecosystem):
        with e_cols[i % 2]: st.markdown(f'<div class="project-card"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:12px; letter-spacing:1.5px;">{e_n}</h4><p style="color:#888; font-size:0.9rem; line-height:1.6;">{e_d}</p></div><div style="margin-top:30px;"><a href="{e_l}" target="_blank" class="btn-launch">🚀 Launch Application</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)