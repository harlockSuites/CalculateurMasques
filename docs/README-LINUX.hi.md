# IPv4 सबनेट मास्क कैलकुलेटर — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · **हिन्दी** · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **`Linux` शाखा**: सॉफ़्टवेयर का Linux संस्करण। `main` शाखा केवल Windows वितरण के लिए आरक्षित है; एक को दूसरी में मर्ज न करें।

IPv4 सबनेट मास्क की गणना के लिए ग्राफ़िकल उपयोगिता, जिसमें 15 भाषाओं का समर्थन, सबनेट विभाजन, इतिहास और निर्यात शामिल हैं।

रिपॉज़िटरी: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## अवलोकन

एप्लिकेशन तीन टैब में व्यवस्थित है:

| टैब | विषय-वस्तु |
|---|---|
| **कैलकुलेटर** | मुख्य गणना, IP रूपांतरण, सदस्यता जाँच |
| **विभाजन** | किसी नेटवर्क का सबनेट में स्वचालित विभाजन |
| **इतिहास** | गणनाओं का रिकॉर्ड, CSV / TXT निर्यात |

---

## विशेषताएँ

### कैलकुलेटर टैब
- **CIDR उपसर्ग** (`/24`) या **दशमलव मास्क** (`255.255.255.0`) द्वारा इनपुट — दोनों अपने-आप समन्वित (सिंक) रहते हैं
- प्रदर्शित परिणाम:
  - नेटवर्क पता
  - सबनेट मास्क
  - CIDR संकेतन
  - वाइल्डकार्ड मास्क
  - पहला / अंतिम होस्ट पता
  - ब्रॉडकास्ट पता
  - उपयोगी होस्ट की संख्या
  - पूर्ण नेटवर्क श्रेणी
