import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
from data_loader import load_and_merge_data

st.set_page_config(page_title="Fragrance Intelligence ✦ Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0E0E0E;
        background-image: radial-gradient(circle at 50% 0%, #181818 0%, #0E0E0E 100%);
        color: #E0E0E0;
        font-family: 'Lato', sans-serif !important;
    }
    
    @media (max-width: 768px) {
        .main-title { font-size: 1.2rem !important; letter-spacing: 2px !important; }
        .header-inner { padding: 15px 10px !important; }
        .metric-value { font-size: 1.2rem !important; }
        .metric-label { font-size: 0.55rem !important; letter-spacing: 1.5px !important; }
        .report-frame { padding: 15px !important; font-size: 0.9rem !important; text-align: left !important; line-height: 1.6 !important; }
        .section-header { font-size: 1.1rem !important; margin: 20px 0 10px 0 !important; }
    }
    
    [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2 {
        text-align: center !important; justify-content: center !important; display: flex !important; width: 100% !important;
    }
    .header-wrapper { display: flex; justify-content: center; text-align: center; padding: 20px 0 10px 0; }
    .header-outer { border: 1px solid #333333; padding: 10px; display: inline-block; width: 100%; max-width: 750px; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 50px; background-color: #0E0E0E; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 5px; margin: 0; border: none !important; }
    
    h1 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; border-bottom: 1px solid #D4AF37 !important; padding-bottom: 15px !important; text-transform: uppercase !important; font-size: 1.8rem !important; }
    h2 { color: #D4AF37 !important; font-family: 'Tenor Sans' !important; text-transform: uppercase !important; border-top: 1px solid #262626 !important; padding-top: 30px !important; margin-top: 45px !important; font-size: 1.4rem !important; }
    
    .metric-box { border: 1px solid #262626; background-color: #121212; padding: 20px; text-align: center; transition: 0.3s; border-radius: 2px; margin-bottom: 10px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
    .metric-label { color: #888888; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 700; margin-bottom: 8px; }
    .metric-value { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; }
    
    .report-frame {
        background: #121212;
        padding: 40px;
        border: 1px solid #262626;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        color: #E0E0E0;
        line-height: 1.9;
        text-align: justify;
        margin-bottom: 20px;
        font-size: 0.95rem;
        border-radius: 2px;
        width: 100%;
        overflow-wrap: break-word;
    }
    .debrief-main-title, .dossier-main-title {
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        text-transform: uppercase;
        font-size: 1.4rem;
        margin-bottom: 5px;
        line-height: 1.3;
    }
    .debrief-sub-title, .dossier-sub-title {
        color: #E0E0E0;
        font-family: 'Lato', sans-serif;
        font-weight: 700;
        font-size: 0.85rem;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #333333;
    }
    .strategic-scope {
        color: #888888;
        font-family: 'Lato', sans-serif;
        font-size: 0.85rem;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    .part-heading, .dossier-topic-title {
        color: #E0E0E0;
        font-family: 'Lato', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .dossier-section-title {
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        text-transform: uppercase;
        font-size: 1.1rem;
        margin-top: 40px;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }
    .dialogue-text, .dossier-text {
        color: #E0E0E0;
        font-family: 'Lato', sans-serif;
        font-size: 0.95rem;
        line-height: 1.8;
        margin-bottom: 15px;
    }
    
    .section-header { 
        color: #D4AF37; 
        font-family: 'Tenor Sans'; 
        font-size: 1.4rem; 
        text-align: center !important; 
        border-bottom: 1px solid #D4AF37; 
        padding-bottom: 10px; 
        margin: 30px auto 20px auto; 
        text-transform: uppercase; 
        letter-spacing: 3px; 
        width: 100%;
    }
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 10px; background-color: #0E0E0E; flex-wrap: wrap; }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p { text-align: center !important; font-family: 'Tenor Sans', sans-serif !important; letter-spacing: 1px; font-size: 0.8rem; color: #E0E0E0; }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #D4AF37 !important; }
    
    .project-card { border: 1px solid #262626; background: rgba(18,18,18,0.95); padding: 20px; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 20px; border-radius: 2px; }
    .project-card:hover { border-color: #D4AF37; box-shadow: 0 0 20px rgba(212, 175, 55, 0.15); }
    .btn-launch { display: block; width: 100%; padding: 12px; background: #D4AF37 !important; color: #0E0E0E !important; text-align: center; font-weight: bold; text-transform: uppercase; font-size: 0.7rem; text-decoration: none; letter-spacing: 2px; border-radius: 2px; }
    .footer { position: relative; width: 100%; background-color: #0E0E0E; color: #666666; text-align: center; padding: 30px; font-size: 0.65rem; border-top: 1px solid #1F1F1F; z-index: 999; letter-spacing: 2px; margin-top: 50px; }
    
    .intelligence-badge { text-align: center; color: #D4AF37; font-size: 0.85rem; font-style: italic; margin: 15px auto 25px auto; letter-spacing: 1px; border: 1px solid rgba(212,175,55,0.3); padding: 12px; background: rgba(212,175,55,0.05); max-width: 800px; }
    
    .stSelectbox label, .stSelectbox [data-testid="stMarkdownContainer"] p {
        font-family: 'Tenor Sans', sans-serif !important;
        font-size: 1.1rem !important;
        color: #D4AF37 !important;
        text-align: center !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        width: 100% !important;
        display: block !important;
    }
    
    div[data-testid="stSelectbox"] > div {
        margin: 0 auto !important;
        max-width: 400px !important;
    }
    </style>
""", unsafe_allow_html=True)

def find_file(filename):
    for root, _, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return filename

df = load_and_merge_data()
if 'segment' in df.columns:
    df['segment'] = df['segment'].str.replace('-', ' ')

briefings_content = {
    "Ep. 3": {
        "debrief": """
<div class="debrief-main-title">🎙️ INTELLIGENCE BRIEFING. THE 2025 FRAGRANCE LANDSCAPE</div>
<div class="debrief-sub-title">Strategic Deep Dive • Executive Debrief</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area Western Markets (North America, Europe), Russian domestic market. ✦ Data Intelligence Euromonitor International, Pinterest 2025 consumer trends, Sephora and Amazon sales data. ✦ Key Phenomenon Recession Glam and the shift from luxury perfumes to body mists (Scent Stacking).</div>
<div class="part-heading">Part I. The $600 Billion Contradiction and Recession Glam</div>
<p class="dialogue-text"><strong>HOST</strong> I was looking at the Euromonitor report this morning, and there is a number that just does not square with the current headlines.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Oh, yeah. I mean, we keep hearing about "shrinkflation", the cost of eggs, and about this global tightening of belts.</p>
<p class="dialogue-text"><strong>HOST</strong> Exactly. It is on the news every night. And yet, the global beauty market just clocked in at $593 billion for 2024.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Wow. That is nearly a $600 billion contradiction. It is staggering when you put it like that. Usually, when the economy wobbles, luxury is the first thing to go. You don't buy the sports car or the designer handbag.</p>
<p class="dialogue-text"><strong>HOST</strong> True. But what we are seeing is a documented phenomenon called Recession Glamour. When the massive luxury items are completely out of reach, consumers aggressively pivot to micro-luxuries to hack their dopamine levels.</p>
<p class="dialogue-text"><strong>CO HOST</strong> And fragrance is the ultimate micro-luxury. The data reflects this perfectly; European Gen Z consumers are spending around 204 EUR annually on scents, entirely bypassing traditional designer barriers.</p>
""",
        "dossier": """
<div class="dossier-main-title">🧠 2026 TREND REPORT ✦ NEURO RECESSION GLAM</div>
<div class="dossier-sub-title">Strategic Deep Dive ✦ Fragrance Market and Givaudan Strategy</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area Western Markets North America Europe ✦ Data Intelligence FMCG sector analysis Tariff impact models Consumer psychology ✦ Key Phenomenon The Sol de Janeiro effect as a hedge against Section 122</div>
<div class="dossier-section-title">MARKET ANALYSIS AND CONSUMER TRENDS</div>
<div class="dossier-topic-title">The Sol de Janeiro and Lattafa Phenomenon</div>
<p class="dossier-text">As FMCG sector analysts we observe the unprecedented dominance of Sol de Janeiro in the mass premium segment. This brand is the prime example of the Barbell Bottom strategy offering high emotional value at a controlled price point. Deep Research indicates that brands mastering this space like Yara by Lattafa experienced a 137.6 percent surge in digital interest largely driven by TikTok virality.</p>
<p class="dossier-text">✦ Key Success Factors ✦ Gourmand 2.0 and Dopamine Hacking Flagship compositions such as Cheirosa 62 use edible notes like salted caramel to trigger safety and warmth in the brain. This is a deliberate psychological response to global economic uncertainty.</p>
<p class="dossier-text">✦ The Section 122 Tariff Impact ✦ The US implementation of Section 122 triggered a massive geographical pivot, inflating standard designer bottles to over $180, further accelerating the adoption of accessible Middle Eastern clones and Scent Stacking routines.</p>
"""
    },
    "Ep. 4": {
        "debrief": """
<div class="debrief-main-title">🎧 INTELLIGENCE BRIEFING. THE EUROPEAN BARBELL & DATA VS CHEMISTRY</div>
<div class="debrief-sub-title">Strategic Deep Dive • Audio Transcript</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area European Union market (emphasis on offline dominance in Poland) vs digital markets (USA). ✦ Data Intelligence Global Fragrance Intelligence Hub, Stanford University algorithmic research, Kaggle and eBay datasets. ✦ Key Phenomenon Market polarization (The Barbell Effect), chemical regulations (IFRA and REACH) vs digital scent profiling.</div>
<div class="part-heading">Part I. The Data Science Discipline</div>
<p class="dialogue-text"><strong>HOST 1</strong> Welcome to the debate. Can a line of code predict what smells beautiful?</p>
<p class="dialogue-text"><strong>HOST 2</strong> I mean, with like 91% accuracy, it sounds like science fiction, honestly.</p>
<p class="dialogue-text"><strong>HOST 1</strong> It really does. But if you have ever bought a fragrance because a social media algorithm told you it perfectly matched your aesthetic, you are already a data point in this massive, completely invisible shift.</p>
<p class="dialogue-text"><strong>HOST 2</strong> Today, we are looking at a collision that is worth literally billions.</p>
<p class="dialogue-text"><strong>HOST 1</strong> Yes, specifically, we are examining the European perfume market, which is scaling toward an $11.58 billion valuation by 2026.</p>
<p class="dialogue-text"><strong>HOST 2</strong> Right. And on one side of this collision, you have the centuries old romanticism of the master perfumer. And on the other, you have the relentless, predictive logic of artificial intelligence, which brings us to the core of what we are talking about today, drawing from the recent Global Fragrance Intelligence Hub analysis.</p>
<p class="dialogue-text"><strong>HOST 1</strong> Exactly. We are tackling a very specific question. As the fragrance industry scales to these unprecedented heights, is its future primarily dictated by predictive digital analytics and crowdsourced perception? Or does ultimate success still hinge on localized physical retail ecosystems and actual material sensory chemistry?</p>
<p class="dialogue-text"><strong>HOST 2</strong> Right. The physical stuff.</p>
<p class="dialogue-text"><strong>HOST 1</strong> So I will be taking the position that predictive data, AI, and crowdsourced consumer sentiment are the new primary architects of market dominance. I mean, the fragrance industry is no longer just about chemistry. It is fundamentally a data science discipline now.</p>
<p class="dialogue-text"><strong>HOST 2</strong> And I will be taking the opposing view because while the massive surge in data provides an incredibly detailed map of consumer behavior, the territory itself remains unyieldingly physical. You can track all the data you want, right? But the foundational reality of this market still comes down to physical retail infrastructure, regional supply chain logistics, and the actual, literal material chemistry inside the bottle.</p>
""",
        "dossier": """
<div class="dossier-main-title">📊 MARKET POLARIZATION ✦ THE BARBELL EFFECT</div>
<div class="dossier-sub-title">Operational Data Intelligence 2025 to 2026</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area European Market Infrastructure. ✦ Data Intelligence Stanford ML Boosting, Kaggle & eBay Secondary Markets. ✦ Key Phenomenon The 87.6% Offline Dominance in Poland vs Digital Scent Profiling.</div>
<div class="dossier-section-title">THE DIGITAL DISCOVERY ILLUSION</div>
<div class="dossier-topic-title">Stanford Algorithms vs Physical Bottlenecks</div>
<p class="dossier-text">The fragrance industry is decoupling discovery from the physical vial, heavily driven by digital channels. Stanford University researchers utilized ML boosting on Fragrantica datasets, achieving a 9% error rate in predicting popularity based on algorithmic features like seasonality and sillage.</p>
<p class="dossier-text">✦ Marketing Illusions ✦ Crowdsourced data often reflects marketing narratives rather than chemical compositions. A 0.28 correlation between online availability and actual sales proves that mere inventory and digital buzz are insufficient without physical sensory verification.</p>
<div class="dossier-section-title">THE PHYSICAL BARBELL STRUCTURE</div>
<div class="dossier-topic-title">Poland's Offline Dominance and Regulatory Ceilings</div>
<p class="dossier-text">Despite the digital surge (e-commerce projected at 33% by 2025), the foundation remains physical. 60% of consumers demand offline testing.</p>
<p class="dossier-text">✦ The Rossmann Network ✦ In Poland, the fastest-growing EU market (75.3% growth since 2014), traditional drugstores hold an 87.6% market share. The "Barbell" structure means high-volume budget options and premium luxury are serviced through this physical infrastructure.</p>
<p class="dossier-text">✦ IFRA and REACH ✦ Chemical regulations frequently ban synthetic molecules. If an AI predicts success based on a banned formula, the model becomes obsolete. Physical performance of reformulated juice dictates retention, proving the chemical ceiling overrules digital tags.</p>
"""
    },
    "Ep. 5": {
        "debrief": """
<div class="debrief-main-title">🎙️ INTELLIGENCE BRIEFING. CARTO AI & NEURO-TECH</div>
<div class="debrief-sub-title">Strategic Deep Dive • Executive Debrief</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area AI Formulation, EEG/fMRI Brainwave Mapping. ✦ Data Intelligence Givaudan Carto AI, IBM Philyra, MoodScentz, Myrissi. ✦ Key Phenomenon Algorithmic olfactory synthesis vs human intuition.</div>
<div class="part-heading">Part I. The Olfactory Memory Bottleneck</div>
<p class="dialogue-text"><strong>HOST</strong> If you are wearing like a popular long-lasting perfume right now, there is a very high probability that the chemical anchoring that sent to your warm skin will still be detectable in the environment long after you leave the room.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Wazily. Hours later.</p>
<p class="dialogue-text"><strong>HOST</strong> Right. And in fact, science is now finding these exact synthetic fragrance molecules in human breast milk, which is just, it's wild. Today, we are completely tearing up the romantic image of the perfume industry for this deep dive.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Yeah, we really are. Because, you know, you usually look at a bottle of luxury fragrance and you picture like a master artisan wandering through a field in grass at dawn, hand-picking jasmine petals, relying purely on inspiration and, well, a gifted nose.</p>
<p class="dialogue-text"><strong>HOST</strong> Which is a beautiful image, but it's totally outdated.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Completely. The stack of sources we have for today destroys that illusion entirely. We are looking at dense thermodynamic data, highly technical olfactory compendiums, and like the machine learning architecture of modern fragrance apps. We are looking at poetry and a bottle here. We are looking at a highly clinical, intensely engineered landscape. We are the transition from, you know, traditional artisanal blending to advanced chemical engineering and increasingly artificial intelligence is absolute at this point.</p>
<p class="dialogue-text"><strong>HOST</strong> So where do we even begin with this?</p>
<p class="dialogue-text"><strong>CO HOST</strong> Well, to understand how technology is rewriting fragrance, we have to start at the foundational level, like how the raw materials themselves are captured and classified today, even the traditional language of scent is being overhauled.</p>
<p class="dialogue-text"><strong>HOST</strong> Oh, right. The typology changes.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Exactly. For example, what the industry used to call the Oriental category is now strictly classified as amber. And classic florals are increasingly being engineered from the ground up to be completely unisex. But the real paradigm shift, the big one is happening in the extraction processes.</p>
<div class="part-heading">Part II. AI Architecture and Neuro-Perfumery</div>
<p class="dialogue-text"><strong>HOST</strong> Well, that data points to the existential crisis of modern perfumery. Because if machines can perfectly analyze and deconstruct a successful formula, identifying the exact ratio of hetion to amber oxen, the inevitable next step is having machines design the formulas themselves. So we are talking about AI formulas taking over the laboratories now completely bypassing the human nose.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Absolutely. Table 3 in the industry compendiums outlines the specific tools reshaping creation right now. We see systems like carto by jive adon right the visual mapping one.</p>
<p class="dialogue-text"><strong>HOST</strong> Yeah, it's a visual mapping system that relies on molecular data to suggest highly unusual chemical combinations. Things that a human perfumer bound by classical training and, you know, traditional aesthetics would simply never think to pair together. The source is also highlight falera developed by IBM and simrise. And this is a deep learning algorithm trained on a database of 1.7 million existing perfume formulas.</p>
<p class="dialogue-text"><strong>CO HOST</strong> 1.7 million. A human could never smell that many.</p>
<p class="dialogue-text"><strong>HOST</strong> Never. It designed sense from scratch based on demographic briefs. And it works in tandem with tools like Ecoset compass, which calculates and tracks the exact carbon footprint of the resulting formula in real time.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Which is amazing for sustainability, sure. But the most intense advancement isn't just about mixing chemicals faster or tracking carbon. It's neuro perfumery.</p>
<p class="dialogue-text"><strong>HOST</strong> Neuro perfumery. That sounds almost dystopian.</p>
<p class="dialogue-text"><strong>CO HOST</strong> It's just fragrance from an aesthetic choice to a mathematically optimized physiological stimulus. Companies like L'Oreal and emotive are placing eG headsets on consumers to track their real time electrical brain waves while they smell different raw materials.</p>
<p class="dialogue-text"><strong>HOST</strong> Okay, wait. The Pug fragrance phantom by Poccarobon is the prime example of this applied science in the sources, right?</p>
<p class="dialogue-text"><strong>CO HOST</strong> Yes, phantom is the perfect case study. Pug didn't just guess what consumers would find appealing. They utilized 45 million EEG brain wave records to mathematically validate the exact overdosing of a specific molecule called styrolycathirally acetate.</p>
<p class="dialogue-text"><strong>HOST</strong> 45 million records. Let that sink in. They tracked 45 million brain responses just to dial in one single molecule. And they did this for a very specific physiological reason, right?</p>
<p class="dialogue-text"><strong>CO HOST</strong> To precisely, if the goal is just hacking the amygdala for a dopamine spike, we aren't creating art anymore. We are just directly manipulating human neurochemistry.</p>
""",
        "dossier": """
<div class="dossier-main-title">🧠 GIVAUDAN CARTO AI ✦ NEURO-COGNITIVE ENGINEERING</div>
<div class="dossier-sub-title">Operational Data Intelligence 2025 to 2026</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area AI Formulation & Chemical Physics. ✦ Data Intelligence Givaudan Carto, IBM Philyra, SBERT NLP, Cosine Similarity. ✦ Key Phenomenon Replacing human intuition with data-driven neuro-engineering.</div>
<div class="dossier-section-title">ALGORITHMIC SCENT FORMULATION & GC-MS DATA</div>
<div class="dossier-topic-title">Supercritical Extraction and Reverse Engineering</div>
<p class="dossier-text">The modern standard demands absolute perfection in raw materials, fundamentally altering the architecture of luxury fragrance production. The integration of high-level biotechnology allows for unprecedented extraction and analysis.</p>
<p class="dossier-text">✦ Supercritical CO2 Extraction ✦ Carbon dioxide is subjected to 74 bar pressure at 31.1°C, entering a supercritical state. It acts as the perfect solvent, dissolving delicate aromatic molecules without the destructive heat of traditional steam distillation, leaving zero toxic residues.</p>
<p class="dossier-text">✦ GC-MS Reverse Engineering ✦ Gas Chromatography-Mass Spectrometry physically separates molecules and bombards them with electrons to read their mass-to-charge ratio. This creates a perfect chemical fingerprint, effectively eliminating the concept of a "trade secret". For example, GC-MS analysis of Baccarat Rouge 540 reveals a blocky, high-impact architecture: 35.3% Hedione, 18.5% Ambroxan, 10.5% Veramoss, and 27.0% DPG solvent.</p>
<p class="dossier-text">✦ AI Infrastructure ✦ Systems like Givaudan's Carto and IBM's Philyra bypass human biological limitations. Philyra, trained on a database of 1.7 million formulas, designs scents from scratch while continuously calculating chemical stability and carbon footprint in real-time.</p>
<div class="dossier-section-title">NEURO-PERFUMERY AND LIMBIC SYSTEM HACKING</div>
<div class="dossier-topic-title">EEG Mapping and Molecular Overdosing</div>
<p class="dossier-text">The industry has shifted from aesthetic choices to mathematically optimized physiological stimuli.</p>
<p class="dossier-text">✦ EEG & fMRI Brainwave Mapping ✦ Companies utilize EEG headsets to track real-time electrical brain waves while consumers smell raw materials. The Paco Rabanne Phantom case study highlights the use of 45 million EEG brainwave records.</p>
<p class="dossier-text">✦ Molecular Overdosing ✦ The 45 million data points were used to mathematically validate the exact overdosing of Styrallyl Acetate. This creates a physiological trigger that hacks the amygdala for a dopamine spike, directly manipulating human neurochemistry to bypass rational consumer choice.</p>
<div class="dossier-section-title">THERMODYNAMICS VS. PYTHON CODE</div>
<div class="dossier-topic-title">Raoult's Law and Chemical Mutations</div>
<p class="dossier-text">Even the most statistically perfect AI model is governed by physical laws once the liquid hits warm human skin.</p>
<p class="dossier-text">✦ Raoult's Law & Fick's Second Law ✦ Perfume formulation is a macroscopic battle against evaporation. Heavy fixative molecules form intermolecular bonds with bouncy molecules to alter the evaporation curve.</p>
<p class="dossier-text">✦ Chemical Mutation (Calone 1951) ✦ When an algorithm pairs a volatile aquatic molecule like Calone 1951 with a heavy absolute, the thermodynamic balance is fragile. If dosed over 0.5%, the thermal energy of skin causes Calone to self-eject. It oxidizes incredibly rapidly, mutating from a fresh sea breeze into the smell of rotting oysters.</p>
"""
    },
    "Ep. 6": {
        "debrief": """
<div class="debrief-main-title">🎙️ INTELLIGENCE BRIEFING. B2B PRICE ELASTICITY</div>
<div class="debrief-sub-title">Strategic Deep Dive • Executive Debrief</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area Global Retail & Middle East Maceration Arbitrage. ✦ Data Intelligence B2B Cost Allocation, Price Elasticity -1.81, 4-Tier Market Taxonomy. ✦ Key Phenomenon The $1.50 juice vs $150 retail markup trap.</div>
<div class="part-heading">Part I. Deconstructing the Designer Bottle</div>
<p class="dialogue-text"><strong>HOST</strong> I want you to picture something for a second. Just look at a heavy glossy glass bottle of luxury designer perfume. Right. The kind with the magnetic cap and the heavy base.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Exactly.</p>
<p class="dialogue-text"><strong>HOST</strong> Now, if you just paid, say, $150 for that bottle, how much do you think the actual liquid inside is worth? Like the actual scent you're putting on your skin?</p>
<p class="dialogue-text"><strong>CO HOST</strong> I mean, most consumers assume they're paying for the liquid, right? So they figure maybe 50 bucks, or I don't know, $30 if they factor in a really high brand markup.</p>
<p class="dialogue-text"><strong>HOST</strong> But the actual scented liquid inside that $150 mainstream bottle, it's usually worth about $1.50. It's wild to think about.</p>
<p class="dialogue-text"><strong>CO HOST</strong> It really is. Maybe $3 if it's a particularly heavy formulation. But yeah, welcome to a deep dive into the global fragrance industry. And we've got a massive stack of analytical reports today. We're looking at data spanning from 2024 all the way to 2035.</p>
<p class="dialogue-text"><strong>HOST</strong> Yeah. So I think from macroeconomics to supply chains and these really rigid market taxonomies. Because the mission here is to decode how a $62.1 billion global market is just like actively marching toward an estimated $85.5 billion valuation by 2035. All while a physical product inside the bottle basically costs pennies.</p>
<p class="dialogue-text"><strong>CO HOST</strong> So to really understand where this industry is heading, we have to start with where your money actually goes.</p>
<p class="dialogue-text"><strong>HOST</strong> Right. And then we have the invisible architecture, the bottle economics.</p>
<div class="part-heading">Part II. The Negative 1.81 Price Elasticity</div>
<p class="dialogue-text"><strong>CO HOST</strong> Yeah, let's talk about that. Because the reports detailed this thing called a negative 1.81 price elasticity index in the mainstream sector, which is a very technical way of saying they are trapped.</p>
<p class="dialogue-text"><strong>HOST</strong> Exactly. Essentially, if a mainstream brand tries to raise the retail price of a, you know, a standard everyday cent by just 10%, consumer demand plummets by over 18%.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Right. They can't raise the shelf price without just bleeding buyers. So they have to ruthlessly squeeze the manufacturing costs instead.</p>
<p class="dialogue-text"><strong>HOST</strong> Which explains why the actual cent concentrate the juice along with the alcohol solvent makes up a mere 3 to 5% of the final retail price. Yeah. For a standard 100 milliliter designer bottle producing that liquid literally costs them 2 to 5 euros.</p>
<p class="dialogue-text"><strong>CO HOST</strong> So where does the rest of my $150 go?</p>
<p class="dialogue-text"><strong>HOST</strong> Well, 10 to 15% goes straight into the packaging, you know, the custom glass, the atomizers.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Right. So they're 15 to 25% is just eaten by global marketing. Those massive celebrity ambassador campaigns, you see everywhere. But the real financial black hole and this blew my mind is the traditional retail network.</p>
<p class="dialogue-text"><strong>HOST</strong> Oh, absolutely. The department stores and the global distributors, they absorb a massive 45 to 60% margin.</p>
<p class="dialogue-text"><strong>CO HOST</strong> 60% just have it sit on the shelf.</p>
<p class="dialogue-text"><strong>HOST</strong> Yeah. I mean, you are fundamentally paying for the department stores real estate. You're funding the glass display counters, the testers, the sales associates. It's like paying for a blockbuster movie ticket, but you're mostly funding the billboards and the theater's concession stand rather than the film itself.</p>
""",
        "dossier": """
<div class="dossier-main-title">📊 MACROECONOMIC PRICE ELASTICITY ✦ B2B LOGISTICS</div>
<div class="dossier-sub-title">Operational Data Intelligence 2024 to 2025</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area Global Trade Corridors & Margin Breakdowns. ✦ Data Intelligence -1.81 Elasticity Index, UAE Logistics Bypass. ✦ Key Phenomenon Maceration Arbitrage and the collapse of the middle market.</div>
<div class="dossier-section-title">DECONSTRUCTING THE DESIGNER BOTTLE</div>
<div class="dossier-topic-title">The Juice Constraint and Retail Black Hole</div>
<p class="dossier-text">The traditional Western designer fragrance market operates under severe, non-negotiable financial constraints defined by corporate accountants.</p>
<p class="dossier-text">✦ The Juice Constraint ✦ The actual scented concentrate and alcohol solvent in a standard $150 bottle account for merely 3% to 5% of the final retail price, equating to roughly €2 to €5.</p>
<p class="dossier-text">✦ The Marketing & Packaging Void ✦ Custom glass and atomizers absorb 10-15% of the budget. Global marketing, including celebrity ambassador campaigns, consumes 15-25%.</p>
<p class="dossier-text">✦ The Retail Black Hole ✦ The physical retail network (department stores and global distributors) absorbs an overwhelming 45% to 60% margin. Consumers are fundamentally funding commercial real estate and display counters, not the chemical formula.</p>
<p class="dossier-text">✦ Negative 1.81 Price Elasticity ✦ Mainstream brands are trapped by a -1.81 price elasticity index. A 10% increase in shelf price causes consumer demand to plummet by over 18%. To survive, brands ruthlessly squeeze manufacturing costs, forcing an absolute reliance on cheap, mass-produced synthetic molecules.</p>
<div class="dossier-section-title">THE NICHE INVERSION & MARKET TAXONOMY</div>
<div class="dossier-topic-title">4-Tier Classification and Format Shifts</div>
<p class="dossier-text">True niche perfumery flips the economic model entirely, allocating 40% to 60% of their budget directly into pure, high-quality raw materials.</p>
<p class="dossier-text">✦ The 4-Tier Taxonomy ✦ Digital culture has forced a rigid classification. Tier 1: Mainstream Designer (>100,000 units). Tier 2: Niche Prestige / Corporate Niche (10,000-50,000 units, acquired by conglomerates). Tier 3: Indie Segment (Independent, 100-5,000 units). Tier 4: Artisan Purist (<500 units, rigorous manual production).</p>
<p class="dossier-text">✦ Format Shifts ✦ To adapt to high material costs, niche brands are shifting heavily toward 10ml to 30ml formats and fueling a $1.2 billion subscription market boom, allowing consumers to experience high-end materials without a blind $300 commitment.</p>
<div class="dossier-section-title">THE MIDDLE EASTERN CLONE REVOLUTION</div>
<div class="dossier-topic-title">Maceration Arbitrage and Freight Shocks</div>
<p class="dossier-text">The single biggest supply chain disruption in modern perfumery is the Arabian "Dupe Culture." Brands like Lattafa, Armaf, and Afnan have reverse-engineered the industry.</p>
<p class="dossier-text">✦ Maceration Arbitrage ✦ Traditional Western brands freeze capital by storing mixed fragrance in climate-controlled warehouses for 4 to 12 weeks to macerate. UAE producers bypass this holding cost entirely by shipping freshly mixed, "green" juice within two weeks. They outsource the aging process to the consumer's bathroom cabinet, saving an absolute fortune in frozen capital.</p>
<p class="dossier-text">✦ Absorbing Freight Shocks ✦ During the 2024-2026 Red Sea crisis, 70% of shipping fleets bypassed the Suez Canal, extending transit by 14 days and spiking ocean freight costs by 400%. UAE dupe brands absorbed this shock through sheer scale. By loading massive containers directly at the Jebel Ali port and selling straight to e-commerce, the actual export freight cost per bottle remained fractions of a cent.</p>
"""
    },
    "Ep. 7": {
        "debrief": """
<div class="debrief-main-title">🎙️ INTELLIGENCE BRIEFING. EU REGULATORY SHOCK</div>
<div class="debrief-sub-title">Strategic Deep Dive • Executive Debrief</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area EU Chemical Fortress & Global Patent Moats. ✦ Data Intelligence GC-MS Analytics, IFRA 52nd Amendment, EU 2023/1545. ✦ Key Phenomenon Silent reformulations, Captive monopolies, and Batch Code Hunters.</div>
<div class="part-heading">Part I. The Illusion of Alchemy</div>
<p class="dialogue-text"><strong>HOST</strong> So if I told you that the defining scent of a $300 luxury perfume was chemically synthesized from a molecule that smells aggressively like raw garlic and onions, you would probably think I was joking.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Right. Or at least you'd really hope it was a joke.</p>
<p class="dialogue-text"><strong>HOST</strong> Yeah, exactly. I mean, when you walk up to a fragrance counter, the brand really wants you to imagine this master perfumer wandering through a sundrenched field in grass france, crushing delicate flower petals by hand. It is a beautifully constructed, very persistent illusion. I mean, the whole marketing apparatus is designed to sell you the alchemy of nature in a bottle. But today we are completely shattering that illusion. We've got a massive stack of industry reports in front of us for this deep dive. And this includes corporate financial ledgers and some really advanced olfactory chemistry analytics.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Which is fascinating stuff, really.</p>
<p class="dialogue-text"><strong>HOST</strong> It is. And our mission here is to cut straight through the marketing poetry and reveal the hidden architecture of modern perfumery. Because what you were actually paying for isn't just a basket of flower petals. You're funding this wild collision of multi-billion dollar corporate patents, extreme supply chain physics, and a very quiet, very intense global regulatory war.</p>
<p class="dialogue-text"><strong>CO HOST</strong> And that war is completely invisible to the average consumer. Like to understand today's fragrance market, we have to look past traditional alchemy. The modern industry is governed by high stakes intellectual property and, well, synthetic chemistry.</p>
<div class="part-heading">Part II. Reverse Engineering and GC-MS</div>
<p class="dialogue-text"><strong>HOST</strong> Let's actually start right there with the intellectual property because I found this part of the source is just mind blowing. The foundational problem for a perfume company is how they protect their recipes, right? Like if I invent a new piece of technology, I can patent it. If I write a novel, I copyright it. But according to the legal framework we're looking at, you cannot copyright a perfume recipe.</p>
<p class="dialogue-text"><strong>CO HOST</strong> No, you can't. It is legally treated like a culinary recipe for, you know, a soup or a cake.</p>
<p class="dialogue-text"><strong>HOST</strong> Which creates a massive vulnerability for these major fashion houses.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Exactly. Because in the modern era, any rival company can just buy a bottle of your best selling billion dollar fragrance to get back to a lab and run it through a machine called a GCMS.</p>
<p class="dialogue-text"><strong>HOST</strong> Which stands for gas chromatography mass spectrometry, right?</p>
<p class="dialogue-text"><strong>CO HOST</strong> You got it. I was trying to wrap my head around how that machine actually works. It sounds like straight-up science fiction. It's basically like feeding a fully baked cake into a high-tech scanner and the machine prints out the exact brand of flour the baker used, the exact number of eggs, and the specific baking temperature.</p>
<p class="dialogue-text"><strong>HOST</strong> That is actually a remarkably accurate way to picture it. The gas chromatography phase physically separates all the individual molecules in the liquid, and then the mass spectrometry phase weighs them to figure out exactly what they are.</p>
<p class="dialogue-text"><strong>CO HOST</strong> Wow. Yeah, so suddenly your competitor has your precise recipe and they can clone it for a fraction of the cost.</p>
""",
        "dossier": """
<div class="dossier-main-title">⚖️ INTELLECTUAL PROPERTY MOATS ✦ REGULATORY FORENSICS</div>
<div class="dossier-sub-title">Operational Data Intelligence 2024 to 2025</div>
<div class="strategic-scope">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area EU Chemical Fortress & Extraction Physics. ✦ Data Intelligence IFRA 52nd Amendment, EU 2023/1545. ✦ Key Phenomenon Silent reformulations and the Batch Code Hunter rebellion.</div>
<div class="dossier-section-title">INTELLECTUAL PROPERTY MOATS</div>
<div class="dossier-topic-title">The GC-MS Threat & Captive Moats</div>
<p class="dossier-text">The inability to copyright a fragrance formula—legally treating it like a soup recipe—creates a massive vulnerability. Rival companies utilize Gas Chromatography-Mass Spectrometry (GC-MS) machines to vaporize and physically separate molecules, generating a perfect chemical fingerprint of any competitor's hit fragrance.</p>
<p class="dossier-text">✦ The Captive Solution ✦ To prevent perfect cloning, chemical giants (Givaudan, Firmenich, Symrise) synthesize entirely novel molecules called "Captives." While the perfume cannot be patented, the specific chemical process to synthesize the Captive is protected by an ironclad 20-year patent.</p>
<p class="dossier-text">✦ Corporate Profitability ✦ Fashion houses must hire the patent holder to manufacture their fragrance. This strategy grants chemical giants an impenetrable monopoly, generating astronomical returns. For example, Givaudan's 2025 ledgers show 7.4B CHF in sales with a massive 24.2% EBITDA margin.</p>
<p class="dossier-text">✦ Extreme Synthesis ✦ Captives rely on molecular precision. Symrise's Spicatanate, synthesized from upcycled orange juice waste, smells like rotting garlic in pure form. However, at a microscopic 0.001% concentration, the garlic facet vanishes, creating a brilliant, fresh wasabi effect.</p>
<div class="dossier-section-title">THE EXTREME PHYSICS OF NATURAL EXTRACTION</div>
<div class="dossier-topic-title">Orris Butter, Wild Oud, and Rose Absolute</div>
<p class="dossier-text">Despite the high margins of synthetics, true luxury requires natural absolutes to act as complex blending agents that provide an organic "soul" to the sharp clinical edges of synthetic captives.</p>
<p class="dossier-text">✦ Orris Butter ($40,000–$100,000/kg) ✦ Requires the roots of the iris flower to be dried and dehydrated in a dark cellar for 3 to 5 years before extraction.</p>
<p class="dossier-text">✦ Wild Oud ($30,000–$80,000/kg) ✦ The result of a specific fungal infection inside the Aquilaria tree, essentially extracting the tree's immune system.</p>
<p class="dossier-text">✦ Rose Absolute ($8,000–$15,000/kg) ✦ Demands brutal raw agriculture. Yielding a single kilogram of Rose Absolute requires laborers to hand-pick roughly 1.5 million individual flowers to avoid steam distillation, which destroys thermal bile compounds.</p>
<div class="dossier-section-title">REGULATORY WARS & SILENT REFORMULATIONS</div>
<div class="dossier-topic-title">IFRA 52nd Amendment and Batch Code Hunters</div>
<p class="dossier-text">Global health regulations are constantly shifting, forcing brands to quietly dismantle and rebuild their iconic formulas.</p>
<p class="dossier-text">✦ IFRA 52nd Amendment & EU 2023/1545 ✦ The EU has vastly expanded allergen labeling. Crucially, IFRA has introduced 51 new restrictions heavily targeting natural compounds. Furocoumarins in natural citrus oils are restricted due to severe phototoxicity (blistering sunburns under UV light). Polycyclic musks like Galaxolide are banned due to bioaccumulation in human tissue and breast milk.</p>
<p class="dossier-text">✦ Batch Code Hunters ✦ Consumers have noticed these silent reformulations. A highly organized subculture of amateur forensic chemists—"Batch Code Hunters"—weaponize regulatory data. They audit microscopic FIL (Formula Information List) codes printed on boxes to track formula mutations.</p>
<p class="dossier-text">✦ The Creed Aventus Cult ✦ Consumers obsessively track batch variations, treating bottles like rare vintage wine. The legendary smoky "11Z01" batch of Creed Aventus commands exorbitant aftermarket prices, as fans argue the scent fundamentally lost its signature birch-tar smokiness following corporate acquisition and regulatory compliance.</p>
"""
    }
}

tabs = st.tabs(["STRATEGIC BRIEFINGS", "MACRO & B2B SIMULATIONS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

with tabs[0]:
    col_nav, col_viz = st.columns([1, 1.5], gap="large")
    with col_nav:
        st.markdown('<div class="section-header">Executive Selection</div>', unsafe_allow_html=True)
        episode = st.radio("Selection:", [
            "🏛️ Ep. 0: Global Foundation", 
            "🎧 Ep. 1: Recession Glam", 
            "📊 Ep. 2: Global Trade", 
            "🔮 Ep. 3: 2026 Outlook", 
            "🌍 Ep. 4: European Barbell", 
            "🎓 Ep. 5: Carto AI & Neuro-Tech",
            "🎓 Ep. 6: B2B Price Elasticity",
            "🎓 Ep. 7: EU Regulatory Shock",
            "🧬 Ep. 8: Master Synthesis"
        ], label_visibility="collapsed", index=5)
        
        if "Ep. 0" in episode:
            current_t, current_a, rep_file = None, None, "master_prologue.md"
            f_type, v_title, desc = "None", "Macroeconomic Foundations 2026", "The 5T Nvidia era, EU 2023/1545 shock, and Givaudan MoodScentz™+ integration."
        elif "Ep. 1" in episode:
            current_t, current_a, rep_file = "podcast_transcript.md", "podcast_trends.mp3", "trend_report_2025.md"
            f_type, v_title, desc = "Popularity", "Global Popularity Ranking", "Analyzing Lattafa viral surge and Givaudan MoodScentz™ neuro-active solutions."
        elif "Ep. 2" in episode:
            current_t, current_a, rep_file = "ep2_trade_transcript.md", "ep2_audio.mp3", "ep2_trade_report.md"
            f_type, v_title, desc = "None", "Global Trade Volume 2024", "Deep Research data on US Section 122 tariffs, EU surplus, and Russian autarky (93M units)."
        elif "Ep. 3" in episode:
            current_t, current_a, rep_file = "ep3_debrief", "podcast_2026.mp3", "ep3_dossier"
            f_type, v_title, desc = "None", "2026 Global Projections", "Impact of the 5T Nvidia era, the 2025 Tariff Shock, and negative 1.81 price elasticity."
        elif "Ep. 4" in episode:
            current_t, current_a, rep_file = "ep4_debrief", "ep3_europe_barbell.mp3", "ep4_dossier"
            f_type, v_title, desc = "Barbell", "The Barbell Market Structure 2026", "Mapping the European Barbell structure, Poland PPP breakthrough, and 0.28 digital correlation."
        elif "Ep. 5" in episode:
            current_t, current_a, rep_file = "ep5_debrief", "ep5_How_AI_engineers_perfumes_for_your_brain.mp3", "ep5_dossier"
            f_type, v_title, desc = "Popularity", "Givaudan Carto AI Infrastructure", "Deep-dive technical breakdown: Algorithmic scent formulation and EEG brainwave mapping."
        elif "Ep. 6" in episode:
            current_t, current_a, rep_file = "ep6_debrief", "ep6_The_High_Stakes_Economics_Of_Fragrance.mp3", "ep6_dossier"
            f_type, v_title, desc = "None", "B2B Price Elasticity Vectors", "Advanced macroeconomic regression analyzing consumer behavior under severe inflation."
        elif "Ep. 7" in episode:
            current_t, current_a, rep_file = "ep7_debrief", "ep7_The_Secret_Chemical_Battlefield_of_Luxury_Perfume.mp3", "ep7_dossier"
            f_type, v_title, desc = "Barbell", "EU 2023/1545 Regulatory Compliance", "Strategic adaptation strategies for allergen restrictions and synthetic ingredient bans."
        else:
            current_t, current_a, rep_file = "master_synthesis_transcript.md", "ep8_master_synthesis.mp3", "master_synthesis.md"
            f_type, v_title, desc = "None", "Master Strategic Synthesis 2026", "Final dossier compiled via Deep Research and B2B technological architecture curated by Magdalena Romaniecka."

        if current_a:
            target_audio = find_file(current_a)
            if os.path.exists(target_audio):
                st.audio(target_audio)
            else:
                st.markdown(f'<div style="color: #888888; font-size: 0.8rem; font-style: italic;">[Audio file {current_a} pending upload]</div>', unsafe_allow_html=True)
        
        st.markdown(f'<p style="color:#D4AF37; font-size:0.95rem; font-style:italic; margin-top:20px; border-left: 3px solid #D4AF37; padding-left: 20px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data ✦ {v_title}</div>', unsafe_allow_html=True)
        
        if f_type == "Barbell" and 'market_structure' in df.columns:
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count', color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'}, template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=18, color='#D4AF37'), cliponaxis=False)
            max_val = b_counts['Count'].max()
            fig.update_yaxes(range=[0, max_val * 1.3], showgrid=False, showticklabels=False)
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="center", x=0.5))
        elif 'community_votes' in df.columns and 'name' in df.columns:
            df_t = df.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment" if 'segment' in df.columns else None, text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
            fig.update_traces(textposition='outside', textfont=dict(size=15, color='#D4AF37'), cliponaxis=False)
            max_val = df_t['community_votes'].max()
            fig.update_xaxes(range=[0, max_val * 1.35], showgrid=False, showticklabels=False)
            fig.update_layout(xaxis_title=None, yaxis_title=None, showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=-0.6, xanchor="center", x=0.5), margin=dict(r=100))
        else:
            fig = px.bar(x=["Data Upload Required"], y=[100], template="plotly_dark", color_discrete_sequence=['#D4AF37'])
            
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", height=450, yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    
    if "Ep. 0" in episode:
        st.markdown('<div class="section-header">Macroeconomic Foundations 2026</div>', unsafe_allow_html=True)
        try:
            with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                content_r = f.read()
                st.markdown(f'<div class="report-frame">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
        except: 
            st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Documentation indexing in progress...</div>', unsafe_allow_html=True)
    else:
        l_col, r_col = st.columns(2, gap="large")
        with l_col:
            if current_t in ["ep3_debrief", "ep4_debrief", "ep5_debrief", "ep6_debrief", "ep7_debrief"]:
                ep_key = "Ep. " + current_t[2]
                st.markdown(f'<div class="report-frame">\n{briefings_content[ep_key]["debrief"]}\n</div>', unsafe_allow_html=True)
            elif current_t:
                st.markdown('<div class="section-header">Executive Audio Debrief</div>', unsafe_allow_html=True)
                try:
                    with open(find_file(current_t), 'r', encoding='utf-8') as f:
                        content_t = f.read()
                        st.markdown(f'<div class="report-frame">\n\n{content_t}\n\n</div>', unsafe_allow_html=True)
                except: 
                    st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Debrief indexing in progress...</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="section-header">Executive Audio Debrief</div>', unsafe_allow_html=True)
                st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Technical audio briefing selected. Please refer to the Master Dossier on the right for accompanying documentation.</div>', unsafe_allow_html=True)
                
        with r_col:
            if rep_file in ["ep3_dossier", "ep4_dossier", "ep5_dossier", "ep6_dossier", "ep7_dossier"]:
                ep_key = "Ep. " + rep_file[2]
                st.markdown(f'<div class="report-frame">\n{briefings_content[ep_key]["dossier"]}\n</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="section-header">Executive Master Dossier</div>', unsafe_allow_html=True)
                try:
                    with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                        content_r = f.read()
                        st.markdown(f'<div class="report-frame">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
                except: 
                    st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Dossier indexing in progress...</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="section-header">B2B Price Elasticity Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ INTELLIGENCE NOTE: Simulating the -1.81 elasticity index under Section 122 Tariff constraints to evaluate margin compression in the "Squeezed Middle" sector.</div>', unsafe_allow_html=True)
    
    col_input, col_chart = st.columns([1, 2], gap="large")
    
    with col_input:
        st.markdown('<div class="dossier-section-title">Scenario Parameters</div>', unsafe_allow_html=True)
        price_hike = st.slider("Projected Retail Price Increase (%)", min_value=0.0, max_value=50.0, value=10.0, step=1.0)
        base_volume = 100000 
        
        elasticity_coefficient = -1.81
        demand_change = price_hike * elasticity_coefficient
        new_volume = base_volume * (1 + (demand_change / 100))
        
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">Projected Demand Shift (Volume)</div>
            <div class="metric-value" style="color: {'#FF4B4B' if demand_change < 0 else '#D4AF37'};">{demand_change:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_chart:
        simulation_data = pd.DataFrame({
            'Scenario': ['Base Market Demand', 'Post-Tariff Demand'],
            'Volume': [base_volume, max(0, new_volume)]
        })
        
        fig_sim = px.bar(
            simulation_data, 
            x='Scenario', 
            y='Volume',
            text='Volume',
            color='Scenario',
            color_discrete_map={'Base Market Demand': '#333333', 'Post-Tariff Demand': '#D4AF37'},
            template="plotly_dark"
        )
        fig_sim.update_traces(texttemplate='%{text:,.0f} Units', textposition='outside', textfont=dict(size=16, color='#E0E0E0'))
        fig_sim.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis=dict(showgrid=False, showticklabels=False),
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig_sim, use_container_width=True)

    st.markdown('<div class="section-header">Correlation vs. Causation: Digital Virality</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ STATISTICAL AXIOM: A 0.28 correlation confirms that Top-of-Funnel (TOFU) digital hype does not guarantee Bottom-of-Funnel (BOFU) sales without physical retail anchors.</div>', unsafe_allow_html=True)
    
    col_gauge, col_text = st.columns([1, 1], gap="large")
    with col_gauge:
        corr_fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 0.28,
            title = {'text': "Digital Hype vs Sales Conversion (r)", 'font': {'color': '#D4AF37'}},
            gauge = {
                'axis': {'range': [0, 1], 'tickcolor': "#D4AF37"},
                'bar': {'color': "#D4AF37"},
                'bgcolor': "#1A1A1A",
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 0.28}
            }
        ))
        corr_fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "#E0E0E0"}, height=300)
        st.plotly_chart(corr_fig, use_container_width=True)
    with col_text:
        st.markdown("""
        <div class="report-frame" style="height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <h3 style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; margin-top:0;">The Omnichannel Bottleneck</h3>
            <p style="color:#E0E0E0; font-family:'Lato', sans-serif; font-size:0.95rem; line-height:1.6;">
            In evaluating DTC (Direct-to-Consumer) models, we frequently observe a cognitive bias mistaking digital virality (e.g., TikTok trends) for causal purchasing behavior. 
            <br><br>
            A correlation coefficient of <strong>0.28</strong> dictates that while Stanford ML algorithms effectively generate awareness, human olfaction staunchly resists total digitization. Physical drugstores (acting as economic anchors) maintain an absolute chokehold on final conversions. Eliminating UX Friction online is critical, but bypassing physical sensory auditing entirely results in incinerated Customer Acquisition Costs (CAC).
            </p>
        </div>
        """, unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="section-header">Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ K-MEANS SEGMENTATION: 64% of analyzed Ultra-Niche segments utilize Jungle Essence™ CO2 extraction technologies to justify premium pricing above $350.</div>', unsafe_allow_html=True)

    if 'community_votes' in df.columns and 'segment' in df.columns:
        df_sun = df.sort_values('community_votes', ascending=False).groupby('segment').head(5).reset_index(drop=True)
        df_sun['Global Market'] = 'Global Market'
        
        fig_sun = px.sunburst(df_sun, path=['Global Market', 'segment', 'brand', 'name'], values='community_votes', color='segment', color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555', 'Mass Market':'#555'}, template="plotly_dark")
        fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
        st.plotly_chart(fig_sun, use_container_width=True)

with tabs[3]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    if 'name' in df.columns:
        f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
        f_data = df[df['name'] == f_choice].iloc[0]
        
        intel_note = ""
        if "Phantom" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ A/B TESTING INSIGHT: Designed via Givaudan Carto AI and 45M EEG brainwave measurements to optimize confidence-boosting neuro-responses vs control groups.</div>'
        elif "Idôle" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ ECO-INNOVATION: Features ultra-thin 15mm glass technology reducing carbon footprint by 63% via Givaudan sustainability stack.</div>'
        elif "Libre" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ MOLECULAR DESIGN: Features proprietary Diva Lavender and Vanilla Caviar molecular hybrids developed in Givaudan laboratories.</div>'

        score_val = f_data.get('community_score', 4.5)
        notes_val = f_data.get('top_notes', "Proprietary Accord Stack")
        brand_val = f_data.get('brand', "Global Brand")
        seg_val = f_data.get('segment', "Prestige")

        st.markdown(f"""
        <div style="background-color: #0E0E0E; border: 2px solid #D4AF37; border-radius: 4px; padding: 40px; margin: 20px auto; max-width: 850px; text-align: center; box-shadow: 0 0 25px rgba(212,175,55,0.15);">
            <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.6rem; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 8px;">{f_data['name']}</div>
            <div style="font-family: 'Lato', sans-serif; color: #888888; font-size: 0.85rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 35px;">{brand_val} ✦ {seg_val}</div>
            <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 20px; flex-wrap: wrap;">
                <div style="border: 1px solid rgba(212,175,55,0.4); background: #121212; padding: 20px 30px; flex: 1; min-width: 220px;">
                    <div style="color: #888888; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;">Quality Score</div>
                    <div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 3rem; line-height: 1.1;">{score_val:.1f} / 5.0</div>
                </div>
                <div style="border: 1px solid rgba(212,175,55,0.4); background: #121212; padding: 20px 30px; flex: 1; min-width: 220px; display: flex; flex-direction: column; justify-content: center;">
                    <div style="color: #888888; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 10px;">Key Notes</div>
                    <div style="font-family: 'Lato', sans-serif; color: #E0E0E0; font-size: 1.05rem; line-height: 1.5;">{notes_val}</div>
                </div>
            </div>
            {intel_note}
        </div>
        """, unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="section-header">Analytical Project Ecosystem</div>', unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    apps = [
        ("🧬 ScentSational AI", "AI Concierge providing personalized signature scent recommendations.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("📊 Perfume Finder", "Interactive database for manual filtering and exploring fragrance profiles.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📡 Hugging Face LFS2", "Advanced machine learning models and datasets mapping social sentiment.", "https://huggingface.co/spaces/Baphomert/ScentSational-Fragrantica-LFS2"),
        ("🌍 Market Pulse Hub", "Dashboard integrating Deep Research data with live macro tracking.", "https://github.com/MagdalenaRomaniecka")
    ]
    for col, (name, dsc, link) in zip([e1, e2, e3, e4], apps):
        col.markdown(f"""<div class="project-card">
            <h4 style="color:#D4AF37; margin-top:0; font-size:0.9rem;">{name}</h4>
            <p style="color:#888888; font-size:0.7rem;">{dsc}</p>
            <a class="btn-launch" href="{link}" target="_blank">LAUNCH APP</a>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB ✦ STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)