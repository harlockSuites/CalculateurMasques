# IPv4 子网掩码计算器 — Linux

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · **中文** · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

> **`Linux` 分支**：本软件的 Linux 版本。`main` 分支专用于 Windows 发行版；请勿将两者互相合并。

用于计算 IPv4 子网掩码的图形化实用工具，支持 15 种语言、子网划分、历史记录和导出。

代码仓库：<https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## 概览

应用程序由三个选项卡组成：

| 选项卡 | 内容 |
|---|---|
| **计算器** | 主要计算、IP 转换、归属验证 |
| **子网划分** | 将网络自动划分为子网 |
| **历史记录** | 记录计算过程，导出 CSV / TXT |

---

## 功能

### 计算器选项卡
- 通过 **CIDR 前缀**（`/24`）或**点分十进制掩码**（`255.255.255.0`）输入——两者自动同步
- 显示的结果：
  - 网络地址
  - 子网掩码
  - CIDR 表示法
  - 通配符掩码（wildcard）
  - 第一个 / 最后一个主机地址
  - 广播地址
  - 可用主机数量
  - 完整网络范围
- 对所输入 IP 地址的**转换**：点分十进制、二进制、十六进制、32 位十进制
- **归属验证**：测试给定的 IP 是否属于所计算的网络
- 在任意值上**单击右键**，即可将其复制到剪贴板
- **反向掩码**（wildcard，例如 `0.0.0.255`）会被拒绝，并显示已翻译的提示信息：请输入子网掩码（`255.255.255.0`）
- **鼠标滚轮**：无论鼠标悬停在哪个元素上，都会滚动页面（X11：`Button-4`/`Button-5`；Wayland：`MouseWheel`）
- 按**回车**键即可触发计算

### 子网划分选项卡
- 将网络划分为 N 个相等的子网
- 或查找能容纳 N 台主机的最小 CIDR
- 子网表格包含网络、掩码、主机数、广播地址
- 每次划分最多 65 536 个子网（超出时会显示提示信息，而不是让界面卡死）
- 在单元格上单击右键即可复制该值

### 历史记录选项卡
- 每次计算都会自动保存，并记录计算时间（在显示和导出时均会保留）
- 双击某条记录，可将其重新加载到计算器中
- 导出 **CSV**（UTF-8 编码）
- 导出 **TXT**（易读格式）

### 语言选择器
应用程序标题栏提供 15 种语言可选：

| 分组 | 语言 |
|---|---|
| 罗曼语族 | Français · English · Español · Português · Italiano |
| 中欧/东欧 | Српски · Polski · Magyar · Русский |
| 南亚/东亚 | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

语言切换即时生效，无需重启。

### “关于”按钮
在语言选择器旁边，**关于**按钮会打开一个窗口，其中显示横幅图片以及消息“这款离线实用软件免费且开源。”，该消息已翻译为 15 种语言。按 Esc 键或点击**关闭**按钮即可将其关闭。

### 韩语与字体
韩语在列表中显示为 **Korean**（使用英文，因为在没有韩文字体的情况下，“한국어”会显示为方框）。如果系统中没有任何韩文字体，选择该语言会打开一个**英文**对话框（“Font needed”），说明所需字体并提供以下选项：
- 一条**可复制的命令**，在终端中运行（为所有用户安装）：`sudo apt install fonts-noto-cjk`（Debian/Ubuntu）、`sudo dnf install google-noto-sans-cjk-fonts`（Fedora）、`sudo pacman -S noto-fonts-cjk`（Arch）——仅 Debian/Ubuntu 的命令已经过验证；
- **Install automatically** 按钮：下载 Noto Sans KR（4.6 MB，SIL OFL 许可证，固定版本，已校验 SHA-256）到 `~/.local/share/fonts/calculateur-masques/`，无需管理员权限。这是软件唯一会使用网络的情况；其余时间均保持离线；
- **Restart now** 按钮：重新启动软件（选项 `--lang ko`），使其能够识别该字体；语言会在重启后切换。语言设置不会在会话之间保留。