- दर्ज किए गए IP पते के **रूपांतरण**: बिंदु दशमलव संकेतन, द्विआधारी, हेक्साडेसिमल, दशमलव (32-बिट पूर्णांक)
- **सदस्यता जाँच**: परखता है कि दिया गया IP गणना किए गए नेटवर्क से संबंधित है या नहीं
- किसी भी मान पर **राइट-क्लिक** करके उसे क्लिपबोर्ड पर कॉपी करें
- एक **उलटा मास्क** (वाइल्डकार्ड, उदा. `0.0.0.255`) अनुवादित संदेश के साथ अस्वीकार कर दिया जाता है: सबनेट मास्क दर्ज करें (`255.255.255.0`)
- **माउस व्हील**: कर्सर किसी भी तत्व पर हो, पृष्ठ को स्क्रोल करता है (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- गणना शुरू करने के लिए **Enter** कुंजी

### विभाजन टैब
- किसी नेटवर्क को N समान सबनेट में विभाजित करना
- या N होस्ट समाहित करने के लिए न्यूनतम CIDR खोजना
- सबनेट की तालिका, जिसमें नेटवर्क, मास्क, होस्ट, ब्रॉडकास्ट दिए जाते हैं
- प्रति विभाजन अधिकतम 65 536 सबनेट (इससे अधिक होने पर इंटरफ़ेस को जमने देने के बजाय एक संदेश दिखता है)
- मान कॉपी करने के लिए किसी सेल पर राइट-क्लिक करें

### इतिहास टैब
- प्रत्येक गणना गणना के समय के साथ अपने-आप दर्ज हो जाती है (यह समय प्रदर्शन और निर्यात में बना रहता है)
- किसी प्रविष्टि को कैलकुलेटर में फिर से लोड करने के लिए उस पर डबल-क्लिक करें
- **CSV** निर्यात (UTF-8 एन्कोडिंग)
- **TXT** निर्यात (पठनीय प्रारूप)

### भाषा चयनकर्ता
एप्लिकेशन के शीर्ष भाग से 15 भाषाएँ उपलब्ध हैं:

| समूह | भाषाएँ |
|---|---|
| रोमांस भाषाएँ | Français · English · Español · Português · Italiano |
| मध्य/पूर्वी यूरोप | Српски · Polski · Magyar · Русский |
| दक्षिण/पूर्वी एशिया | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

भाषा बदलना तुरंत होता है, पुनः आरंभ करने की आवश्यकता नहीं।

### परिचय बटन
भाषा चयनकर्ता के बगल में, यह एक विंडो खोलता है, जिसमें बैनर और संदेश « यह ऑफ़लाइन उपयोगिता सॉफ़्टवेयर निःशुल्क और ओपन-सोर्स है। » दिखता है, जो 15 भाषाओं में अनुवादित है। Esc कुंजी या **बंद करें** बटन इसे बंद कर देता है। `.deb` पैकेज, AppImage या स्वतंत्र निष्पादन योग्य फ़ाइल से चलाने पर, इस विंडो के नीचे बाईं ओर एक छोटा बटन सॉफ़्टवेयर का आइकन जोड़ता या हटाता है (नीचे देखें)।

### मेनू और डेस्कटॉप आइकन
`.deb` पैकेज, AppImage या स्वतंत्र निष्पादन योग्य फ़ाइल से चलाने पर, पहली बार खोलने पर **« आइकन जोड़ें? »** विंडो खुलती है, जिसमें तीन बटन होते हैं: **जोड़ें**, **फिर न पूछें** और **बंद करें** (जो कुछ याद नहीं रखता: अगली बार चलाने पर प्रश्न फिर आएगा)। यह याद दिलाती है कि आइकन बाद में « परिचय » विंडो के नीचे दिए बटन से जोड़ा या हटाया जा सकता है।
- **जोड़ें** **एप्लिकेशन मेनू** की प्रविष्टि और **डेस्कटॉप फ़ोल्डर** का आइकन बनाता है, प्रशासक अधिकारों के बिना। AppImage और स्वतंत्र निष्पादन योग्य फ़ाइल के साथ, सॉफ़्टवेयर पहले `~/.local/share/calculateur-masques/app` में कॉपी होता है (डाउनलोड की गई फ़ाइल को दूसरी जगह ले जाने पर भी आइकन बना रहता है); `.deb` के साथ कुछ भी कॉपी नहीं होता।
- **फिर न पूछें** चुनाव को `~/.config/calculateur-masques/config.json` में दर्ज करता है; « परिचय » के बटन से आइकन हटाना भी इसे दर्ज करता है।
- `.deb` स्थापना के समय कोई आइकन नहीं जोड़ता: उसका लॉन्चर छिपा रहता है, आइकन केवल माँगने पर दिखता है।

> **GNOME** « Desktop Icons » एक्सटेंशन के बिना डेस्कटॉप फ़ोल्डर के आइकन नहीं दिखाता: तब डेस्कटॉप आइकन मौजूद होता है, पर दिखाई नहीं देता (सॉफ़्टवेयर इसकी सूचना देता है)। एप्लिकेशन मेनू की प्रविष्टि दिखाई देती है।

सब कुछ हाथ से हटाने के लिए:

```bash
rm -r ~/.local/share/calculateur-masques
rm -f ~/.local/share/applications/calculateur-masques.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/calculateur-masques.png
rm -f ~/Bureau/calculateur-masques.desktop ~/Desktop/calculateur-masques.desktop
rm -r ~/.config/calculateur-masques
```

### कोरियाई और फ़ॉन्ट
कोरियाई भाषा सूची में **Korean** नाम से दिखती है (अंग्रेज़ी में, क्योंकि कोरियाई फ़ॉन्ट के बिना « 한국어 » चौकोर खानों के रूप में दिखेगा)। यदि सिस्टम में कोई कोरियाई फ़ॉन्ट नहीं है, तो इसे चुनने पर **अंग्रेज़ी में** एक संवाद बॉक्स (« Font needed ») खुलता है, जो आवश्यकता समझाता है और ये विकल्प देता है:
- टर्मिनल में **कॉपी करने के लिए एक कमांड** (सभी उपयोगकर्ताओं के लिए स्थापना): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — केवल Debian/Ubuntu कमांड का सत्यापन किया गया है;
- एक **Install automatically** बटन: Noto Sans KR (4,6 MB, SIL OFL लाइसेंस, स्थिर संस्करण, SHA-256 योग सत्यापित) को `~/.local/share/fonts/calculateur-masques/` में डाउनलोड करता है, प्रशासक अधिकारों के बिना। यही एकमात्र स्थिति है जब सॉफ़्टवेयर नेटवर्क का उपयोग करता है; बाकी समय यह ऑफ़लाइन रहता है;
- एक **Restart now** बटन: सॉफ़्टवेयर को फिर से चलाता है (विकल्प `--lang ko`) ताकि उसे फ़ॉन्ट दिखे; भाषा पुनः आरंभ पर बदलती है। भाषा एक सत्र से दूसरे सत्र तक याद नहीं रखी जाती।

डाउनलोड किया गया फ़ॉन्ट हटाने के लिए: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`।

> गैर-लैटिन लिपि वाली अन्य भाषाओं (हिन्दी, जापानी, चीनी…) के लिए ऐसा कोई संवाद बॉक्स नहीं है: उपयुक्त फ़ॉन्ट के बिना चौकोर खाने दिख सकते हैं। जापानी और चीनी के लिए: `sudo apt install fonts-noto-cjk`।

---

## आवश्यकताएँ

Python 3.8+, `tkinter` मॉड्यूल के साथ।

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

किसी अन्य निर्भरता की आवश्यकता नहीं है।

---

## चलाना

### तेज़ तरीका

```bash
chmod +x lancer.sh
./lancer.sh
```

स्क्रिप्ट अपने-आप जाँचती है कि Python और tkinter मौजूद हैं या नहीं, और कोई निर्भरता न मिलने पर स्पष्ट त्रुटि संदेश दिखाती है।

### Python के माध्यम से सीधे

```bash
python3 calculateur_masques.py
```

### `.deb` पैकेज के माध्यम से (Debian, Ubuntu, Linux Mint)

पहले से संकलित फ़ाइलें (`.deb`, AppImage, स्वतंत्र निष्पादन योग्य फ़ाइल और `SHA256SUMS-linux.txt`) रिपॉज़िटरी के [रिलीज़](https://github.com/harlockSuites/CalculateurMasques/releases) में `Linux-v*` टैग के अंतर्गत प्री-रिलीज़ के रूप में प्रकाशित हैं; ये Debian 12 पर बनी हैं (glibc 2.36, Python 3.11, x86-64)। यह पैकेज सॉफ़्टवेयर को सभी उपयोगकर्ताओं के लिए स्थापित करता है:

```bash
sudo apt install ./calculateur-masques_1.0.1_amd64.deb
calculateur-masques
```

स्थापना मेनू या डेस्कटॉप में कोई आइकन नहीं जोड़ती: `calculateur-masques` को पहली बार चलाएँ, « आइकन जोड़ें? » विंडो उसे जोड़ने का प्रस्ताव देती है। स्थापना हटाने के लिए:

```bash
sudo apt remove calculateur-masques
```

सॉफ़्टवेयर द्वारा जोड़ी गई मेनू प्रविष्टि अपने-आप हट जाती है; डेस्कटॉप शॉर्टकट रह जाता है (वह एक साधारण फ़ाइल है): उसे पहले « परिचय » के बटन से या हाथ से हटा दें।

### AppImage के माध्यम से

एक ही फ़ाइल, बिना स्थापना के:

```bash
chmod +x CalculateurMasques-1.0.1-x86_64.AppImage
./CalculateurMasques-1.0.1-x86_64.AppImage
```

यदि सिस्टम में FUSE नहीं है:

```bash
./CalculateurMasques-1.0.1-x86_64.AppImage --appimage-extract-and-run
```

### स्वतंत्र निष्पादन योग्य फ़ाइल के माध्यम से

स्वतंत्र निष्पादन योग्य फ़ाइल (PyInstaller) एक ही कमांड से संकलित हो जाती है (नीचे « स्वतंत्र निष्पादन योग्य फ़ाइल संकलित करना » देखें); एक पहले से संकलित संस्करण रिलीज़ में है:

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

डाउनलोड की गई फ़ाइलों की जाँच के लिए:

```bash
sha256sum -c SHA256SUMS-linux.txt
```

> **glibc संबंधी सावधानी**: ये फ़ाइलें Debian 12 पर बनी हैं। इनका सत्यापन उसी वितरण पर किया गया है; ये glibc 2.36 या उससे नए संस्करण वाले वितरणों पर भी चलनी चाहिए, पर पुराने संस्करण वाले पर नहीं। ऐसी स्थिति में सोर्स से दोबारा संकलित करें।

---

## सिस्टम स्थापना (वैकल्पिक)

एप्लिकेशन को डेस्कटॉप एनवायरनमेंट (GNOME, KDE, XFCE…) के मेनू में जोड़ने के लिए:

```bash
# फ़ाइलों को /opt में कॉपी करें
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# आवश्यकता हो तो .desktop फ़ाइल में पथ बदलें
# Exec=bash /opt/calculateur-masques/lancer.sh

# एप्लिकेशन मेनू में जोड़ें
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# या
sudo kbuildsycoca6              # KDE Plasma
```

---

## स्वतंत्र निष्पादन योग्य फ़ाइल संकलित करना

PyInstaller से ऐसी बाइनरी बनाई जा सकती है जिसे Python निर्भरता की आवश्यकता नहीं:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

निष्पादन योग्य फ़ाइल `./dist/CalculateurMasquesIPv4` में बनेगी। `--add-data` विकल्प विंडो आइकन (रनटाइम पर Pillow होने पर उसके द्वारा, अन्यथा Tk द्वारा लोड किया जाता है) और « परिचय » विंडो का बैनर अंतर्निहित करते हैं; Pillow वैकल्पिक है (`pip3 install pillow`)।

> **नोट:** Ubuntu पर संकलित Linux बाइनरी glibc संस्करणों के अंतर के कारण Arch या Fedora पर चले, यह आवश्यक नहीं। लक्षित वितरण पर संकलित करें या उस वितरण के लिए Docker इमेज का उपयोग करें।

### `.deb` और AppImage बनाना

Debian या Ubuntu पर, PATH में PyInstaller और `appimagetool` होने पर, स्क्रिप्ट पहले एक PyInstaller फ़ोल्डर बनाती है, फिर `dist/` में दोनों पैकेज:

```bash
python3 packaging/build_linux_packages.py
python3 packaging/build_linux_packages.py --only deb
```

विकल्प `--only deb` (या `--only appimage`) दोनों में से केवल एक बनाता है।

---

## फ़ाइलों की संरचना

```
CalculateurMasques/            (Linux शाखा)
├── calculateur_masques.py      # मुख्य एप्लिकेशन (Linux के लिए अनुकूलित)
├── translations.py             # 15 भाषाओं का शब्दकोश (main शाखा के समान)
├── icon.png                    # विंडो / मेनू आइकन (512 px)
├── banner.png                  # परिचय विंडो का बैनर (600 x 200)
├── lancer.sh                   # निर्भरता जाँच के साथ लॉन्च स्क्रिप्ट
├── calculateur-masques.desktop # डेस्कटॉप एनवायरनमेंट के लिए मेनू प्रविष्टि
├── packaging/                  # .deb और AppImage का निर्माण
│   ├── build_linux_packages.py # निर्माण स्क्रिप्ट
│   └── linux/                  # AppRun, लॉन्चर, मैन्युअल पृष्ठ, .deb का चेंजलॉग
├── INSTALLER.md                # विस्तृत स्थापना निर्देश (फ़्रेंच में)
├── LICENSE                     # MIT लाइसेंस
├── README-LINUX.md             # यह मार्गदर्शिका, फ़्रेंच में
└── docs/README-LINUX.<code>.md # अनुवाद: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Windows संस्करण से अंतर

| पहलू | Windows | Linux |
|---|---|---|
| फ़ॉन्ट | Segoe UI / Consolas | स्वचालित पहचान (Noto Sans, DejaVu Sans, Liberation…) |
| माउस व्हील | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| CSV निर्यात | BOM के साथ UTF-8 (Excel) | BOM के बिना UTF-8 (मानक) |
| निष्पादन योग्य फ़ाइल | स्वतंत्र `.exe` | PyInstaller से ELF बाइनरी (वितरण पर निर्भर) |
| डेस्कटॉप एकीकरण | Windows शॉर्टकट | `.deb` पैकेज, AppImage, मेनू और डेस्कटॉप आइकन (`.desktop` फ़ाइलें, XDG) |

---

## विशेष मामले जिन्हें सँभाला गया है

| उपसर्ग | व्यवहार |
|---|---|
| `/31` | पॉइंट-टू-पॉइंट लिंक (RFC 3021) — 2 पते, पारंपरिक ब्रॉडकास्ट नहीं |
| `/32` | एकल होस्ट — पहला = अंतिम = नेटवर्क पता |
| `/0` | सार्वभौमिक नेटवर्क `0.0.0.0` |

---

## लाइसेंस

MIT लाइसेंस — `LICENSE` फ़ाइल देखें।
