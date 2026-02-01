
import streamlit as st

# 1. SETUP PAGINA AURORA 7 GOLD
st.set_page_config(page_title="AURORA 7 GOLD - FULL OS", layout="wide")

# STILE CSS PER ARCHITETTURA A 7 QUADRANTI
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #d4af37; font-family: 'Inter', sans-serif; }
    .nucleo-q0 { border: 3px solid #ff4500; padding: 25px; text-align: center; border-radius: 15px; margin-bottom: 20px; background: rgba(255, 69, 0, 0.05); }
    .quadrante { border: 1px solid #d4af37; padding: 15px; border-radius: 8px; background: #111; min-height: 350px; margin-bottom: 15px; }
    .ticker { color: #ffffff; font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 2px; }
    .news-box { font-size: 0.75em; color: #aaa; margin-top: 10px; border-top: 0.5px solid #444; padding-top: 5px; }
    .sentiment-label { font-size: 0.75em; font-weight: bold; margin-bottom: 10px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- Q0: NUCLEO DI VALIDAZIONE BIOLOGICA (Sempre al Top) ---
st.markdown('<div class="nucleo-q0"><h1>🎯 Q0: NUCLEO DI VALIDAZIONE BIOLOGICA</h1><h3>STATO: CALMA PIATTA | SINCRONIZZAZIONE: 5/10</h3></div>', unsafe_allow_index=True)

# CREAZIONE GRIGLIA OPERATIVA
riga1_col1, riga1_col2, riga1_col3 = st.columns(3)
riga2_col1, riga2_col2, riga2_col3 = st.columns(3)

# --- RIGA 1 (Analisi di Sistema) ---
with riga1_col1:
    st.markdown('<div class="quadrante"><h3>Q1: IONOSFERICA</h3><p class="ticker">Segnali Esterni</p><p class="ticker">Intuizione Biologica</p><div class="news-box">Monitoraggio risonanza e flussi energetici globali.</div></div>', unsafe_allow_index=True)

with riga1_col2:
    st.markdown('<div class="quadrante"><h3>Q2: ASSET RIFUGIO</h3><p class="ticker">ORO (Gold)</p><p class="ticker">ARGENTO (Silver)</p><p class="ticker">BRENT CRUDE OIL</p><div class="news-box">Brent stabile a $61.40. Focus su materie prime energetiche.</div></div>', unsafe_allow_index=True)

with riga1_col3:
    st.markdown('<div class="quadrante"><h3>Q3: RESET SISTEMA</h3><p class="ticker">Pulizia Cognitiva</p><p class="ticker">Rimozione Vecchi Schemi</p><div class="news-box">Mantenimento Calma Piatta operativa.</div></div>', unsafe_allow_index=True)

# --- RIGA 2 (DETTAGLIO DEI 16 TITOLI INTERNAZIONALI) ---

with riga2_col1:
    st.markdown('<div class="quadrante"><h3>Q4: DIFESA & GUERRA</h3>'
                '<span class="sentiment-label" style="color:#00ff00;">SENTIMENT: RALLY GEOPOLITICO</span>'
                '<span class="ticker">RHEINMETALL (RHM.DE)</span>'
                '<span class="ticker">PALANTIR (PLTR)</span>'
                '<span class="ticker">RTX (RAYTHEON)</span>'
                '<span class="ticker">NORTHROP GRUMMAN (NOC)</span>'
                '<span class="ticker">BOEING (BA)</span>'
                '<span class="ticker">LOCKHEED MARTIN (LMT)</span>'
                '<div class="news-box">Alert: Budget NATO 2026 in aumento. Titoli Difesa ai massimi storici.</div></div>', unsafe_allow_index=True)

with riga2_col2:
    st.markdown('<div class="quadrante"><h3>Q5: TECH & AI CORE</h3>'
                '<span class="sentiment-label" style="color:#00ff00;">SENTIMENT: HARDWARE DOMINANCE</span>'
                '<span class="ticker">NVIDIA (NVDA)</span>'
                '<span class="ticker">AMD</span>'
                '<span class="ticker">MICROSOFT (MSFT)</span>'
                '<span class="ticker">IBM</span>'
                '<span class="ticker">SIEMENS</span>'
                '<div class="news-box">Focus: Domanda chip AI. Rotazione da software a infrastruttura fisica.</div></div>', unsafe_allow_index=True)

with riga2_col3:
    st.markdown('<div class="quadrante"><h3>Q6: FINANZA & INDUSTRY</h3>'
                '<span class="sentiment-label" style="color:#ff4500;">SENTIMENT: ATTESA BCE / MACRO</span>'
                '<span class="ticker">UNICREDIT (UCG.MI)</span>'
                '<span class="ticker">DEUTSCHE BANK (DBK.DE)</span>'
                '<span class="ticker">STELLANTIS</span>'
                '<span class="ticker">HEIDELBERG MATERIALS</span>'
                '<span class="ticker">WISDOMTREE BRENT OIL</span>'
                '<div class="news-box">Monitoraggio tassi BCE 5 Feb. Focus su stabilità industriale EU.</div></div>', unsafe_allow_index=True)

# --- FOOTER: ALERT INCIDENTI ANOMALI ---
st.write("---")
st.error("⚠️ ALERT INCIDENTI ANOMALI: Volatilità VIX in aumento | Rilevata anomalia su flussi Foreign Exchange Management")

