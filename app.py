
import streamlit as st
import yfinance as yf

# Configurazione della pagina
st.set_page_config(page_title="Aurora 7 Gold", layout="wide")

# Recupero dati mercati
def get_market_data():
    try:
        petrolio = yf.Ticker("CL=F").fast_info['last_price']
        oro = yf.Ticker("GC=F").fast_info['last_price']
        sp500 = yf.Ticker("^GSPC").fast_info['last_price']
        return f"${petrolio:,.2f}", f"${oro:,.2f}", f"{sp500:,.2f}"
    except:
        return "Attendere...", "Attendere...", "Attendere..."

val_petrolio, val_oro, val_sp = get_market_data()

# CSS per garantire la visibilità di tutti gli elementi
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #d4af37; }
    .quadrante { 
        border: 2px solid #d4af37; 
        padding: 20px; 
        border-radius: 10px; 
        background: rgba(0,0,0,0.8); 
        color: #d4af37;
        margin-bottom: 20px;
        min-height: 220px;
    }
    .q-title { font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #d4af37; margin-bottom: 15px; }
    .q-val { font-size: 2em; color: white; font-weight: bold; }
    h1 { text-align: center; color: #d4af37; }
    /* Forza il colore del testo nelle aree di input */
    .stTextArea textarea, .stTextInput input { color: #d4af37 !important; background-color: #1a1a1a !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("AURORA 7 GOLD - PLANCIA INTEGRALE")

# --- BARRA DI VIGILANZA MANUALE (POSIZIONE CENTRALE) ---
st.markdown("### LIVELLO DI VIGILANZA MANUALE")
vigilanza = st.select_slider(
    "Sposta la barra per indicare il tuo stato:",
    options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    value=5
)

if vigilanza <= 3:
    st.error(f"LIVELLO {vigilanza}: Stanco e poco vigile")
elif 4 <= vigilanza <= 6:
    st.warning(f"LIVELLO {vigilanza}: Equilibrato")
else:
    st.success(f"LIVELLO {vigilanza}: SUPER EQUILIBRATO")

st.markdown("---")

# --- PRIMA RIGA: Q1 - Q0 - Q2 ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q1 - Petrolio</div><div class="q-val">{val_petrolio}</div>Flussi Energia</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="quadrante" style="border: 4px solid #d4af37;"><div class="q-title">Q0 - NUCLEO</div><div class="q-val">SOVRANO</div>Centro di Comando</div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q2 - Oro</div><div class="q-val">{val_oro}</div>Valore Intrinseco</div>', unsafe_allow_html=True)

# --- SECONDA RIGA: Q3 - Q4 ---
c4, c5 = st.columns(2)
with c4:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q3 - S&P 500</div><div class="q-val">{val_sp}</div>Mercato Globale</div>', unsafe_allow_html=True)
with c5:
    st.markdown('<div class="quadrante"><div class="q-title">Q4 - Ionosfera (Interattivo)</div>', unsafe_allow_html=True)
    st.text_area("Digita qui le tue intuizioni:", key="area_q4", height=100)
    st.markdown('</div>', unsafe_allow_html=True)

# --- TERZA RIGA: Q5 - Q6 ---
c6, c7 = st.columns(2)
with c6:
    st.markdown('<div class="quadrante"><div class="q-title">Q5 - Pulizia (Manuale)</div>', unsafe_allow_html=True)
    st.checkbox("Rimuovi schemi obsoleti", key="p1")
    st.checkbox("Decostruzione interferenze", key="p2")
    st.checkbox("Sincronizzazione attiva", key="p3")
    st.markdown('</div>', unsafe_allow_html=True)
with c7:
    st.markdown('<div class="quadrante"><div class="q-title">Q6 - Output Finale</div>', unsafe_allow_html=True)
    if st.button("ESEGUI DIAGNOSTICA"):
        st.write(f"Stato Vigilanza: {vigilanza}/10")
        st.write("Sincronizzazione Griglia: OTTIMALE")
    st.markdown('</div>', unsafe_allow_html=True)

Inviato da Outlook per Android
