import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS - PEŁNA REKONSTRUKCJA ESTETYKI
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

    /* ZŁOTY NAGŁÓWEK GŁÓWNY - PODWÓJNA RAMKA */
    .header-wrapper { display: flex; justify-content: center; padding: 40px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 10px; display: inline-block; width: 100%; max-width: 750px; }
    .header-inner { border: 1px solid #D4AF37; padding: 35px 70px; text-align: center; background-color: #050505; box-shadow: inset 0 0 30px rgba(212,175,55,0.15); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.8rem; text-transform: uppercase; letter-spacing: 7px; margin: 0; }
    
    /* WYŚRODKOWANE NAGŁÓWKI GLOBALNE */
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; text-align: center !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; margin-bottom: 30px !important; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-align: center !important; text-transform: uppercase !important; border-top: 1px solid #333 !important; padding-top: 30px !important; margin-top: 45px !important; }
    
    /* STRATEGIC METRICS */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 25px; text-align: center; transition: 0.3s; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #666; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 3px; font-weight: 700; margin-bottom: 10px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2.2rem; }
    
    /* FRAGRANCE VAULT CARD - PEŁNE CENTROWANIE */
    .vault-card { border: 1px solid #D4AF37; background: #050505; padding: 60px 40px; text-align: center; border-radius: 2px; box-shadow: 0 0 40px rgba(212,175,55,0.15); margin: 30px auto; max-width: 950px; }
    .vault-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 3rem; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 15px; }

    /* ECOSYSTEM TILES */
    .project-card { border: 1px solid #222; background: rgba(15,15,15,0.95); padding: 35px; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: space-between; }
    .project-card:hover { border-color: #D4AF37; }
    .btn-launch { display: block; width: 100%; padding: 14px; background: #D4AF37 !important; color: #000 !important; text-align: center; font-weight: bold; text-transform: uppercase; font-size: 0.8rem; text-decoration: none; letter-spacing: 1.5px; border-radius: 1px; }

    .report-frame { background: #080808; padding: 45px; border: 1px solid #222; box-shadow: 0 15px 40px rgba(0,0,0,0.6); color: #dfdfdf; line-height: 2; text-align: justify; margin-bottom: 30px; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.6rem; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 40px 0 25px 0; text-transform: uppercase; letter-spacing: 4px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 15px; font-size: 0.7rem; border-top: 1px solid #111; z-index: 999; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. NAGŁÓWEK GŁÓWNY
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title" style="border:none!important;">Fragrance Intelligence</h1>
                <div style="font-family: 'Lato'; color: #888; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 5px; margin-top: 15px;">Global Strategic Hub • Predictive Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Sector", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Intelligence Precision", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. ANALYTICAL TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Briefing Series:", ["🎧 Ep. 1: Recession Glam & 2025 Market", "🔮 Ep. 2: 2026 Outlook & AI Architecture", "🌍 Ep. 3: The European Barbell & Poland"], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_t, current_a, report_f, f_type, v_title = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md", "Notes_Gourmand", "The Gourmand 2.0 Movement"
            desc = "Analyzing 'The Lipstick Effect' and Sol de Janeiro's dominance."
        else:
            current_t = "podcast_transcript_2026.md" if "Ep. 2" in episode else "ep3_whisper_transcript_EN.md"
            current_a = "podcast_2026.mp3" if "Ep. 2" in episode else "ep3_europe_barbell.mp3"
            report_f, f_type = "macro_report_2026.md", ("None" if "Ep. 2" in episode else "Barbell")
            v_title = "2026 Global Projections" if "Ep. 2" in episode else "The Barbell Market Structure 2026"
            desc = "Strategic deep dive into macroeconomic shifts and the bifurcation of the EU market."

        st.audio(current_a)
        st.markdown(f'<p style="color:#888; font-size:0.95rem; font-style:italic; margin-top:20px; border-left: 3px solid #333; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data: {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            fig = px.bar(b_counts.sort_values('Tier'), x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
        else:
            df_v = df.copy(); df_t = df_v.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450)
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 READ EXECUTIVE SUMMARY TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Transcript missing.")
    with d2:
        r_label = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(r_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report '{report_f}' not found.")

# --- TAB 2: MARKET ANALYTICS ---
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment", hover_name="name", 
                       labels={'community_votes': 'Global Votes', 'community_score': 'Quality Score (1-5)'},
                       color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark", size_max=40)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=650, font_family="Lato")
    st.plotly_chart(fig_b, use_container_width=True)
    
    st.markdown("""
        <div style="border: 1px solid #D4AF37; background: #080808; padding: 45px; margin-top: 40px; border-radius: 2px; text-align: center; box-shadow: 0 0 20px rgba(212,175,55,0.1);">
            <div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.8rem; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 25px; border-bottom: 1px solid #222; padding-bottom: 20px;">Strategic Insight: The Trickle-Down Effect</div>
            <p style="color: #ccc; font-family: 'Lato'; font-size: 1.2rem; line-height: 2; text-align: justify; max-width: 1000px; margin: 0 auto;">
                Analiza rynkowa wykazuje wyraźny <strong>Trickle-Down Effect</strong>. Innowacje olfaktoryczne zazwyczaj debiutują w segmencie <strong>Niche</strong>, gdzie priorytetem jest artyzm i unikalne molekuły. W ciągu 18-24 miesięcy te same profile zapachowe są komercjalizowane przez domy <strong>Prestige</strong>. Ostatecznie trend osiąga fazę dojrzałości w segmencie <strong>Mass-Market</strong>, generując ogromne wolumeny sprzedaży poprzez przystępne cenowo alternatywy, co widać na powyższym wykresie jako skupisko w dolnej lewej strefie popularności, która z czasem przesuwa się w stronę masowego zaangażowania.
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 3: FRAGRANCE VAULT ---
with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Intelligence Profile:", ["-- Choose a Profile --"] + sorted(df['name'].tolist()))
    if f_choice != "-- Choose a Profile --":
        f_data = df[df['name'] == f_choice].iloc[0]
        st.markdown(f"""
            <div class="vault-card">
                <div class="vault-title">{f_data['name']}</div>
                <div style="font-family: 'Lato'; color: #888; font-size: 1rem; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 45px;">{f_data['brand']} • {f_data['segment']}</div>
                <div style="display: flex; justify-content: center; gap: 90px; margin: 50px 0; flex-wrap: wrap;">
                    <div><p style="color:#666; font-size:0.9rem; letter-spacing:3px; margin-bottom:15px;">QUALITY SCORE</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:3.5rem; margin:0;">{f_data['community_score']:.1f}/5.0</h3></div>
                    <div><p style="color:#666; font-size:0.9rem; letter-spacing:3px; margin-bottom:15px;">GLOBAL VOTES</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:3.5rem; margin:0;">{f_data['community_votes']}</h3></div>
                </div>
                <div style="border-top:1px solid #222; padding-top:40px; max-width:750px; margin:0 auto;">
                    <p style="color:#D4AF37; font-size:1rem; font-weight:bold; letter-spacing:3px; margin-bottom:20px; text-transform:uppercase;">Olfactory Strategic Profile</p>
                    <p style="color:#ccc; font-size:1.4rem; line-height:2; font-style:italic;">{f_data['top_notes']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 4: 2026 OUTLOOK ---
with tabs[3]:
    st.markdown('<div class="section-header">Strategic Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    trends = [
        ("🧪 Functional Scent", "AI-designed neuro-perfs designed for mental wellness. Scent moves from pure aesthetics to a critical biotech wellness pillar, integrating with smart-home systems for bio-feedback and mood regulation."), 
        ("🧛‍♀️ Vamp Romantic", "The definitive shift toward gothic opulence. Dark cherry, leather, and smoked oud dominance in Gen Z prestige, replacing the previous decade's clean and minimalist aesthetics."), 
        ("📈 Macro Resilience", "Poland's rise as a top-tier European economy. Local high-end production and regional logistic hubs become key to supply chain resilience amidst global trade protectionism.")
    ]
    for col, (t_title, t_text) in zip([c1, c2, c3], trends):
        col.markdown(f'<div style="border:1px solid #333; background:rgba(10,10,10,0.95); padding:45px; border-left: 5px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans; font-size:1.5rem; letter-spacing:2px; margin-bottom:20px; text-transform:uppercase;">{t_title}</h4><p style="color:#bbb; font-size:1.1rem; line-height:2;">{t_text}</p></div>', unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tabs[4]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    ecosystem = [
        ("🌍 Aromo Intelligence", "Russian market scraping engine and strategic dashboard for real-time regional trend monitoring and competitive analysis.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"), 
        ("🔍 Perfume Finder", "Consumer recommendation PoC based on high-fidelity preference matching and AI-driven olfactory mapping.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning trend visualization and community mapping for global fragrance launches and consumer sentiment.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS Hub", "Backend architecture for high-fidelity massive dataset management and olfactory data versioning.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    e_cols = st.columns(2)
    for i, (e_n, e_d, e_l) in enumerate(ecosystem):
        with e_cols[i % 2]: 
            st.markdown(f'<div class="project-card"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:15px; letter-spacing:2px; text-transform:uppercase;">{e_n}</h4><p style="color:#888; font-size:1.05rem; line-height:1.8;">{e_d}</p></div><div style="margin-top:35px;"><a href="{e_l}" target="_blank" class="btn-launch">🚀 Launch Professional Application</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 120px;"></div><div class="footer">FRAGRANCE INTELLIGENCE HUB • STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)