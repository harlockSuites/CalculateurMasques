# IPv4 Alhálózati Maszk Kalkulátor — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · **Magyar** · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **`Linux` ág**: a szoftver Linux-verziója. A `main` ág a Windows-terjesztésnek van fenntartva; ne egyesítse az egyiket a másikkal.

Grafikus segédprogram IPv4 alhálózati maszkok kiszámításához, 15 nyelv támogatásával, alhálózatokra osztással, előzményekkel és exportálással.

Tárhely: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## Áttekintés

Az alkalmazás három fülből áll:

| Fül | Tartalom |
|---|---|
| **Kalkulátor** | Fő számítás, IP-konverziók, tagság ellenőrzése |
| **Felosztás** | Hálózat automatikus felosztása alhálózatokra |
| **Előzmények** | A számítások naplózása, CSV / TXT exportálás |

---

## Funkciók

### Kalkulátor fül
- Megadás **CIDR előtaggal** (`/24`) vagy **decimális maszkkal** (`255.255.255.0`) — a kettő automatikusan szinkronizálódik
- Megjelenített eredmények:
  - Hálózati cím
  - Alhálózati maszk
  - CIDR jelölés
  - Helyettesítő maszk (wildcard)
  - Első hoszt cím / Utolsó hoszt cím
  - Broadcast cím
  - Használható hosztok száma
  - Teljes hálózati tartomány
