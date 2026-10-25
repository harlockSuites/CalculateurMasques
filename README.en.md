# IPv4 Subnet Mask Calculator

[Français](README.md) · **English** · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

**Offline**, free and open-source graphical utility to calculate IPv4 subnet masks, split a network into subnets, keep a history and export it. Interface in **15 languages**.

Repository: <https://github.com/harlockSuites/CalculateurMasques>

---

## Overview

The application is organized into three tabs:

| Tab | Contents |
|---|---|
| **Calculator** | Main calculation, IP conversions, membership check |
| **Subnetting** | Automatic division of a network into subnets |
| **History** | Calculation log, CSV / TXT export |

---

## Features

### Calculator tab
- Input by **CIDR prefix** (`/24`) or **decimal mask** (`255.255.255.0`) — the two synchronize automatically
- Results displayed:
  - Network Address
  - Subnet Mask
  - CIDR Notation
  - Wildcard Mask
  - First / Last Host Address
  - Broadcast Address
  - Number of Usable Hosts
  - Full Network Range
- **Conversions** of the entered IP address: Dotted Decimal Notation, Binary, Hexadecimal, Decimal (32-bit integer)
- **Membership Check**: tests whether a given IP belongs to the calculated network
- **Right-click** any value to copy it to the clipboard
- **Enter** key to trigger the calculation

### Subnetting tab
- Division of a network into N equal subnets
- Or search for the minimal CIDR able to hold N hosts
- Table of subnets with network, mask, hosts, broadcast (capped at 65,536 rows, with a message in the selected language beyond that)
- Right-click a cell to copy its value

### History tab
- Each calculation is saved automatically, with the time of the calculation
- Double-click an entry to reload it in the Calculator
- **CSV** export (UTF-8 encoding with BOM, Excel-compatible)
- **TXT** export (human-readable format)

### Language selector
15 languages available, accessible from the application header:

| Group | Languages |
|---|---|
| Romance | Français · English · Español · Português · Italiano |
| Central/Eastern Europe | Српски · Polski · Magyar · Русский |
| South/East Asia | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

The language changes instantly, without a restart.

### About button
Next to the language selector, the **About** button opens a window with the author's banner (`banner.png`) and the message "This offline utility software is free and open-source.", translated into all 15 languages.

---

## Requirements

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- `tkinter` module (included in the standard Python installation)

No external dependencies are required to run the script. [Pillow](https://pypi.org/project/pillow/) is optional: it is only used to display the window icon at full resolution.

---

## Running

### With Python
```
python calculateur_masques.py
```

### With the compiled executable
Double-click `dist\CalculateurMasquesIPv4.exe`. The executable is standalone and needs no installation. It is not versioned in this repository: build it yourself (see below).

---

## Building the executable

The repository provides a PyInstaller spec (`CalculateurMasquesIPv4.spec`) that bundles the icon, the banner and the translations. From this folder:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

The executable is generated in the `dist\` folder. The icon (`icon.ico`) is embedded in the exe.

---

## File structure

```
CalculateurMasques\
├── calculateur_masques.py        # Main application
├── translations.py               # Dictionary of the 15 languages
├── CalculateurMasquesIPv4.spec   # PyInstaller specification
├── icon.ico                      # Exe icon (Windows)
├── icon.png                      # Window icon (512 px)
├── banner.png                    # Banner of the About window (600 px)
├── LICENSE                       # MIT license
└── README.md
```

---

## Special cases handled

| Prefix | Behavior |
|---|---|
| `/31` | Point-to-point link (RFC 3021) — 2 addresses, no conventional broadcast |
| `/32` | Single host — first = last = network address |
| `/0` | Universal network `0.0.0.0` |

---

## License

Distributed under the [MIT](LICENSE) license — © 2026 Harlock S.
