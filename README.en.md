# IPv4 Subnet Mask Calculator

[Français](README.md) · **English** · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

**Offline**, free and open-source graphical utility to calculate IPv4 subnet masks, split a network into subnets, keep a history and export it. Interface in **15 languages**.

Repository: <https://github.com/harlockSuites/CalculateurMasques>

> **Linux:** a dedicated Linux version is available on the [`Linux` branch](https://github.com/harlockSuites/CalculateurMasques/tree/Linux). A prebuilt executable (pre-release, Debian 12, x86-64) is published in the [`Linux-v1.0` release](https://github.com/harlockSuites/CalculateurMasques/releases/tag/Linux-v1.0). This README describes the Windows version.

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

## Antivirus and false positives

As of October 25, 2026, VirusTotal flags the `CalculateurMasquesIPv4.exe` executable of version 1.0 with **5 detections out of 69 engines**: Arctic Wolf, Bkav Pro, Microsoft, SecureAge and Zillya. We believe these are **false positives**, which are common for a recent, digitally unsigned Python program packaged with PyInstaller. The program contains no network code (it only uses `tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys` and `os`, plus Pillow for the window icon) and all of its source code is public in this repository.

False positive reports were sent to the five vendors concerned on October 25, 2026. This section will be updated with their responses.

To verify your download:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- VirusTotal report: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- You can also build the executable yourself from the source code (see "Building the executable").

---

## License

Distributed under the [MIT](LICENSE) license — © 2026 Harlock S.
