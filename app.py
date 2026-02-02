
import streamlit as st

# --- CONFIGURAZIONE PROTOCOLLO AURORA GOLD 7 ---
st.set_page_config(layout="wide", page_title="Aurora Grid 7")

# Stile CSS per i bordi dorati (come da screenshot)
st.markdown("""
    <style>
    .grid-box {
        border: 2px solid #FFD700;
        border-radius: 10px;
        padding: 20px;
        height: 250px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INIZIO GRIGLIA ---
# Riga 1
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="grid-box"><strong>Q1 - RILEVAMENTO</strong></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="grid-box"><strong>Q2 - ANALISI DATI</strong></div>', unsafe_allow_html=True)

# Riga 2
col3, col4 = st.columns(2)
with col3:
    st.markdown('<div class="grid-box"><strong>Q3 - FREQUENZA</strong></div>', unsafe_allow_html=True)
with col4:
    # DEFINIZIONE CORRETTA Q4 (Ionosfera)
    st.markdown('<div class="grid-box"><strong>Q4 - IONOSFERA</strong><br><hr></div>', unsafe_allow_html=True)

# --- AREA TRASCRIZIONE INTUIZIONE ---
# Qui è dove invii il commento con Ctrl+Enter
intuizione = st.text_area("Trascrizione Intuizione:", 
                          placeholder="Inserisci qui il segnale...",
                          help="Premi Ctrl+Enter per applicare")

if intuizione:
    st.success(f"Segnale acquisito: {intuizione}")

# Riga 3
col5, col6 = st.columns(2)
with col5:
    st.markdown('<div class="grid-box"><strong>Q5 - MONITORAGGIO</strong></div>', unsafe_allow_html=True)
with col6:
    # DEFINIZIONE CORRETTA Q6 (Azione)
    st.markdown('<div class="grid-box"><strong>Q6 - AZIONE</strong></div>', unsafe_allow_html=True)

# --- CORREZIONE ERRORE RIGA 80 ---
# Assicuriamoci che 'c8' non venga chiamato a vuoto. 
# Se serve un quadrante extra, lo definiamo ora:
c8 = "Sistema Stabilizzato" 

# Log di controllo
st.info(f"Stato: {c8}") # Ora la riga 80 non darà più errore
