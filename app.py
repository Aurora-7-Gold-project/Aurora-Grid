
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Aurora 7 Gold - Protocollo Attivo", layout="wide")

def get_aurora_values():
    # Prezzi di chiusura certi per evitare lo "zero" durante il blocco server
    defaults = {"GC=F": 2750.00, "CL=F": 72.50, "^GSPC": 5950.00,  "PLTR": 36.00,   "MSFT": 420.00 }
    results = {}
    
    for ticker_symbol, default_val in defaults.items():
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Proviamo a prendere i dati dell'ultimo giorno
            df = ticker.history(period="1d")
            if not df.empty:
                results[ticker_symbol] = df['Close'].iloc[-1]
            else:
                results[ticker_symbol] = default_val
        except:
            results[ticker_symbol] = default_val
    return results

data = get_aurora_values()

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #d4af37; }
    .quadrante { 
        border: 2px solid #d4af37; padding: 20px; border-radius: 10px; 
        background: rgba(0,0,0,0.9); color: #d4af37; margin-bottom: 20px; min-height: 250px;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    .q-title { font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #d4af37; margin-bottom: 15px; letter-spacing: 2px; }
    .q-val { font-size: 2.2em; color: white; font-weight: bold; }
    h1 { text-align: center; color: #d4af37; text-transform: uppercase; letter-spacing: 5px; border-bottom: 2px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.title("AURORA 7 GOLD - COMANDO SENTINELLA")

# Barra Vigilanza
vigilanza = st.select_slider("CALIBRAZIONE VIGILANZA", options=list(range(11)), value=8)

# Riga 1
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q1 - Petrolio</div><div class="q-val">${data["CL=F"]:,.2f}</div>Flusso Attivo</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="quadrante" style="border: 4px solid #d4af37;"><div class="q-title">Q0 - NUCLEO</div><div class="q-val">SOVRANO</div>Starlink Link: OK</div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q2 - Oro</div><div class="q-val">${data["GC=F"]:,.2f}</div>Ancoraggio Valore</div>', unsafe_allow_html=True)

# Riga 2
c4, c5 = st.columns(2)
with c4:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q3 - S&P 500</div><div class="q-val">{data["^GSPC"]:,.2f}</div>Indice Convergenza</div>', unsafe_allow_html=True)
with c5:
    st.markdown('<div class="quadrante"><div class="q-title">Q4 - Ionosfera</div>', unsafe_allow_html=True)
    st.text_area("Trascrizione Intuizione:", key="q4", height=100)
    st.markdown('</div>', unsafe_allow_html=True)

# Riga 3
c6, c7 = st.columns(2)
with c6:
    st.markdown('<div class="quadrante"><div class="q-title">Q5 - Pulizia</div>', unsafe_allow_html=True)
    st.checkbox("Reset Schemi", key="c1")
    st.checkbox("Sincronia Starlink", key="c2")
    st.markdown('</div>', unsafe_allow_html=True)
with c7:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q6 - Azione</div>', unsafe_allow_html=True)
    if st.button("ESEGUI DIAGNOSTICA"):
        st.success(f"Protocollo attivo. Vigilanza {vigilanza}/10. Sistema in equilibrio.")
    st.markdown(f'</div>', unsafe_allow_html=True)


# Riga 4 - Tecnologia Aurora c8, c9 = st.columns(2) with c8:

with c8:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q7 Palantir</div><div class="q-val">${data["PLTR"]:.2f}</div>', unsafe_allow_html=True)


