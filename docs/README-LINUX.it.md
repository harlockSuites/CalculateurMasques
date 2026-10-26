# Calcolatore di Maschere di Sottorete IPv4 — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · **Italiano** · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **Ramo `Linux`**: versione Linux del software. Il ramo `main` è riservato alla distribuzione Windows; non unire l'uno all'altro.

Utility grafica per il calcolo delle maschere di sottorete IPv4, con supporto di 15 lingue, suddivisione in sottoreti, cronologia ed esportazione.

Repository: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

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
- Una **maschera inversa** (wildcard, ad es. `0.0.0.255`) viene rifiutata con un messaggio tradotto: inserisci una maschera di sottorete (`255.255.255.0`)
- **Rotellina del mouse**: scorre la pagina, qualunque sia l'elemento sotto il puntatore (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Tasto **Invio** per avviare il calcolo

### Scheda Suddivisione
- Divisione di una rete in N sottoreti uguali
- Oppure ricerca del CIDR minimo per contenere N host
- Tabella delle sottoreti con rete, maschera, host, broadcast
- Limite di 65 536 sottoreti per suddivisione (oltre tale soglia, un messaggio lo segnala invece di bloccare l'interfaccia)
- Clic destro su una cella per copiarne il valore

### Scheda Cronologia
- Ogni calcolo viene registrato automaticamente, con l'ora del calcolo (conservata nella visualizzazione e nell'esportazione)
- Doppio clic su una voce per ricaricarla nel calcolatore
- Esportazione **CSV** (codifica UTF-8)
- Esportazione **TXT** (formato leggibile)

### Selettore della lingua
15 lingue disponibili, accessibili dall'intestazione dell'applicazione:

| Gruppo | Lingue |
|---|---|
| Romanze | Français · English · Español · Português · Italiano |
| Europa centro-orientale | Српски · Polski · Magyar · Русский |
| Asia meridionale e orientale | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

Il cambio di lingua è istantaneo, senza riavvio.

### Pulsante Informazioni
Accanto al selettore della lingua, apre una finestra con il banner e il messaggio «Questo software di utilità offline è gratuito e open source.», tradotto nelle 15 lingue. Il tasto Esc o il pulsante Chiudi la richiude. Dal pacchetto `.deb`, dall'AppImage o dall'eseguibile autonomo, un piccolo pulsante in basso a sinistra di questa finestra aggiunge o rimuove l'icona del software (vedi sotto).

### Icona del menu e della scrivania
Dal pacchetto `.deb`, dall'AppImage o dall'eseguibile autonomo, alla prima apertura compare una finestra **«Aggiungere un'icona?»**, con tre pulsanti: **Aggiungi**, **Non chiedere più** e **Chiudi** (che non memorizza nulla: la domanda tornerà al prossimo avvio). Ricorda che l'icona potrà poi essere aggiunta o rimossa con il pulsante in basso nella finestra «Informazioni».
- **Aggiungi** crea la voce del **menu delle applicazioni** e l'icona nella **cartella Scrivania**, senza diritti di amministratore. Con l'AppImage e l'eseguibile autonomo, il software si copia prima in `~/.local/share/calculateur-masques/app` (l'icona sopravvive se sposti il file scaricato); con il `.deb`, non viene copiato nulla.
- **Non chiedere più** memorizza la scelta in `~/.config/calculateur-masques/config.json`; anche rimuovere l'icona con il pulsante di «Informazioni» la memorizza.
- Il `.deb` non aggiunge alcuna icona durante l'installazione: il suo lanciatore è nascosto, l'icona compare solo su richiesta.

> **GNOME** non mostra le icone della cartella Scrivania senza l'estensione «Desktop Icons»: l'icona della scrivania esiste allora, ma resta invisibile (il software lo segnala). La voce del menu delle applicazioni, invece, è visibile.

Per rimuovere tutto a mano:

