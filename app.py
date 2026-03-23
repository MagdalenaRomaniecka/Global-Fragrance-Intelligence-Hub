import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS - CENTERED LUXURY & CLEAN TYPOGRAPHY (100% ENGLISH)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* Global styling */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%); 
        font-family: 'Lato', sans-serif !important; 
    }

    /* FORCED HEADER CENTERING */
    [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2 {
        text-align: center !important;
        justify-content: center !important;
        display: flex !important;
        width: 100% !important;
    }

    /* MAIN TITLE HEADER */
    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 40px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 10px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 50px; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 5px; margin: 0; border: none !important; }
    
    /* GLOBAL MARKDOWN HEADERS STYLING */
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; font-size: 1.8rem !important; }
    h2 { color: #F0E68C !important; font-family: 'Tenor Sans' !important; text-transform: uppercase !important; border-top: 1px solid #333 !important; padding-top: 30px !important; margin-top: 45px !important; font-size: 1.4rem !important; }

    /* KPI BOXES */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 20px; text-align: center; transition: 0.3s; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 8px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }

    /* REPORTS & TRANSCRIPTS */
    .report-frame { background: #080808; padding: 45px; border: 1px solid #222; box-shadow: 0 15px 40px rgba(0,0,0,0.6); color: #dfdfdf; line-height: 1.9; text-align: justify; margin-bottom: 30px; font-size: 1.05rem; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.4rem; border-left: 5px solid #D4AF37; padding-left: 20px; margin: 30px 0 20px 0; text-transform: uppercase; letter-spacing: 3px; }
    
    /* TABS */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p { text-align: center !important; font-family: 'Tenor Sans', sans-serif !important; letter-spacing: 1px; }

    /* ECOSYSTEM PROJECTS */
    .project-card { border:1px solid #222; background:rgba(15,15,15,0.95); padding:25px; transition:0.3s; height:100%; display:flex; flex-direction:column; justify-content:space-between; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:12px; background:#D4AF37 !important; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.75rem; text-decoration:none; letter-spacing: 1px; }

    /* FOOTER */
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. MAIN HEADER & KPI METRICS
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Fragrance Intelligence</h1>
                <div style="font-family: 'Lato'; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 4px; margin-top: 10px;">Global Strategic Hub • Predictive Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [("Global Beauty Market", "$593.2B"), ("EU Market Growth", "+16.2%"), ("Poland Growth (Max)", "+75.3%"), ("Intelligence Precision", "91%")]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. ANALYTICAL TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Briefing Series Selection:", ["🎧 Ep. 1: Recession Glam & 2025 Market", "🔮 Ep. 2: 2026 Outlook & AI Architecture", "🌍 Ep. 3: The European Barbell & Poland"], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_t, current_a, report_f, f_type, v_title = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", "trend_report_2025.md", "Popularity", "Global Popularity Ranking"
            desc = "Analyzing 'The Lipstick Effect' and Sol de Janeiro's market dominance."
        else:
            current_t = "podcast_transcript_2026.md" if "Ep. 2" in episode else "ep3_whisper_transcript_EN.md"
            current_a = "podcast_2026.mp3" if "Ep. 2" in episode else "ep3_europe_barbell.mp3"
            report_f, f_type = "macro_report_2026.md", ("None" if "Ep. 2" in episode else "Barbell")
            v_title = "2026 Global Projections" if "Ep. 2" in episode else "The Barbell Market Structure 2026"
            desc = "Strategic deep dive into macroeconomic shifts and the hollowing out of the middle tier."

        st.audio(current_a)
        st.markdown(f'<p style="color:#888; font-size:0.9rem; font-style:italic; margin-top:20px; border-left: 3px solid #333; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data: {v_title}</div>', unsafe_allow_html=True)
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            fig = px.bar(b_counts.sort_values('Tier'), x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
        else:
            df_v = df.copy()
            df_t = df_v.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment", text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450)
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
        r_label = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(r_label):
            try:
                with open(report_f, 'r', encoding='utf-8') as f:
                    st.markdown('<div class="report-frame">', unsafe_allow_html=True)
                    st.markdown(f.read())
                    st.markdown('</div>', unsafe_allow_html=True)
            except: st.info(f"Report '{report_f}' not found in directory.")

# --- TAB 2: MARKET ANALYTICS (EXECUTIVE SUNBURST - TOP 5 PER SEGMENT) ---
with tabs[1]:
    st.markdown('<div class="section-header">Market Segmentation Strategic Hierarchy</div>', unsafe_allow_html=True)
    
    df_sunburst = df.groupby('segment').apply(lambda x: x.nlargest(5, 'community_votes')).reset_index(drop=True)
    
    fig_sun = px.sunburst(df_sunburst, path=[px.Constant("Global Market"), 'segment', 'brand', 'name'], 
                          values='community_votes', color='segment',
                          color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555'},
                          template="plotly_dark")
    
    fig_sun.update_traces(textfont=dict(family="Lato, sans-serif", size=14), insidetextorientation='auto')
    
    fig_sun.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        height=750, 
        margin=dict(t=20, l=10, r=10, b=20),
        font=dict(family="Lato, sans-serif")
    )
    st.plotly_chart(fig_sun, use_container_width=True)
    
    st.markdown("""
        <div style="border: 1px solid #D4AF37; background: #080808; padding: 40px; margin-top: 40px; text-align: center;">
            <div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.6rem; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 25px; border-bottom: 1px solid #222; padding-bottom: 20px;">Strategic Insight: The Trickle-Down Effect</div>
            <div style="color: #ccc; font-family: 'Lato'; font-size: 1.1rem; line-height: 1.9; text-align: justify;">
                Market analysis reveals a clear <strong>Trickle-Down Effect</strong>. Olfactory innovations typically debut in the <strong>Niche</strong> segment, where artistry and unique molecules are prioritized. Within 18-24 months, these same fragrance profiles are commercialized by <strong>Prestige</strong> houses. Ultimately, the trend reaches maturity in the <strong>Mass-Market</strong> segment, generating massive sales volumes through affordable alternatives.
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 3: FRAGRANCE VAULT (BULLETPROOF INLINE CSS FOR PLAQUES) ---
with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Intelligence Profile:", ["-- Choose a Profile --"] + sorted(df['name'].tolist()))
    
    if f_choice != "-- Choose a Profile --":
        f_data = df[df['name'] == f_choice].iloc[0]
        
        # BULLETPROOF INLINE STYLES - Streamlit CANNOT strip these!
        st.markdown(f"""
            <div style="border: 2px solid #D4AF37; padding: 6px; background: #000; margin: 30px auto; max-width: 900px; box-shadow: 0 0 30px rgba(212,175,55,0.15);">
                <div style="border: 1px solid rgba(212,175,55,0.4); background: radial-gradient(circle at 50% 50%, #0a0a0a 0%, #000000 100%); padding: 50px 30px; text-align: center;">
                    
                    <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.8rem; letter-spacing: 6px; text-transform: uppercase; margin-bottom: 10px;">{f_data['name']}</div>
                    <div style="color: #D4AF37; font-size: 0.9rem; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 40px;">{f_data['brand']} • {f_data['segment']}</div>
                    
                    <div style="display: flex; justify-content: center; gap: 40px; margin-bottom: 40px; flex-wrap: wrap;">
                        
                        <div style="border: 2px solid #D4AF37; background: linear-gradient(145deg, #1a1500 0%, #050505 100%); padding: 4px; min-width: 250px; box-shadow: 0 10px 20px rgba(0,0,0,0.8); border-radius: 2px;">
                            <div style="border: 1px solid rgba(212,175,55,0.3); padding: 20px 30px;">
                                <div style="color:#D4AF37; font-size:0.85rem; letter-spacing:3px; margin-bottom:10px; text-transform:uppercase;">Quality Score</div>
                                <div style="color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 3.5rem; line-height: 1.2; margin: 0; text-shadow: 0 0 10px rgba(240, 230, 140, 0.2);">{f_data['community_score']:.1f}/5.0</div>
                            </div>
                        </div>

                        <div style="border: 2px solid #D4AF37; background: linear-gradient(145deg, #1a1500 0%, #050505 100%); padding: 4px; min-width: 250px; box-shadow: 0 10px 20px rgba(0,0,0,0.8); border-radius: 2px;">
                            <div style="border: 1px solid rgba(212,175,55,0.3); padding: 20px 30px;">
                                <div style="color:#D4AF37; font-size:0.85rem; letter-spacing:3px; margin-bottom:10px; text-transform:uppercase;">Global Votes</div>
                                <div style="color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 3.5rem; line-height: 1.2; margin: 0; text-shadow: 0 0 10px rgba(240, 230, 140, 0.2);">{f_data['community_votes']}</div>
                            </div>
                        </div>

                    </div>
                    
                    <hr style="border: 0; height: 1px; background: linear-gradient(to right, transparent, #D4AF37, transparent); margin: 40px 0;">
                    
                    <div style="color:#D4AF37; font-size:0.9rem; font-weight:bold; letter-spacing:3px; margin-bottom:15px; text-transform:uppercase;">Olfactory Strategic Profile</div>
                    <div style="color:#F0E68C; font-family:'Tenor Sans'; font-size:1.6rem; font-style:italic;">{f_data['top_notes']}</div>
                    
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 4: 2026 OUTLOOK ---
with tabs[3]:
    st.markdown('<div class="section-header">Strategic Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    t_list = [
        ("🧪 Functional Scent", "AI-designed neuro-perfs engineered for mental wellness and cognitive optimization."), 
        ("🧛‍♀️ Vamp Romantic", "Gothic opulence. Dark cherry and leather dominance in Gen Z prestige collections."), 
        ("📈 Macro Resilience", "Poland's rise as a top-tier European economy with highly resilient supply chains.")]
    for col, (t_title, t_text) in zip([c1, c2, c3], t_list):
        col.markdown(f'<div style="border:1px solid #333; background:rgba(10,10,10,0.95); padding:40px; border-left: 5px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans; font-size:1.4rem; letter-spacing:2px; margin-bottom:20px; text-transform:uppercase;">{t_title}</h4><p style="color:#bbb; font-size:1.05rem; line-height:1.8;">{t_text}</p></div>', unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tabs[4]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    eco = [
        ("🌍 Aromo Intelligence", "Russian market scraping engine and strategic dashboard.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"), 
        ("🔍 Perfume Finder", "Consumer recommendation PoC based on preference matching.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning trend visualization and community mapping.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS Hub", "Backend architecture for massive dataset management.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    e_cols = st.columns(2)
    for i, (n, d, l) in enumerate(eco):
        with e_cols[i % 2]: 
            st.markdown(f'<div class="project-card"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:15px; letter-spacing:2px; text-transform:uppercase;">{n}</h4><p style="color:#888; font-size:1rem; line-height:1.8;">{d}</p></div><div style="margin-top:35px;"><a href="{l}" target="_blank" class="btn-launch">🚀 Launch Professional Application</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)