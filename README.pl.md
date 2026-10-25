# Kalkulator Masek Podsieci IPv4

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · **Polski** · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

Graficzne narzędzie **offline**, darmowe i open source, do obliczania masek podsieci IPv4, dzielenia sieci na podsieci, prowadzenia historii obliczeń i jej eksportu. Interfejs w **15 językach**.

Repozytorium: <https://github.com/harlockSuites/CalculateurMasques>

> **Linux:** dedykowana wersja dla systemu Linux jest dostępna w [gałęzi `Linux`](https://github.com/harlockSuites/CalculateurMasques/tree/Linux). Gotowy plik wykonywalny (wersja wstępna, Debian 12, x86-64) opublikowano w [wydaniu `Linux-v1.0`](https://github.com/harlockSuites/CalculateurMasques/releases/tag/Linux-v1.0). Ten plik README opisuje wersję dla systemu Windows.

---

## Przegląd

Aplikacja jest podzielona na trzy zakładki:

| Zakładka | Zawartość |
|---|---|
| **Kalkulator** | Główne obliczenia, konwersje adresów IP, weryfikacja przynależności |
| **Podział** | Automatyczny podział sieci na podsieci |
| **Historia** | Rejestr obliczeń, eksport do CSV / TXT |

---

## Funkcje

### Zakładka Kalkulator
- Wprowadzanie przez **prefiks CIDR** (`/24`) lub **maskę dziesiętną** (`255.255.255.0`) — oba pola synchronizują się automatycznie
- Wyświetlane wyniki:
  - Adres sieci
  - Maska podsieci
  - Notacja CIDR
  - Maska symboliczna (wildcard)
  - Pierwszy / Ostatni adres hosta
  - Adres rozgłoszeniowy (broadcast)
  - Liczba użytecznych hostów
  - Pełny zakres sieci
- **Konwersje** wprowadzonego adresu IP: notacja dziesiętna z kropkami, binarna, szesnastkowa, dziesiętna 32-bitowa
- **Weryfikacja przynależności**: sprawdza, czy podany adres IP należy do obliczonej sieci
- **Prawy klik** na dowolnej wartości kopiuje ją do schowka
- Klawisz **Enter** uruchamia obliczenie

### Zakładka Podział
- Podział sieci na N równych podsieci
- Lub wyszukiwanie minimalnego CIDR mieszczącego N hostów
- Tabela podsieci z siecią, maską, hostami i broadcastem (ograniczona do 65 536 wierszy, a po jego przekroczeniu wyświetlany jest komunikat w wybranym języku)
- Prawy klik na komórce kopiuje jej wartość

### Zakładka Historia
- Każde obliczenie jest zapisywane automatycznie wraz z godziną jego wykonania
- Dwukrotne kliknięcie wpisu przeładowuje go w kalkulatorze
- Eksport do **CSV** (kodowanie UTF-8 z BOM, zgodne z Excelem)
- Eksport do **TXT** (czytelny format)

### Wybór języka
15 dostępnych języków, wybieranych w nagłówku aplikacji:

| Grupa | Języki |
|---|---|
| Romańskie | Français · English · Español · Português · Italiano |
| Europa Środkowa i Wschodnia | Српски · Polski · Magyar · Русский |
| Azja Południowa i Wschodnia | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

Zmiana języka następuje natychmiast, bez ponownego uruchamiania.

### Przycisk O programie
Obok wyboru języka przycisk **O programie** otwiera okno z banerem autora (`banner.png`) oraz komunikatem „To narzędzie działające offline jest darmowe i open source.”, przetłumaczonym na 15 języków.

---

## Wymagania

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- Moduł `tkinter` (wchodzi w skład standardowej instalacji Pythona)

Do uruchomienia skryptu nie są potrzebne żadne zewnętrzne zależności. [Pillow](https://pypi.org/project/pillow/) jest opcjonalny: służy wyłącznie do wyświetlania ikony okna w pełnej rozdzielczości.

---

## Uruchamianie

### Przez Pythona
```
python calculateur_masques.py
```

### Przez skompilowany plik wykonywalny
Kliknij dwukrotnie `dist\CalculateurMasquesIPv4.exe`. Plik wykonywalny jest samodzielny i nie wymaga instalacji. Nie jest wersjonowany w tym repozytorium: skompiluj go samodzielnie (patrz niżej).

---

## Kompilacja pliku wykonywalnego

Repozytorium zawiera plik spec dla PyInstallera (`CalculateurMasquesIPv4.spec`), który osadza ikonę, baner i tłumaczenia. Z poziomu tego folderu:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

Plik wykonywalny zostaje wygenerowany w folderze `dist\`. Ikona (`icon.ico`) jest wbudowana w plik exe.

---

## Struktura plików

```
CalculateurMasques\
├── calculateur_masques.py        # Główna aplikacja
├── translations.py               # Słownik 15 języków
├── CalculateurMasquesIPv4.spec   # Specyfikacja PyInstallera
├── icon.ico                      # Ikona pliku exe (Windows)
├── icon.png                      # Ikona okna (512 px)
├── banner.png                    # Baner okna O programie (600 px)
├── LICENSE                       # Licencja MIT
└── README.md
```

---

## Obsługiwane przypadki szczególne

| Prefiks | Zachowanie |
|---|---|
| `/31` | Łącze punkt-punkt (RFC 3021) — 2 adresy, brak konwencjonalnego broadcastu |
| `/32` | Pojedynczy host — pierwszy = ostatni = adres sieci |
| `/0` | Sieć uniwersalna `0.0.0.0` |

---

## Antywirusy i fałszywe alarmy

Według stanu na 25 października 2026 r. VirusTotal oznacza plik wykonywalny `CalculateurMasquesIPv4.exe` w wersji 1.0 jako zagrożenie w przypadku **5 z 69 silników**: Arctic Wolf, Bkav Pro, Microsoft, SecureAge i Zillya. Uważamy, że są to **fałszywe alarmy**, częste w przypadku programu w Pythonie spakowanego za pomocą PyInstaller, świeżego i niepodpisanego cyfrowo. Program nie zawiera żadnego kodu sieciowego (używa wyłącznie `tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys` i `os`, a ponadto Pillow do ikony okna), a cały jego kod źródłowy jest publicznie dostępny w tym repozytorium.

Zgłoszenia fałszywych alarmów zostały wysłane 25 października 2026 r. do wszystkich pięciu wymienionych producentów. Ta sekcja zostanie zaktualizowana o ich odpowiedzi.

Aby zweryfikować pobrany plik:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- Raport VirusTotal: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- Możesz też samodzielnie skompilować plik wykonywalny z kodu źródłowego (zobacz „Kompilacja pliku wykonywalnego”).

---

## Licencja

Rozpowszechniane na licencji [MIT](LICENSE) — © 2026 Harlock S.
