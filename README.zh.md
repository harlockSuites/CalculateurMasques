# IPv4 子网掩码计算器

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · **中文** · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

**离线**、免费、开源的图形化实用工具，用于计算 IPv4 子网掩码、将网络划分为子网、保存历史记录并导出。界面支持 **15 种语言**。

代码仓库：<https://github.com/harlockSuites/CalculateurMasques>

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
- 按**回车**键即可触发计算

### 子网划分选项卡
- 将网络划分为 N 个相等的子网
- 或查找能容纳 N 台主机的最小 CIDR
- 子网表格包含网络、掩码、主机数、广播地址（上限为 65 536 行，超出时以所选语言显示提示信息）
- 在单元格上单击右键即可复制该值

### 历史记录选项卡
- 每次计算都会自动保存，并记录计算时间
- 双击某条记录，可将其重新加载到计算器中
- 导出 **CSV**（UTF-8 编码并带 BOM，兼容 Excel）
- 导出 **TXT**（易读格式）

### 语言选择器
应用程序标题栏提供 15 种语言可选：

| 分组 | 语言 |
|---|---|
| 罗曼语族 | Français · English · Español · Português · Italiano |
| 中欧/东欧 | Српски · Polski · Magyar · Русский |
| 南亚/东亚 | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

语言切换即时生效，无需重启。

### “关于”按钮
在语言选择器旁边，**关于**按钮会打开一个窗口，其中显示作者的横幅图片（`banner.png`）以及消息“这款离线实用软件免费且开源。”，该消息已翻译为 15 种语言。

---

## 环境要求

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- `tkinter` 模块（包含在 Python 标准安装中）

运行脚本无需任何外部依赖。[Pillow](https://pypi.org/project/pillow/) 为可选项：仅用于以完整分辨率显示窗口图标。

---

## 运行

### 通过 Python
```
python calculateur_masques.py
```

### 通过已编译的可执行文件
双击 `dist\CalculateurMasquesIPv4.exe`。该可执行文件可独立运行，无需安装。它未纳入本仓库的版本管理：请自行编译（见下文）。

---

## 编译可执行文件

本仓库提供了一个 PyInstaller 规格文件（`CalculateurMasquesIPv4.spec`），会嵌入图标、横幅和翻译文件。在此文件夹中执行：

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

可执行文件将生成在 `dist\` 文件夹中。图标（`icon.ico`）已嵌入 exe。

---

## 文件结构

```
CalculateurMasques\
├── calculateur_masques.py        # 主程序
├── translations.py               # 15 种语言的字典
├── CalculateurMasquesIPv4.spec   # PyInstaller 规格文件
├── icon.ico                      # exe 图标（Windows）
├── icon.png                      # 窗口图标（512 px）
├── banner.png                    # “关于”窗口的横幅（600 px）
├── LICENSE                       # MIT 许可证
└── README.md
```

---

## 已处理的特殊情况

| 前缀 | 行为 |
|---|---|
| `/31` | 点对点链路（RFC 3021）——2 个地址，无常规广播地址 |
| `/32` | 单个主机——第一个 = 最后一个 = 网络地址 |
| `/0` | 通用网络 `0.0.0.0` |

---

## 许可证

基于 [MIT](LICENSE) 许可证发布 — © 2026 Harlock S.
