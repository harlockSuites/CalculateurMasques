# Máy Tính Mặt Nạ Mạng Con IPv4 — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · **Tiếng Việt** · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **Nhánh `Linux`**: phiên bản Linux của phần mềm. Nhánh `main` chỉ dành cho bản phân phối Windows; không hợp nhất nhánh này vào nhánh kia.

Tiện ích đồ họa để tính mặt nạ mạng con IPv4, hỗ trợ 15 ngôn ngữ, chia mạng con, lưu lịch sử và xuất ra tệp.

Kho mã: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## Tổng quan

Ứng dụng được tổ chức thành ba tab:

| Tab | Nội dung |
|---|---|
| **Máy tính** | Tính toán chính, chuyển đổi IP, kiểm tra thuộc mạng |
| **Phân chia** | Tự động chia một mạng thành các mạng con |
| **Lịch sử** | Ghi lại các phép tính, xuất CSV / TXT |

---

## Tính năng

### Tab Máy tính
- Nhập bằng **tiền tố CIDR** (`/24`) hoặc **mặt nạ thập phân** (`255.255.255.0`) — hai giá trị tự động đồng bộ với nhau
- Các kết quả hiển thị:
  - Địa chỉ mạng
  - Mặt nạ mạng con
  - Ký hiệu CIDR
  - Mặt nạ đại diện (wildcard)
  - Địa chỉ máy chủ đầu tiên / cuối cùng
  - Địa chỉ broadcast
  - Số máy chủ khả dụng
  - Phạm vi mạng đầy đủ
