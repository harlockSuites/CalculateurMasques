# IPv4 Subnet Mask Calculator

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · **Filipino**

**Offline** na graphical utility, libre at open-source, para kalkulahin ang mga IPv4 subnet mask, hatiin ang isang network sa mga subnet, magtago ng kasaysayan at i-export ito. Ang interface ay may **15 wika**.

Repository: <https://github.com/harlockSuites/CalculateurMasques>

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
- Pindutin ang **Enter** para simulan ang kalkulasyon

### Tab na Paghahati
- Paghahati ng isang network sa N magkakapantay na subnet
- O paghahanap ng pinakamaliit na CIDR na kayang maglaman ng N host
- Talaan ng mga subnet na may network, mask, mga host, broadcast (may limitasyong 65,536 na row; kapag lumampas dito, may lalabas na mensahe sa napiling wika)
- I-right click ang isang cell para kopyahin ang halaga

### Tab na Kasaysayan
- Awtomatikong nire-record ang bawat kalkulasyon, kasama ang oras ng kalkulasyon
- Mag-double click sa isang entry para i-reload ito sa kalkulator
- **CSV** export (UTF-8 encoding na may BOM, compatible sa Excel)
- **TXT** export (madaling basahing format)

### Tagapili ng wika
Available ang 15 wika, mapipili mula sa header ng application:

| Grupo | Mga Wika |
|---|---|
| Romance | Français · English · Español · Português · Italiano |
| Gitna/Silangang Europa | Српски · Polski · Magyar · Русский |
| Timog/Silangang Asya | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

Agad ang pagpapalit ng wika, hindi kailangang i-restart ang application.

### Button na Tungkol
Sa tabi ng tagapili ng wika, binubuksan ng button na **Tungkol** ang isang window na may banner ng may-akda (`banner.png`) at ang mensaheng "Ang offline na utility software na ito ay libre at open-source.", na isinalin sa 15 wika.

---

## Mga Kinakailangan

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- Module na `tkinter` (kasama sa karaniwang installation ng Python)

Walang kailangang external na dependency para patakbuhin ang script. Opsyonal ang [Pillow](https://pypi.org/project/pillow/): ginagamit lamang ito para ipakita ang icon ng window sa buong resolution.

---

## Pagpapatakbo

### Gamit ang Python
```
python calculateur_masques.py
```

### Gamit ang na-compile na executable
I-double click ang `dist\CalculateurMasquesIPv4.exe`. Standalone ang executable, hindi kailangang i-install. Hindi ito kasama sa version control ng repository na ito: i-compile ito (tingnan sa ibaba).

---

## Pag-compile ng executable

Nagbibigay ang repository ng PyInstaller spec (`CalculateurMasquesIPv4.spec`) na nagsasama ng icon, banner at mga salin. Mula sa folder na ito:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

Ang executable ay nalilikha sa folder na `dist\`. Isinama sa exe ang icon (`icon.ico`).

---

## Istruktura ng mga file

```
CalculateurMasques\
├── calculateur_masques.py        # Pangunahing application
├── translations.py               # Diksyunaryo ng 15 wika
├── CalculateurMasquesIPv4.spec   # PyInstaller specification
├── icon.ico                      # Icon ng exe (Windows)
├── icon.png                      # Icon ng window (512 px)
├── banner.png                    # Banner ng window na Tungkol (600 px)
├── LICENSE                       # MIT na lisensya
└── README.md
```

---

## Mga espesyal na kasong pinangangasiwaan

| Prefix | Pag-uugali |
|---|---|
| `/31` | Point-to-point na link (RFC 3021) — 2 address, walang karaniwang broadcast |
| `/32` | Nag-iisang host — una = huli = network address |
| `/0` | Universal na network `0.0.0.0` |

---

## Lisensya

Ipinamamahagi sa ilalim ng lisensyang [MIT](LICENSE) — © 2026 Harlock S.
