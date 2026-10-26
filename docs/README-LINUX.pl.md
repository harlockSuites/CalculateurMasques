# Kalkulator Masek Podsieci IPv4 — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · **Polski** · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

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
Obok wyboru języka przycisk **O programie** otwiera okno z banerem oraz komunikatem „To narzędzie działające offline jest darmowe i open source.”, przetłumaczonym na 15 języków. Klawisz Esc lub przycisk Zamknij zamyka to okno. W pakiecie `.deb`, AppImage lub samodzielnym pliku wykonywalnym mały przycisk w lewym dolnym rogu tego okna dodaje lub usuwa ikonę programu (patrz niżej).

### Ikona w menu i na pulpicie
W pakiecie `.deb`, AppImage lub samodzielnym pliku wykonywalnym przy pierwszym uruchomieniu otwiera się okno **„Dodać ikonę?”** z trzema przyciskami: **Dodaj**, **Nie pytaj ponownie** i **Zamknij** (który niczego nie zapamiętuje: pytanie wróci przy następnym uruchomieniu). Przypomina ono, że ikonę będzie można później dodać lub usunąć przyciskiem na dole okna „O programie”.
- **Dodaj** tworzy wpis w **menu aplikacji** oraz ikonę w **folderze Pulpit**, bez uprawnień administratora. W przypadku AppImage i samodzielnego pliku wykonywalnego program najpierw kopiuje się do `~/.local/share/calculateur-masques/app` (ikona przetrwa przeniesienie pobranego pliku); w przypadku `.deb` nic nie jest kopiowane.
- **Nie pytaj ponownie** zapisuje wybór w `~/.config/calculateur-masques/config.json`; usunięcie ikony przyciskiem w oknie „O programie” również go zapisuje.
- Pakiet `.deb` nie dodaje żadnej ikony podczas instalacji: jego starter jest ukryty, ikona pojawia się tylko na żądanie.

> **GNOME** nie wyświetla ikon z folderu Pulpit bez rozszerzenia „Desktop Icons”: ikona pulpitu istnieje wtedy, ale pozostaje niewidoczna (program to sygnalizuje). Wpis w menu aplikacji jest natomiast widoczny.

Aby usunąć wszystko ręcznie:

```bash
rm -r ~/.local/share/calculateur-masques
rm -f ~/.local/share/applications/calculateur-masques.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/calculateur-masques.png
rm -f ~/Bureau/calculateur-masques.desktop ~/Desktop/calculateur-masques.desktop
rm -r ~/.config/calculateur-masques
```

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

### Przez pakiet `.deb` (Debian, Ubuntu, Linux Mint)

Prekompilowane pliki (`.deb`, AppImage, samodzielny plik wykonywalny i `SHA256SUMS-linux.txt`) są publikowane jako wersja wstępna w [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) repozytorium, pod tagiem `Linux-v*`; są zbudowane na Debianie 12 (glibc 2.36, Python 3.11, x86-64). Pakiet instaluje program dla wszystkich użytkowników:

```bash
sudo apt install ./calculateur-masques_1.0.1_amd64.deb
calculateur-masques
```

Instalacja nie dodaje żadnej ikony do menu ani na Pulpit: uruchom `calculateur-masques` po raz pierwszy, a okno „Dodać ikonę?” ją zaproponuje. Aby odinstalować:

```bash
sudo apt remove calculateur-masques
```

Wpis w menu dodany przez program znika sam; skrót na Pulpicie natomiast pozostaje (to zwykły plik): usuń go wcześniej przyciskiem w oknie „O programie” lub ręcznie.

### Przez AppImage

Jeden plik, bez instalacji:

```bash
chmod +x CalculateurMasques-1.0.1-x86_64.AppImage
./CalculateurMasques-1.0.1-x86_64.AppImage
```

Jeśli system nie ma FUSE:

```bash
./CalculateurMasques-1.0.1-x86_64.AppImage --appimage-extract-and-run
```

### Przez samodzielny plik wykonywalny

Samodzielny plik wykonywalny (PyInstaller) kompiluje się jednym poleceniem (patrz „Kompilacja samodzielnego pliku wykonywalnego” poniżej); prekompilowana wersja jest w Releases:

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

Aby zweryfikować pobrane pliki:

```bash
sha256sum -c SHA256SUMS-linux.txt
```

> **Zastrzeżenie dotyczące glibc**: te pliki są zbudowane na Debianie 12. Sprawdzono je na tej dystrybucji; powinny też działać na dystrybucjach z glibc 2.36 lub nowszą, ale nie na starszej. W takim przypadku skompiluj je ponownie ze źródeł.

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

### Budowanie `.deb` i AppImage

W Debianie lub Ubuntu, mając PyInstaller i `appimagetool` w PATH, skrypt najpierw buduje katalog PyInstaller, a następnie oba pakiety w `dist/`:

```bash
python3 packaging/build_linux_packages.py
python3 packaging/build_linux_packages.py --only deb
```

Opcja `--only deb` (lub `--only appimage`) buduje tylko jeden z dwóch.

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
├── packaging/                  # Budowanie pakietu .deb i AppImage
│   ├── build_linux_packages.py # Skrypt budujący
│   └── linux/                  # AppRun, starter, strona man, dziennik zmian .deb
├── INSTALLER.md                # Szczegółowa instrukcja instalacji (po francusku)
├── LICENSE                     # Licencja MIT
├── README-LINUX.md             # Ten przewodnik, po francusku
└── docs/README-LINUX.<code>.md # Tłumaczenia: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Różnice względem wersji Windows

| Aspekt | Windows | Linux |
|---|---|---|
| Czcionki | Segoe UI / Consolas | Automatyczne wykrywanie (Noto Sans, DejaVu Sans, Liberation…) |
| Kółko myszy | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Eksport CSV | UTF-8 z BOM (Excel) | UTF-8 bez BOM (standard) |
| Plik wykonywalny | samodzielny `.exe` | Plik binarny ELF przez PyInstaller (zależy od dystrybucji) |
| Integracja z pulpitem | Skrót Windows | Pakiet `.deb`, AppImage, ikona w menu i na pulpicie (pliki `.desktop`, XDG) |

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
