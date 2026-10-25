# IPv4 서브넷 마스크 계산기 — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · **한국어** · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **`Linux` 브랜치**: 소프트웨어의 Linux 버전입니다. `main` 브랜치는 Windows 배포용으로만 사용되므로 서로 병합하지 마세요.

15개 언어를 지원하며, 서브넷 분할, 기록, 내보내기 기능을 갖춘 IPv4 서브넷 마스크 계산용 그래픽 유틸리티입니다.

저장소: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## 개요

애플리케이션은 세 개의 탭으로 구성되어 있습니다.

| 탭 | 내용 |
|---|---|
| **계산기** | 기본 계산, IP 변환, 소속 확인 |
| **서브넷 분할** | 네트워크를 서브넷으로 자동 분할 |
| **기록** | 계산 내역 기록, CSV / TXT 내보내기 |

---

## 기능

### 계산기 탭
- **CIDR 접두사**(`/24`) 또는 **10진수 마스크**(`255.255.255.0`)로 입력 — 두 값은 자동으로 동기화됩니다
- 표시되는 결과:
  - 네트워크 주소
  - 서브넷 마스크
  - CIDR 표기법
  - 와일드카드 마스크
  - 첫 번째 / 마지막 호스트 주소
  - 브로드캐스트 주소
  - 사용 가능한 호스트 수
  - 전체 네트워크 범위
- 입력한 IP 주소의 **변환**: 점진 10진수 표기법, 이진수, 16진수, 10진수(32비트 정수)
- **소속 확인**: 지정한 IP가 계산된 네트워크에 속하는지 테스트
- 임의의 값에서 **오른쪽 클릭**하면 클립보드로 복사
- **와일드카드(역) 마스크**(예: `0.0.0.255`)는 번역된 메시지와 함께 거부됩니다. 서브넷 마스크를 입력하세요(`255.255.255.0`)
- **마우스 휠**: 마우스 포인터가 어느 요소 위에 있든 페이지를 스크롤합니다(X11: `Button-4`/`Button-5`, Wayland: `MouseWheel`)
- **Enter** 키로 계산 실행

### 서브넷 분할 탭
- 네트워크를 N개의 동일한 서브넷으로 분할
- 또는 N개의 호스트를 수용할 수 있는 최소 CIDR 검색
- 네트워크, 마스크, 호스트, 브로드캐스트가 표시되는 서브넷 표
- 분할당 서브넷은 최대 65,536개이며, 초과하면 인터페이스가 멈추는 대신 메시지가 표시됩니다
- 셀을 오른쪽 클릭하면 값 복사

### 기록 탭
- 모든 계산이 계산 시각과 함께 자동으로 저장됩니다(시각은 화면 표시와 내보내기에 유지됩니다)
- 항목을 더블 클릭하면 계산기에 다시 불러옵니다
- **CSV** 내보내기(UTF-8 인코딩)
- **TXT** 내보내기(읽기 쉬운 형식)

### 언어 선택기
애플리케이션 상단의 헤더에서 15개 언어를 선택할 수 있습니다.

| 그룹 | 언어 |
|---|---|
| 로망스어군 | Français · English · Español · Português · Italiano |
| 중부/동유럽 | Српски · Polski · Magyar · Русский |
| 남아시아/동아시아 | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

언어 변경은 재시작 없이 즉시 적용됩니다.

### 정보 버튼
언어 선택기 옆의 **정보** 버튼을 누르면 배너와 "이 오프라인 유틸리티 소프트웨어는 무료이며 오픈 소스입니다."라는 메시지가 담긴 창이 열리며, 이 메시지는 15개 언어로 번역되어 있습니다. Esc 키 또는 **닫기** 버튼으로 창을 닫습니다.

### 한국어와 글꼴
한국어는 목록에 **Korean**이라는 이름(영어)으로 표시됩니다(한국어 글꼴이 없는 시스템에서는 「한국어」가 네모 칸으로 표시되기 때문입니다). 시스템에 한국어 글꼴이 하나도 없으면, 이 언어를 선택할 때 **영어**로 된 대화 상자("Font needed")가 열려 글꼴이 필요한 이유를 설명하고 다음을 제공합니다.
- 터미널에 **복사해서 실행할 명령**(모든 사용자를 대상으로 설치): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — Debian/Ubuntu 명령만 검증되었습니다.
- **Install automatically** 버튼: 관리자 권한 없이 Noto Sans KR(4.6MB, SIL OFL 라이선스, 고정 버전, SHA-256 체크섬 검증)을 `~/.local/share/fonts/calculateur-masques/`에 다운로드합니다. 소프트웨어가 네트워크를 사용하는 유일한 경우이며, 그 외에는 계속 오프라인으로 동작합니다.
- **Restart now** 버튼: 소프트웨어가 글꼴을 인식하도록 다시 시작합니다(`--lang ko` 옵션). 언어는 재시작할 때 바뀝니다. 언어는 세션 간에 기억되지 않습니다.

