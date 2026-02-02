
import yfinance as yf
import time
import os
from datetime import datetime

# --- PARAMETRI DI FLUSSO ---
QUALIFICA = "SENTINELLA SOVRANA"
STATO_MODULO = "Q7-OPEN"
TARGET_GAP = 71.00

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def salva_commento_analogico(testo):
    """
    Salva il commento nel log locale e lo prepara per la sincronizzazione server.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [Q7-LOG] {testo}\n"
    with open("aurora_sentinel_logs.txt", "a") as f:
        f.write(entry)
    print(f"\n✅ COMMENTO SINCRO-REGISTRATO NEL SERVER AURORA.")
    time.sleep(1.5)

def run_aurora_grid():
    try:
        while True:
            clear_console()
            now = datetime.now()
            ts = now.strftime("%H:%M:%S")
            
            print(f"============================================================")
            print(f"   AURORA 7 GOLD - NODO SOVRANO | {ts}")
            print(f"   STATUS: {STATO_MODULO} | QUADRANTI: Q1-Q4 ATTIVI")
            print(f"============================================================")

            # --- MAPPATURA QUADRANTI ---
            assets = {
                "Q1 - ENERGIA (WTI)": "CL=F", 
                "Q2 - SCHERMO (GOLD)": "GC=F", 
                "Q3 - GOTHAM (PLTR)": "PLTR", 
                "Q4 - CORE (MSFT)": "MSFT"
            }

            for name, ticker in assets.items():
                try:
                    t = yf.Ticker(ticker)
                    val = t.fast_info['last_price']
                    change = ((val - t.fast_info['previous_close']) / t.fast_info['previous_close']) * 100
                    color = "\033[92m" if change >= 0 else "\033[91m"
                    print(f"{name:<25} | {val:>12.4f} | {color}{change:>+8.2f}% \033[0m")
                except:
                    print(f"{name:<25} | OFFLINE")

            print("-" * 60)
            
            # --- INTERFACCIA DI INPUT SENTINELLA ---
            print("\n[Comandi: 'c' per commentare, 'q' per uscire]")
            comando = input("\nAZIONE SENTINELLA > ").lower()

            if comando == 'c':
                commento = input("INSERIRE DATO ANALOGICO (Input Pineale): ")
                salva_commento_analogico(commento)
            elif comando == 'q':
                break
            
            # Se non ci sono input, il sistema continua il monitoraggio
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n[!] Protocollo oscurato. Sensore protetto.")

if __name__ == "__main__":
    run_aurora_grid()
