import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS - CENTERED GOLD AESTHETICS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    .stApp { background-color: #000000; background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%); font-family: 'Lato', sans-serif !important; }

    /* CENTERED HEADER FRAME */
    .header-wrapper { display: flex; justify-content: center; padding: 40px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 10px; display: inline-block; width: 100%; max-width: 700px; box-sizing: border-box; }
    .header-inner { border: 1px solid #D4AF37; padding: 35px 70px; text-align: center; background-color: #050505; box-shadow: inset 0 0 30px rgba(212,175,55,0.15); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.6rem; text-transform: uppercase; letter-spacing: 6px; margin: 0; border: none !important; }
    
    /* GLOBAL HEADERS (CENTERED & GOLD) */
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; text-align: center !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; letter-spacing: 3px !important; font-size: 2rem !important; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-align: center !important; text-transform: uppercase !important; border-top: 1px solid #333 !important; padding-top: 30px !important; margin-top: 45px !important; font-size: 1.5rem !important; }
    
    /* STRATEGIC METRICS */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 25px; text-align: center; border-radius: 2px; height: 100%; }
    .metric-label { color: #666; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 10px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }
    
    /* VAULT CARD - SCENTSATIONAL STYLE */
    .vault-card { border: 1px solid #D4AF37; background: #050505; padding: 60px 40px; text-align: center; border-radius: 2px; box-shadow: 0 0 30px rgba(212,175,55,0.15); margin: 30px auto; max-width: 850px; }
    .vault-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.8rem; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 15px; }

    /* REPORT FRAME */
    .report-frame { background: #080808; padding: 45px; border: 1px solid #222; box-shadow: 0 15px 40px rgba(0,0,0,0.6); color: #dfdfdf; line-height: 1.9; text-align: justify; margin-bottom: 30px; font-size: 1.05rem; }
    
    /* ECOSYSTEM TILES */
    .project-card { border:1px solid #222; background:rgba(15,15,15,0.95); padding:30px; transition:0.3s; height:100%; display:flex; flex-direction:column; justify-content:space-between; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:14px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.8rem; text-decoration:none; letter-spacing: 1.5px; }

    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.5rem; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 40px 0 25px 0; text-transform: uppercase; letter-spacing: 3px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 15px; font-size: 0.7rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 3px; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# 2. HEADER
st.markdown("""<div class="header-wrapper"><div class="header-outer"><div class="header-inner"><h1 class="main-title">Fragrance Intelligence</h1><div style="font-family: 'Lato'; color: #888; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 5px; margin-top: 15px;">Global Strategic Hub • Predictive Forecast 2026</div></div></div></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Sector", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Intelligence Precision", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# 3. TABS
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# TAB 1: BRIEFING (Gwarancja raportu 2026)
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Briefing Series Selection:", ["🎧 Ep. 1: Recession Glam & 2025 Market", "🔮 Ep. 2: 2026 Outlook & AI Architecture", "🌍 Ep. 3: The European Barbell & Poland"], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_t, current_a, report_f, f_type, v_title = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md", "Popularity", "Global Popularity Ranking"
            desc = "Analyzing 'The Lipstick Effect' and Sol de Janeiro's dominance."
        else: # Ep 2 & 3 - FIXED 2026 LOGIC
            current_t = "podcast_transcript_2026.md" if "Ep. 2" in episode else "ep3_whisper_transcript_EN.md"
            current_a = "podcast_2026.mp3" if "Ep. 2" in episode else "ep3_europe_barbell.mp3"
            report_f, f_type = "macro_report_2026.md", ("None" if "Ep. 2" in episode else "Barbell")
            v_title = "2026 Global Projections" if "Ep. 2" in episode else "The Barbell Structure"
            desc = "Strategic deep dive into macroeconomic shifts and the bifurcation of the market."

        st.audio(current_a); st.markdown(f'<p style="color:#888; font-size:0.95rem; font-style:italic; margin-top:20px; border-left: 3px solid #333; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data: {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
        else:
            df_t = df.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color_discrete_sequence=['#D4AF37'], text="community_votes", template="plotly_dark")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450); st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 READ EXECUTIVE SUMMARY TRANSCRIPT"):
            try:
                with open(current_t, 'r', encoding='utf-8') as f: st.markdown('<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.error("Transcript missing.")
    with d2:
        r_label = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(r_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f: st.markdown('<div class="report-frame">', unsafe_allow_html=True); st.markdown(f.read()); st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report '{report_f}' not found.")

# TAB 2: MARKET ANALYTICS (REINSTATED CLEAN BUBBLE MATRIX WITH QUADRANTS)
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    
    # STRATEGIC FIX: Scatter with Quadrant Lines
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment", hover_name="name", 
                       labels={'community_votes': 'Popularity (Global Votes)', 'community_score': 'Quality Score (1-5)'},
                       color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark", size_max=40, opacity=0.7)
    
    # Adding Quadrant Lines for Strategic Reading
    fig_b.add_hline(y=4.15, line_dash="dot", line_color="#333", annotation_text="High Quality Threshold", annotation_position="bottom right")
    fig_b.add_vline(x=1500, line_dash="dot", line_color="#333", annotation_text="Mass Popularity", annotation_position="top left")
    
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=650, font_family="Lato")
    st.plotly_chart(fig_b, use_container_width=True)
    
    st.markdown("""<div style="border: 1px solid #D4AF37; background: #080808; padding: 45px; margin-top: 40px; text-align: center;"><div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.8rem; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 25px; border-bottom: 1px solid #222; padding-bottom: 20px;">Strategic Insight: The Trickle-Down Effect</div><div style="color: #ccc; font-family: 'Lato'; font-size: 1.15rem; line-height: 2; text-align: justify;">The matrix above visualizes the **Trickle-Down Effect**. Top-right quadrant features the 'Strategic Icons' – high quality and high mass appeal. Bottom-left represents the 'Emerging Niche' where innovations originate. Business strategy dictates monitoring the migration of profiles from the Artistic Niche to the Mass-Market volume, driving global growth.</div></div>""", unsafe_allow_html=True)

# TAB 3: FRAGRANCE VAULT (GOLD FRAME & CENTERED RESULT)
with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Intelligence Profile:", ["-- Choose a Profile --"] + sorted(df['name'].tolist()))
    if f_choice != "-- Choose a Profile --":
        f_data = df[df['name'] == f_choice].iloc[0]
        st.markdown(f"""<div class="vault-card"><div class="vault-title">{f_data['name']}</div><div style="font-family: 'Lato'; color: #888; font-size: 1rem; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 45px;">{f_data['brand']} • {f_data['segment']}</div><div style="display: flex; justify-content: center; gap: 80px; margin: 50px 0; flex-wrap: wrap;"><div><p style="color:#666; font-size:0.9rem; letter-spacing:3px; margin-bottom:15px;">QUALITY SCORE</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:3.5rem; margin:0; border:none !important; text-align:center !important;">{f_data['community_score']:.1f}/5.0</h3></div><div><p style="color:#666; font-size:0.9rem; letter-spacing:3px; margin-bottom:15px;">GLOBAL VOTES</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:3.5rem; margin:0; border:none !important; text-align:center !important;">{f_data['community_votes']}</h3></div></div><div style="border-top:1px solid #222; padding-top:40px; max-width:750px; margin:0 auto;"><p style="color:#D4AF37; font-size:1rem; font-weight:bold; letter-spacing:3px; margin-bottom:20px; text-transform:uppercase;">Olfactory Strategic Profile</p><p style="color:#ccc; font-size:1.4rem; line-height:2; font-style:italic;">{f_data['top_notes']}</p></div></div>""", unsafe_allow_html=True)

# TAB 4: 2026 OUTLOOK (RESTORED FULL DESCRIPTIONS)
with tabs[3]:
    st.markdown('<div class="section-header">Strategic Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    trends = [
        ("🧪 Functional Scent", "AI-designed neuro-perfs designed for mental wellness. Scent moves from aesthetics to biotech wellness, integrating with smart-home systems for bio-feedback and real-time mood regulation."), 
        ("🧛‍♀️ Vamp Romantic", "The definitive shift toward gothic opulence. Dark cherry, leather, and smoked oud dominance in Gen Z prestige, replacing the previous decade's minimalism."), 
        ("📈 Macro Resilience", "Poland's rise as a top-tier European economy. Local production and regional logistic hubs become key to supply chain resilience amidst global trade shifts.")
    ]
    for col, (t_title, t_text) in zip([c1, c2, c3], trends):
        col.markdown(f'<div style="border:1px solid #333; background:rgba(10,10,10,0.95); padding:45px; border-left: 5px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans; font-size:1.4rem; letter-spacing:2px; margin-bottom:20px; text-transform:uppercase;">{t_title}</h4><p style="color:#bbb; font-size:1.1rem; line-height:2;">{t_text}</p></div>', unsafe_allow_html=True)

# TAB 5: ECOSYSTEM (ALL 4 APPS RESTORED)
with tabs[4]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    ecosystem = [
        ("🌍 Aromo Intelligence", "Russian market scraping engine and strategic dashboard for real-time regional monitoring.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"), 
        ("🔍 Perfume Finder", "Consumer recommendation PoC based on high-fidelity preference matching.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning trend visualization and community mapping hub.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS Hub", "Backend architecture for massive dataset management.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    e_cols = st.columns(2)
    for i, (e_n, e_d, e_l) in enumerate(ecosystem):
        with e_cols[i % 2]: 
            st.markdown(f'<div class="project-card" style="margin-bottom:20px;"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:15px; letter-spacing:2px; text-transform:uppercase;">{e_n}</h4><p style="color:#888; font-size:1rem; line-height:1.8;">{e_d}</p></div><div style="margin-top:35px;"><a href="{e_l}" target="_blank" class="btn-launch">🚀 Launch Professional Application</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 120px;"></div><div class="footer">FRAGRANCE INTELLIGENCE HUB • STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)