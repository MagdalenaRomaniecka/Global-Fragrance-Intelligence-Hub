import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS (MOBILE-FIRST LUXURY & SMALLER FONTS)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    .stApp { background-color: #000000; background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%); font-family: 'Lato', sans-serif !important; }

    /* RESPONSIVE HEADER */
    .header-wrapper { display: flex; justify-content: center; padding: 20px 0; }
    .header-inner { border: 0.5px solid #D4AF37; padding: 15px 30px; text-align: center; background-color: #050505; box-shadow: 0 0 15px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans'; color: #D4AF37; font-size: 1.6rem; text-transform: uppercase; letter-spacing: 3px; margin: 0; }
    
    /* GLOBAL HEADERS (FORCED SCALE FOR MOBILE) */
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; text-align: center !important; font-size: 1.3rem !important; text-transform: uppercase !important; border-bottom: 1px solid #D4AF37; padding-bottom: 10px; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-align: center !important; font-size: 1.1rem !important; border-top: 1px solid #333; padding-top: 15px; margin-top: 25px !important; }
    h3 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; font-size: 1rem !important; border-left: 3px solid #D4AF37; padding-left: 10px; }

    /* KPI BOXES */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 12px; text-align: center; }
    .metric-label { color: #666; font-size: 0.55rem; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans'; font-size: 1.3rem; }
    
    /* VAULT CARD & REPORTS */
    .vault-card { border: 1px solid #D4AF37; background: #050505; padding: 30px 15px; text-align: center; max-width: 800px; margin: 0 auto; }
    .report-frame { background: #080808; padding: 25px; border: 1px solid #222; color: #dfdfdf; font-size: 0.9rem; line-height: 1.6; text-align: justify; }

    @media (max-width: 768px) {
        .main-title { font-size: 1.2rem; }
        .metric-value { font-size: 1rem; }
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; z-index: 999; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# 2. HEADER
st.markdown("""<div class="header-wrapper"><div class="header-inner"><h1 class="main-title" style="border:none!important;">Fragrance Intelligence</h1><div style="color:#888; font-size:0.7rem; text-transform:uppercase; letter-spacing:2px;">Strategic Forecast 2026</div></div></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Market", "$593B"), ("EU Growth", "+16%"), ("Poland Max", "+75%"), ("Reliability", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# 3. TABS
tabs = st.tabs(["STRATEGIC BRIEFING", "ANALYTICS", "VAULT", "OUTLOOK", "ECOSYSTEM"])

# TAB 1: BRIEFING
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.5], gap="medium")
    with col_audio:
        episode = st.radio("Briefing:", ["Ep. 1: 2025 Market Trends", "Ep. 2: 2026 Macro Outlook", "Ep. 3: European Barbell"], label_visibility="collapsed")
        
        # LOGIC: Ensure 2026 Macro Report loads for Ep 2 and Ep 3
        if "Ep. 1" in episode:
            current_t, current_a, report_f, f_type, v_title = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md", "Notes_Gourmand", "Top Gourmand Trends"
        else:
            current_t = "podcast_transcript_2026.md" if "Ep. 2" in episode else "ep3_whisper_transcript_EN.md"
            current_a = "podcast_2026.mp3" if "Ep. 2" in episode else "ep3_europe_barbell.mp3"
            report_f, f_type, v_title = "macro_report_2026.md", ("None" if "Ep. 2" in episode else "Barbell"), ("2026 Projections" if "Ep. 2" in episode else "EU Barbell Market")

        st.audio(current_a)

    with col_viz:
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            fig = px.bar(b_counts, x='Tier', y='Count', text='Count', color_discrete_sequence=['#D4AF37'], template="plotly_dark")
        else:
            # FIX: Clean Top 5 Gourmand Ranking
            df_v = df[df['top_notes'].str.contains('Vanilla|Pistachio', case=False, na=False)]
            df_t = df_v.nlargest(5, 'community_votes').sort_values('community_votes')
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', text="community_votes", color_discrete_sequence=['#D4AF37'], template="plotly_dark")
        
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=300, showlegend=False)
        fig.update_xaxes(showgrid=False, title="Global Votes"); fig.update_yaxes(showgrid=False, title="")
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f: st.markdown(f'<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("File missing.")
    with d2:
        r_lbl = "📈 READ 2025 REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(r_lbl):
            try:
                with open(report_f, 'r', encoding='utf-8') as f: st.markdown(f'<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report {report_f} not found.")

# TAB 2: ANALYTICS
with tabs[1]:
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment", hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=500); st.plotly_chart(fig_b, use_container_width=True)
    st.markdown('<div style="border: 1px solid #D4AF37; padding: 20px; text-align: center; font-size: 0.85rem; color: #ccc;"><strong>Insight: The Trickle-Down Effect</strong><br>Olfactory innovations typically originate in the Niche segment before being commercialized by Prestige houses and finally reaching Mass-Market volume.</div>', unsafe_allow_html=True)

# TAB 3: VAULT
with tabs[2]:
    f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
    f_data = df[df['name'] == f_choice].iloc[0]
    st.markdown(f"""<div class="vault-card"><h2 style="border:none!important; margin:0!important; color:#D4AF37!important;">{f_data['name']}</h2><p style="color:#888; font-size:0.7rem; text-transform:uppercase;">{f_data['brand']} • {f_data['segment']}</p><div style="display:flex; justify-content:center; gap:30px; margin:20px 0;"><div><p style="color:#666; font-size:0.6rem;">QUALITY</p><h3 style="border:none!important; margin:0!important;">{f_data['community_score']:.1f}/5.0</h3></div><div><p style="color:#666; font-size:0.6rem;">VOTES</p><h3 style="border:none!important; margin:0!important;">{f_data['community_votes']}</h3></div></div><p style="color:#ccc; font-style:italic; font-size:0.85rem;">{f_data['top_notes']}</p></div>""", unsafe_allow_html=True)

# TAB 4: OUTLOOK
with tabs[3]:
    c1, c2, c3 = st.columns(3)
    trends = [("🧪 Functional", "AI-designed neuro-perfs for mental wellness. Scent becomes biotech wellness."), ("🧛‍♀️ Vamp", "Gothic opulence. Dark cherry and leather dominance in Gen Z prestige."), ("📈 Resilience", "Poland's rise as a top-tier European economy with regional supply chain hubs.")]
    for col, (t, d) in zip([c1, c2, c3], trends):
        col.markdown(f'<div style="border-left: 2px solid #D4AF37; padding-left: 10px; height:100%;"><h4 style="color:#D4AF37; font-size:0.9rem; margin-bottom:5px;">{t}</h4><p style="color:#888; font-size:0.8rem;">{d}</p></div>', unsafe_allow_html=True)

# TAB 5: ECOSYSTEM
with tabs[4]:
    apps = [("🌍 Aromo", "Regional market dashboard.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"), ("🔍 Perfume Finder", "AI recommendation engine.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"), ("📊 ScentSational", "Trend visualization hub.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"), ("🧪 LFS Hub", "Massive dataset backend.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")]
    e_cols = st.columns(2)
    for i, (n, d, l) in enumerate(apps):
        with e_cols[i % 2]: st.markdown(f'<div style="border:1px solid #222; padding:15px; margin-bottom:10px;"><strong>{n}</strong><br><small style="color:#666;">{d}</small><br><br><a href="{l}" target="_blank" class="btn-launch">LAUNCH APP</a></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 80px;"></div><div class="footer">FRAGRANCE INTELLIGENCE HUB</div>', unsafe_allow_html=True)