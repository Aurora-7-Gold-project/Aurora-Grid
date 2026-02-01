
import streamlit as st
import yfinance as yf

# Configurazione della pagina
st.set_page_config(page_title="Aurora 7 Gold", layout="wide")

# Funzione per recuperare solo i tre valori originali
def get_market_data():
    try:
        # Oro (GC=F), Petrolio (CL=F), S&P 500 (^GSPC)
        oro = yf.Ticker("GC=F").fast_info['last_price']
        petrolio = yf.Ticker("CL=F").fast_info['last_price']
        sp500 = yf.Ticker("^GSPC").fast_info['last_price']
        return f"${oro:,.2f}", f"${petrolio:,.2f}", f"{sp500:,.2f}"
    except:
        return "Caricamento...", "Caricamento...", "Caricamento..."

val_oro, val_petrolio, val_sp = get_market_data()

# CSS Originale - Semplice e senza raggruppamenti
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .quadrante { 
        border: 2px solid #d4af37; 
        padding: 20px; 
        border-radius: 8px; 
        background: rgba(0,0,0,0.7); 
        color: #d4af37;
        margin-bottom: 15px;
        text-align: center;
        min-height: 140px;
    }
    .q-title { font-size: 1em; font-weight: bold; text-transform: uppercase; margin-bottom: 8px; }
    .q-val { font-size: 1.6em; color: white; font-weight: bold; }
    h1 { color: #d4af37; text-align: center; border-bottom: 2px solid #d4af37; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1>AURORA 7 GOLD - ARCHITETTURA ORIGINALE</h1>', unsafe_allow_html=True)

# --- GRIGLIA Q0 -> Q6 ---

# Prima Riga: I Flussi (Q1, Q0, Q2)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q1 - Petrolio</div><div class="q-val">{val_petrolio}</div>Monitoraggio Flussi</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="quadrante" style="border: 3px solid #d4af37;"><div class="q-title">Q0 - CENTRO</div><div class="q-val">SOVRANO</div>Nucleo Aurora</div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q2 - Oro</div><div class="q-val">{val_oro}</div>Valore Intrinseco</div>', unsafe_allow_html=True)

# Seconda Riga: S&P e Percezione (Q3, Q4)
c4, c5 = st.columns(2)
with c4:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q3 - S&P 500</div><div class="q-val">{val_sp}</div>Mercato Globale</div>', unsafe_allow_html=True)
with c5:
    st.markdown('<div class="quadrante"><div class="q-title">Q4 - Ionosfera</div>Segnali e Intuizione</div>', unsafe_allow_html=True)

# Terza Riga: Pulizia e Risultato (Q5, Q6)
c6, c7 = st.columns(2)
with c6:
    st.markdown('<div class="quadrante"><div class="q-title">Q5 - Pulizia</div>Rimozione Schemi</div>', unsafe_allow_html=True)
with c7:
    st.markdown('<div class="quadrante"><div class="q-title">Q6 - Output</div>Griglia Attiva</div>', unsafe_allow_html=True)


