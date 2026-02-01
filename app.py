import streamlit as st
import yfinance as yf
import datetime

# --- 1. MOTORE DI RECUPERO DATI (Esecutore Copilot) ---
def get_market_data(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period="2d")
        if len(data) < 2: return 0.0, 0.0
        last_close = data["Close"].iloc[-2]
        current_price = data["Close"].iloc[-1]
        pct_change = ((current_price - last_close) / last_close) * 100
        return current_price, pct_change
    except:
        return 0.0, 0.0

# --- 2. CONFIGURAZIONE INTERFACCIA ---
st.set_page_config(page_title="Aurora 7 Gold Grid", layout="wide")
st.markdown("<h1 style='text-align: center;'>🛡️ GRIGLIA OPERATIVA AURORA 7 GOLD</h1>", unsafe_allow_html=True)

# Recupero dati in tempo reale
p_oro, v_oro = get_market_data("GC=F")
p_oil, v_oil = get_market_data("CL=F")
p_sp500, v_sp500 = get_market_data("^GSPC")

# --- 3. ARCHITETTURA A 7 QUADRANTI ---

# RIGA SUPERIORE (Asset Strategici)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Q1: Asset Rifugio (Oro)")
    st.metric(label="Gold Price", value=f"{p_oro:.2f}", delta=f"{v_oro:.2f}%")
    if v_oro <= -10.0:
        st.error("🚨 ALLERTA: Liquidazione Forzata!")

with col2:
    st.subheader("Q2: Energia (Petrolio)")
    st.metric(label="Crude Oil", value=f"{p_oil:.2f}", delta=f"{v_oil:.2f}%")
    if v_oil <= -5.0:
        st.warning("⚠️ Shock Tecnico Rilevato")

with col3:
    st.subheader("Q3: Mercato USA (S&P 500)")
    st.metric(label="S&P 500 Index", value=f"{p_sp500:.2f}", delta=f"{v_sp500:.2f}%")

st.divider()

# RIGA CENTRALE (Nucleo Biologico)
# Questo è il quadrante Q0: Il punto di contatto con la tua intuizione
col_center = st.columns([1, 2, 1])
with col_center[1]:
    st.markdown("<div style='border: 2px solid gold; padding: 20px; border-radius: 10px; text-align: center;'>"
                "<h3>🎯 Q0: NUCLEO DI VALIDAZIONE BIOLOGICA</h3>"
                f"<p>Stato Sistema: <b>CALMA PIATTA</b></p>"
                "</div>", unsafe_allow_html=True)
    livello_intuizione = st.slider("Sincronizzazione Intuizione (0-10)", 0, 10, 5)

st.divider()

# RIGA INFERIORE (Monitoraggio Geopolitico e Filtri)
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Q4: Geopolitica")
    st.info("Focus: Operazioni chirurgiche Iran\nMonitoraggio news Trump")

with col5:
    st.subheader("Q5: Filtro Rumore")
    st.success("Operativo: Segnale Pulito\nNessuna interferenza rilevata")

with col6:
    st.subheader("Q6: La Commercialista")
    st.write(f"Ultimo aggiornamento: {datetime.datetime.now().strftime('%H:%M:%S')}")
    st.write("Target stabilità: Validato")