```bash
rm -r ~/.local/share/calculateur-masques
rm -f ~/.local/share/applications/calculateur-masques.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/calculateur-masques.png
rm -f ~/Bureau/calculateur-masques.desktop ~/Desktop/calculateur-masques.desktop
rm -r ~/.config/calculateur-masques
```

### Coreano e carattere
Il coreano compare con il nome **Korean** nell'elenco (in inglese, perché «한국어» verrebbe visualizzato come quadratini senza un carattere coreano). Se il sistema non ne ha nessuno, selezionarlo apre una finestra di dialogo **in inglese** («Font needed») che spiega la necessità e propone:
- un **comando da copiare** in un terminale (installazione per tutti gli utenti): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch); solo il comando per Debian/Ubuntu è stato verificato;
- un pulsante **Install automatically**: scarica Noto Sans KR (4,6 MB, licenza SIL OFL, versione fissa, somma SHA-256 verificata) in `~/.local/share/fonts/calculateur-masques/`, senza diritti di amministratore. È l'unico caso in cui il software usa la rete; per il resto del tempo resta offline;
- un pulsante **Restart now**: riavvia il software (opzione `--lang ko`) affinché veda il carattere; la lingua cambia al riavvio. La lingua non viene memorizzata da una sessione all'altra.

Per rimuovere il carattere scaricato: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Le altre lingue con scrittura non latina (hindi, giapponese, cinese…) non hanno una finestra di questo tipo: senza un carattere adatto possono comparire dei quadratini. Per il giapponese e il cinese: `sudo apt install fonts-noto-cjk`.

---

## Prerequisiti

Python 3.8+ con il modulo `tkinter`.

```bash
# Debian / Ubuntu / Linux Mint
sudo apt install python3 python3-tk

# Fedora / RHEL / CentOS
sudo dnf install python3 python3-tkinter

# Arch Linux / Manjaro
sudo pacman -S python tk

# openSUSE
sudo zypper install python3 python3-tk
```

Non è richiesta alcuna altra dipendenza.

---

## Avvio

### Metodo rapido

```bash
chmod +x lancer.sh
./lancer.sh
```

Lo script verifica automaticamente la presenza di Python e di tkinter e mostra un messaggio di errore esplicito se manca una dipendenza.

### Direttamente tramite Python

```bash
python3 calculateur_masques.py
```

### Tramite il pacchetto `.deb` (Debian, Ubuntu, Linux Mint)

I file precompilati (`.deb`, AppImage, eseguibile autonomo e `SHA256SUMS-linux.txt`) sono pubblicati come anteprima nelle [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) del repository, con un tag `Linux-v*`; sono costruiti su Debian 12 (glibc 2.36, Python 3.11, x86-64). Il pacchetto installa il software per tutti gli utenti:

```bash
sudo apt install ./calculateur-masques_1.0.1_amd64.deb
calculateur-masques
```

L'installazione non aggiunge alcuna icona al menu né alla Scrivania: avvia `calculateur-masques` una prima volta, la finestra «Aggiungere un'icona?» la propone. Per disinstallare:

```bash
sudo apt remove calculateur-masques
```

La voce di menu aggiunta dal software scompare da sola; il collegamento sulla Scrivania, invece, resta (è un semplice file): rimuovilo prima con il pulsante di «Informazioni», oppure a mano.

### Tramite l'AppImage

Un solo file, senza installazione:

```bash
chmod +x CalculateurMasques-1.0.1-x86_64.AppImage
./CalculateurMasques-1.0.1-x86_64.AppImage
```

Se il sistema non ha FUSE:

```bash
./CalculateurMasques-1.0.1-x86_64.AppImage --appimage-extract-and-run
```

### Tramite un eseguibile autonomo

Un eseguibile autonomo (PyInstaller) si compila con un solo comando (vedi «Compilare un eseguibile autonomo» più sotto); una versione precompilata è nelle Releases:

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

Per verificare i file scaricati:

