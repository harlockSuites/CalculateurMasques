# IPv4 Subnet Mask Calculator — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · **Filipino**

> **Branch na `Linux`**: ang bersyong Linux ng software. Nakalaan ang branch na `main` sa distribusyon para sa Windows; huwag pagsamahin ang dalawa.

Graphical utility para kalkulahin ang mga IPv4 subnet mask, na may suporta sa 15 wika, paghahati ng network sa mga subnet, kasaysayan at export.

Repository: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## Pangkalahatang-ideya

Ang application ay binubuo ng tatlong tab:

| Tab | Nilalaman |
|---|---|
| **Kalkulator** | Pangunahing kalkulasyon, mga conversion ng IP, pagsusuri ng pagiging miyembro |
| **Paghahati** | Awtomatikong paghahati ng isang network sa mga subnet |
| **Kasaysayan** | Talaan ng mga kalkulasyon, export sa CSV / TXT |

---

## Mga Tampok

### Tab na Kalkulator
- Pagpasok gamit ang **CIDR prefix** (`/24`) o **decimal na mask** (`255.255.255.0`) — awtomatikong nagsi-synchronize ang dalawa
- Mga ipinapakitang resulta:
  - Network Address
  - Subnet Mask
  - CIDR Notation
  - Wildcard Mask
  - Unang / Huling Host Address
  - Broadcast Address
  - Bilang ng Mga Magagamit na Host
  - Buong Saklaw ng Network
