
import streamlit as st
import yfinance as yf

# Configurazione della pagina
st.set_page_config(page_title="Aurora 7 Gold", layout="wide")

# Funzione rapida per i due valori cardine
def get_values():
    try:
        oro = yf.Ticker("GC=F").fast_info['last_price']
        petrolio = yf.Ticker("CL=F").fast_info['last_price']
        return f"ORO: ${oro:,.2f}", f"PETROLIO: ${petrolio:,.2f}"
    except:
        return "ORO: Caricamento...", "PETROLIO: Caricamento..."

val_oro, val_petrolio = get_values()

# CSS per la Griglia Aurora
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #d4af37; }
    .header { text-align: center; padding: 20px; border-bottom: 2px solid #d4af37; margin-bottom: 20px; }
    .quadrante { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(0,0,0,0.5); min-height: 120px; margin-bottom: 10px; }
    .q-title { color: #d4af37; font-weight: bold; border-bottom: 1px solid #d4af37; margin-bottom: 10px; }
    .valore { font-size: 1.2em; font-weight: bold; color: #ffffff; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header"><h1>AURORA 7 GOLD - ARCHITETTURA DI COMANDO</h1></div>', unsafe_allow_html=True)

# --- Layout dei Quadranti (Q1 e Q2 Superiori) ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q1 - FLUSSI FINANZIARI</div><div class="valore">{val_petrolio}</div>Monitoraggio valore intrinseco.</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q2 - ASSET ORO</div><div class="valore">{val_oro}</div>Scansione mercati reali.</div>', unsafe_allow_html=True)

# --- Livello Centrale (Q3 - Q0 - Q4) ---
col3, col4, col5 = st.columns([1, 2, 1])
with col3:
    st.markdown('<div class="quadrante"><div class="q-title">Q3 - IONOSFERA</div>Segnali e intuizione biologica.</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="quadrante" style="border: 3px solid #d4af37;"><div class="q-title">Q0 - NUCLEO CENTRALE</div>Punto di Origine. Decisione Sovrana.</div>', unsafe_allow_html=True)
with col5:
    st.markdown('<div class="quadrante"><div class="q-title">Q4 - ESTERNO</div>Monitoraggio segnali esterni.</div>', unsafe_allow_html=True)

# --- Livello Inferiore (Q5 - Q6) ---
col6, col7 = st.columns(2)
with col6:
    st.markdown('<div class="quadrante"><div class="q-title">Q5 - PULIZIA</div>Rimozione vecchi schemi di pensiero.</div>', unsafe_allow_html=True)
with col7:
    st.markdown('<div class="quadrante"><div class="q-title">Q6 - OUTPUT</div>Analisi implementazione della Griglia.</div>', unsafe_allow_html=True)


