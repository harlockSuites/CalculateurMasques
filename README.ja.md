# IPv4 サブネットマスク計算機 — Linux

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · **日本語** · [Filipino](README.fil.md)

> **`Linux` ブランチ**：ソフトウェアの Linux 版です。`main` ブランチは Windows 向け配布専用です。どちらか一方をもう一方にマージしないでください。

IPv4 サブネットマスクを計算するグラフィカルユーティリティです。15 言語に対応し、サブネット分割、履歴の保存、エクスポートができます。

リポジトリ：<https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## 概要

アプリケーションは 3 つのタブで構成されています。

| タブ | 内容 |
|---|---|
| **計算機** | メインの計算、IP アドレスの変換、所属確認 |
| **サブネット分割** | ネットワークのサブネットへの自動分割 |
| **履歴** | 計算の記録、CSV / TXT へのエクスポート |

---

## 機能

### 計算機タブ
- **CIDR プレフィックス**（`/24`）または**ドット付き 10 進マスク**（`255.255.255.0`）で入力できます。両者は自動的に同期されます
- 表示される結果：
  - ネットワークアドレス
  - サブネットマスク
  - CIDR表記
  - ワイルドカードマスク
  - 最初のホストアドレス / 最後のホストアドレス
  - ブロードキャストアドレス
  - 使用可能なホスト数
  - ネットワーク全範囲
- 入力した IP アドレスの**変換**：ドット付き10進表記、2進数、16進数、10進数（32ビット整数）
- **所属確認**：指定した IP が計算されたネットワークに属しているかをテストします
- 任意の値を**右クリック**してクリップボードにコピーできます
- **逆マスク**（ワイルドカード。例：`0.0.0.255`）は、選択した言語のメッセージで拒否されます：「ワイルドカード（逆）マスクは使用できません。サブネットマスクを入力してください。例: 255.255.255.0」
- **マウスホイール**：カーソルがどの要素の上にあっても、ページをスクロールします（X11：`Button-4`/`Button-5`、Wayland：`MouseWheel`）
- **Enter** キーで計算を実行します

### サブネット分割タブ
- ネットワークを N 個の同じ大きさのサブネットに分割します
- または、N 台のホストを収容できる最小の CIDR を求めます
- ネットワーク、マスク、ホスト数、ブロードキャストを示すサブネットの表
- 1 回の分割につき最大 65,536 サブネットまで（それを超える場合は、インターフェースを固まらせる代わりにメッセージが表示されます）
- セルを右クリックすると値をコピーできます

### 履歴タブ
- すべての計算が、計算時刻とともに自動的に記録されます（時刻は表示にもエクスポートにも保持されます）
- エントリをダブルクリックすると、計算機に再読み込みされます
- **CSV** 出力（UTF-8）
- **TXT** 出力（読みやすい形式）

### 言語セレクター
アプリケーションのヘッダーから、15 言語を選択できます。

| グループ | 言語 |
|---|---|
| ロマンス諸語 | Français · English · Español · Português · Italiano |
| 中欧・東欧 | Српски · Polski · Magyar · Русский |
| 南アジア・東アジア | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

言語の切り替えは即座に反映され、再起動は不要です。

### このソフトについてボタン
言語セレクターの横にある**このソフトについて**ボタンを押すと、バナーと、15 言語に翻訳されたメッセージ「このオフラインのユーティリティソフトは無料で、オープンソースです。」を表示するウィンドウが開きます。Esc キーまたは**閉じる**ボタンで閉じます。

### 韓国語とフォント
韓国語は、リスト内では **Korean** という名前で表示されます（英語表記なのは、韓国語フォントがないと「한국어」が四角で表示されてしまうためです）。システムに韓国語フォントが 1 つもない場合、この言語を選ぶと**英語の**ダイアログ（「Font needed」）が開き、必要な理由を説明したうえで、次の選択肢を提示します：
- ターミナルに**コピーして実行するコマンド**（すべてのユーザー向けのインストール）：`sudo apt install fonts-noto-cjk`（Debian/Ubuntu）、`sudo dnf install google-noto-sans-cjk-fonts`（Fedora）、`sudo pacman -S noto-fonts-cjk`（Arch）— 動作を確認したのは Debian/Ubuntu のコマンドだけです。
- **Install automatically** ボタン：Noto Sans KR（4.6 MB、SIL OFL ライセンス、バージョン固定、SHA-256 チェックサムを検証）を `~/.local/share/fonts/calculateur-masques/` にダウンロードします。管理者権限は不要です。ソフトウェアがネットワークを使うのはこの場合だけで、それ以外のときはオフラインのままです。
- **Restart now** ボタン：ソフトウェアを再起動し（`--lang ko` オプション）、フォントを認識させます。言語は再起動時に切り替わります。言語設定は次回以降のセッションには引き継がれません。

