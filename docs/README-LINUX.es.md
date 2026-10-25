# Calculadora de Máscaras de Subred IPv4 — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · **Español** · [Português](README-LINUX.pt.md) · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **Rama `Linux`**: versión Linux del programa. La rama `main` está reservada a la distribución para Windows; no fusione una en la otra.

Utilidad gráfica de cálculo de máscaras de subred IPv4, con soporte para 15 idiomas, división en subredes, historial y exportación.

Repositorio: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## Descripción general

La aplicación se organiza en tres pestañas:

| Pestaña | Contenido |
|---|---|
| **Calculadora** | Cálculo principal, conversiones de IP, verificación de pertenencia |
| **División** | División automática de una red en subredes |
| **Historial** | Registro de los cálculos, exportación a CSV / TXT |

---

## Funcionalidades

### Pestaña Calculadora
- Entrada mediante **prefijo CIDR** (`/24`) o **máscara decimal** (`255.255.255.0`): ambos se sincronizan automáticamente
- Resultados mostrados:
  - Dirección de red
  - Máscara de subred
  - Notación CIDR
  - Máscara comodín (wildcard)
  - Primera / Última dirección de host
  - Dirección de broadcast
  - Número de hosts utilizables
  - Rango completo de la red
- **Conversiones** de la dirección IP introducida: notación decimal punteada, binario, hexadecimal, decimal (entero de 32 bits)
- **Verificación de pertenencia**: comprueba si una IP dada pertenece a la red calculada
- **Clic derecho** sobre cualquier valor para copiarlo al portapapeles
- Una **máscara inversa** (wildcard, p. ej. `0.0.0.255`) se rechaza con un mensaje traducido: introduzca una máscara de subred (`255.255.255.0`)
- **Rueda del ratón**: desplaza la página, sea cual sea el elemento sobre el que se encuentre el puntero (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Tecla **Intro** para lanzar el cálculo

### Pestaña División
- División de una red en N subredes iguales
- O búsqueda del CIDR mínimo para contener N hosts
- Tabla de subredes con red, máscara, hosts, broadcast
- Límite de 65 536 subredes por división (a partir de ahí, un mensaje lo indica en lugar de bloquear la interfaz)
- Clic derecho sobre una celda para copiar el valor

### Pestaña Historial
- Cada cálculo se registra automáticamente, con la hora a la que se hizo (conservada en pantalla y en la exportación)
- Doble clic en una entrada para recargarla en la calculadora
- Exportación **CSV** (codificación UTF-8)
- Exportación **TXT** (formato legible)

### Selector de idioma
15 idiomas disponibles, accesibles desde el encabezado de la aplicación:

| Grupo | Idiomas |
|---|---|
| Romances | Français · English · Español · Português · Italiano |
| Centro/Este de Europa | Српски · Polski · Magyar · Русский |
| Sur/Este de Asia | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

El cambio de idioma es instantáneo, sin reiniciar.

### Botón Acerca de
Junto al selector de idioma, abre una ventana con el banner y el mensaje «Este software de utilidad sin conexión es gratuito y de código abierto.», traducido a los 15 idiomas. La tecla Esc o el botón Cerrar la cierra.

### Coreano y fuente
El coreano aparece con el nombre **Korean** en la lista (en inglés, porque «한국어» se mostraría como cuadrados sin una fuente coreana). Si el sistema no tiene ninguna, al elegirlo se abre un cuadro de diálogo **en inglés** («Font needed») que explica la necesidad y ofrece:
- un **comando para copiar** en un terminal (instalación para todos los usuarios): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch); solo se ha verificado el comando de Debian/Ubuntu;
- un botón **Install automatically**: descarga Noto Sans KR (4,6 MB, licencia SIL OFL, versión fija, suma SHA-256 verificada) en `~/.local/share/fonts/calculateur-masques/`, sin derechos de administrador. Es el único caso en que el programa usa la red; el resto del tiempo permanece sin conexión;
- un botón **Restart now**: reinicia el programa (opción `--lang ko`) para que vea la fuente; el idioma cambia al reiniciar. El idioma no se conserva de una sesión a otra.

