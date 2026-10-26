# IPv4 Subnet Mask Calculator — Linux

[Français](../README-LINUX.md) · **English** · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **`Linux` branch**: Linux version of the software. The `main` branch is reserved for the Windows distribution; do not merge one into the other.

Graphical utility to calculate IPv4 subnet masks, with support for 15 languages, subnet splitting, history and export.

Repository: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

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
- An **inverse mask** (wildcard, e.g. `0.0.0.255`) is rejected with a message in the selected language: enter a subnet mask (`255.255.255.0`)
- **Mouse wheel**: scrolls the page, whatever element is under the pointer (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- **Enter** key to trigger the calculation

### Subnetting tab
- Division of a network into N equal subnets
- Or search for the minimal CIDR able to hold N hosts
- Table of subnets with network, mask, hosts, broadcast
- Cap of 65,536 subnets per split (beyond that, a message says so instead of freezing the interface)
- Right-click a cell to copy its value

### History tab
- Each calculation is saved automatically, with the time at which it was made (kept in the display and in the export)
- Double-click an entry to reload it in the Calculator
- **CSV** export (UTF-8 encoding)
- **TXT** export (human-readable format)

### Language selector
15 languages available, accessible from the application header:

| Group | Languages |
|---|---|
| Romance | Français · English · Español · Português · Italiano |
| Central/Eastern Europe | Српски · Polski · Magyar · Русский |
| South/East Asia | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

The language changes instantly, without a restart.

### About button
Next to the language selector, it opens a window with the banner and the message "This offline utility software is free and open-source.", translated into all 15 languages. The Esc key or the Close button closes it. From the `.deb` package, the AppImage or the standalone executable, a small button at the bottom left of this window adds or removes the software's icon (see below).

### Menu and desktop icon
From the `.deb` package, the AppImage or the standalone executable, an **"Add an icon?"** window opens on first launch, with three buttons: **Add**, **Don't ask again** and **Close** (which remembers nothing: the question will come back at the next launch). It reminds you that the icon can later be added or removed with the button at the bottom of the About window.
- **Add** creates the **applications menu** entry and the icon in the **Desktop folder**, without administrator rights. With the AppImage and the standalone executable, the software is first copied to `~/.local/share/calculateur-masques/app` (the icon survives if you move the downloaded file); with the `.deb`, nothing is copied.
- **Don't ask again** saves the choice in `~/.config/calculateur-masques/config.json`; removing the icon with the About button saves it too.
- The `.deb` adds no icon at installation: its launcher is hidden, and the icon appears only on request.

> **GNOME** does not display the icons of the Desktop folder without the "Desktop Icons" extension: the desktop icon then exists, but stays invisible (the software points this out). The applications menu entry, on the other hand, is visible.

To remove everything by hand:

```bash
rm -r ~/.local/share/calculateur-masques
rm -f ~/.local/share/applications/calculateur-masques.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/calculateur-masques.png
rm -f ~/Bureau/calculateur-masques.desktop ~/Desktop/calculateur-masques.desktop
rm -r ~/.config/calculateur-masques
```

### Korean and font
Korean appears under the name **Korean** in the list (in English, because "한국어" would be displayed as squares without a Korean font). If the system has none, choosing it opens a dialog box **in English** ("Font needed") that explains the need and offers:
- a **command to copy** into a terminal (installation for all users): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — only the Debian/Ubuntu command has been verified;
- an **Install automatically** button: downloads Noto Sans KR (4.6 MB, SIL OFL license, pinned version, SHA-256 checksum verified) into `~/.local/share/fonts/calculateur-masques/`, without administrator rights. This is the only case where the software uses the network; it stays offline the rest of the time;
- a **Restart now** button: relaunches the software (`--lang ko` option) so that it picks up the font; the language changes on restart. The language is not remembered from one session to the next.

To remove the downloaded font: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> The other languages with a non-Latin script (Hindi, Japanese, Chinese…) have no such dialog: without a suitable font, squares may be displayed. For Japanese and Chinese: `sudo apt install fonts-noto-cjk`.

---

## Requirements

Python 3.8+ with the `tkinter` module.

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

No other dependency required.

---

## Running

### Quick method

```bash
chmod +x lancer.sh
./lancer.sh
```

The script automatically checks for the presence of Python and tkinter, and displays a clear error message if a dependency is missing.

### With Python directly

```bash
python3 calculateur_masques.py
```

### With the `.deb` package (Debian, Ubuntu, Linux Mint)

The precompiled files (`.deb`, AppImage, standalone executable and `SHA256SUMS-linux.txt`) are published as a pre-release in the repository's [Releases](https://github.com/harlockSuites/CalculateurMasques/releases), under a `Linux-v*` tag; they are built on Debian 12 (glibc 2.36, Python 3.11, x86-64). The package installs the software for all users:

```bash
sudo apt install ./calculateur-masques_1.0.1_amd64.deb
calculateur-masques
```

The installation adds no icon to the menu or to the Desktop: launch `calculateur-masques` once, and the "Add an icon?" window offers it. To uninstall:

```bash
sudo apt remove calculateur-masques
```

The menu entry added by the software disappears by itself; the Desktop shortcut, however, stays (it is a plain file): remove it beforehand with the About button, or by hand.

### With the AppImage

A single file, no installation:

```bash
chmod +x CalculateurMasques-1.0.1-x86_64.AppImage
./CalculateurMasques-1.0.1-x86_64.AppImage
```

If the system has no FUSE:

```bash
./CalculateurMasques-1.0.1-x86_64.AppImage --appimage-extract-and-run
```

### With a standalone executable

A standalone executable (PyInstaller) can be built with a single command (see "Building a standalone executable" below); a precompiled version is in the Releases:

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

To check the downloaded files:

```bash
sha256sum -c SHA256SUMS-linux.txt
```

> **glibc caveat**: these files are built on Debian 12. They are verified on that distribution; they should also work on distributions with glibc 2.36 or newer, but not on an older one. In that case, build from source.

---

## System installation (optional)

To integrate the application into the desktop environment menu (GNOME, KDE, XFCE…):

```bash
# Copy the files to /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Edit the path in the .desktop file if necessary
# Exec=bash /opt/calculateur-masques/lancer.sh

# Add to the applications menu
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# or
sudo kbuildsycoca6              # KDE Plasma
```

---

## Building a standalone executable

PyInstaller can generate a binary with no Python dependency:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

The executable will be generated in `./dist/CalculateurMasquesIPv4`. The `--add-data` options embed the window icon (loaded at runtime via Pillow if present, otherwise by Tk) and the banner of the About window; Pillow is optional (`pip3 install pillow`).

> **Note:** a Linux binary built on Ubuntu will not necessarily run on Arch or Fedora because of differences in glibc versions. Build on the target distribution or use a Docker image for the intended distribution.

### Building the `.deb` and the AppImage

On Debian or Ubuntu, with PyInstaller and `appimagetool` in the PATH, the script first builds a PyInstaller folder, then the two packages in `dist/`:

```bash
python3 packaging/build_linux_packages.py
python3 packaging/build_linux_packages.py --only deb
```

The `--only deb` option (or `--only appimage`) builds only one of the two.

---

## File structure

```
CalculateurMasques/            (Linux branch)
├── calculateur_masques.py      # Main application (Linux-adapted)
├── translations.py             # Dictionary of the 15 languages (identical to the main branch)
├── icon.png                    # Window / menu icon (512 px)
├── banner.png                  # Banner of the About window (600 x 200)
├── lancer.sh                   # Launch script with dependency checks
├── calculateur-masques.desktop # Menu entry for desktop environments
├── packaging/                  # Building the .deb and the AppImage
│   ├── build_linux_packages.py # Build script
│   └── linux/                  # AppRun, launcher, man page, .deb changelog
├── INSTALLER.md                # Detailed installation instructions (in French)
├── LICENSE                     # MIT license
├── README-LINUX.md             # This guide, in French
└── docs/README-LINUX.<code>.md # Translations: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Differences from the Windows version

| Aspect | Windows | Linux |
|---|---|---|
| Fonts | Segoe UI / Consolas | Automatic detection (Noto Sans, DejaVu Sans, Liberation…) |
| Mouse wheel | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| CSV export | UTF-8 with BOM (Excel) | UTF-8 without BOM (standard) |
| Executable | Standalone `.exe` | ELF binary via PyInstaller (depends on the distro) |
| Desktop integration | Windows shortcut | `.deb` package, AppImage, menu and desktop icon (`.desktop` files, XDG) |

---

## Special cases handled

| Prefix | Behavior |
|---|---|
| `/31` | Point-to-point link (RFC 3021) — 2 addresses, no conventional broadcast |
| `/32` | Single host — first = last = network address |
| `/0` | Universal network `0.0.0.0` |

---

## License

MIT license — see the `LICENSE` file.
