# IPv4 Калкулатор Мрежних Маски — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · **Српски** · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **Грана `Linux`**: Linux верзија програма. Грана `main` је резервисана за Windows дистрибуцију; не спајати једну са другом.

Графички алат за израчунавање IPv4 маски подмрежа, са подршком за 15 језика, поделом мреже на подмреже, историјом и извозом.

Репозиторијум: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## Преглед

Апликација је организована у три картице:

| Картица | Садржај |
|---|---|
| **Калкулатор** | Главно израчунавање, IP конверзије, провера припадности |
| **Подела** | Аутоматска подела мреже на подмреже |
| **Историја** | Бележење израчунавања, извоз у CSV / TXT |

---

## Функционалности

### Картица Калкулатор
- Унос преко **CIDR префикса** (`/24`) или **децималне маске** (`255.255.255.0`) — оба се аутоматски синхронизују
- Приказани резултати:
  - Адреса мреже
  - Маска подмреже
  - CIDR нотација
  - Wildcard маска
  - Прва / Последња адреса хоста
  - Broadcast адреса
  - Број употребљивих хостова
  - Потпуни опсег мреже
- **Конверзије** унете IP адресе: децимална нотација са тачкама, бинарно, хексадецимално, децимално (32-битни цео број)
- **Провера припадности**: проверава да ли задата IP адреса припада израчунатој мрежи
- **Десни клик** на било коју вредност за копирање у привремену меморију
- **Инверзна маска** (wildcard, нпр. `0.0.0.255`) се одбија уз поруку на изабраном језику: унесите маску подмреже (`255.255.255.0`)
- **Точкић миша**: помера страницу, без обзира на то који је елемент испод показивача (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Тастер **Enter** за покретање израчунавања

### Картица Подела
- Подела мреже на N једнаких подмрежа
- Или налажење минималног CIDR-а који може да садржи N хостова
- Табела подмрежа са мрежом, маском, хостовима, broadcast-ом
- Ограничење од 65 536 подмрежа по подели (изнад тога порука то објашњава, уместо да се интерфејс замрзне)
- Десни клик на ћелију за копирање вредности

### Картица Историја
- Свако израчунавање се аутоматски бележи, заједно са временом када је обављено (чува се при приказу и при извозу)
- Двоструки клик на унос за његово поновно учитавање у калкулатор
- Извоз **CSV** (UTF-8 кодирање)
- Извоз **TXT** (читљив формат)

### Избор језика
15 доступних језика, до којих се долази из заглавља апликације:

| Група | Језици |
|---|---|
| Романски | Français · English · Español · Português · Italiano |
| Централна/Источна Европа | Српски · Polski · Magyar · Русский |
| Јужна/Источна Азија | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

Промена језика је тренутна, без поновног покретања.

### Дугме О програму
Поред избора језика, отвара прозор са банером и поруком „Овај помоћни програм који ради ван мреже је бесплатан и отвореног кода.“, преведеном на свих 15 језика. Тастер Esc или дугме Затвори га затвара. Из `.deb` пакета, AppImage-а или самосталног извршног фајла, мало дугме у доњем левом углу овог прозора додаје или уклања иконицу програма (видети испод).

### Иконица менија и радне површине
Из `.deb` пакета, AppImage-а или самосталног извршног фајла, при првом покретању отвара се прозор **„Додати иконицу?“** са три дугмета: **Додај**, **Не питај више** и **Затвори** (које ништа не памти: питање ће се поново појавити при следећем покретању). Он подсећа да се иконица касније може додати или уклонити дугметом при дну прозора „О програму“.
- **Додај** прави ставку у **менију апликација** и иконицу у **фолдеру радне површине**, без администраторских права. Са AppImage-ом и самосталним извршним фајлом, програм се прво копира у `~/.local/share/calculateur-masques/app` (иконица остаје и ако преместите преузети фајл); са `.deb` пакетом, ништа се не копира.
- **Не питај више** памти избор у `~/.config/calculateur-masques/config.json`; уклањање иконице дугметом из прозора „О програму“ такође га памти.
- `.deb` пакет при инсталацији не додаје никакву иконицу: његов покретач је сакривен, а иконица се појављује само на захтев.

> **GNOME** не приказује иконице из фолдера радне површине без проширења „Desktop Icons“: иконица тада постоји, али остаје невидљива (програм то јавља). Ставка у менију апликација је, међутим, видљива.

Да бисте све уклонили ручно:

```bash
rm -r ~/.local/share/calculateur-masques
rm -f ~/.local/share/applications/calculateur-masques.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/calculateur-masques.png
rm -f ~/Bureau/calculateur-masques.desktop ~/Desktop/calculateur-masques.desktop
rm -r ~/.config/calculateur-masques
```

### Корејски и фонт
Корејски се у листи појављује под именом **Korean** (на енглеском, јер би се „한국어“ приказало као квадратићи без корејског фонта). Ако систем нема ниједан, његов избор отвара дијалог **на енглеском** („Font needed“) који објашњава потребу и нуди:
- **команду за копирање** у терминал (инсталација за све кориснике): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — проверена је само команда за Debian/Ubuntu;
- дугме **Install automatically**: преузима Noto Sans KR (4,6 MB, лиценца SIL OFL, фиксирана верзија, проверен SHA-256 збир) у `~/.local/share/fonts/calculateur-masques/`, без администраторских права. То је једини случај у којем програм користи мрежу; у осталом времену ради ван мреже;
- дугме **Restart now**: поново покреће програм (опција `--lang ko`) да би видео фонт; језик се мења при поновном покретању. Језик се не памти од једне сесије до друге.

Да бисте уклонили преузети фонт: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Остали језици са нелатиничним писмом (хинди, јапански, кинески…) немају такав дијалог: без одговарајућег фонта могу се приказати квадратићи. За јапански и кинески: `sudo apt install fonts-noto-cjk`.

---

## Предуслови

Python 3.8+ са модулом `tkinter`.

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

Није потребна ниједна друга зависност.

---

## Покретање

### Брзи начин

```bash
chmod +x lancer.sh
./lancer.sh
```

Скрипта аутоматски проверава присуство Python-а и tkinter-а и приказује јасну поруку о грешци ако нека зависност недостаје.

### Директно преко Python-а

```bash
python3 calculateur_masques.py
```

### Преко `.deb` пакета (Debian, Ubuntu, Linux Mint)

Претходно компајлирани фајлови (`.deb`, AppImage, самостални извршни фајл и `SHA256SUMS-linux.txt`) објављени су (као пред-издање) у [Издањима](https://github.com/harlockSuites/CalculateurMasques/releases) репозиторијума, под ознаком `Linux-v*`; направљени су на Debian-у 12 (glibc 2.36, Python 3.11, x86-64). Пакет инсталира програм за све кориснике:

```bash
sudo apt install ./calculateur-masques_1.0.1_amd64.deb
calculateur-masques
```

Инсталација не додаје никакву иконицу у мени нити на радну површину: покрените `calculateur-masques` први пут, прозор „Додати иконицу?“ је нуди. За деинсталацију:

```bash
sudo apt remove calculateur-masques
```

Ставка менија коју је додао програм нестаје сама; пречица на радној површини, међутим, остаје (то је обичан фајл): уклоните је претходно дугметом из прозора „О програму“ или ручно.

### Преко AppImage-а

Један фајл, без инсталације:

```bash
chmod +x CalculateurMasques-1.0.1-x86_64.AppImage
./CalculateurMasques-1.0.1-x86_64.AppImage
```

Ако систем нема FUSE:

```bash
./CalculateurMasques-1.0.1-x86_64.AppImage --appimage-extract-and-run
```

### Преко самосталног извршног фајла

Самостални извршни фајл (PyInstaller) компајлира се једном командом (видети „Компајлирање самосталног извршног фајла“ испод); претходно компајлирана верзија налази се у Издањима:

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

Да бисте проверили преузете фајлове:

```bash
sha256sum -c SHA256SUMS-linux.txt
```

> **Напомена о glibc-у**: ови фајлови су направљени на Debian-у 12. Проверени су на тој дистрибуцији; требало би да раде и на дистрибуцијама са glibc 2.36 или новијим, али не и са старијим. У том случају компајлирајте из изворног кода.

---

## Системска инсталација (опционо)

Да бисте апликацију интегрисали у мени desktop окружења (GNOME, KDE, XFCE…):

```bash
# Копирање фајлова у /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# По потреби измените путању у .desktop фајлу
# Exec=bash /opt/calculateur-masques/lancer.sh

# Додавање у мени апликација
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# или
sudo kbuildsycoca6              # KDE Plasma
```

---

## Компајлирање самосталног извршног фајла

PyInstaller омогућава стварање бинарног фајла без Python зависности:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

Извршни фајл ће бити генерисан у `./dist/CalculateurMasquesIPv4`. Опције `--add-data` уграђују икону прозора (учитава се током извршавања преко Pillow-а ако је присутан, иначе преко Tk-а) и банер прозора „О програму“; Pillow је опционалан (`pip3 install pillow`).

> **Напомена:** Linux бинарни фајл компајлиран на Ubuntu-у неће нужно радити на Arch-у или Fedora-и због разлика у верзијама glibc-а. Компајлирајте на циљној дистрибуцији или користите Docker слику за жељену дистрибуцију.

### Прављење `.deb` пакета и AppImage-а

На Debian-у или Ubuntu-у, са PyInstaller-ом и `appimagetool` у PATH-у, скрипта прво прави PyInstaller фолдер, а затим оба пакета у `dist/`:

```bash
python3 packaging/build_linux_packages.py
python3 packaging/build_linux_packages.py --only deb
```

Опција `--only deb` (или `--only appimage`) прави само један од два.

---

## Структура фајлова

```
CalculateurMasques/            (грана Linux)
├── calculateur_masques.py      # Главна апликација (прилагођена за Linux)
├── translations.py             # Речник са 15 језика (идентичан као у грани main)
├── icon.png                    # Икона прозора / менија (512 px)
├── banner.png                  # Банер прозора „О програму“ (600 x 200)
├── lancer.sh                   # Скрипта за покретање са провером зависности
├── calculateur-masques.desktop # Ставка менија за desktop окружења
├── packaging/                  # Прављење .deb пакета и AppImage-а
│   ├── build_linux_packages.py # Скрипта за прављење
│   └── linux/                  # AppRun, покретач, man страница, дневник промена .deb пакета
├── INSTALLER.md                # Детаљна упутства за инсталацију (на француском)
├── LICENSE                     # MIT лиценца
├── README-LINUX.md             # Овај водич, на француском
└── docs/README-LINUX.<code>.md # Преводи: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Разлике у односу на Windows верзију

| Аспект | Windows | Linux |
|---|---|---|
| Фонтови | Segoe UI / Consolas | Аутоматско откривање (Noto Sans, DejaVu Sans, Liberation…) |
| Точкић миша | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Извоз CSV | UTF-8 са BOM-ом (Excel) | UTF-8 без BOM-а (стандард) |
| Извршни фајл | Самостални `.exe` | ELF бинарни фајл преко PyInstaller-а (зависи од дистрибуције) |
| Интеграција у desktop | Windows пречица | `.deb` пакет, AppImage, иконица менија и радне површине (фајлови `.desktop`, XDG) |

---

## Подржани посебни случајеви

| Префикс | Понашање |
|---|---|
| `/31` | Веза тачка-тачка (RFC 3021) — 2 адресе, без конвенционалног broadcast-а |
| `/32` | Један хост — прва = последња = адреса мреже |
| `/0` | Универзална мрежа `0.0.0.0` |

---

## Лиценца

MIT лиценца — видети фајл `LICENSE`.