Para eliminar la fuente descargada: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Los demás idiomas de escritura no latina (hindi, japonés, chino…) no tienen un cuadro de este tipo: sin una fuente adecuada, pueden mostrarse cuadrados. Para japonés y chino: `sudo apt install fonts-noto-cjk`.

---

## Requisitos previos

Python 3.8+ con el módulo `tkinter`.

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

No se requiere ninguna otra dependencia.

---

## Ejecución

### Método rápido

```bash
chmod +x lancer.sh
./lancer.sh
```

El script comprueba automáticamente la presencia de Python y de tkinter, y muestra un mensaje de error explícito si falta alguna dependencia.

### Mediante Python

```bash
python3 calculateur_masques.py
```

### Mediante un ejecutable autónomo

Un ejecutable autónomo (PyInstaller) se compila con un solo comando (véase «Compilar un ejecutable autónomo» más abajo). Hay una versión precompilada publicada (como versión preliminar) en las [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) del repositorio, bajo una etiqueta `Linux-v*`; está construida sobre Debian 12 (glibc 2.36, Python 3.11, x86-64):

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **Reserva sobre glibc**: este binario está construido sobre Debian 12. Está verificado en esa distribución; también debería funcionar en las distribuciones con glibc 2.36 o más reciente, pero no en una más antigua. En ese caso, recompile desde el código fuente.

---

## Instalación en el sistema (opcional)

Para integrar la aplicación en el menú del entorno de escritorio (GNOME, KDE, XFCE…):

```bash
# Copiar los archivos en /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Modificar la ruta en el archivo .desktop si es necesario
# Exec=bash /opt/calculateur-masques/lancer.sh

# Añadir al menú de aplicaciones
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# o
sudo kbuildsycoca6              # KDE Plasma
```

---

## Compilar un ejecutable autónomo

PyInstaller permite generar un binario sin dependencia de Python:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

El ejecutable se generará en `./dist/CalculateurMasquesIPv4`. Las opciones `--add-data` incorporan el icono de la ventana (cargado en tiempo de ejecución mediante Pillow si está presente, y si no mediante Tk) y el banner de la ventana «Acerca de»; Pillow es opcional (`pip3 install pillow`).

> **Nota:** un binario Linux compilado en Ubuntu no funcionará necesariamente en Arch o Fedora debido a las diferencias entre versiones de glibc. Compile en la distribución de destino o use una imagen de Docker de la distribución deseada.

---

## Estructura de archivos

```
CalculateurMasques/            (rama Linux)
├── calculateur_masques.py      # Aplicación principal (adaptada a Linux)
├── translations.py             # Diccionario de los 15 idiomas (idéntico al de la rama main)
├── icon.png                    # Icono de la ventana / del menú (512 px)
├── banner.png                  # Banner de la ventana «Acerca de» (600 x 200)
├── lancer.sh                   # Script de lanzamiento con verificación de dependencias
├── calculateur-masques.desktop # Entrada de menú para entornos de escritorio
├── INSTALLER.md                # Instrucciones de instalación detalladas (en francés)
├── LICENSE                     # Licencia MIT
├── README-LINUX.md             # Esta guía, en francés
└── docs/README-LINUX.<code>.md # Traducciones: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Diferencias con la versión de Windows

| Aspecto | Windows | Linux |
|---|---|---|
| Fuentes | Segoe UI / Consolas | Detección automática (Noto Sans, DejaVu Sans, Liberation…) |
| Rueda del ratón | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Exportación CSV | UTF-8 con BOM (Excel) | UTF-8 sin BOM (estándar) |
| Ejecutable | `.exe` autónomo | Binario ELF mediante PyInstaller (depende de la distribución) |
| Integración en el escritorio | Acceso directo de Windows | Archivo `.desktop` (XDG) |

---

## Casos particulares gestionados

| Prefijo | Comportamiento |
|---|---|
| `/31` | Enlace punto a punto (RFC 3021): 2 direcciones, sin broadcast convencional |
| `/32` | Host único: primera = última = dirección de red |
| `/0` | Red universal `0.0.0.0` |

---

## Licencia

Licencia MIT — véase el archivo `LICENSE`.
