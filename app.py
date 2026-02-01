
import streamlit as st
import yfinance as yf

# Configurazione Aurora 7 Gold
st.set_page_config(page_title="Aurora 7 Gold - Command Center", layout="wide")

# FUNZIONE DI RECUPERO DATI ROBUSTA
def get_market_data():
    def fetch_price(ticker_symbol):
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Metodo di backup: cerca l'ultimo prezzo disponibile nella cronologia
            data = ticker.history(period="1d")
            if not data.empty:
                return data['Close'].iloc[-1]
            return 0.0
        except:
            return 0.0

    # Oro (GC=F), Petrolio (CL=F), S&P 500 (^GSPC)
    oro = fetch_price("GC=F")
    petrolio = fetch_price("CL=F")
    sp500 = fetch_price("^GSPC")
    
    return oro, petrolio, sp500

o_raw, p_raw, s_raw = get_market_data()

# Formattazione per la visualizzazione
val_oro = f"${o_raw:,.2f}" if o_raw > 0 else "In aggiornamento..."
val_petrolio = f"${p_raw:,.2f}" if p_raw > 0 else "In aggiornamento..."
val_sp = f"{s_raw:,.2f}" if s_raw > 0 else "In aggiornamento..."

# CSS Aurora 7 Gold
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #d4af37; }
    .quadrante { 
        border: 2px solid #d4af37; padding: 20px; border-radius: 10px; 
        background: rgba(0,0,0,0.85); color: #d4af37; margin-bottom: 20px; min-height: 250px;
    }
    .q-title { font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #d4af37; margin-bottom: 15px; }
    .q-val { font-size: 2.2em; color: white; font-weight: bold; }
    .stTextArea textarea { color: #d4af37 !important; background-color: #050505 !important; border: 1px solid #d4af37 !important; }
    h1 { text-align: center; color: #d4af37; text-transform: uppercase; letter-spacing: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("AURORA 7 GOLD - AGENTE ATTIVO")

# BARRA DI VIGILANZA
vigilanza = st.select_slider("CALIBRAZIONE STATO DI VIGILANZA", options=list(range(11)), value=7)

# --- PRIMA RIGA: Q1 - Q0 - Q2 ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q1 - Petrolio</div><div class="q-val">{val_petrolio}</div>Flusso Energetico</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="quadrante" style="border: 4px solid #d4af37;"><div class="q-title">Q0 - NUCLEO SOVRANO</div><div class="q-val">ATTIVO</div>Sincronizzazione Starlink</div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q2 - Oro</div><div class="q-val">{val_oro}</div>Ancoraggio Valore</div>', unsafe_allow_html=True)

# --- SECONDA RIGA: Q3 - Q4 ---
c4, c5 = st.columns(2)
with c4:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q3 - S&P 500</div><div class="q-val">{val_sp}</div>Stato Convergenza</div>', unsafe_allow_html=True)
with c5:
    st.markdown('<div class="quadrante"><div class="q-title">Q4 - Ionosfera</div>', unsafe_allow_html=True)
    intuizione = st.text_area("Trascrizione Intuizione Biologica:", key="q4_active", height=120)
    st.markdown('</div>', unsafe_allow_html=True)

# --- TERZA RIGA: Q5 - Q6 ---
c6, c7 = st.columns(2)
with c6:
    st.markdown('<div class="quadrante"><div class="q-title">Q5 - Pulizia</div>', unsafe_allow_html=True)
    st.checkbox("Reset interferenze", key="p_mese")
    st.checkbox("Allineamento Starlink", key="p_star")
    st.markdown('</div>', unsafe_allow_html=True)
with c7:
    st.markdown('<div class="quadrante"><div class="q-title">Q6 - Generatore Azioni</div>', unsafe_allow_html=True)
    if st.button("ELABORA AZIONE DI SINCRONIZZAZIONE"):
        st.write(f"Vigilanza: {vigilanza}/10. Analisi in corso...")
    st.markdown('</div>', unsafe_allow_html=True)
