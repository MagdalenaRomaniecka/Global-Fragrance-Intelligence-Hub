import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS - PERFECT CENTERING & MOBILE OPTIMIZATION
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    .stApp { background-color: #000000; background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%); font-family: 'Lato', sans-serif !important; }

    /* Nagłówek główny - Złota Ramka + Centrowanie */
    .header-wrapper { display: flex; justify-content: center; padding: 25px 0 15px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; width: 100%; max-width: 600px; }
    .header-inner { border: 1px solid #D4AF37; padding: 20px 40px; text-align: center; background-color: #050505; }
    .main-title { font-family: 'Tenor Sans'; color: #D4AF37; font-size: 2rem; text-transform: uppercase; letter-spacing: 4px; margin: 0; }
    
    /* Globalne Nagłówki Markdown - Złote i Wyśrodkowane */
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; text-align: center !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; font-size: 1.6rem !important; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-align: center !important; text-transform: uppercase !important; border-top: 1px solid #333 !important; padding-top: 20px !important; margin-top: 35px !important; font-size: 1.25rem !important; }
    
    /* Metryki KPI */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 15px; text-align: center; border-radius: 2px; }
    .metric-label { color: #666; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans'; font-size: 1.5rem; }
    
    /* Vault Case Study - Centrowanie + Złoty Box */
    .vault-card { border: 1px solid #D4AF37; background: #050505; padding: 40px 20px; text-align: center; border-radius: 2px; box-shadow: 0 0 25px rgba(212,175,55,0.1); margin: 20px auto; max-width: 800px; }
    .vault-title { font-family: 'Tenor Sans'; color: #D4AF37; font-size: 2.2rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px; }

    .report-frame { background: #080808; padding: 30px; border: 1px solid #222; color: #dfdfdf; line-height: 1.7; text-align: justify; font-size: 0.95rem; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.2rem; border-left: 3px solid #D4AF37; padding-left: 15px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 2px; }
    .btn-launch { display:block; width:100%; padding:10px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; text-decoration:none; letter-spacing: 1px; }

    @media (max-width: 768px) {
        .main-title { font-size: 1.4rem; letter-spacing: 2px; }
        .metric-value { font-size: 1.2rem; }
        .report-frame { padding: 15px; font-size: 0.85rem; }
        .vault-title { font-size: 1.6rem; }
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; z-index: 999; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# 2. HEADER
st.markdown("""<div class="header-wrapper"><div class="header-outer"><div class="header-inner"><h1 class="main-title">Fragrance Intelligence</h1><div style="font-family:'Lato'; color:#888; font-size:0.75rem; text-transform:uppercase; letter-spacing:3px; margin-top:10px;">Strategic Forecast 2026</div></div></div></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
stats = [("Market Cap", "$593.2B"), ("EU Growth", "+16.2%"), ("Poland Peak", "+75.3%"), ("Precision", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], stats):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# 3. TABS
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.4], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Briefing:", ["🎧 Ep. 1: 2025 Market Trends", "🔮 Ep. 2: 2026 Macro Outlook", "🌍 Ep. 3: European Barbell"], label_visibility="collapsed")
        
        # DEFINITIVE LOGIC: Gwarantujemy raport 2026 dla Ep 2 i 3
        if "Ep. 1" in episode:
            current_t, current_a, report_f, f_type, v_title = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md", "Gourmand", "Top Popular Trends"
        else:
            current_t = "podcast_transcript_2026.md" if "Ep. 2" in episode else "ep3_whisper_transcript_EN.md"
            current_a = "podcast_2026.mp3" if "Ep. 2" in episode else "ep3_europe_barbell.mp3"
            report_f, f_type, v_title = "macro_report_2026.md", ("None" if "Ep. 2" in episode else "Barbell"), ("2026 Global Projections" if "Ep. 2" in episode else "European Barbell Market")

        st.audio(current_a)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Data: {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            fig = px.bar(b_counts, x='Tier', y='Count', text='Count', color_discrete_sequence=['#D4AF37'], template="plotly_dark")
        else:
            df_v = df.nlargest(8, 'community_votes').sort_values('community_votes')
            fig = px.bar(df_v, x="community_votes", y="name", orientation='h', text="community_votes", color_discrete_sequence=['#D4AF37'], template="plotly_dark")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, showlegend=False); st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 READ TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f: st.markdown(f'<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Transcript missing.")
    with d2:
        r_lbl = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(r_lbl):
            try:
                with open(report_f, 'r', encoding='utf-8') as f: st.markdown(f'<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report '{report_f}' missing.")

# --- TAB 2: MARKET ANALYTICS ---
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    # POPRAWKA WYKRESU: Lepsza czytelność, większe bąbelki, mniejsza masa
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment", hover_name="name",
                       labels={'community_votes': 'Popularity (Global Votes)', 'community_score': 'Quality Score (1-5)'},
                       color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark", size_max=40, opacity=0.7)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=600)
    st.plotly_chart(fig_b, use_container_width=True)
    
    st.markdown("""
        <div style="border: 1px solid #D4AF37; padding: 40px; text-align: center; background: #080808;">
            <div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.5rem; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 20px;">Strategic Insight: The Trickle-Down Effect</div>
            <div style="color: #ccc; font-family: 'Lato'; font-size: 1.05rem; line-height: 1.8; text-align: justify;">
                Analiza rynkowa wykazuje wyraźny <strong>Trickle-Down Effect</strong>. Innowacje olfaktoryczne zazwyczaj debiutują w segmencie <strong>Niche</strong>, gdzie priorytetem jest artyzm i unikalne molekuły. W ciągu 18-24 miesięcy te same profile zapachowe są komercjalizowane przez domy <strong>Prestige</strong>. Ostatecznie trend osiąga fazę dojrzałości w segmencie <strong>Mass-Market</strong>, generując ogromne wolumeny sprzedaży poprzez przystępne cenowo alternatywy, co na powyższym wykresie widać jako klastry w dolnej lewej strefie popularności, ewoluujące w stronę masowego zaangażowania.
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 3: FRAGRANCE VAULT ---
with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
    f_data = df[df['name'] == f_choice].iloc[0]
    st.markdown(f"""
        <div class="vault-card">
            <div class="vault-title">{f_data['name']}</div>
            <div style="color:#888; text-transform:uppercase; letter-spacing:4px; font-size:0.9rem;">{f_data['brand']} • {f_data['segment']}</div>
            <div style="display:flex; justify-content:center; gap:60px; margin:40px 0; flex-wrap:wrap;">
                <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px;">QUALITY SCORE</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem; margin:0; border:none!important;">{f_data['community_score']:.1f}/5.0</h3></div>
                <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px;">GLOBAL VOTES</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem; margin:0; border:none!important;">{f_data['community_votes']}</h3></div>
            </div>
            <div style="border-top:1px solid #222; padding-top:30px; max-width:600px; margin:0 auto;">
                <p style="color:#D4AF37; font-size:0.85rem; font-weight:bold; text-transform:uppercase; letter-spacing:2px;">Olfactory Strategic Profile</p>
                <p style="color:#ccc; font-size:1.2rem; font-style:italic;">{f_data['top_notes']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 4: 2026 OUTLOOK ---
with tabs[3]:
    st.markdown('<div class="section-header">Strategic Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    trends = [
        ("🧪 Functional Scent", "AI-designed neuro-perfs designed for mental wellness. Scent moves from aesthetics to biotech wellness, integrating with smart-home systems for bio-feedback and real-time mood regulation."), 
        ("🧛‍♀️ Vamp Romantic", "The definitive shift toward gothic opulence. Dark cherry, leather, and smoked oud dominance in Gen Z prestige, replacing the previous decade's clean and minimalist aesthetics."), 
        ("📈 Macro Resilience", "Poland's rise as a top-tier European economy. Local high-end production and regional logistic hubs become key to supply chain resilience amidst global trade protectionism.")
    ]
    for col, (t_title, t_text) in zip([c1, c2, c3], trends):
        col.markdown(f'<div style="border:1px solid #333; background:rgba(10,10,10,0.95); padding:35px; border-left: 4px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans; letter-spacing:1px; margin-bottom:15px; text-transform:uppercase;">{t_title}</h4><p style="color:#bbb; font-size:1rem; line-height:1.7;">{t_text}</p></div>', unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tabs[4]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    ecosystem = [
        ("🌍 Aromo Intelligence", "Russian market scraping engine and strategic dashboard for real-time regional trend monitoring.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"), 
        ("🔍 Perfume Finder", "Consumer recommendation PoC based on high-fidelity preference matching and AI olfactory mapping.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning trend visualization and community mapping for global fragrance launches.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS Hub", "Backend architecture for high-fidelity massive dataset management and olfactory data versioning.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    e_cols = st.columns(2)
    for i, (e_n, e_d, e_l) in enumerate(ecosystem):
        with e_cols[i % 2]: 
            st.markdown(f'<div class="project-card" style="margin-bottom:20px;"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:12px; letter-spacing:2px; text-transform:uppercase;">{e_n}</h4><p style="color:#888; font-size:0.95rem; line-height:1.7;">{e_d}</p></div><div style="margin-top:25px;"><a href="{e_l}" target="_blank" class="btn-launch">🚀 Launch Professional Application</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 120px;"></div><div class="footer">FRAGRANCE INTELLIGENCE HUB • DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)