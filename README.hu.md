# IPv4 Alhálózati Maszk Kalkulátor

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · **Magyar** · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

**Offline**, ingyenes és nyílt forráskódú grafikus segédprogram IPv4 alhálózati maszkok kiszámításához, hálózatok alhálózatokra osztásához, előzmények vezetéséhez és exportálásához. A felület **15 nyelven** érhető el.

Tárhely: <https://github.com/harlockSuites/CalculateurMasques>

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
- Az **Enter** billentyű elindítja a számítást

### Felosztás fül
- Hálózat felosztása N egyenlő alhálózatra
- Vagy a minimális CIDR megkeresése N hoszt befogadásához
- Az alhálózatok táblázata hálózat, maszk, hosztok és broadcast oszlopokkal (legfeljebb 65 536 sor, ezen felül a választott nyelven megjelenő üzenet)
- Jobb kattintás egy cellán az érték másolásához

### Előzmények fül
- Minden számítás automatikusan mentésre kerül, a számítás időpontjával
- Dupla kattintás egy bejegyzésen a kalkulátorba való visszatöltéshez
- **CSV** exportálás (UTF-8 kódolás BOM-mal, Excellel kompatibilis)
- **TXT** exportálás (olvasható formátum)

### Nyelvválasztó
15 nyelv érhető el az alkalmazás fejlécéből:

| Csoport | Nyelvek |
|---|---|
| Újlatin | Français · English · Español · Português · Italiano |
| Közép-/Kelet-Európa | Српски · Polski · Magyar · Русский |
| Dél-/Kelet-Ázsia | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

A nyelvváltás azonnali, újraindítás nélkül.

### Névjegy gomb
A nyelvválasztó mellett a **Névjegy** gomb egy ablakot nyit meg a szerző bannerével (`banner.png`) és a „Ez az offline segédprogram ingyenes és nyílt forráskódú." üzenettel, mind a 15 nyelvre lefordítva.

---

## Előfeltételek

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- `tkinter` modul (a Python szokásos telepítésének része)

A szkript futtatásához nincs szükség külső függőségre. A [Pillow](https://pypi.org/project/pillow/) választható: kizárólag az ablak ikonjának teljes felbontású megjelenítésére szolgál.

---

## Indítás

### Pythonnal
```
python calculateur_masques.py
```

### A lefordított futtatható fájllal
Kattintson duplán a `dist\CalculateurMasquesIPv4.exe` fájlra. A futtatható fájl önálló, telepítést nem igényel. Nem része a verziókezelt tárhelynek: fordítsa le (lásd lent).

---

## A futtatható fájl fordítása

A tárhely tartalmaz egy PyInstaller spec fájlt (`CalculateurMasquesIPv4.spec`), amely beágyazza az ikont, a bannert és a fordításokat. Ebből a mappából:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

A futtatható fájl a `dist\` mappában jön létre. Az ikon (`icon.ico`) be van építve az exe-be.

---

## Fájlstruktúra

```
CalculateurMasques\
├── calculateur_masques.py        # Fő alkalmazás
├── translations.py               # A 15 nyelv szótára
├── CalculateurMasquesIPv4.spec   # PyInstaller specifikáció
├── icon.ico                      # Az exe ikonja (Windows)
├── icon.png                      # Az ablak ikonja (512 px)
├── banner.png                    # A Névjegy ablak bannere (600 px)
├── LICENSE                       # MIT licenc
└── README.md
```

---

## Kezelt különleges esetek

| Előtag | Viselkedés |
|---|---|
| `/31` | Pont-pont kapcsolat (RFC 3021) — 2 cím, hagyományos broadcast nélkül |
| `/32` | Egyetlen hoszt — első = utolsó = hálózati cím |
| `/0` | Univerzális hálózat `0.0.0.0` |

---

## Vírusirtók és téves riasztások

2026. október 25-én a VirusTotal az 1.0 verzió `CalculateurMasquesIPv4.exe` futtatható fájlját **69 motorból 5 észleléssel** jelzi: Arctic Wolf, Bkav Pro, Microsoft, SecureAge és Zillya. Úgy véljük, hogy ezek **téves riasztások**, amelyek gyakoriak egy PyInstallerrel csomagolt, új és digitálisan alá nem írt Python-programnál. A program nem tartalmaz hálózati kódot (csak a `tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys` és `os` modulokat használja, valamint a Pillow-t az ablak ikonjához), és a teljes forráskódja nyilvános ebben a tárhelyen.

2026. október 25-én téves riasztásra vonatkozó jelentéseket küldtünk mind az öt érintett gyártónak. Ez a szakasz frissülni fog a válaszaikkal.

Letöltésének ellenőrzéséhez:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- VirusTotal-jelentés: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- A futtatható fájlt a forráskódból saját maga is lefordíthatja (lásd „A futtatható fájl fordítása”).

---

## Licenc

[MIT](LICENSE) licenc alatt terjesztve — © 2026 Harlock S.