다운로드한 글꼴을 삭제하려면: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> 라틴 문자가 아닌 다른 언어(힌디어, 일본어, 중국어 등)에는 이런 대화 상자가 없습니다. 알맞은 글꼴이 없으면 네모 칸이 표시될 수 있습니다. 일본어와 중국어의 경우: `sudo apt install fonts-noto-cjk`.

---

## 요구 사항

`tkinter` 모듈이 포함된 Python 3.8+.

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

다른 의존성은 필요하지 않습니다.

---

## 실행

### 빠른 방법

```bash
chmod +x lancer.sh
./lancer.sh
```

스크립트가 Python과 tkinter의 존재 여부를 자동으로 확인하며, 의존성이 없으면 명확한 오류 메시지를 표시합니다.

### Python으로 직접 실행

```bash
python3 calculateur_masques.py
```

### 독립 실행형 실행 파일로 실행

독립 실행형 실행 파일(PyInstaller)은 명령 하나로 컴파일할 수 있습니다(아래 「독립 실행형 실행 파일 컴파일」 참조). 미리 컴파일된 버전은 저장소의 [릴리스](https://github.com/harlockSuites/CalculateurMasques/releases)에 `Linux-v*` 태그로 (프리릴리스로) 게시되어 있으며, Debian 12(glibc 2.36, Python 3.11, x86-64)에서 빌드되었습니다.

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **glibc 관련 주의**: 이 바이너리는 Debian 12에서 빌드되었습니다. 해당 배포판에서 검증되었으며, glibc 2.36 이상의 배포판에서도 동작해야 하지만 그보다 오래된 버전에서는 동작하지 않습니다. 이 경우 소스에서 다시 컴파일하세요.

---

## 시스템 설치 (선택 사항)

애플리케이션을 데스크톱 환경(GNOME, KDE, XFCE…)의 메뉴에 통합하려면:

```bash
# 파일을 /opt로 복사
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# 필요하면 .desktop 파일의 경로를 수정
# Exec=bash /opt/calculateur-masques/lancer.sh

# 애플리케이션 메뉴에 추가
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# 또는
sudo kbuildsycoca6              # KDE Plasma
```

---

## 독립 실행형 실행 파일 컴파일

PyInstaller로 Python 의존성이 없는 바이너리를 생성할 수 있습니다.

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

실행 파일은 `./dist/CalculateurMasquesIPv4`에 생성됩니다. `--add-data` 옵션은 창 아이콘(실행 시 Pillow가 있으면 Pillow로, 없으면 Tk로 불러옴)과 「정보」 창의 배너를 포함시킵니다. Pillow는 선택 사항입니다(`pip3 install pillow`).

> **참고:** Ubuntu에서 컴파일한 Linux 바이너리는 glibc 버전 차이로 인해 Arch나 Fedora에서 반드시 동작하는 것은 아닙니다. 대상 배포판에서 컴파일하거나 대상 배포판용 Docker 이미지를 사용하세요.

---

## 파일 구조

```
CalculateurMasques/            (Linux 브랜치)
├── calculateur_masques.py      # 메인 애플리케이션 (Linux용으로 조정됨)
├── translations.py             # 15개 언어 사전 (main 브랜치와 동일)
├── icon.png                    # 창 / 메뉴 아이콘 (512 px)
├── banner.png                  # 정보 창의 배너 (600 x 200)
├── lancer.sh                   # 의존성 확인 기능이 있는 실행 스크립트
├── calculateur-masques.desktop # 데스크톱 환경용 메뉴 항목
├── INSTALLER.md                # 상세 설치 안내 (프랑스어)
├── LICENSE                     # MIT 라이선스
├── README-LINUX.md             # 이 가이드 (프랑스어)
└── docs/README-LINUX.<code>.md # 번역본: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Windows 버전과의 차이

| 항목 | Windows | Linux |
|---|---|---|
| 글꼴 | Segoe UI / Consolas | 자동 감지 (Noto Sans, DejaVu Sans, Liberation…) |
| 마우스 휠 | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| CSV 내보내기 | BOM이 있는 UTF-8 (Excel) | BOM이 없는 UTF-8 (표준) |
| 실행 파일 | 독립 실행형 `.exe` | PyInstaller로 만든 ELF 바이너리 (배포판에 따라 다름) |
| 데스크톱 통합 | Windows 바로 가기 | `.desktop` 파일 (XDG) |

---

## 처리되는 특수 사례

| 접두사 | 동작 |
|---|---|
| `/31` | 지점 간(point-to-point) 링크(RFC 3021) — 주소 2개, 일반적인 브로드캐스트 없음 |
| `/32` | 단일 호스트 — 첫 번째 = 마지막 = 네트워크 주소 |
| `/0` | 범용 네트워크 `0.0.0.0` |

---

## 라이선스

MIT 라이선스 — `LICENSE` 파일을 참조하세요.
