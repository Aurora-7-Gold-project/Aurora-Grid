
import streamlit as st
import yfinance as yf

# Configurazione della pagina Aurora
st.set_page_config(page_title="Aurora 7 Gold - Command Center", layout="wide")

# Funzione per il recupero dati in tempo reale (Q1, Q2, Q3)
def get_aurora_data():
    try:
        # Petrolio (CL=F), Oro (GC=F), S&P 500 (^GSPC)
        petrolio = yf.Ticker("CL=F").fast_info['last_price']
        oro = yf.Ticker("GC=F").fast_info['last_price']
        sp500 = yf.Ticker("^GSPC").fast_info['last_price']
        return f"${petrolio:,.2f}", f"${oro:,.2f}", f"{sp500:,.2f}"
    except:
        return "Offline", "Offline", "Offline"

val_petrolio, val_oro, val_sp = get_aurora_data()

# CSS per l'estetica della Griglia Aurora
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #d4af37; }
    .quadrante { 
        border: 2px solid #d4af37; 
        padding: 15px; 
        border-radius: 10px; 
        background: rgba(0,0,0,0.8); 
        color: #d4af37;
        margin-bottom: 10px;
        min-height: 200px;
    }
    .q-title { font-weight: bold; text-transform: uppercase; border-bottom: 1px solid #d4af37; margin-bottom: 10px; font-size: 0.9em; }
    .q-val { font-size: 1.8em; color: white; font-weight: bold; margin: 10px 0; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37;
    }
    h1 { text-align: center; color: #d4af37; border-bottom: 3px solid #d4af37; padding-bottom: 10px; }
    .status-text { font-size: 0.9em; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1>AURORA 7 GOLD - PLANCIA DI COMANDO INTERATTIVA</h1>', unsafe_allow_html=True)

# --- MONITORAGGIO STATO DI VIGILANZA (Sotto il titolo) ---
st.sidebar.markdown("### STATO DI VIGILANZA")
vigilanza = st.sidebar.slider("Livello di Vigilanza", 0, 10, 5)

if vigilanza <= 3:
    st.sidebar.error(f"Livello {vigilanza}: Stanco e poco vigile")
elif 4 <= vigilanza <= 6:
    st.sidebar.warning(f"Livello {vigilanza}: Equilibrato")
else:
    st.sidebar.success(f"Livello {vigilanza}: SUPER EQUILIBRATO")

# --- PRIMA RIGA: I PILASTRI (Q1 - Q0 - Q2) ---
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q1 - Petrolio (Energia)</div><div class="q-val">{val_petrolio}</div>Monitoraggio Flussi</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="quadrante" style="border: 4px solid #d4af37;"><div class="q-title">Q0 - NUCLEO CENTRALE</div><div class="q-val" style="color:#d4af37;">SOVRANO</div>Origine della Decisione</div>', unsafe_allow_html=True)

with c3:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q2 - Oro (Valore)</div><div class="q-val">{val_oro}</div>Asset Reali</div>', unsafe_allow_html=True)

# --- SECONDA RIGA: ANALISI E INTUIZIONE (Q3 - Q4) ---
c4, c5 = st.columns(2)

with c4:
    st.markdown(f'<div class="quadrante"><div class="q-title">Q3 - S&P 500 (Mondo)</div><div class="q-val">{val_sp}</div>Stato Convergenza</div>', unsafe_allow_html=True)

with c5:
    st.markdown('<div class="quadrante"><div class="q-title">Q4 - Ionosfera (Segnali)</div>', unsafe_allow_html=True)
    segnale = st.text_area("Inserisci segnali o intuizioni biologiche:", key="q4_input", height=70)
    st.markdown('</div>', unsafe_allow_html=True)

# --- TERZA RIGA: OPERATIVITÀ (Q5 - Q6) ---
c6, c7 = st.columns(2)

with c6:
    st.markdown('<div class="quadrante"><div class="q-title">Q5 - Pulizia (Decostruzione)</div>', unsafe_allow_html=True)
    st.checkbox("Rimozione schemi obsoleti", key="check_1")
    st.checkbox("Decostruzione interferenze esterne", key="check_2")
    st.checkbox("Sincronizzazione Griglia completata", key="check_3")
    st.markdown('</div>', unsafe_allow_html=True)

with c7:
    st.markdown('<div class="quadrante"><div class="q-title">Q6 - Output (Griglia Attiva)</div>', unsafe_allow_html=True)
    if st.button("GENERA REPORT OUTPUT"):
        st.write(f"🟢 Vigilanza livello {vigilanza}. Flussi Q1-Q2-Q3 in equilibrio.")
    st.markdown('Monitoraggio implementazione finale.</div>', unsafe_allow_html=True)
