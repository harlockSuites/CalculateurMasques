# Kalkulator Masek Podsieci IPv4 — Linux

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · **Polski** · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

> **Gałąź `Linux`**: wersja programu dla Linuksa. Gałąź `main` jest zarezerwowana dla dystrybucji Windows; nie należy scalać jednej z drugą.

Graficzne narzędzie do obliczania masek podsieci IPv4, z obsługą 15 języków, podziałem na podsieci, historią i eksportem.

Repozytorium: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

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
- **Maska odwrotna** (wildcard, np. `0.0.0.255`) jest odrzucana z komunikatem w wybranym języku: wpisz maskę podsieci (`255.255.255.0`)
- **Kółko myszy**: przewija stronę, niezależnie od tego, nad którym elementem znajduje się kursor (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Klawisz **Enter** uruchamia obliczenie

### Zakładka Podział
- Podział sieci na N równych podsieci
- Lub wyszukiwanie minimalnego CIDR mieszczącego N hostów
- Tabela podsieci z siecią, maską, hostami i broadcastem
- Ograniczenie do 65 536 podsieci na jeden podział (po jego przekroczeniu komunikat informuje o tym, zamiast zawieszać interfejs)
- Prawy klik na komórce kopiuje jej wartość

### Zakładka Historia
- Każde obliczenie jest zapisywane automatycznie wraz z godziną jego wykonania (zachowaną w widoku i w eksporcie)
- Dwukrotne kliknięcie wpisu przeładowuje go w kalkulatorze
- Eksport do **CSV** (kodowanie UTF-8)
- Eksport do **TXT** (czytelny format)

### Wybór języka
15 dostępnych języków, wybieranych w nagłówku aplikacji:

| Grupa | Języki |
|---|---|
| Romańskie | Français · English · Español · Português · Italiano |
| Europa Środkowa i Wschodnia | Српски · Polski · Magyar · Русский |
| Azja Południowa i Wschodnia | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

Zmiana języka następuje natychmiast, bez ponownego uruchamiania.

### Przycisk O programie
Obok wyboru języka przycisk **O programie** otwiera okno z banerem oraz komunikatem „To narzędzie działające offline jest darmowe i open source.”, przetłumaczonym na 15 języków. Klawisz Esc lub przycisk Zamknij zamyka to okno.

### Koreański i czcionka
Koreański jest wyświetlany na liście pod nazwą **Korean** (po angielsku, ponieważ „한국어” wyświetliłoby się jako kwadraty bez czcionki koreańskiej). Jeśli system nie ma żadnej takiej czcionki, jej wybranie otwiera okno dialogowe **po angielsku** („Font needed”), które wyjaśnia potrzebę i proponuje:
- **polecenie do skopiowania** w terminalu (instalacja dla wszystkich użytkowników): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — sprawdzono tylko polecenie dla Debian/Ubuntu;
- przycisk **Install automatically**: pobiera Noto Sans KR (4,6 MB, licencja SIL OFL, wersja zamrożona, suma SHA-256 zweryfikowana) do `~/.local/share/fonts/calculateur-masques/`, bez uprawnień administratora. To jedyny przypadek, w którym program korzysta z sieci; w pozostałym czasie działa offline;
- przycisk **Restart now**: uruchamia program ponownie (opcja `--lang ko`), aby widział czcionkę; język zmienia się po ponownym uruchomieniu. Język nie jest zapamiętywany między sesjami.

Aby usunąć pobraną czcionkę: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Inne języki z pismem nielacińskim (hindi, japoński, chiński…) nie mają takiego okna: bez odpowiedniej czcionki mogą pojawić się kwadraty. Dla japońskiego i chińskiego: `sudo apt install fonts-noto-cjk`.

---

## Wymagania

Python 3.8+ z modułem `tkinter`.

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

Żadne inne zależności nie są wymagane.

---

## Uruchamianie

### Szybka metoda

```bash
chmod +x lancer.sh
./lancer.sh
```

Skrypt automatycznie sprawdza obecność Pythona i tkintera oraz wyświetla czytelny komunikat o błędzie, jeśli brakuje jakiejś zależności.

### Bezpośrednio przez Pythona

```bash
python3 calculateur_masques.py
```

### Przez samodzielny plik wykonywalny

Samodzielny plik wykonywalny (PyInstaller) kompiluje się jednym poleceniem (patrz „Kompilacja samodzielnego pliku wykonywalnego” poniżej). Prekompilowana wersja jest publikowana (jako wersja wstępna) w [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) repozytorium, pod tagiem `Linux-v*`; jest zbudowana na Debianie 12 (glibc 2.36, Python 3.11, x86-64):

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **Zastrzeżenie dotyczące glibc**: ten plik binarny jest zbudowany na Debianie 12. Sprawdzono go na tej dystrybucji; powinien też działać na dystrybucjach z glibc 2.36 lub nowszą, ale nie na starszej. W takim przypadku skompiluj go ponownie ze źródeł.

---

## Instalacja systemowa (opcjonalnie)

Aby zintegrować aplikację z menu środowiska graficznego (GNOME, KDE, XFCE…):

```bash
# Skopiuj pliki do /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# W razie potrzeby zmień ścieżkę w pliku .desktop
# Exec=bash /opt/calculateur-masques/lancer.sh

# Dodaj do menu aplikacji
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# lub
sudo kbuildsycoca6              # KDE Plasma
```

---

## Kompilacja samodzielnego pliku wykonywalnego

PyInstaller pozwala wygenerować plik binarny niewymagający Pythona:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

Plik wykonywalny zostanie wygenerowany w `./dist/CalculateurMasquesIPv4`. Opcje `--add-data` osadzają ikonę okna (ładowaną w czasie działania przez Pillow, jeśli jest dostępny, w przeciwnym razie przez Tk) oraz baner okna „O programie”; Pillow jest opcjonalny (`pip3 install pillow`).

> **Uwaga:** plik binarny Linuksa skompilowany na Ubuntu nie musi działać na Archu ani Fedorze z powodu różnic w wersjach glibc. Kompiluj na dystrybucji docelowej lub użyj obrazu Dockera dla docelowej dystrybucji.

---

## Struktura plików

```
CalculateurMasques/            (gałąź Linux)
├── calculateur_masques.py      # Główna aplikacja (dostosowana do Linuksa)
├── translations.py             # Słownik 15 języków (identyczny jak w gałęzi main)
├── icon.png                    # Ikona okna / menu (512 px)
├── banner.png                  # Baner okna „O programie” (600 x 200)
├── lancer.sh                   # Skrypt uruchamiający ze sprawdzaniem zależności
├── calculateur-masques.desktop # Wpis menu dla środowisk graficznych
├── INSTALLER.md                # Szczegółowa instrukcja instalacji (po francusku)
├── LICENSE                     # Licencja MIT
├── README.md                   # Ten przewodnik, po francusku
└── README.<code>.md            # Tłumaczenia: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Różnice względem wersji Windows

| Aspekt | Windows | Linux |
|---|---|---|
| Czcionki | Segoe UI / Consolas | Automatyczne wykrywanie (Noto Sans, DejaVu Sans, Liberation…) |
| Kółko myszy | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Eksport CSV | UTF-8 z BOM (Excel) | UTF-8 bez BOM (standard) |
| Plik wykonywalny | samodzielny `.exe` | Plik binarny ELF przez PyInstaller (zależy od dystrybucji) |
| Integracja z pulpitem | Skrót Windows | Plik `.desktop` (XDG) |

---

## Obsługiwane przypadki szczególne

| Prefiks | Zachowanie |
|---|---|
| `/31` | Łącze punkt-punkt (RFC 3021) — 2 adresy, brak konwencjonalnego broadcastu |
| `/32` | Pojedynczy host — pierwszy = ostatni = adres sieci |
| `/0` | Sieć uniwersalna `0.0.0.0` |

---

## Licencja

Licencja MIT — zobacz plik `LICENSE`.