```bash
sha256sum -c SHA256SUMS-linux.txt
```

> **Riserva glibc**: questi file sono costruiti su Debian 12. Sono verificati su tale distribuzione; dovrebbero funzionare anche sulle distribuzioni con glibc 2.36 o più recente, ma non su una più vecchia. In tal caso, ricompila dai sorgenti.

---

## Installazione di sistema (opzionale)

Per integrare l'applicazione nel menu dell'ambiente desktop (GNOME, KDE, XFCE…):

```bash
# Copiare i file in /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Modificare il percorso nel file .desktop se necessario
# Exec=bash /opt/calculateur-masques/lancer.sh

# Aggiungere al menu delle applicazioni
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# oppure
sudo kbuildsycoca6              # KDE Plasma
```

---

## Compilare un eseguibile autonomo

PyInstaller permette di generare un binario senza dipendenze da Python:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

L'eseguibile verrà generato in `./dist/CalculateurMasquesIPv4`. Le opzioni `--add-data` incorporano l'icona della finestra (caricata a runtime tramite Pillow se presente, altrimenti da Tk) e il banner della finestra Informazioni; Pillow è facoltativo (`pip3 install pillow`).

> **Nota:** un binario Linux compilato su Ubuntu non funzionerà necessariamente su Arch o Fedora a causa delle differenze tra le versioni di glibc. Compila sulla distribuzione di destinazione oppure usa un'immagine Docker per la distribuzione desiderata.

### Costruire il `.deb` e l'AppImage

Su Debian o Ubuntu, con PyInstaller e `appimagetool` nel PATH, lo script costruisce prima una cartella PyInstaller, poi i due pacchetti in `dist/`:

```bash
python3 packaging/build_linux_packages.py
python3 packaging/build_linux_packages.py --only deb
```

L'opzione `--only deb` (o `--only appimage`) ne costruisce solo uno dei due.

---

## Struttura dei file

```
CalculateurMasques/            (ramo Linux)
├── calculateur_masques.py      # Applicazione principale (adattata a Linux)
├── translations.py             # Dizionario delle 15 lingue (identico al ramo main)
├── icon.png                    # Icona della finestra / del menu (512 px)
├── banner.png                  # Banner della finestra Informazioni (600 x 200)
├── lancer.sh                   # Script di avvio con verifica delle dipendenze
├── calculateur-masques.desktop # Voce di menu per gli ambienti desktop
├── packaging/                  # Costruzione del .deb e dell'AppImage
│   ├── build_linux_packages.py # Script di costruzione
│   └── linux/                  # AppRun, lanciatore, pagina di manuale, registro delle modifiche del .deb
├── INSTALLER.md                # Istruzioni di installazione dettagliate (in francese)
├── LICENSE                     # Licenza MIT
├── README-LINUX.md             # Questa guida, in francese
└── docs/README-LINUX.<code>.md # Traduzioni: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Differenze con la versione Windows

| Aspetto | Windows | Linux |
|---|---|---|
| Caratteri | Segoe UI / Consolas | Rilevamento automatico (Noto Sans, DejaVu Sans, Liberation…) |
| Rotellina del mouse | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Esportazione CSV | UTF-8 con BOM (Excel) | UTF-8 senza BOM (standard) |
| Eseguibile | `.exe` autonomo | Binario ELF tramite PyInstaller (dipende dalla distrib.) |
| Integrazione desktop | Collegamento Windows | Pacchetto `.deb`, AppImage, icona del menu e della scrivania (file `.desktop`, XDG) |

---

## Casi particolari gestiti

| Prefisso | Comportamento |
|---|---|
| `/31` | Collegamento punto-punto (RFC 3021) — 2 indirizzi, nessun broadcast convenzionale |
| `/32` | Host singolo — primo = ultimo = indirizzo di rete |
| `/0` | Rete universale `0.0.0.0` |

---

## Licenza

Licenza MIT — vedi il file `LICENSE`.