- A megadott IP-cím **konverziói**: Decimális pontozott jelölés, Bináris, Hexadecimális, Decimális (32 bites egész)
- **Tagság ellenőrzése**: megvizsgálja, hogy egy adott IP-cím a kiszámított hálózathoz tartozik-e
- **Jobb kattintás** bármely értéken a vágólapra másoláshoz
- A **fordított maszkot** (wildcard, pl. `0.0.0.255`) a program lefordított üzenettel elutasítja: adjon meg alhálózati maszkot (`255.255.255.0`)
- **Egérgörgő**: görgeti az oldalt, függetlenül attól, melyik elem fölött áll a kurzor (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Az **Enter** billentyű elindítja a számítást

### Felosztás fül
- Hálózat felosztása N egyenlő alhálózatra
- Vagy a minimális CIDR megkeresése N hoszt befogadásához
- Az alhálózatok táblázata hálózat, maszk, hosztok és broadcast oszlopokkal
- Felosztásonként legfeljebb 65 536 alhálózat (ezen felül egy üzenet jelzi ezt a felület lefagyása helyett)
- Jobb kattintás egy cellán az érték másolásához

### Előzmények fül
- Minden számítás automatikusan mentésre kerül, a számítás időpontjával (megjelenítéskor és exportáláskor is megmarad)
- Dupla kattintás egy bejegyzésen a kalkulátorba való visszatöltéshez
- **CSV** exportálás (UTF-8 kódolás)
- **TXT** exportálás (olvasható formátum)

### Nyelvválasztó
15 nyelv érhető el az alkalmazás fejlécéből:

| Csoport | Nyelvek |
|---|---|
| Újlatin | Français · English · Español · Português · Italiano |
| Közép-/Kelet-Európa | Српски · Polski · Magyar · Русский |
| Dél-/Kelet-Ázsia | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

A nyelvváltás azonnali, újraindítás nélkül.

### Névjegy gomb
A nyelvválasztó mellett egy ablakot nyit meg a bannerrel és a „Ez az offline segédprogram ingyenes és nyílt forráskódú." üzenettel, mind a 15 nyelvre lefordítva. Az Esc billentyű vagy a Bezárás gomb bezárja.

### Koreai nyelv és betűtípus
A koreai a listában **Korean** néven jelenik meg (angolul, mert a „한국어" koreai betűtípus nélkül négyzetekként jelenne meg). Ha a rendszeren nincs ilyen betűtípus, a kiválasztásakor egy **angol nyelvű** párbeszédablak („Font needed") nyílik meg, amely elmagyarázza a szükségességet, és felajánlja:
- egy **másolandó parancsot** egy terminálba (telepítés minden felhasználó számára): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — csak a Debian/Ubuntu parancs lett ellenőrizve;
- egy **Install automatically** gombot: letölti a Noto Sans KR betűtípust (4,6 MB, SIL OFL licenc, rögzített verzió, ellenőrzött SHA-256 összeg) a `~/.local/share/fonts/calculateur-masques/` mappába, rendszergazdai jogok nélkül. Ez az egyetlen eset, amikor a szoftver hálózatot használ; egyébként offline marad;
- egy **Restart now** gombot: újraindítja a szoftvert (`--lang ko` opcióval), hogy lássa a betűtípust; a nyelv az újraindításkor változik meg. A nyelv nem őrződik meg egyik munkamenetről a másikra.

A letöltött betűtípus eltávolításához: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> A többi nem latin írású nyelvhez (hindi, japán, kínai…) nincs ilyen párbeszédablak: megfelelő betűtípus nélkül négyzetek jelenhetnek meg. Japánhoz és kínaihoz: `sudo apt install fonts-noto-cjk`.

---

## Előfeltételek

Python 3.8+ a `tkinter` modullal.

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

Más függőségre nincs szükség.

---

## Indítás

### Gyors módszer

```bash
chmod +x lancer.sh
./lancer.sh
```

A szkript automatikusan ellenőrzi a Python és a tkinter jelenlétét, és egyértelmű hibaüzenetet jelenít meg, ha valamelyik függőség hiányzik.

### Közvetlenül Pythonnal

```bash
python3 calculateur_masques.py
```

### Önálló futtatható fájllal

Egy önálló futtatható fájl (PyInstaller) egyetlen paranccsal lefordítható (lásd lent az „Önálló futtatható fájl fordítása" szakaszt). Egy előre lefordított változat is közzé van téve (előzetes verzióként) a tárhely [Kiadások](https://github.com/harlockSuites/CalculateurMasques/releases) között, egy `Linux-v*` címke alatt; Debian 12 rendszeren készült (glibc 2.36, Python 3.11, x86-64):

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **glibc-fenntartás**: ez a bináris Debian 12 rendszeren készült. Ezen a disztribúción ellenőrizték; működnie kell a glibc 2.36-os vagy újabb verzióját használó disztribúciókon is, régebbin viszont nem. Ebben az esetben fordítsa le a forráskódból.

---

## Rendszerszintű telepítés (opcionális)

Az alkalmazás beillesztéséhez az asztali környezet menüjébe (GNOME, KDE, XFCE…):

```bash
# Fájlok másolása az /opt mappába
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Az elérési út módosítása a .desktop fájlban, ha szükséges
# Exec=bash /opt/calculateur-masques/lancer.sh

# Hozzáadás az alkalmazásmenühöz
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# vagy
sudo kbuildsycoca6              # KDE Plasma
```

---

## Önálló futtatható fájl fordítása

A PyInstaller lehetővé teszi Python-függőség nélküli bináris előállítását:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

A futtatható fájl a `./dist/CalculateurMasquesIPv4` helyen jön létre. Az `--add-data` opciók beágyazzák az ablak ikonját (futásidőben a Pillow tölti be, ha jelen van, egyébként a Tk) és a Névjegy ablak bannerét; a Pillow választható (`pip3 install pillow`).

> **Megjegyzés:** az Ubuntun lefordított Linux bináris nem feltétlenül fog működni Archon vagy Fedorán a glibc-verziók közötti különbségek miatt. Fordítson a célzott disztribúción, vagy használjon Docker-képet a célzott disztribúcióhoz.

---

## Fájlstruktúra

```
CalculateurMasques/            (Linux ág)
├── calculateur_masques.py      # Fő alkalmazás (Linuxra adaptálva)
├── translations.py             # A 15 nyelv szótára (azonos a main ággal)
├── icon.png                    # Az ablak / menü ikonja (512 px)
├── banner.png                  # A Névjegy ablak bannere (600 x 200)
├── lancer.sh                   # Indítószkript függőség-ellenőrzéssel
├── calculateur-masques.desktop # Menübejegyzés asztali környezetekhez
├── INSTALLER.md                # Részletes telepítési útmutató (franciául)
├── LICENSE                     # MIT licenc
├── README-LINUX.md             # Ez az útmutató, franciául
└── docs/README-LINUX.<code>.md # Fordítások: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Különbségek a Windows-verzióhoz képest

| Szempont | Windows | Linux |
|---|---|---|
| Betűtípusok | Segoe UI / Consolas | Automatikus felismerés (Noto Sans, DejaVu Sans, Liberation…) |
| Egérgörgő | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| CSV exportálás | UTF-8 BOM-mal (Excel) | UTF-8 BOM nélkül (szabványos) |
| Futtatható fájl | Önálló `.exe` | ELF bináris PyInstallerrel (disztribúciófüggő) |
| Asztali integráció | Windows parancsikon | `.desktop` fájl (XDG) |

---

## Kezelt különleges esetek

| Előtag | Viselkedés |
|---|---|
| `/31` | Pont-pont kapcsolat (RFC 3021) — 2 cím, hagyományos broadcast nélkül |
| `/32` | Egyetlen hoszt — első = utolsó = hálózati cím |
| `/0` | Univerzális hálózat `0.0.0.0` |

---

## Licenc

MIT licenc — lásd a `LICENSE` fájlt.
