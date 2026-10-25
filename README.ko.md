# IPv4 서브넷 마스크 계산기

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · **한국어** · [日本語](README.ja.md) · [Filipino](README.fil.md)

IPv4 서브넷 마스크를 계산하고, 네트워크를 서브넷으로 분할하고, 기록을 보관하고 내보낼 수 있는 **오프라인**, 무료, 오픈 소스 그래픽 유틸리티입니다. 인터페이스는 **15개 언어**를 지원합니다.

저장소: <https://github.com/harlockSuites/CalculateurMasques>

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
- **Enter** 키로 계산 실행

### 서브넷 분할 탭
- 네트워크를 N개의 동일한 서브넷으로 분할
- 또는 N개의 호스트를 수용할 수 있는 최소 CIDR 검색
- 네트워크, 마스크, 호스트, 브로드캐스트가 표시되는 서브넷 표(최대 65,536행이며, 초과하면 선택한 언어로 메시지가 표시됨)
- 셀을 오른쪽 클릭하면 값 복사

### 기록 탭
- 모든 계산이 계산 시각과 함께 자동으로 저장됩니다
- 항목을 더블 클릭하면 계산기에 다시 불러옵니다
- **CSV** 내보내기(BOM이 있는 UTF-8 인코딩, Excel 호환)
- **TXT** 내보내기(읽기 쉬운 형식)

### 언어 선택기
애플리케이션 상단의 헤더에서 15개 언어를 선택할 수 있습니다.

| 그룹 | 언어 |
|---|---|
| 로망스어군 | Français · English · Español · Português · Italiano |
| 중부/동유럽 | Српски · Polski · Magyar · Русский |
| 남아시아/동아시아 | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

언어 변경은 재시작 없이 즉시 적용됩니다.

### 정보 버튼
언어 선택기 옆의 **정보** 버튼을 누르면 작성자의 배너(`banner.png`)와 "이 오프라인 유틸리티 소프트웨어는 무료이며 오픈 소스입니다."라는 메시지가 담긴 창이 열리며, 이 메시지는 15개 언어로 번역되어 있습니다.

---

## 요구 사항

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- `tkinter` 모듈(Python 표준 설치에 포함)

스크립트를 실행하는 데 외부 의존성은 필요하지 않습니다. [Pillow](https://pypi.org/project/pillow/)는 선택 사항이며, 창 아이콘을 전체 해상도로 표시하는 용도로만 사용됩니다.

---

## 실행

### Python으로 실행
```
python calculateur_masques.py
```

### 컴파일된 실행 파일로 실행
`dist\CalculateurMasquesIPv4.exe`를 더블 클릭하세요. 실행 파일은 독립 실행형이며 설치가 필요하지 않습니다. 이 저장소에는 버전 관리되지 않으므로 직접 컴파일해야 합니다(아래 참조).

---

## 실행 파일 컴파일

저장소에는 아이콘, 배너, 번역을 포함하는 PyInstaller spec(`CalculateurMasquesIPv4.spec`)이 제공됩니다. 이 폴더에서 다음을 실행하세요.

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

실행 파일은 `dist\` 폴더에 생성됩니다. 아이콘(`icon.ico`)은 exe에 포함됩니다.

---

## 파일 구조

```
CalculateurMasques\
├── calculateur_masques.py        # 메인 애플리케이션
├── translations.py               # 15개 언어 사전
├── CalculateurMasquesIPv4.spec   # PyInstaller 사양
├── icon.ico                      # exe 아이콘 (Windows)
├── icon.png                      # 창 아이콘 (512 px)
├── banner.png                    # 정보 창의 배너 (600 px)
├── LICENSE                       # MIT 라이선스
└── README.md
```

---

## 처리되는 특수 사례

| 접두사 | 동작 |
|---|---|
| `/31` | 지점 간(point-to-point) 링크(RFC 3021) — 주소 2개, 일반적인 브로드캐스트 없음 |
| `/32` | 단일 호스트 — 첫 번째 = 마지막 = 네트워크 주소 |
| `/0` | 범용 네트워크 `0.0.0.0` |

---

## 백신 프로그램과 오탐

2026년 10월 25일 기준, VirusTotal은 버전 1.0의 실행 파일 `CalculateurMasquesIPv4.exe`에 대해 **69개 엔진 중 5개 탐지**를 보고하고 있습니다(Arctic Wolf, Bkav Pro, Microsoft, SecureAge, Zillya). 이는 **오탐(false positive)**으로 판단됩니다. PyInstaller로 패키징되고, 최근에 만들어졌으며, 디지털 서명이 없는 Python 프로그램에서는 흔히 발생하는 일입니다. 이 프로그램에는 네트워크 관련 코드가 전혀 없으며(`tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys`, `os`만 사용하고, 창 아이콘용으로 Pillow를 사용합니다), 전체 소스 코드는 이 저장소에 공개되어 있습니다.

2026년 10월 25일에 해당 업체 다섯 곳 모두에 오탐 신고를 보냈습니다. 이 섹션은 업체의 답변에 따라 갱신될 예정입니다.

다운로드한 파일을 확인하려면:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- VirusTotal 보고서: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- 소스 코드에서 직접 실행 파일을 컴파일할 수도 있습니다(「실행 파일 컴파일」 참조).

---

## 라이선스

[MIT](LICENSE) 라이선스로 배포됩니다 — © 2026 Harlock S.