- Mga **conversion** ng ipinasok na IP address: Dotted Decimal Notation, Binary, Hexadecimal, Decimal (32-bit na integer)
- **Pagsusuri ng pagiging miyembro**: sinusubukan kung ang isang ibinigay na IP ay kabilang sa nakalkulang network
- **I-right click** ang anumang halaga para kopyahin ito sa clipboard
- Ang **inverse mask** (wildcard, hal. `0.0.0.255`) ay tinatanggihan na may mensaheng nakasalin sa napiling wika: maglagay ng subnet mask (`255.255.255.0`)
- **Mouse wheel**: nag-i-scroll ng pahina, anuman ang elementong dinadaanan ng cursor (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Pindutin ang **Enter** para simulan ang kalkulasyon

### Tab na Paghahati
- Paghahati ng isang network sa N magkakapantay na subnet
- O paghahanap ng pinakamaliit na CIDR na kayang maglaman ng N host
- Talaan ng mga subnet na may network, mask, mga host, broadcast
- May limitasyong 65,536 na subnet bawat paghahati (kapag lumampas dito, may lalabas na mensahe sa halip na mag-freeze ang interface)
- I-right click ang isang cell para kopyahin ang halaga

### Tab na Kasaysayan
- Awtomatikong nire-record ang bawat kalkulasyon, kasama ang oras ng kalkulasyon (makikita sa display at sa export)
- Mag-double click sa isang entry para i-reload ito sa kalkulator
- **CSV** export (UTF-8 encoding)
- **TXT** export (madaling basahing format)

### Tagapili ng wika
Available ang 15 wika, mapipili mula sa header ng application:

| Grupo | Mga Wika |
|---|---|
| Romance | Français · English · Español · Português · Italiano |
| Gitna/Silangang Europa | Српски · Polski · Magyar · Русский |
| Timog/Silangang Asya | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

Agad ang pagpapalit ng wika, hindi kailangang i-restart ang application.

### Button na Tungkol
Sa tabi ng tagapili ng wika, binubuksan ng button na **Tungkol** ang isang window na may banner at ang mensaheng "Ang offline na utility software na ito ay libre at open-source.", na isinalin sa 15 wika. Isinasara ito ng Esc key o ng button na Isara. Mula sa `.deb` package, sa AppImage o sa standalone na executable, may maliit na button sa kaliwang ibaba ng window na ito na nagdaragdag o nag-aalis ng icon ng software (tingnan sa ibaba).

### Icon ng menu at ng desktop
Mula sa `.deb` package, sa AppImage o sa standalone na executable, may bubukas na window na **"Magdagdag ng icon?"** sa unang pagbukas, na may tatlong button: **Idagdag**, **Huwag nang magtanong** at **Isara** (na walang itinatala: babalik ang tanong sa susunod na pagpapatakbo). Ipinapaalala nito na maaaring idagdag o alisin ang icon pagkatapos gamit ang button sa ibaba ng window na "Tungkol".
- Ang **Idagdag** ay gumagawa ng entry sa **menu ng mga application** at ng icon sa **folder ng Desktop**, nang walang administrator rights. Sa AppImage at sa standalone na executable, kinokopya muna ang software sa `~/.local/share/calculateur-masques/app` (hindi mawawala ang icon kung ililipat mo ang na-download na file); sa `.deb`, walang kinokopya.
- Ang **Huwag nang magtanong** ay nagtatala ng pinili sa `~/.config/calculateur-masques/config.json`; ang pag-alis ng icon gamit ang button ng "Tungkol" ay nagtatala rin nito.
- Ang `.deb` ay hindi nagdaragdag ng anumang icon sa pag-install: nakatago ang launcher nito, lumalabas lamang ang icon kapag hiniling.

> Hindi ipinapakita ng **GNOME** ang mga icon ng folder ng Desktop kung walang extension na "Desktop Icons": umiiral ang icon sa desktop, ngunit nananatiling hindi nakikita (ipinapaalam ito ng software). Nakikita naman ang entry sa menu ng mga application.

Para alisin ang lahat nang mano-mano:

```bash
rm -r ~/.local/share/calculateur-masques
rm -f ~/.local/share/applications/calculateur-masques.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/calculateur-masques.png
rm -f ~/Bureau/calculateur-masques.desktop ~/Desktop/calculateur-masques.desktop
rm -r ~/.config/calculateur-masques
```

### Korean at font
Lumalabas ang Korean sa pangalang **Korean** sa listahan (sa Ingles, dahil ang "한국어" ay lalabas na mga kahon kung walang Korean font). Kung wala nito ang system, ang pagpili rito ay magbubukas ng dialog box **sa Ingles** ("Font needed") na nagpapaliwanag ng pangangailangan at nag-aalok ng:
- isang **command na kokopyahin** sa terminal (pag-install para sa lahat ng user): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — ang command lamang para sa Debian/Ubuntu ang na-verify;
- isang button na **Install automatically**: dina-download ang Noto Sans KR (4.6 MB, lisensyang SIL OFL, naka-pin na bersyon, na-verify ang SHA-256 checksum) papunta sa `~/.local/share/fonts/calculateur-masques/`, nang walang administrator rights. Ito lamang ang pagkakataong gumagamit ng network ang software; offline ito sa lahat ng iba pang oras;
- isang button na **Restart now**: nire-relaunch ang software (option na `--lang ko`) para makita nito ang font; magpapalit ang wika sa pag-restart. Hindi naaalala ang wika mula sa isang session patungo sa susunod.

Para alisin ang na-download na font: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Walang ganitong dialog box ang iba pang wikang hindi Latin ang pagsulat (Hindi, Japanese, Chinese…): kung walang angkop na font, maaaring lumabas ang mga kahon. Para sa Japanese at Chinese: `sudo apt install fonts-noto-cjk`.

---

## Mga Kinakailangan

Python 3.8+ na may module na `tkinter`.

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

Walang kailangang ibang dependency.

---

## Pagpapatakbo

### Mabilis na paraan

```bash
chmod +x lancer.sh
./lancer.sh
```

Awtomatikong tinitingnan ng script kung may Python at tkinter, at nagpapakita ng malinaw na mensahe ng error kung may kulang na dependency.

### Gamit ang Python

```bash
python3 calculateur_masques.py
```

### Gamit ang `.deb` package (Debian, Ubuntu, Linux Mint)

Ang mga precompiled na file (`.deb`, AppImage, standalone na executable at `SHA256SUMS-linux.txt`) ay nakapublish bilang pre-release sa [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) ng repository, sa ilalim ng tag na `Linux-v*`; binuo ang mga ito sa Debian 12 (glibc 2.36, Python 3.11, x86-64). Ini-install ng package ang software para sa lahat ng user:

```bash
sudo apt install ./calculateur-masques_1.0.1_amd64.deb
calculateur-masques
```

Hindi nagdaragdag ng anumang icon sa menu o sa Desktop ang pag-install: patakbuhin ang `calculateur-masques` sa unang pagkakataon, at iaalok ito ng window na "Magdagdag ng icon?". Para i-uninstall:

```bash
sudo apt remove calculateur-masques
```

Kusang nawawala ang entry ng menu na idinagdag ng software; nananatili naman ang shortcut sa Desktop (isa lamang itong file): alisin muna ito gamit ang button ng "Tungkol", o nang mano-mano.

### Gamit ang AppImage

Isang file lang, walang pag-install:

```bash
chmod +x CalculateurMasques-1.0.1-x86_64.AppImage
./CalculateurMasques-1.0.1-x86_64.AppImage
```

Kung walang FUSE ang system:

```bash
./CalculateurMasques-1.0.1-x86_64.AppImage --appimage-extract-and-run
```

### Gamit ang standalone na executable

Isang standalone na executable (PyInstaller) ang nako-compile sa isang command (tingnan ang "Pag-compile ng standalone na executable" sa ibaba); may precompiled na bersyon sa Releases:

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

Para i-verify ang mga na-download na file:

```bash
sha256sum -c SHA256SUMS-linux.txt
```

> **Paalala sa glibc**: binuo ang mga file na ito sa Debian 12. Na-verify ang mga ito sa distribusyong iyon; dapat din silang gumana sa mga distribusyong may glibc 2.36 o mas bago, ngunit hindi sa mas luma. Sa ganoong kaso, mag-compile mula sa source code.

---

## Pag-install sa system (opsyonal)

Para isama ang application sa menu ng desktop environment (GNOME, KDE, XFCE…):

```bash
# Kopyahin ang mga file sa /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Baguhin ang path sa .desktop file kung kinakailangan
# Exec=bash /opt/calculateur-masques/lancer.sh

# Idagdag sa menu ng mga application
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# o
sudo kbuildsycoca6              # KDE Plasma
```

---

## Pag-compile ng standalone na executable

Nakakagawa ang PyInstaller ng binary na walang dependency sa Python:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

Ang executable ay nalilikha sa `./dist/CalculateurMasquesIPv4`. Isinasama ng mga option na `--add-data` ang icon ng window (nilo-load sa runtime gamit ang Pillow kung mayroon, kung wala ay gamit ang Tk) at ang banner ng window na Tungkol; opsyonal ang Pillow (`pip3 install pillow`).

> **Tandaan:** ang Linux binary na na-compile sa Ubuntu ay hindi kinakailangang gumana sa Arch o Fedora dahil sa pagkakaiba ng mga bersyon ng glibc. Mag-compile sa target na distribusyon o gumamit ng Docker image para sa nais na distribusyon.

### Pagbuo ng `.deb` at ng AppImage

Sa Debian o Ubuntu, na nasa PATH ang PyInstaller at `appimagetool`, binubuo muna ng script ang isang PyInstaller folder, pagkatapos ay ang dalawang package sa `dist/`:

```bash
python3 packaging/build_linux_packages.py
python3 packaging/build_linux_packages.py --only deb
```

Ang option na `--only deb` (o `--only appimage`) ay isa lamang sa dalawa ang binubuo.

---

## Istruktura ng mga file

```
CalculateurMasques/            (branch na Linux)
├── calculateur_masques.py      # Pangunahing application (iniangkop sa Linux)
├── translations.py             # Diksyunaryo ng 15 wika (kapareho ng branch na main)
├── icon.png                    # Icon ng window / menu (512 px)
├── banner.png                  # Banner ng window na Tungkol (600 x 200)
├── lancer.sh                   # Script sa pagpapatakbo na may pagsusuri ng mga dependency
├── calculateur-masques.desktop # Entry ng menu para sa mga desktop environment
├── packaging/                  # Pagbuo ng .deb at ng AppImage
│   ├── build_linux_packages.py # Script sa pagbuo
│   └── linux/                  # AppRun, launcher, manual page, changelog ng .deb
├── INSTALLER.md                # Detalyadong tagubilin sa pag-install (sa Pranses)
├── LICENSE                     # MIT na lisensya
├── README-LINUX.md             # Gabay na ito, sa Pranses
└── docs/README-LINUX.<code>.md # Mga salin: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Mga pagkakaiba sa bersyong Windows

| Aspeto | Windows | Linux |
|---|---|---|
| Mga font | Segoe UI / Consolas | Awtomatikong pagtukoy (Noto Sans, DejaVu Sans, Liberation…) |
| Mouse wheel | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| CSV export | UTF-8 na may BOM (Excel) | UTF-8 na walang BOM (standard) |
| Executable | Standalone na `.exe` | ELF binary mula sa PyInstaller (nakadepende sa distro) |
| Integrasyon sa desktop | Shortcut ng Windows | `.deb` package, AppImage, icon ng menu at ng desktop (mga `.desktop` file, XDG) |

---

## Mga espesyal na kasong pinangangasiwaan

| Prefix | Pag-uugali |
|---|---|
| `/31` | Point-to-point na link (RFC 3021) — 2 address, walang karaniwang broadcast |
| `/32` | Nag-iisang host — una = huli = network address |
| `/0` | Universal na network `0.0.0.0` |

---

## Lisensya

Lisensyang MIT — tingnan ang file na `LICENSE`.