- **Chuyển đổi** địa chỉ IP đã nhập: thập phân có dấu chấm, nhị phân, thập lục phân, thập phân 32 bit
- **Kiểm tra thuộc mạng**: kiểm tra xem một IP cho trước có thuộc mạng đã tính hay không
- **Nhấp chuột phải** vào bất kỳ giá trị nào để sao chép vào bộ nhớ tạm
- **Mặt nạ đảo** (wildcard, ví dụ `0.0.0.255`) bị từ chối kèm một thông báo đã được dịch: hãy nhập mặt nạ mạng con (`255.255.255.0`)
- **Con lăn chuột**: cuộn trang, bất kể con trỏ đang nằm trên thành phần nào (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Nhấn phím **Enter** để thực hiện phép tính

### Tab Phân chia
- Chia một mạng thành N mạng con bằng nhau
- Hoặc tìm CIDR nhỏ nhất đủ chứa N máy chủ
- Bảng các mạng con gồm mạng, mặt nạ, máy chủ, broadcast
- Giới hạn tối đa 65 536 mạng con cho mỗi lần phân chia (vượt quá sẽ hiển thị một thông báo thay vì làm treo giao diện)
- Nhấp chuột phải vào một ô để sao chép giá trị

### Tab Lịch sử
- Mỗi phép tính được tự động lưu lại, kèm thời gian thực hiện (được giữ khi hiển thị và khi xuất)
- Nhấp đúp vào một mục để tải lại vào máy tính
- Xuất **CSV** (mã hóa UTF-8)
- Xuất **TXT** (định dạng dễ đọc)

### Bộ chọn ngôn ngữ
15 ngôn ngữ có sẵn, truy cập từ phần đầu của ứng dụng:

| Nhóm | Ngôn ngữ |
|---|---|
| Ngữ hệ Rôman | Français · English · Español · Português · Italiano |
| Trung/Đông Âu | Српски · Polski · Magyar · Русский |
| Nam/Đông Á | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

Việc đổi ngôn ngữ diễn ra ngay lập tức, không cần khởi động lại.

### Nút Giới thiệu
Bên cạnh bộ chọn ngôn ngữ, nút này mở một cửa sổ có biểu ngữ và thông báo “Phần mềm tiện ích ngoại tuyến này miễn phí và mã nguồn mở.”, được dịch sang cả 15 ngôn ngữ. Nhấn phím Esc hoặc nút Đóng để đóng cửa sổ.

### Tiếng Hàn và phông chữ
Tiếng Hàn xuất hiện trong danh sách dưới tên **Korean** (bằng tiếng Anh, vì “한국어” sẽ hiện thành các ô vuông nếu không có phông chữ tiếng Hàn). Nếu hệ thống không có phông nào, việc chọn ngôn ngữ này sẽ mở một hộp thoại **bằng tiếng Anh** (“Font needed”) giải thích nhu cầu này và đề xuất:
- một **lệnh để sao chép** vào terminal (cài đặt cho mọi người dùng): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — chỉ lệnh Debian/Ubuntu đã được kiểm chứng;
- một nút **Install automatically**: tải Noto Sans KR (4,6 MB, giấy phép SIL OFL, phiên bản cố định, đã kiểm tra tổng SHA-256) vào `~/.local/share/fonts/calculateur-masques/`, không cần quyền quản trị. Đây là trường hợp duy nhất phần mềm dùng đến mạng; thời gian còn lại nó vẫn hoạt động ngoại tuyến;
- một nút **Restart now**: khởi động lại phần mềm (tùy chọn `--lang ko`) để nó nhận ra phông chữ; ngôn ngữ đổi khi khởi động lại. Ngôn ngữ không được ghi nhớ giữa các phiên làm việc.

Để gỡ phông chữ đã tải: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Các ngôn ngữ khác dùng chữ viết không phải Latin (Hindi, tiếng Nhật, tiếng Trung…) không có hộp thoại như vậy: nếu thiếu phông chữ phù hợp, có thể hiện các ô vuông. Với tiếng Nhật và tiếng Trung: `sudo apt install fonts-noto-cjk`.

---

## Yêu cầu

Python 3.8+ với module `tkinter`.

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

Không cần phụ thuộc nào khác.

---

## Khởi chạy

### Cách nhanh

```bash
chmod +x lancer.sh
./lancer.sh
```

Script tự động kiểm tra sự có mặt của Python và tkinter, và hiển thị một thông báo lỗi rõ ràng nếu thiếu một phụ thuộc.

### Qua Python trực tiếp

```bash
python3 calculateur_masques.py
```

### Qua tệp thực thi độc lập

Một tệp thực thi độc lập (PyInstaller) được biên dịch chỉ bằng một lệnh (xem « Biên dịch tệp thực thi độc lập » bên dưới). Một bản biên dịch sẵn được phát hành (ở dạng bản xem trước) trong [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) của kho mã, dưới nhãn `Linux-v*`; nó được xây dựng trên Debian 12 (glibc 2.36, Python 3.11, x86-64):

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **Lưu ý về glibc**: tệp nhị phân này được xây dựng trên Debian 12. Nó đã được kiểm chứng trên bản phân phối đó; nó cũng nên chạy được trên các bản phân phối có glibc 2.36 hoặc mới hơn, nhưng không chạy được trên bản cũ hơn. Trong trường hợp đó, hãy biên dịch lại từ mã nguồn.

---

## Cài đặt vào hệ thống (tùy chọn)

Để tích hợp ứng dụng vào menu của môi trường desktop (GNOME, KDE, XFCE…):

```bash
# Sao chép các tệp vào /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Sửa đường dẫn trong tệp .desktop nếu cần
# Exec=bash /opt/calculateur-masques/lancer.sh

# Thêm vào menu ứng dụng
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# hoặc
sudo kbuildsycoca6              # KDE Plasma
```

---

## Biên dịch tệp thực thi độc lập

PyInstaller cho phép tạo ra một tệp nhị phân không phụ thuộc vào Python:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

Tệp thực thi sẽ được tạo trong `./dist/CalculateurMasquesIPv4`. Các tùy chọn `--add-data` nhúng biểu tượng cửa sổ (được nạp khi chạy qua Pillow nếu có, nếu không thì qua Tk) và biểu ngữ của cửa sổ Giới thiệu; Pillow là tùy chọn (`pip3 install pillow`).

> **Lưu ý:** một tệp nhị phân Linux biên dịch trên Ubuntu không nhất thiết chạy được trên Arch hay Fedora do khác biệt về phiên bản glibc. Hãy biên dịch trên bản phân phối đích hoặc dùng một image Docker của bản phân phối nhắm tới.

---

## Cấu trúc tệp

```
CalculateurMasques/            (nhánh Linux)
├── calculateur_masques.py      # Ứng dụng chính (đã điều chỉnh cho Linux)
├── translations.py             # Từ điển của 15 ngôn ngữ (giống nhánh main)
├── icon.png                    # Biểu tượng cửa sổ / menu (512 px)
├── banner.png                  # Biểu ngữ của cửa sổ Giới thiệu (600 x 200)
├── lancer.sh                   # Script khởi chạy có kiểm tra phụ thuộc
├── calculateur-masques.desktop # Mục menu cho các môi trường desktop
├── INSTALLER.md                # Hướng dẫn cài đặt chi tiết (bằng tiếng Pháp)
├── LICENSE                     # Giấy phép MIT
├── README-LINUX.md             # Hướng dẫn này, bằng tiếng Pháp
└── docs/README-LINUX.<code>.md # Các bản dịch: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Khác biệt so với phiên bản Windows

| Khía cạnh | Windows | Linux |
|---|---|---|
| Phông chữ | Segoe UI / Consolas | Tự động phát hiện (Noto Sans, DejaVu Sans, Liberation…) |
| Con lăn chuột | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Xuất CSV | UTF-8 có BOM (Excel) | UTF-8 không BOM (chuẩn) |
| Tệp thực thi | `.exe` độc lập | Tệp nhị phân ELF qua PyInstaller (tùy bản phân phối) |
| Tích hợp desktop | Lối tắt Windows | Tệp `.desktop` (XDG) |

---

## Các trường hợp đặc biệt được xử lý

| Tiền tố | Hành vi |
|---|---|
| `/31` | Liên kết điểm-điểm (RFC 3021) — 2 địa chỉ, không có broadcast theo quy ước |
| `/32` | Một máy chủ duy nhất — đầu tiên = cuối cùng = địa chỉ mạng |
| `/0` | Mạng toàn cục `0.0.0.0` |

---

## Giấy phép

Giấy phép MIT — xem tệp `LICENSE`.