ダウンロードしたフォントを削除するには：`rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`。

> 非ラテン文字の他の言語（ヒンディー語、日本語、中国語など）には、このようなダイアログはありません。適切なフォントがないと、四角が表示されることがあります。日本語と中国語の場合：`sudo apt install fonts-noto-cjk`。

---

## 動作環境

Python 3.8+ と `tkinter` モジュール。

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

その他の依存パッケージは不要です。

---

## 起動方法

### 簡単な方法

```bash
chmod +x lancer.sh
./lancer.sh
```

スクリプトは Python と tkinter の有無を自動的に確認し、依存パッケージが不足している場合は分かりやすいエラーメッセージを表示します。

### Python から直接起動

```bash
python3 calculateur_masques.py
```

### 単体の実行ファイルから起動

単体の実行ファイル（PyInstaller）は、1 つのコマンドでビルドできます（後述の「単体の実行ファイルのビルド」を参照）。ビルド済みのバージョンは、リポジトリの [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) に、`Linux-v*` というタグでプレリリースとして公開されています。Debian 12（glibc 2.36、Python 3.11、x86-64）上でビルドされています：

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **glibc に関する注意**：このバイナリは Debian 12 上でビルドされています。このディストリビューションでは動作を確認済みです。glibc 2.36 以降のディストリビューションでも動作するはずですが、それより古いものでは動作しません。その場合は、ソースから再ビルドしてください。

---

## システムへのインストール（任意）

アプリケーションをデスクトップ環境（GNOME、KDE、XFCE など）のメニューに統合するには：

```bash
# ファイルを /opt にコピーする
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# 必要に応じて .desktop ファイル内のパスを変更する
# Exec=bash /opt/calculateur-masques/lancer.sh

# アプリケーションメニューに追加する
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# または
sudo kbuildsycoca6              # KDE Plasma
```

---

## 単体の実行ファイルのビルド

PyInstaller を使うと、Python に依存しないバイナリを生成できます：

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

実行ファイルは `./dist/CalculateurMasquesIPv4` に生成されます。`--add-data` オプションは、ウィンドウアイコン（実行時に Pillow があれば Pillow で、なければ Tk で読み込まれます）と、このソフトについてウィンドウのバナーを組み込みます。Pillow は必須ではありません（`pip3 install pillow`）。

> **注意：** Ubuntu でコンパイルした Linux バイナリは、glibc のバージョンの違いにより、Arch や Fedora では動作するとは限りません。対象のディストリビューション上でコンパイルするか、対象ディストリビューションの Docker イメージを使用してください。

---

## ファイル構成

```
CalculateurMasques/            (Linux ブランチ)
├── calculateur_masques.py      # メインアプリケーション（Linux 向けに調整済み）
├── translations.py             # 15 言語の辞書（main ブランチと同一）
├── icon.png                    # ウィンドウ / メニューのアイコン（512 px）
├── banner.png                  # このソフトについてウィンドウのバナー（600 x 200）
├── lancer.sh                   # 依存パッケージを確認する起動スクリプト
├── calculateur-masques.desktop # デスクトップ環境向けのメニューエントリ
├── INSTALLER.md                # 詳細なインストール手順（フランス語）
├── LICENSE                     # MIT ライセンス
├── README.md                   # このガイド（フランス語）
└── README.<code>.md            # 翻訳：en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Windows 版との違い

| 項目 | Windows | Linux |
|---|---|---|
| フォント | Segoe UI / Consolas | 自動検出（Noto Sans、DejaVu Sans、Liberation など） |
| マウスホイール | `MouseWheel`（WinAPI） | `Button-4` / `Button-5`（X11）+ `MouseWheel`（Wayland） |
| CSV 出力 | BOM 付き UTF-8（Excel 対応） | BOM なし UTF-8（標準） |
| 実行ファイル | 単体の `.exe` | PyInstaller による ELF バイナリ（ディストリビューションに依存） |
| デスクトップ統合 | Windows のショートカット | `.desktop` ファイル（XDG） |

---

## 特殊なケースへの対応

| プレフィックス | 動作 |
|---|---|
| `/31` | ポイントツーポイントリンク（RFC 3021）— 2 アドレス、通常のブロードキャストなし |
| `/32` | 単一ホスト — 最初 = 最後 = ネットワークアドレス |
| `/0` | ユニバーサルネットワーク `0.0.0.0` |

---

## ライセンス

MIT ライセンス — `LICENSE` ファイルを参照してください。