如需删除已下载的字体：`rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`。

> 其他使用非拉丁文字的语言（印地语、日语、中文等）没有此类对话框：如果没有合适的字体，可能会显示方框。对于日语和中文：`sudo apt install fonts-noto-cjk`。

---

## 环境要求

Python 3.8+ 以及 `tkinter` 模块。

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

无需任何其他依赖。

---

## 运行

### 快速方法

```bash
chmod +x lancer.sh
./lancer.sh
```

该脚本会自动检查是否存在 Python 和 tkinter，如果缺少依赖，则会显示明确的错误信息。

### 直接通过 Python

```bash
python3 calculateur_masques.py
```

### 通过独立可执行文件

只需一条命令即可编译出独立可执行文件（PyInstaller）（参见下文“编译独立可执行文件”）。预编译版本（预发布版）发布在仓库的 [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) 中，标签为 `Linux-v*`；它基于 Debian 12（glibc 2.36、Python 3.11、x86-64）构建：

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **glibc 限制**：该二进制文件基于 Debian 12 构建。已在此发行版上验证；它也应能在 glibc 2.36 或更新版本的发行版上运行，但无法在更旧的版本上运行。遇到这种情况时，请从源代码重新编译。

---

## 系统安装（可选）

将应用程序集成到桌面环境（GNOME、KDE、XFCE……）的菜单中：

```bash
# 将文件复制到 /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# 如有需要，修改 .desktop 文件中的路径
# Exec=bash /opt/calculateur-masques/lancer.sh

# 添加到应用程序菜单
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# 或
sudo kbuildsycoca6              # KDE Plasma
```

---

## 编译独立可执行文件

PyInstaller 可以生成不依赖 Python 的二进制文件：

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

可执行文件将生成在 `./dist/CalculateurMasquesIPv4`。`--add-data` 选项会嵌入窗口图标（运行时若存在 Pillow 则通过 Pillow 加载，否则通过 Tk 加载）和“关于”窗口的横幅；Pillow 为可选项（`pip3 install pillow`）。

> **注意：**在 Ubuntu 上编译的 Linux 二进制文件不一定能在 Arch 或 Fedora 上运行，原因是 glibc 版本不同。请在目标发行版上编译，或为目标发行版使用 Docker 镜像。

---

## 文件结构

```
CalculateurMasques/            (Linux 分支)
├── calculateur_masques.py      # 主程序（已适配 Linux）
├── translations.py             # 15 种语言的字典（与 main 分支相同）
├── icon.png                    # 窗口 / 菜单图标（512 px）
├── banner.png                  # “关于”窗口的横幅（600 x 200）
├── lancer.sh                   # 启动脚本，带依赖检查
├── calculateur-masques.desktop # 桌面环境的菜单项
├── INSTALLER.md                # 详细安装说明（法语）
├── LICENSE                     # MIT 许可证
├── README.md                   # 本指南，法语版
└── README.<code>.md            # 翻译版本：en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## 与 Windows 版本的差异

| 方面 | Windows | Linux |
|---|---|---|
| 字体 | Segoe UI / Consolas | 自动检测（Noto Sans、DejaVu Sans、Liberation……） |
| 鼠标滚轮 | `MouseWheel`（WinAPI） | `Button-4` / `Button-5`（X11）+ `MouseWheel`（Wayland） |
| 导出 CSV | 带 BOM 的 UTF-8（Excel） | 不带 BOM 的 UTF-8（标准） |
| 可执行文件 | 独立的 `.exe` | 通过 PyInstaller 生成的 ELF 二进制文件（取决于发行版） |
| 桌面集成 | Windows 快捷方式 | `.desktop` 文件（XDG） |

---

## 已处理的特殊情况

| 前缀 | 行为 |
|---|---|
| `/31` | 点对点链路（RFC 3021）——2 个地址，无常规广播地址 |
| `/32` | 单个主机——第一个 = 最后一个 = 网络地址 |
| `/0` | 通用网络 `0.0.0.0` |

---

## 许可证

基于 MIT 许可证发布 — 参见 `LICENSE` 文件。
