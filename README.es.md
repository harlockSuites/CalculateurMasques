# Calculadora de Máscaras de Subred IPv4

[Français](README.md) · [English](README.en.md) · **Español** · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

Utilidad gráfica **sin conexión**, gratuita y de código abierto, para calcular máscaras de subred IPv4, dividir una red en subredes, conservar un historial y exportarlo. Interfaz en **15 idiomas**.

Repositorio: <https://github.com/harlockSuites/CalculateurMasques>

> **Linux:** hay una versión específica para Linux en la [rama `Linux`](https://github.com/harlockSuites/CalculateurMasques/tree/Linux). Un ejecutable precompilado (versión preliminar, Debian 12, x86-64) está publicado en la [versión `Linux-v1.0`](https://github.com/harlockSuites/CalculateurMasques/releases/tag/Linux-v1.0). Este README describe la versión de Windows.

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
- Tecla **Intro** para lanzar el cálculo

### Pestaña División
- División de una red en N subredes iguales
- O búsqueda del CIDR mínimo para contener N hosts
- Tabla de subredes con red, máscara, hosts, broadcast (limitada a 65 536 filas, con un mensaje en el idioma elegido a partir de ese límite)
- Clic derecho sobre una celda para copiar el valor

### Pestaña Historial
- Cada cálculo se registra automáticamente, con la hora del cálculo
- Doble clic en una entrada para recargarla en la calculadora
- Exportación **CSV** (codificación UTF-8 con BOM, compatible con Excel)
- Exportación **TXT** (formato legible)

### Selector de idioma
15 idiomas disponibles, accesibles desde el encabezado de la aplicación:

| Grupo | Idiomas |
|---|---|
| Romances | Français · English · Español · Português · Italiano |
| Centro/Este de Europa | Српски · Polski · Magyar · Русский |
| Sur/Este de Asia | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

El cambio de idioma es instantáneo, sin reiniciar.

### Botón Acerca de
Junto al selector de idioma, el botón **Acerca de** abre una ventana con el banner del autor (`banner.png`) y el mensaje «Este software de utilidad sin conexión es gratuito y de código abierto.», traducido a los 15 idiomas.

---

## Requisitos previos

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- Módulo `tkinter` (incluido en la instalación estándar de Python)

No se requiere ninguna dependencia externa para ejecutar el script. [Pillow](https://pypi.org/project/pillow/) es opcional: solo sirve para mostrar el icono de la ventana a resolución completa.

---

## Ejecución

### Mediante Python
```
python calculateur_masques.py
```

### Mediante el ejecutable compilado
Haga doble clic en `dist\CalculateurMasquesIPv4.exe`. El ejecutable es autónomo, sin instalación. No está versionado en este repositorio: compílelo (véase más abajo).

---

## Compilar el ejecutable

El repositorio incluye una spec de PyInstaller (`CalculateurMasquesIPv4.spec`) que incorpora el icono, el banner y las traducciones. Desde esta carpeta:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

El ejecutable se genera en la carpeta `dist\`. El icono (`icon.ico`) se integra en el exe.

---

## Estructura de archivos

```
CalculateurMasques\
├── calculateur_masques.py        # Aplicación principal
├── translations.py               # Diccionario de los 15 idiomas
├── CalculateurMasquesIPv4.spec   # Especificación de PyInstaller
├── icon.ico                      # Icono del exe (Windows)
├── icon.png                      # Icono de la ventana (512 px)
├── banner.png                    # Banner de la ventana Acerca de (600 px)
├── LICENSE                       # Licencia MIT
└── README.md
```

---

## Casos particulares gestionados

| Prefijo | Comportamiento |
|---|---|
| `/31` | Enlace punto a punto (RFC 3021): 2 direcciones, sin broadcast convencional |
| `/32` | Host único: primera = última = dirección de red |
| `/0` | Red universal `0.0.0.0` |

---

## Antivirus y falsos positivos

A fecha de 25 de octubre de 2026, VirusTotal señala el ejecutable `CalculateurMasquesIPv4.exe` de la versión 1.0 con **5 detecciones de 69 motores**: Arctic Wolf, Bkav Pro, Microsoft, SecureAge y Zillya. Creemos que se trata de **falsos positivos**, frecuentes en un programa de Python empaquetado con PyInstaller, reciente y sin firma digital. El programa no contiene ningún código de red (solo usa `tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys` y `os`, además de Pillow para el icono de la ventana) y todo su código fuente es público en este repositorio.

Se enviaron informes de falsos positivos el 25 de octubre de 2026 a los cinco proveedores afectados. Esta sección se actualizará con sus respuestas.

Para verificar su descarga:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- Informe de VirusTotal: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- También puede compilar el ejecutable usted mismo a partir del código fuente (véase «Compilar el ejecutable»).

---

## Licencia

Distribuido bajo licencia [MIT](LICENSE) — © 2026 Harlock S.
