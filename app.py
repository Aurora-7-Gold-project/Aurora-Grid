
import streamlit as st

# Configurazione della pagina per visualizzare la plancia a pieno schermo
st.set_page_config(page_title="Aurora 7 Gold - Command Center", layout="wide")

# Iniezione del CSS (Qui è dove c'era l'errore nel tuo screenshot)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #d4af37;
    }
    .header {
        text-align: center;
        padding: 20px;
        border-bottom: 2px solid #d4af37;
        background-color: rgba(212, 175, 55, 0.1);
        margin-bottom: 30px;
    }
    .quadrante {
        border: 1px solid #d4af37;
        padding: 15px;
        border-radius: 10px;
        background: rgba(0, 0, 0, 0.5);
        min-height: 150px;
        margin-bottom: 10px;
    }
    .q-title {
        color: #d4af37;
        font-weight: bold;
        text-transform: uppercase;
        border-bottom: 1px solid #d4af37;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Intestazione Principale
st.markdown('<div class="header"><h1>AURORA 7 GOLD - ARCHITETTURA DI COMANDO</h1></div>', unsafe_allow_html=True)

# --- Layout dei Quadranti ---

# Livello Superiore (Q1 - Q2)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="quadrante"><div class="q-title">Q1 - Ali Superiori</div>Monitoraggio Flussi Finanziari e Valore Intrinseco.</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="quadrante"><div class="q-title">Q2 - Ali Superiori</div>Scansione Mercati e Asset Oro.</div>', unsafe_allow_html=True)

# Livello Centrale (Q3 - Q0 - Q4)
col3, col4, col5 = st.columns([1, 2, 1])
with col3:
    st.markdown('<div class="quadrante"><div class="q-title">Q3 - Laterale Sinistro</div>Ricezione Segnali Ionosferici e Intuizione.</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="quadrante" style="border: 3px solid #d4af37;"><div class="q-title" style="font-size: 1.5em;">Q0 - NUCLEO CENTRALE</div>Punto di Origine. Decisione Sovrana.</div>', unsafe_allow_html=True)
with col5:
    st.markdown('<div class="quadrante"><div class="q-title">Q4 - Laterale Destro</div>Monitoraggio Segnali Esterni e Input Biologici.</div>', unsafe_allow_html=True)

# Livello Inferiore (Q5 - Q6)
col6, col7 = st.columns(2)
with col6:
    st.markdown('<div class="quadrante"><div class="q-title">Q5 - Ali Inferiori</div>Sistemi di Pulizia e Decostruzione Vecchi Schemi.</div>', unsafe_allow_html=True)
with col7:
    st.markdown('<div class="quadrante"><div class="q-title">Q6 - Ali Inferiori</div>Analisi Implementazione e Output della Griglia.</div>', unsafe_allow_html=True)

# Footer di sistema
st.sidebar.title("Stato Sistema Aurora")
st.sidebar.success("Griglia Sincronizzata")
st.sidebar.info(f"Monitoraggio attivo sui Quadranti Q0-Q6")

 
