# Calcolatore di Maschere di Sottorete IPv4

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · **Italiano** · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

Utility grafica **offline**, gratuita e open source, per calcolare le maschere di sottorete IPv4, suddividere una rete in sottoreti, conservare una cronologia ed esportarla. Interfaccia in **15 lingue**.

Repository: <https://github.com/harlockSuites/CalculateurMasques>

> **Linux:** esiste una versione dedicata a Linux nel [branch `Linux`](https://github.com/harlockSuites/CalculateurMasques/tree/Linux). Un eseguibile precompilato (versione preliminare, Debian 12, x86-64) è pubblicato nella [release `Linux-v1.0`](https://github.com/harlockSuites/CalculateurMasques/releases/tag/Linux-v1.0). Questo README descrive la versione per Windows.

---

## Panoramica

L'applicazione è organizzata in tre schede:

| Scheda | Contenuto |
|---|---|
| **Calcolatore** | Calcolo principale, conversioni IP, verifica di appartenenza |
| **Suddivisione** | Divisione automatica di una rete in sottoreti |
| **Cronologia** | Registro dei calcoli, esportazione CSV / TXT |

---

## Funzionalità

### Scheda Calcolatore
- Inserimento tramite **prefisso CIDR** (`/24`) o **maschera decimale** (`255.255.255.0`): i due valori si sincronizzano automaticamente
- Risultati visualizzati:
  - Indirizzo di rete
  - Maschera di sottorete
  - Notazione CIDR
  - Maschera jolly (wildcard)
  - Primo / Ultimo indirizzo host
  - Indirizzo broadcast
  - Numero di host utilizzabili
  - Intervallo completo della rete
- **Conversioni** dell'indirizzo IP inserito: notazione decimale puntata, binario, esadecimale, decimale (intero a 32 bit)
- **Verifica appartenenza**: controlla se un IP dato appartiene alla rete calcolata
- **Clic destro** su qualsiasi valore per copiarlo negli appunti
- Tasto **Invio** per avviare il calcolo

### Scheda Suddivisione
- Divisione di una rete in N sottoreti uguali
- Oppure ricerca del CIDR minimo per contenere N host
- Tabella delle sottoreti con rete, maschera, host, broadcast (limitata a 65 536 righe, con un messaggio nella lingua scelta oltre tale soglia)
- Clic destro su una cella per copiarne il valore

### Scheda Cronologia
- Ogni calcolo viene registrato automaticamente, con l'ora del calcolo
- Doppio clic su una voce per ricaricarla nel calcolatore
- Esportazione **CSV** (codifica UTF-8 con BOM, compatibile con Excel)
- Esportazione **TXT** (formato leggibile)

### Selettore della lingua
15 lingue disponibili, accessibili dall'intestazione dell'applicazione:

| Gruppo | Lingue |
|---|---|
| Romanze | Français · English · Español · Português · Italiano |
| Europa centro-orientale | Српски · Polski · Magyar · Русский |
| Asia meridionale e orientale | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

Il cambio di lingua è istantaneo, senza riavvio.

### Pulsante Informazioni
Accanto al selettore della lingua, il pulsante **Informazioni** apre una finestra con il banner dell'autore (`banner.png`) e il messaggio «Questo software di utilità offline è gratuito e open source.», tradotto nelle 15 lingue.

---

## Prerequisiti

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- Modulo `tkinter` (incluso nell'installazione standard di Python)

Non è richiesta alcuna dipendenza esterna per avviare lo script. [Pillow](https://pypi.org/project/pillow/) è opzionale: serve solo a mostrare l'icona della finestra a piena risoluzione.

---

## Avvio

### Tramite Python
```
python calculateur_masques.py
```

### Tramite l'eseguibile compilato
Fai doppio clic su `dist\CalculateurMasquesIPv4.exe`. L'eseguibile è autonomo, senza installazione. Non è versionato in questo repository: compilalo (vedi sotto).

---

## Compilare l'eseguibile

Il repository fornisce una spec PyInstaller (`CalculateurMasquesIPv4.spec`) che incorpora l'icona, il banner e le traduzioni. Da questa cartella:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

L'eseguibile viene generato nella cartella `dist\`. L'icona (`icon.ico`) è integrata nell'exe.

---

## Struttura dei file

```
CalculateurMasques\
├── calculateur_masques.py        # Applicazione principale
├── translations.py               # Dizionario delle 15 lingue
├── CalculateurMasquesIPv4.spec   # Specifica PyInstaller
├── icon.ico                      # Icona dell'exe (Windows)
├── icon.png                      # Icona della finestra (512 px)
├── banner.png                    # Banner della finestra Informazioni (600 px)
├── LICENSE                       # Licenza MIT
└── README.md
```

---

## Casi particolari gestiti

| Prefisso | Comportamento |
|---|---|
| `/31` | Collegamento punto-punto (RFC 3021) — 2 indirizzi, nessun broadcast convenzionale |
| `/32` | Host singolo — primo = ultimo = indirizzo di rete |
| `/0` | Rete universale `0.0.0.0` |

---

## Antivirus e falsi positivi

Al 25 ottobre 2026, VirusTotal segnala l'eseguibile `CalculateurMasquesIPv4.exe` della versione 1.0 con **5 rilevamenti su 69 motori**: Arctic Wolf, Bkav Pro, Microsoft, SecureAge e Zillya. Riteniamo che si tratti di **falsi positivi**, frequenti per un programma Python impacchettato con PyInstaller, recente e privo di firma digitale. Il programma non contiene alcun codice di rete (usa solo `tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys` e `os`, più Pillow per l'icona della finestra) e tutto il suo codice sorgente è pubblico in questo repository.

Il 25 ottobre 2026 sono state inviate segnalazioni di falsi positivi ai cinque fornitori interessati. Questa sezione verrà aggiornata con le loro risposte.

Per verificare il tuo download:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- Report VirusTotal: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- Puoi anche compilare l'eseguibile tu stesso a partire dal codice sorgente (vedi « Compilare l'eseguibile »).

---

## Licenza

Distribuito con licenza [MIT](LICENSE) — © 2026 Harlock S.
