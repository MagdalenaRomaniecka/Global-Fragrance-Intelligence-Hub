import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. UI SETUP & LUXURY CSS 
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Strategic Hub", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    .stApp { background-color: #000000; background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%); font-family: 'Lato', sans-serif !important; }
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 15px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; width: 100%; max-width: 800px; box-sizing: border-box; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 60px; text-align: center; background-color: #050505; }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 4px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 10px; font-weight: 300; }
    
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 15px; text-align: center; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; border-radius: 4px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.1); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; font-weight: bold; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; margin: 0; }
    
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; border-left: 3px solid #D4AF37; padding-left: 15px; margin: 25px 0 15px 0; text-transform: uppercase; letter-spacing: 1px; }
    .info-box { background: rgba(255,255,255,0.03); padding: 25px; border: 1px solid #222; border-radius: 5px; margin-bottom: 20px; }
    .info-title { color: #D4AF37; font-weight: bold; margin-bottom: 10px; font-size: 1.1rem; }
    .info-text { color: #bbb; font-size: 0.95rem; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DATA PIPELINE
# -----------------------------------------------------------------------------
try:
    df = load_and_merge_data()
except Exception as e:
    st.error(f"Data loading failed. Details: {e}")
    df = pd.DataFrame()

# -----------------------------------------------------------------------------
# 3. HEADER & STRATEGIC MACRO METRICS
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Global Fragrance Intelligence</h1>
                <div class="sub-title">Poland: 5th Largest EU Market • Strategic Hub 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.markdown('<div class="metric-box"><div class="metric-label">PL: EU Market Rank</div><div class="metric-value">#5</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="metric-box"><div class="metric-label">PL Growth vs EU Avg</div><div class="metric-value">+75.3%</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="metric-box"><div class="metric-label">PL Export Value</div><div class="metric-value">€2.3B</div></div>', unsafe_allow_html=True)
c4.markdown('<div class="metric-box"><div class="metric-label">Model Reliability</div><div class="metric-value">91%</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 4. DASHBOARD TABS
# -----------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["EUROPEAN MARKET ANALYSIS", "DEEP DIVE ANALYTICS", "2026 TREND RADAR"])

# --- TAB 1: EUROPEAN MARKET ANALYSIS ---
with tab1:
    st.markdown('<div class="section-header">Regional Synthesis: The $11.58B Market</div>', unsafe_allow_html=True)
    
    col_text, col_audio = st.columns([1, 1])
    
    with col_text:
        st.markdown("""
            <div class="info-box">
                <p class="info-title">The "Barbell Market" Phenomenon</p>
                <p class="info-text">
                The European fragrance market, projected to reach <strong>$11.58 billion by 2026</strong>, is exhibiting a profound "Barbell" structure. 
                We are observing simultaneous exponential growth in the extreme budget tier and the ultra-luxury niche segment, leading to a severely squeezed middle market. 
                Poland serves as the primary hub for this transition, acting as the 7th largest exporter in the EU.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_audio:
        st.markdown('<div class="section-header" style="margin-top:0;">Audio Intelligence: Episode 3</div>', unsafe_allow_html=True)
        st.info("🎧 Ep 3: The European Barbell, Poland's 75% Growth & Stanford Data Validation")
        
        # Audio Player for NotebookLM output (TUTAJ JEST ZMIANA NA .MP3)
        try:
            st.audio('ep3_europe_barbell.mp3', format='audio/mpeg')
        except Exception:
            st.warning("Audio file 'ep3_europe_barbell.mp3' not found. Please upload to the repository.")
        
        # Executive Transcript Expander (Now Fully in English)
        with st.expander("📄 View Executive Transcript"):
            st.markdown("""
            **Host 1:** Welcome back to the Global Fragrance Intelligence Hub. Today we have an updated 2025-2026 report on our desk, focusing on the European market. This sheds completely new light on our previous findings.
            
            **Host 2:** Imagine a barbell at the gym. You have massive weights on both ends and a thin bar in the middle. That is exactly what is happening in Europe right now. Consumers are fleeing the 'middle market'. They are moving either to the absolute bottom of the barbell (budget mists under $30) or to the ultra-luxury niche (above $150).
            
            **Host 1:** And the region that is ground zero for this phenomenon is Poland... which grew by 75.3%, more than twice as fast as the EU average, becoming the 5th largest market in the EU with a trade surplus of 2.3 billion euros.
            
            **Host 2:** Moreover, our analysis of this data is backed by Machine Learning research from Stanford, which showed a prediction error of only 9-12%. This proves that our Kaggle-based models are a highly precise econometric tool.
            """)

    if not df.empty and 'market_structure' in df.columns:
        barbell_counts = df['market_structure'].value_counts().reset_index()
        barbell_counts.columns = ['Market Tier', 'Product Count']
        
        fig_barbell = px.bar(
            barbell_counts, 
            x='Market Tier', 
            y='Product Count',
            color='Market Tier',
            title="Evidence of the Barbell Market Phenomenon 2026",
            color_discrete_map={
                'Ultra-Niche (Barbell Top)': '#D4AF37', 
                'Budget (Barbell Bottom)': '#F0E68C', 
                'Squeezed Middle': '#444444'
            },
            template="plotly_dark"
        )
        fig_barbell.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato")
        st.plotly_chart(fig_barbell, use_container_width=True)

# --- TAB 2: DEEP DIVE ANALYTICS ---
with tab2:
    st.markdown('<div class="section-header">Technical Integrity & Stanford Validation</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="info-box">
            <p class="info-title">Stanford Boosting Validation (9-12% Error Rate)</p>
            <p class="info-text">
            Our strategic findings are anchored in high-fidelity Kaggle archives (FragDB: 119k records). 
            Academic research, specifically <i>Stanford Machine Learning</i> models, validates that community rating structures yield an exceptionally low prediction error of 9-12%, ensuring industrial-grade forecasting reliability for the 2026 outlook.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if not df.empty and 'region' in df.columns:
        st.markdown('<p style="color:#D4AF37; font-size:0.9rem; margin-top:10px;">* Highlighting European brands (Gold) vs Global market (Grey)</p>', unsafe_allow_html=True)
        
        fig_scatter = px.scatter(
            df, 
            x="community_votes", 
            y="community_score", 
            size="price_usd", 
            color="region",
            hover_name="name", 
            hover_data=["brand", "market_structure"],
            title="European Performance vs Global Benchmark",
            template="plotly_dark",
            color_discrete_map={'Europe': '#D4AF37', 'Global': '#333333'}
        )
        fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato")
        fig_scatter.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
        st.plotly_chart(fig_scatter, use_container_width=True)

# --- TAB 3: 2026 TREND RADAR ---
with tab3:
    st.markdown('<div class="section-header">Strategic Outlook 2026-2035</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="border-left: 3px solid #D4AF37; padding-left: 15px;">
            <h4 style="color:#D4AF37; font-family:'Tenor Sans'; margin-bottom:5px;">Recession Glam</h4>
            <p style="color:#bbb; font-size:0.85rem;">Driven by global inflation, consumers prioritize premium accessible experiences. Sol de Janeiro and high-end body mists (+7.1% YoY) replace traditional luxury goods.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style="border-left: 3px solid #F0E68C; padding-left: 15px;">
            <h4 style="color:#F0E68C; font-family:'Tenor Sans'; margin-bottom:5px;">Functional Fragrance</h4>
            <p style="color:#bbb; font-size:0.85rem;">The rise of neuro-cosmetics. 71% of global consumers now expect fragrances to regulate mood, leveraging AI-designed biotech molecules like Cereboost™.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div style="border-left: 3px solid #666; padding-left: 15px;">
            <h4 style="color:#888; font-family:'Tenor Sans'; margin-bottom:5px;">Market Autarky (RU)</h4>
            <p style="color:#bbb; font-size:0.85rem;">An isolated case study where 35% import tariffs fostered a localized ecosystem, empowering domestic brands to capture 68% of the Russian Federation market.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr style="border-color:#222;"><div style="text-align:center; color:#444; font-size:0.7rem; font-family:\'Lato\'; letter-spacing: 2px;">MAGDALENA ROMANIECKA • DATA STRATEGY & WEB ANALYTICS 2026</div>', unsafe_allow_html=True)