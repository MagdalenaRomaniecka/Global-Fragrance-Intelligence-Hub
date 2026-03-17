import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. ATELIER SUPREME CSS (RECOVERED AESTHETICS + MOBILE RESPONSIVE)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* Background & Global */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%); 
        font-family: 'Lato', sans-serif !important; 
    }

    /* RECOVERED: Original Centered Gold Header Wrapper */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 15px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; width: 100%; max-width: 600px; box-sizing: border-box; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 60px; text-align: center; background-color: #050505; }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 4px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 10px; font-weight: 300; }
    
    /* RECOVERED: Original Metric Box Style */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 15px; text-align: center; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.1); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Lato', sans-serif; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2.2rem; margin: 0; }
    
    /* RECOVERED: Original Section Headers */
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; border-left: 3px solid #D4AF37; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }
    
    /* RECOVERED: Original Transcript & Report Styling */
    .transcript-box { font-family: 'Lato', sans-serif; font-size: 0.95rem; line-height: 1.6; color: #cccccc; background: #080808; padding: 30px; border: 1px solid #222; overflow-x: hidden; text-align: justify; }
    .transcript-box h1 { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.5rem; text-align: center; border-bottom: 1px solid #D4AF37; padding-bottom: 15px; margin-bottom: 25px; text-transform: uppercase; }
    .transcript-box h2 { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.25rem; border-bottom: 1px solid #333; padding-bottom: 10px; margin-top: 25px; text-align: center; }
    .transcript-box strong { color: #F0E68C; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; font-weight: 700; }

    /* RECOVERED: Centered Vault Card Style */
    .vault-card { border: 1px solid #D4AF37; background: #050505; padding: 40px 20px; margin-top: 20px; text-align: center; border-radius: 2px; }
    .vault-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; letter-spacing: 2px; margin-bottom: 5px; text-transform: uppercase; }
    .vault-subtitle { font-family: 'Lato', sans-serif; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 30px; }

    /* Project Cards & Mobile Responsiveness */
    .project-card { border:1px solid #222; background:#0a0a0a; padding:20px; transition:0.3s; display:flex; flex-direction:column; justify-content:space-between; height:100%; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:10px; background:#D4AF37; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; margin-bottom:10px; text-decoration:none; }
    
    @media (max-width: 768px) {
        .header-outer { padding: 4px; }
        .header-inner { padding: 15px 10px; }
        .main-title { font-size: 1.4rem; letter-spacing: 2px; }
        .metric-value { font-size: 1.6rem; }
        .transcript-box { padding: 15px; font-size: 0.85rem; }
    }

    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; letter-spacing: 1px; z-index: 999; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER & TOP KPI (RECOVERED LAYOUT)
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Fragrance Intelligence</h1>
                <div class="sub-title">Global Hub • Strategic Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.markdown('<div class="metric-box"><div class="metric-label">Global Beauty Market</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="metric-box"><div class="metric-label">EU Market Growth</div><div class="metric-value">+16.2%</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="metric-box"><div class="metric-label">Poland Growth (Max)</div><div class="metric-value">+75.3%</div></div>', unsafe_allow_html=True)
c4.markdown('<div class="metric-box"><div class="metric-label">Model Reliability</div><div class="metric-value">91%</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. STRATEGIC TABS (LATEST CONTENT)
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tab1:
    col_audio, col_viz = st.columns([1, 1.4], gap="large")
    
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Select Briefing:", [
            "🎧 Ep. 1: Recession Glam & 2025 Market", 
            "🔮 Ep. 2: 2026 Outlook & AI Architecture",
            "🌍 Ep. 3: The European Barbell & Poland"
        ], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_transcript, current_audio = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"
            report_file = "trend_report_2025.md"
            f_type, v_title = "Notes_Gourmand", "The Gourmand 2.0 Movement"
            desc = "Analyzing 'The Lipstick Effect' and Sol de Janeiro's dominance."
        elif "Ep. 2" in episode:
            current_transcript, current_audio = "podcast_transcript_2026.md", "podcast_2026.mp3"
            report_file = "macro_report_2026.md"
            f_type, v_title = "None", "2026 Global Projections"
            desc = "Deep dive into NVIDIA's AI dominance, US trade protectionism, and neuro-perfumery."
        else:
            current_transcript, current_audio = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3"
            report_file = "macro_report_2026.md"
            f_type, v_title = "Barbell", "The Barbell Market Structure 2026"
            desc = "Bifurcation of the EU market: The hollowing out of the middle tier."

        st.audio(current_audio)
        st.markdown(f'<p style="color:#888; font-size:0.85rem; font-style:italic; margin-top:15px; border-left: 2px solid #333; padding-left: 15px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data: {v_title}</div>', unsafe_allow_html=True)
        
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            b_counts = b_counts.sort_values('Tier')
            
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count',
                         color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'},
                         template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#D4AF37', marker_line_width=2)
        else:
            df_v = df.copy()
            if f_type == "Notes_Gourmand":
                df_v = df_v[df_v['top_notes'].str.contains('Vanilla|Pistachio', case=False, na=False)]
            df_t = df_v.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment",
                         text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#D4AF37', marker_line_width=1.5)

        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", showlegend=False, height=420)
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 READ EXECUTIVE SUMMARY TRANSCRIPT"):
            try:
                with open(current_transcript, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
    with d2:
        report_label = "📈 READ 2025 TREND REPORT" if "Ep. 1" in episode else "📈 READ 2026 MACRO REPORT"
        with st.expander(report_label):
            try:
                with open(report_file, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.info(f"Report file '{report_file}' not found.")

# --- TAB 2: MARKET ANALYTICS ---
with tab2:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment",
                       hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'],
                       template="plotly_dark", size_max=45)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=600)
    st.plotly_chart(fig_b, use_container_width=True)

    # RECOVERED: Original Strategic Insight Box
    st.markdown("""
        <div style="border: 1px solid #D4AF37; background: #080808; padding: 35px; margin-top: 30px; border-radius: 2px;">
            <div style="color: #D4AF37; font-family: 'Tenor Sans'; font-size: 1.4rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px; border-bottom: 1px solid #222; padding-bottom: 15px; text-align: center;">
                Strategic Insight: The Trickle-Down Effect
            </div>
            <div style="color: #ccc; font-family: 'Lato'; font-size: 1rem; line-height: 1.8; text-align: justify;">
                Market data reveals a clear <strong>Trickle-Down Effect</strong>. Innovations typically originate in the <strong>Niche</strong> segment, prioritizing artistry. Within 1-2 years, these profiles are commercialized by <strong>Prestige</strong> houses. Finally, the trend reaches the <strong>Mass-Market</strong> maturity phase, driving massive volume and community engagement.
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 3: FRAGRANCE VAULT ---
with tab3:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Profile:", ["-- Choose a Profile --"] + sorted(df['name'].tolist()))
    if f_choice != "-- Choose a Profile --":
        f_data = df[df['name'] == f_choice].iloc[0]
        # RECOVERED: Centered Luxury Card
        st.markdown(f"""
            <div class="vault-card">
                <div class="vault-title">{f_data['name']}</div>
                <div class="vault-subtitle">{f_data['brand']} • {f_data['segment']}</div>
                <div style="display: flex; justify-content: center; gap: 70px; margin: 45px 0; flex-wrap: wrap;">
                    <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px; margin-bottom:12px;">QUALITY SCORE</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem;">{f_data['community_score']}/5.0</h3></div>
                    <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px; margin-bottom:12px;">GLOBAL VOTES</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem;">{f_data['community_votes']}</h3></div>
                </div>
                <div style="border-top:1px solid #222; padding-top:30px; max-width:650px; margin:0 auto;">
                    <p style="color:#D4AF37; font-size:0.85rem; font-weight:bold; letter-spacing:2px; margin-bottom:15px; text-transform:uppercase;">Olfactory Strategic Profile</p>
                    <p style="color:#ccc; font-size:1.15rem; line-height:1.7;">{f_data['top_notes']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 4: 2026 OUTLOOK ---
with tab4:
    st.markdown('<div class="section-header">Strategic Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    t_list = [
        ("🧪 Functional Scent", "AI-designed neuro-perfs designed for mental wellness. Scent becomes a biotech pillar."),
        ("🧛‍♀️ Vamp Romantic", "The shift toward gothic opulence. Dark cherry and leather dominance in Gen Z prestige."),
        ("📈 Macro Resilience", "Poland's trillion-dollar powerhouse status. Supply chains adapting to regional shifts.")
    ]
    for col, (t_title, t_text) in zip([c1, c2, c3], t_list):
        col.markdown(f'<div style="border:1px solid #333; background:rgba(10,10,10,0.95); padding:35px; border-left: 4px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans; letter-spacing:1px; margin-bottom:15px;">{t_title}</h4><p style="color:#bbb; font-size:0.95rem; line-height:1.7;">{t_text}</p></div>', unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tab5:
    st.markdown('<div class="section-header">Interconnected Analytical Ecosystem</div>', unsafe_allow_html=True)
    ecosystem = [
        ("🌍 Aromo Intelligence", "Russian market scraping engine and strategic regional dashboard.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"),
        ("🔍 Perfume Finder", "Consumer recommendation PoC based on preference matching.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning trend visualization and community mapping.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS Hub", "Backend architecture for high-fidelity massive dataset management.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    e_cols = st.columns(2)
    for i, (e_n, e_d, e_l) in enumerate(ecosystem):
        with e_cols[i % 2]:
            st.markdown(f'<div class="project-card"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:12px; letter-spacing:1.5px;">{e_n}</h4><p style="color:#888; font-size:0.9rem; line-height:1.6;">{e_d}</p></div><div style="margin-top:30px;"><a href="{e_l}" target="_blank" class="btn-launch">🚀 Launch Professional Application</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)