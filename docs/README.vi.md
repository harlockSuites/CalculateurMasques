# Máy Tính Mặt Nạ Mạng Con IPv4

[Français](../README.md) · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · **Tiếng Việt** · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

Tiện ích đồ họa **ngoại tuyến**, miễn phí và mã nguồn mở, dùng để tính mặt nạ mạng con IPv4, chia một mạng thành các mạng con, lưu lịch sử và xuất ra tệp. Giao diện hỗ trợ **15 ngôn ngữ**.

Kho mã: <https://github.com/harlockSuites/CalculateurMasques>

> **Linux:** có phiên bản dành riêng cho Linux trên [nhánh `Linux`](https://github.com/harlockSuites/CalculateurMasques/tree/Linux). Tệp thực thi biên dịch sẵn (bản phát hành thử nghiệm, Debian 12, x86-64) được đăng trong [bản phát hành `Linux-v1.0`](https://github.com/harlockSuites/CalculateurMasques/releases/tag/Linux-v1.0). README này mô tả phiên bản Windows.

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
- Nhấn phím **Enter** để thực hiện phép tính

### Tab Phân chia
- Chia một mạng thành N mạng con bằng nhau
- Hoặc tìm CIDR nhỏ nhất đủ chứa N máy chủ
- Bảng các mạng con gồm mạng, mặt nạ, máy chủ, broadcast (giới hạn tối đa 65 536 dòng, vượt quá sẽ hiển thị một thông báo bằng ngôn ngữ đã chọn)
- Nhấp chuột phải vào một ô để sao chép giá trị

### Tab Lịch sử
- Mỗi phép tính được tự động lưu lại, kèm thời gian thực hiện
- Nhấp đúp vào một mục để tải lại vào máy tính
- Xuất **CSV** (mã hóa UTF-8 có BOM, tương thích với Excel)
- Xuất **TXT** (định dạng dễ đọc)

### Bộ chọn ngôn ngữ
15 ngôn ngữ có sẵn, truy cập từ phần đầu của ứng dụng:

| Nhóm | Ngôn ngữ |
|---|---|
| Ngữ hệ Rôman | Français · English · Español · Português · Italiano |
| Trung/Đông Âu | Српски · Polski · Magyar · Русский |
| Nam/Đông Á | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

Việc đổi ngôn ngữ diễn ra ngay lập tức, không cần khởi động lại.

### Nút Giới thiệu
Bên cạnh bộ chọn ngôn ngữ, nút **Giới thiệu** mở một cửa sổ có biểu ngữ của tác giả (`banner.png`) và thông báo “Phần mềm tiện ích ngoại tuyến này miễn phí và mã nguồn mở.”, được dịch sang cả 15 ngôn ngữ.

---

## Yêu cầu

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- Module `tkinter` (đã có sẵn trong bản cài đặt Python tiêu chuẩn)

Không cần phụ thuộc bên ngoài để chạy script. [Pillow](https://pypi.org/project/pillow/) là tùy chọn: nó chỉ dùng để hiển thị biểu tượng cửa sổ ở độ phân giải đầy đủ.

---

## Khởi chạy

### Qua Python
```
python calculateur_masques.py
```

### Qua tệp thực thi đã biên dịch
Nhấp đúp vào `dist\CalculateurMasquesIPv4.exe`. Tệp thực thi này độc lập, không cần cài đặt. Nó không được đưa vào quản lý phiên bản trong kho mã này: hãy tự biên dịch (xem bên dưới).

---

## Biên dịch tệp thực thi

Kho mã cung cấp một tệp spec PyInstaller (`CalculateurMasquesIPv4.spec`) nhúng sẵn biểu tượng, biểu ngữ và các bản dịch. Từ thư mục này:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

Tệp thực thi được tạo trong thư mục `dist\`. Biểu tượng (`icon.ico`) được tích hợp vào tệp exe.

---

## Cấu trúc tệp

```
CalculateurMasques\
├── calculateur_masques.py        # Ứng dụng chính
├── translations.py               # Từ điển của 15 ngôn ngữ
├── CalculateurMasquesIPv4.spec   # Đặc tả PyInstaller
├── icon.ico                      # Biểu tượng của exe (Windows)
├── icon.png                      # Biểu tượng cửa sổ (512 px)
├── banner.png                    # Biểu ngữ của cửa sổ Giới thiệu (600 px)
├── LICENSE                       # Giấy phép MIT
└── README.md
```

---

## Các trường hợp đặc biệt được xử lý

| Tiền tố | Hành vi |
|---|---|
| `/31` | Liên kết điểm-điểm (RFC 3021) — 2 địa chỉ, không có broadcast theo quy ước |
| `/32` | Một máy chủ duy nhất — đầu tiên = cuối cùng = địa chỉ mạng |
| `/0` | Mạng toàn cục `0.0.0.0` |

---

## Phần mềm diệt virus và báo động giả

Tính đến ngày 25 tháng 10 năm 2026, VirusTotal gắn cờ tệp thực thi `CalculateurMasquesIPv4.exe` của phiên bản 1.0 với **5 phát hiện trên 69 công cụ quét**: Arctic Wolf, Bkav Pro, Microsoft, SecureAge và Zillya. Chúng tôi cho rằng đây là **báo động giả**, vốn thường gặp với một chương trình Python được đóng gói bằng PyInstaller, còn mới và chưa được ký số. Chương trình không chứa bất kỳ mã mạng nào (chỉ dùng `tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys` và `os`, cùng với Pillow cho biểu tượng cửa sổ) và toàn bộ mã nguồn được công khai trong kho mã này.

Các báo cáo báo động giả đã được gửi vào ngày 25 tháng 10 năm 2026 tới cả năm nhà phát hành liên quan. Phần này sẽ được cập nhật cùng với phản hồi của họ.

Để kiểm tra tệp bạn đã tải về:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- Báo cáo VirusTotal: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- Bạn cũng có thể tự biên dịch tệp thực thi từ mã nguồn (xem « Biên dịch tệp thực thi »).

---

## Giấy phép

Phân phối theo giấy phép [MIT](../LICENSE) — © 2026 Harlock S.
