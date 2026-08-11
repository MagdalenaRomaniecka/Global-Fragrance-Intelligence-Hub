import streamlit as st
import plotly.express as px
import pandas as pd
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

    .report-title {
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        text-transform: uppercase;
        font-size: 1.4rem;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .report-subtitle {
        color: #E0E0E0;
        font-weight: 700;
        font-size: 0.85rem;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid #333333;
    }

    .scope-text {
        color: #888888;
        font-size: 0.85rem;
        margin-bottom: 30px;
        line-height: 1.6;
    }

    .part-title {
        color: #E0E0E0;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    
    .dossier-title {
        color: #D4AF37;
        font-family: 'Tenor Sans', sans-serif;
        text-transform: uppercase;
        font-size: 1.2rem;
        margin-top: 35px;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }

    .report-frame p {
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
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 10px; background-color: #0E0E0E; }
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
    "Ep. 5": {
        "debrief": """
<div class="report-title">🎙️ INTELLIGENCE BRIEFING. CARTO AI & NEURO-TECH</div>
<div class="report-subtitle">Strategic Deep Dive ✦ Executive Debrief</div>
<div class="scope-text">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area AI Formulation, EEG/fMRI Brainwave Mapping. ✦ Data Intelligence Givaudan Carto AI, IBM Philyra, MoodScentz, Myrissi. ✦ Key Phenomenon Algorithmic olfactory synthesis vs human intuition.</div>

<div class="part-title">Part I. The Olfactory Memory Bottleneck</div>

<p><strong>HOST</strong> If you are wearing like a popular long-lasting perfume right now, there is a very high probability that the chemical anchoring that sent to your warm skin will still be detectable in the environment long after you leave the room.</p>

<p><strong>CO HOST</strong> Wazily. Hours later.</p>

<p><strong>HOST</strong> Right. And in fact, science is now finding these exact synthetic fragrance molecules in human breast milk, which is just, it's wild. Today, we are completely tearing up the romantic image of the perfume industry for this deep dive.</p>

<p><strong>CO HOST</strong> Yeah, we really are. Because, you know, you usually look at a bottle of luxury fragrance and you picture like a master artisan wandering through a field in grass at dawn, hand-picking jasmine petals, relying purely on inspiration and, well, a gifted nose.</p>

<p><strong>HOST</strong> Which is a beautiful image, but it's totally outdated.</p>

<p><strong>CO HOST</strong> Completely. The stack of sources we have for today destroys that illusion entirely. We are looking at dense thermodynamic data, highly technical olfactory compendiums, and like the machine learning architecture of modern fragrance apps. We are looking at poetry and a bottle here. We are looking at a highly clinical, intensely engineered landscape. We are the transition from, you know, traditional artisanal blending to advanced chemical engineering and increasingly artificial intelligence is absolute at this point.</p>

<p><strong>HOST</strong> So where do we even begin with this?</p>

<p><strong>CO HOST</strong> Well, to understand how technology is rewriting fragrance, we have to start at the foundational level, like how the raw materials themselves are captured and classified today, even the traditional language of scent is being overhauled.</p>

<p><strong>HOST</strong> Oh, right. The typology changes.</p>

<p><strong>CO HOST</strong> Exactly. For example, what the industry used to call the Oriental category is now strictly classified as amber. And classic florals are increasingly being engineered from the ground up to be completely unisex. But the real paradigm shift, the big one is happening in the extraction processes.</p>

<div class="part-title">Part II. AI Architecture and Neuro-Perfumery</div>

<p><strong>HOST</strong> Well, that data points to the existential crisis of modern perfumery. Because if machines can perfectly analyze and deconstruct a successful formula, identifying the exact ratio of hetion to amber oxen, the inevitable next step is having machines design the formulas themselves. So we are talking about AI formulas taking over the laboratories now completely bypassing the human nose.</p>

<p><strong>CO HOST</strong> Absolutely. Table 3 in the industry compendiums outlines the specific tools reshaping creation right now. We see systems like carto by jive adon right the visual mapping one.</p>

<p><strong>HOST</strong> Yeah, it's a visual mapping system that relies on molecular data to suggest highly unusual chemical combinations. Things that a human perfumer bound by classical training and, you know, traditional aesthetics would simply never think to pair together. The source is also highlight falera developed by IBM and simrise. And this is a deep learning algorithm trained on a database of 1.7 million existing perfume formulas.</p>

<p><strong>CO HOST</strong> 1.7 million. A human could never smell that many.</p>

<p><strong>HOST</strong> Never. It designed sense from scratch based on demographic briefs. And it works in tandem with tools like Ecoset compass, which calculates and tracks the exact carbon footprint of the resulting formula in real time.</p>

<p><strong>CO HOST</strong> Which is amazing for sustainability, sure. But the most intense advancement isn't just about mixing chemicals faster or tracking carbon. It's neuro perfumery.</p>

<p><strong>HOST</strong> Neuro perfumery. That sounds almost dystopian.</p>

<p><strong>CO HOST</strong> It's just fragrance from an aesthetic choice to a mathematically optimized physiological stimulus. Companies like L'Oreal and emotive are placing eG headsets on consumers to track their real time electrical brain waves while they smell different raw materials.</p>

<p><strong>HOST</strong> Okay, wait. The Pug fragrance phantom by Poccarobon is the prime example of this applied science in the sources, right?</p>

<p><strong>CO HOST</strong> Yes, phantom is the perfect case study. Pug didn't just guess what consumers would find appealing. They utilized 45 million EEG brain wave records to mathematically validate the exact overdosing of a specific molecule called styrolycathirally acetate.</p>

<p><strong>HOST</strong> 45 million records. Let that sink in. They tracked 45 million brain responses just to dial in one single molecule. And they did this for a very specific physiological reason, right?</p>

<p><strong>CO HOST</strong> To precisely, if the goal is just hacking the amygdala for a dopamine spike, we aren't creating art anymore. We are just directly manipulating human neurochemistry.</p>
""",
        "dossier": """
<div class="report-title">🧠 GIVAUDAN CARTO AI ✦ NEURO-COGNITIVE ENGINEERING</div>
<div class="report-subtitle">Operational Data Intelligence 2025 to 2026</div>
<div class="scope-text">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area AI Formulation & Chemical Physics. ✦ Data Intelligence Givaudan Carto, IBM Philyra, SBERT NLP, Cosine Similarity. ✦ Key Phenomenon Replacing human intuition with data-driven neuro-engineering.</div>

<div class="dossier-title">ALGORITHMIC SCENT FORMULATION & GC-MS DATA</div>
<p>The modern standard demands absolute perfection in raw materials, fundamentally altering the architecture of luxury fragrance production. The integration of high-level biotechnology allows for unprecedented extraction and analysis.</p>

<p>✦ Supercritical CO2 Extraction: Carbon dioxide is subjected to 74 bar pressure at 31.1°C, entering a supercritical state. It acts as the perfect solvent, dissolving delicate aromatic molecules without the destructive heat of traditional steam distillation, leaving zero toxic residues.</p>

<p>✦ GC-MS Reverse Engineering: Gas Chromatography-Mass Spectrometry physically separates molecules and bombards them with electrons to read their mass-to-charge ratio. This creates a perfect chemical fingerprint, effectively eliminating the concept of a "trade secret". For example, GC-MS analysis of Baccarat Rouge 540 reveals a blocky, high-impact architecture: 35.3% Hedione (diffusive lift), 18.5% Ambroxan (mineral skeleton), 10.5% Veramoss, and 27.0% DPG solvent.</p>

<p>✦ AI Infrastructure: Systems like Givaudan's Carto and IBM's Philyra bypass human biological limitations. Philyra, trained on a database of 1.7 million formulas, designs scents from scratch while continuously calculating chemical stability and carbon footprint in real-time.</p>

<div class="dossier-title">NEURO-PERFUMERY AND LIMBIC SYSTEM HACKING</div>
<p>The industry has shifted from aesthetic choices to mathematically optimized physiological stimuli.</p>

<p>✦ EEG & fMRI Brainwave Mapping: Companies utilize EEG headsets to track real-time electrical brain waves while consumers smell raw materials. The Paco Rabanne Phantom case study highlights the use of 45 million EEG brainwave records.</p>

<p>✦ Molecular Overdosing: The 45 million data points were used to mathematically validate the exact overdosing of Styrallyl Acetate. This creates a physiological trigger that hacks the amygdala for a dopamine spike, directly manipulating human neurochemistry to bypass rational consumer choice.</p>

<div class="dossier-title">THERMODYNAMICS VS. PYTHON CODE: RAOULT'S LAW</div>
<p>Even the most statistically perfect AI model is governed by physical laws once the liquid hits warm human skin.</p>

<p>✦ Raoult's Law & Fick's Second Law: Perfume formulation is a macroscopic battle against evaporation. Heavy fixative molecules (like Iso E Super) form intermolecular bonds with bouncy molecules (like Limonene) to alter the evaporation curve.</p>

<p>✦ Chemical Mutation (Calone 1951): When an algorithm pairs a volatile aquatic molecule like Calone 1951 with a heavy absolute, the thermodynamic balance is fragile. If dosed over 0.5%, the thermal energy of skin causes Calone to self-eject. It oxidizes incredibly rapidly, mutating from a fresh sea breeze into the smell of rotting oysters.</p>
"""
    },
    "Ep. 6": {
        "debrief": """
<div class="report-title">🎙️ INTELLIGENCE BRIEFING. B2B PRICE ELASTICITY</div>
<div class="report-subtitle">Strategic Deep Dive ✦ Executive Debrief</div>
<div class="scope-text">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area Global Retail & Middle East Maceration Arbitrage. ✦ Data Intelligence B2B Cost Allocation, Price Elasticity -1.81, 4-Tier Market Taxonomy. ✦ Key Phenomenon The $1.50 juice vs $150 retail markup trap.</div>

<div class="part-title">Part I. Deconstructing the Designer Bottle</div>

<p><strong>HOST</strong> I want you to picture something for a second. Just look at a heavy glossy glass bottle of luxury designer perfume. Right. The kind with the magnetic cap and the heavy base.</p>

<p><strong>CO HOST</strong> Exactly.</p>

<p><strong>HOST</strong> Now, if you just paid, say, $150 for that bottle, how much do you think the actual liquid inside is worth? Like the actual scent you're putting on your skin?</p>

<p><strong>CO HOST</strong> I mean, most consumers assume they're paying for the liquid, right? So they figure maybe 50 bucks, or I don't know, $30 if they factor in a really high brand markup.</p>

<p><strong>HOST</strong> But the actual scented liquid inside that $150 mainstream bottle, it's usually worth about $1.50. It's wild to think about.</p>

<p><strong>CO HOST</strong> It really is. Maybe $3 if it's a particularly heavy formulation. But yeah, welcome to a deep dive into the global fragrance industry. And we've got a massive stack of analytical reports today. We're looking at data spanning from 2024 all the way to 2035.</p>

<p><strong>HOST</strong> Yeah. So I think from macroeconomics to supply chains and these really rigid market taxonomies. Because the mission here is to decode how a $62.1 billion global market is just like actively marching toward an estimated $85.5 billion valuation by 2035. All while a physical product inside the bottle basically costs pennies.</p>

<p><strong>CO HOST</strong> So to really understand where this industry is heading, we have to start with where your money actually goes.</p>

<p><strong>HOST</strong> Right. And then we have the invisible architecture, the bottle economics.</p>

<div class="part-title">Part II. The Negative 1.81 Price Elasticity</div>

<p><strong>CO HOST</strong> Yeah, let's talk about that. Because the reports detailed this thing called a negative 1.81 price elasticity index in the mainstream sector, which is a very technical way of saying they are trapped.</p>

<p><strong>HOST</strong> Exactly. Essentially, if a mainstream brand tries to raise the retail price of a, you know, a standard everyday cent by just 10%, consumer demand plummets by over 18%.</p>

<p><strong>CO HOST</strong> Right. They can't raise the shelf price without just bleeding buyers. So they have to ruthlessly squeeze the manufacturing costs instead.</p>

<p><strong>HOST</strong> Which explains why the actual cent concentrate the juice along with the alcohol solvent makes up a mere 3 to 5% of the final retail price. Yeah. For a standard 100 milliliter designer bottle producing that liquid literally costs them 2 to 5 euros.</p>

<p><strong>CO HOST</strong> So where does the rest of my $150 go?</p>

<p><strong>HOST</strong> Well, 10 to 15% goes straight into the packaging, you know, the custom glass, the atomizers.</p>

<p><strong>CO HOST</strong> Right. So they're 15 to 25% is just eaten by global marketing. Those massive celebrity ambassador campaigns, you see everywhere. But the real financial black hole and this blew my mind is the traditional retail network.</p>

<p><strong>HOST</strong> Oh, absolutely. The department stores and the global distributors, they absorb a massive 45 to 60% margin.</p>

<p><strong>CO HOST</strong> 60% just have it sit on the shelf.</p>

<p><strong>HOST</strong> Yeah. I mean, you are fundamentally paying for the department stores real estate. You're funding the glass display counters, the testers, the sales associates. It's like paying for a blockbuster movie ticket, but you're mostly funding the billboards and the theater's concession stand rather than the film itself.</p>
""",
        "dossier": """
<div class="report-title">📊 MACROECONOMIC PRICE ELASTICITY ✦ B2B LOGISTICS</div>
<div class="report-subtitle">Operational Data Intelligence 2024 to 2025</div>
<div class="scope-text">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area Global Trade Corridors & Margin Breakdowns. ✦ Data Intelligence -1.81 Elasticity Index, UAE Logistics Bypass. ✦ Key Phenomenon Maceration Arbitrage and the collapse of the middle market.</div>

<div class="dossier-title">DECONSTRUCTING THE DESIGNER BOTTLE</div>
<p>The traditional Western designer fragrance market operates under severe, non-negotiable financial constraints defined by corporate accountants.</p>

<p>✦ The Juice Constraint: The actual scented concentrate and alcohol solvent in a standard $150 bottle account for merely 3% to 5% of the final retail price, equating to roughly €2 to €5.</p>

<p>✦ The Marketing & Packaging Void: Custom glass and atomizers absorb 10-15% of the budget. Global marketing, including celebrity ambassador campaigns, consumes 15-25%.</p>

<p>✦ The Retail Black Hole: The physical retail network (department stores and global distributors) absorbs an overwhelming 45% to 60% margin. Consumers are fundamentally funding commercial real estate and display counters, not the chemical formula.</p>

<p>✦ Negative 1.81 Price Elasticity: Mainstream brands are trapped by a -1.81 price elasticity index. A 10% increase in shelf price causes consumer demand to plummet by over 18%. To survive, brands ruthlessly squeeze manufacturing costs, forcing an absolute reliance on cheap, mass-produced synthetic molecules.</p>

<div class="dossier-title">THE NICHE INVERSION & MARKET TAXONOMY</div>
<p>True niche perfumery flips the economic model entirely, allocating 40% to 60% of their budget directly into pure, high-quality raw materials.</p>

<p>✦ The 4-Tier Taxonomy: Digital culture has forced a rigid classification. Tier 1: Mainstream Designer (>100,000 units). Tier 2: Niche Prestige / Corporate Niche (10,000-50,000 units, acquired by conglomerates). Tier 3: Indie Segment (Independent, 100-5,000 units). Tier 4: Artisan Purist (<500 units, rigorous manual production).</p>

<p>✦ Format Shifts: To adapt to high material costs, niche brands are shifting heavily toward 10ml to 30ml formats and fueling a $1.2 billion subscription market boom, allowing consumers to experience high-end materials without a blind $300 commitment.</p>

<div class="dossier-title">THE MIDDLE EASTERN CLONE REVOLUTION</div>
<p>The single biggest supply chain disruption in modern perfumery is the Arabian "Dupe Culture." Brands like Lattafa, Armaf, and Afnan have reverse-engineered the industry.</p>

<p>✦ Maceration Arbitrage: Traditional Western brands freeze capital by storing mixed fragrance in climate-controlled warehouses for 4 to 12 weeks to macerate. UAE producers bypass this holding cost entirely by shipping freshly mixed, "green" juice within two weeks. They outsource the aging process to the consumer's bathroom cabinet, saving an absolute fortune in frozen capital.</p>

<p>✦ Absorbing Freight Shocks: During the 2024-2026 Red Sea crisis, 70% of shipping fleets bypassed the Suez Canal, extending transit by 14 days and spiking ocean freight costs by 400%. UAE dupe brands absorbed this shock through sheer scale. By loading massive containers directly at the Jebel Ali port and selling straight to e-commerce, the actual export freight cost per bottle remained fractions of a cent.</p>
"""
    },
    "Ep. 7": {
        "debrief": """
<div class="report-title">🎙️ INTELLIGENCE BRIEFING. EU REGULATORY SHOCK</div>
<div class="report-subtitle">Strategic Deep Dive ✦ Executive Debrief</div>
<div class="scope-text">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area EU Chemical Fortress & Global Patent Moats. ✦ Data Intelligence GC-MS Analytics, IFRA 52nd Amendment, EU 2023/1545. ✦ Key Phenomenon Silent reformulations, Captive monopolies, and Batch Code Hunters.</div>

<div class="part-title">Part I. The Illusion of Alchemy</div>

<p><strong>HOST</strong> So if I told you that the defining scent of a $300 luxury perfume was chemically synthesized from a molecule that smells aggressively like raw garlic and onions, you would probably think I was joking.</p>

<p><strong>CO HOST</strong> Right. Or at least you'd really hope it was a joke.</p>

<p><strong>HOST</strong> Yeah, exactly. I mean, when you walk up to a fragrance counter, the brand really wants you to imagine this master perfumer wandering through a sundrenched field in grass france, crushing delicate flower petals by hand. It is a beautifully constructed, very persistent illusion. I mean, the whole marketing apparatus is designed to sell you the alchemy of nature in a bottle. But today we are completely shattering that illusion. We've got a massive stack of industry reports in front of us for this deep dive. And this includes corporate financial ledgers and some really advanced olfactory chemistry analytics.</p>

<p><strong>CO HOST</strong> Which is fascinating stuff, really.</p>

<p><strong>HOST</strong> It is. And our mission here is to cut straight through the marketing poetry and reveal the hidden architecture of modern perfumery. Because what you were actually paying for isn't just a basket of flower petals. You're funding this wild collision of multi-billion dollar corporate patents, extreme supply chain physics, and a very quiet, very intense global regulatory war.</p>

<p><strong>CO HOST</strong> And that war is completely invisible to the average consumer. Like to understand today's fragrance market, we have to look past traditional alchemy. The modern industry is governed by high stakes intellectual property and, well, synthetic chemistry.</p>

<div class="part-title">Part II. Reverse Engineering and GC-MS</div>

<p><strong>HOST</strong> Let's actually start right there with the intellectual property because I found this part of the source is just mind blowing. The foundational problem for a perfume company is how they protect their recipes, right? Like if I invent a new piece of technology, I can patent it. If I write a novel, I copyright it. But according to the legal framework we're looking at, you cannot copyright a perfume recipe.</p>

<p><strong>CO HOST</strong> No, you can't. It is legally treated like a culinary recipe for, you know, a soup or a cake.</p>

<p><strong>HOST</strong> Which creates a massive vulnerability for these major fashion houses.</p>

<p><strong>CO HOST</strong> Exactly. Because in the modern era, any rival company can just buy a bottle of your best selling billion dollar fragrance to get back to a lab and run it through a machine called a GCMS.</p>

<p><strong>HOST</strong> Which stands for gas chromatography mass spectrometry, right?</p>

<p><strong>CO HOST</strong> You got it. I was trying to wrap my head around how that machine actually works. It sounds like straight-up science fiction. It's basically like feeding a fully baked cake into a high-tech scanner and the machine prints out the exact brand of flour the baker used, the exact number of eggs, and the specific baking temperature.</p>

<p><strong>HOST</strong> That is actually a remarkably accurate way to picture it. The gas chromatography phase physically separates all the individual molecules in the liquid, and then the mass spectrometry phase weighs them to figure out exactly what they are.</p>

<p><strong>CO HOST</strong> Wow. Yeah, so suddenly your competitor has your precise recipe and they can clone it for a fraction of the cost.</p>
""",
        "dossier": """
<div class="report-title">⚖️ INTELLECTUAL PROPERTY MOATS ✦ REGULATORY FORENSICS</div>
<div class="report-subtitle">Operational Data Intelligence 2024 to 2025</div>
<div class="scope-text">[ STRATEGIC SCOPE ] ✦ Primary Analysis Area EU Chemical Fortress & Extraction Physics. ✦ Data Intelligence IFRA 52nd Amendment, EU 2023/1545. ✦ Key Phenomenon Silent reformulations and the Batch Code Hunter rebellion.</div>

<div class="dossier-title">THE GC-MS THREAT & CAPTIVE MOATS</div>
<p>The inability to copyright a fragrance formula—legally treating it like a soup recipe—creates a massive vulnerability. Rival companies utilize Gas Chromatography-Mass Spectrometry (GC-MS) machines to vaporize and physically separate molecules, generating a perfect chemical fingerprint of any competitor's hit fragrance.</p>

<p>✦ The Captive Solution: To prevent perfect cloning, chemical giants (Givaudan, Firmenich, Symrise) synthesize entirely novel molecules called "Captives." While the perfume cannot be patented, the specific chemical process to synthesize the Captive is protected by an ironclad 20-year patent.</p>

<p>✦ Corporate Profitability: Fashion houses must hire the patent holder to manufacture their fragrance. This strategy grants chemical giants an impenetrable monopoly, generating astronomical returns. For example, Givaudan's 2025 ledgers show 7.4B CHF in sales with a massive 24.2% EBITDA margin.</p>

<p>✦ Extreme Synthesis: Captives rely on molecular precision. Symrise's Spicatanate, synthesized from upcycled orange juice waste, smells like rotting garlic in pure form. However, at a microscopic 0.001% concentration, the garlic facet vanishes, creating a brilliant, fresh wasabi effect.</p>

<div class="dossier-title">THE EXTREME PHYSICS OF NATURAL EXTRACTION</div>
<p>Despite the high margins of synthetics, true luxury requires natural absolutes to act as complex blending agents that provide an organic "soul" to the sharp clinical edges of synthetic captives.</p>

<p>✦ Orris Butter ($40,000–$100,000/kg): Requires the roots of the iris flower to be dried and dehydrated in a dark cellar for 3 to 5 years before extraction.</p>

<p>✦ Wild Oud ($30,000–$80,000/kg): The result of a specific fungal infection inside the Aquilaria tree, essentially extracting the tree's immune system.</p>

<p>✦ Rose Absolute ($8,000–$15,000/kg): Demands brutal raw agriculture. Yielding a single kilogram of Rose Absolute requires laborers to hand-pick roughly 1.5 million individual flowers to avoid steam distillation, which destroys thermal bile compounds.</p>

<div class="dossier-title">REGULATORY WARS & SILENT REFORMULATIONS</div>
<p>Global health regulations are constantly shifting, forcing brands to quietly dismantle and rebuild their iconic formulas.</p>

<p>✦ IFRA 52nd Amendment & EU 2023/1545: The EU has vastly expanded allergen labeling. Crucially, IFRA has introduced 51 new restrictions heavily targeting natural compounds. Furocoumarins in natural citrus oils are restricted due to severe phototoxicity (blistering sunburns under UV light). Polycyclic musks like Galaxolide are banned due to bioaccumulation in human tissue and breast milk.</p>

<p>✦ Batch Code Hunters: Consumers have noticed these silent reformulations. A highly organized subculture of amateur forensic chemists—"Batch Code Hunters"—weaponize regulatory data. They audit microscopic FIL (Formula Information List) codes printed on boxes to track formula mutations.</p>

<p>✦ The Creed Aventus Cult: Consumers obsessively track batch variations, treating bottles like rare vintage wine. The legendary smoky "11Z01" batch of Creed Aventus commands exorbitant aftermarket prices, as fans argue the scent fundamentally lost its signature birch-tar smokiness following corporate acquisition and regulatory compliance.</p>
"""
    }
}

tabs = st.tabs(["STRATEGIC BRIEFINGS", "MARKET ANALYTICS", "FRAGRANCE VAULT", "ECOSYSTEM"])

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
            current_t, current_a, rep_file = "podcast_transcript_2026.md", "podcast_2026.mp3", "ep3_outlook_report.md"
            f_type, v_title, desc = "None", "2026 Global Projections", "Impact of the 5T Nvidia era, the 2025 Tariff Shock, and negative 1.81 price elasticity."
        elif "Ep. 4" in episode:
            current_t, current_a, rep_file = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3", "barbell_strategy_2026.md"
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
            fig.update_traces(textposition='outside', textfont=dict(size=18, color='#D4AF37'))
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
            st.markdown('<div class="section-header">Executive Audio Debrief</div>', unsafe_allow_html=True)
            if current_t in ["ep5_debrief", "ep6_debrief", "ep7_debrief"]:
                ep_key = "Ep. " + current_t[2]
                st.markdown(f'<div class="report-frame">\n{briefings_content[ep_key]["debrief"]}\n</div>', unsafe_allow_html=True)
            elif current_t:
                try:
                    with open(find_file(current_t), 'r', encoding='utf-8') as f:
                        content_t = f.read()
                        st.markdown(f'<div class="report-frame">\n\n{content_t}\n\n</div>', unsafe_allow_html=True)
                except: 
                    st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Debrief indexing in progress...</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Technical audio briefing selected. Please refer to the Master Dossier on the right for accompanying documentation.</div>', unsafe_allow_html=True)
                
        with r_col:
            st.markdown('<div class="section-header">Executive Master Dossier</div>', unsafe_allow_html=True)
            if rep_file in ["ep5_dossier", "ep6_dossier", "ep7_dossier"]:
                ep_key = "Ep. " + rep_file[2]
                st.markdown(f'<div class="report-frame">\n{briefings_content[ep_key]["dossier"]}\n</div>', unsafe_allow_html=True)
            else:
                try:
                    with open(find_file(rep_file), 'r', encoding='utf-8') as f:
                        content_r = f.read()
                        st.markdown(f'<div class="report-frame">\n\n{content_r}\n\n</div>', unsafe_allow_html=True)
                except: 
                    st.markdown('<div class="report-frame" style="text-align: center; font-style: italic; color: #888;">Dossier indexing in progress...</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="section-header">Market Strategic Hierarchy</div>', unsafe_allow_html=True)
    st.markdown('<div class="intelligence-badge">✦ INTELLIGENCE NOTE: 64% of analyzed Ultra-Niche segments utilize Jungle Essence™ CO2 extraction technologies to justify premium pricing above $350.</div>', unsafe_allow_html=True)

    if 'community_votes' in df.columns and 'segment' in df.columns:
        df_sun = df.sort_values('community_votes', ascending=False).groupby('segment').head(5).reset_index(drop=True)
        df_sun['Global Market'] = 'Global Market'
        
        fig_sun = px.sunburst(df_sun, path=['Global Market', 'segment', 'brand', 'name'], values='community_votes', color='segment', color_discrete_map={'(?)':'#333', 'Niche':'#D4AF37', 'Prestige':'#F0E68C', 'Mass-Market':'#555', 'Mass Market':'#555'}, template="plotly_dark")
        fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=700)
        st.plotly_chart(fig_sun, use_container_width=True)

with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    if 'name' in df.columns:
        f_choice = st.selectbox("Select Profile:", sorted(df['name'].tolist()))
        f_data = df[df['name'] == f_choice].iloc[0]
        
        intel_note = ""
        if "Phantom" in f_choice:
            intel_note = '<div class="intelligence-badge" style="margin-top: 25px;">✦ B2B CASE STUDY: Designed via Givaudan Carto AI and 45M EEG brainwave measurements to optimize confidence-boosting neuro-responses.</div>'
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

with tabs[3]:
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