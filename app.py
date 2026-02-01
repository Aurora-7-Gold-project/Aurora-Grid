<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GRIGLIA OPERATIVA AURORA 7 GOLD</title>
    <style>
        body { background: #050505; color: #d4af37; font-family: 'Inter', sans-serif; margin: 0; overflow: hidden; }
        .header { text-align: center; padding: 20px; border-bottom: 2px solid #d4af37; background: rgba(212, 175, 55, 0.1); }
        .main-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; padding: 20px; }
        .quadrante { border: 1px solid #d4af37; padding: 15px; background: #111; border-radius: 5px; height: 180px; }
        .nucleo-bio { grid-column: 1 / 4; border: 2px solid #ff4500; text-align: center; padding: 20px; margin-bottom: 10px; }
        .ticker-list { font-size: 0.85em; color: #fff; line-height: 1.6; }
        .sentiment-tag { display: inline-block; padding: 2px 8px; border-radius: 3px; font-weight: bold; margin-top: 10px; }
        .bullish { background: #004d00; color: #00ff00; }
        .neutral { background: #333; color: #aaa; }
        .alert-bar { position: fixed; bottom: 0; width: 100%; background: #1a1a1a; padding: 10px; border-top: 1px solid #ff4500; }
        marquee { color: #ff4500; font-weight: bold; }
    </style>
</head>
<body>

<div class="header">
    <h1>GRIGLIA OPERATIVA AURORA 7 GOLD</h1>
</div>

<div class="main-grid">
    <div class="nucleo-bio">
        <h2>🎯 Q0: NUCLEO DI VALIDAZIONE BIOLOGICA</h2>
        <p>STATO: <span style="color:#00ff00;">CALMA PIATTA</span> | Sincronizzazione: 5/10</p>
    </div>

    <div class="quadrante">
        <h3>Q4: DIFESA & GEOPOLITICA</h3>
        <div class="ticker-list">RHM.DE, PLTR, RTX, NOC, BA, LMT</div>
        <div class="sentiment-tag bullish">SENTIMENT: ALTO RISCHIO / ALTO RALLY</div>
        <p style="font-size: 0.7em;">Focus: Budget NATO 2026</p>
    </div>

    <div class="quadrante">
        <h3>Q5: TECH & INFRASTRUTTURA AI</h3>
        <div class="ticker-list">AMD, MSFT, NVDA, IBM</div>
        <div class="sentiment-tag neutral">SENTIMENT: ROTAZIONE HARDWARE</div>
        <p style="font-size: 0.7em;">Focus: Nvidia Hardware Demand</p>
    </div>

    <div class="quadrante">
        <h3>Q6: ASSET EU & INDUSTRY</h3>
        <div class="ticker-list">SIE, STLA, HEI, DBK, UCG, BRNT</div>
        <div class="sentiment-tag neutral">SENTIMENT: ATTESA BCE (5 FEB)</div>
        <p style="font-size: 0.7em;">Focus: Tassi stabili Eurozona</p>
    </div>
</div>

<div class="alert-bar">
    <marquee>
        +++ [ANOMALIA] VIX IN AUMENTO +++ [RHEINMETALL] ORDINI RECORD IN EUROPA +++ [OIL] BRENT STABILE A $61.40 +++ [POLITICA] REVISIONE FOREIGN EXCHANGE MANAGEMENT +++ 
    </marquee>
</div>

</body>
</html>

Nascondi testo citato

Il Dom 1 Feb 2026, 12:17 Fabio Baruffolo <fabio.b.posta@gmail.com> ha scritto:
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

 
