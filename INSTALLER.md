# Installation — Calculateur de Masques IPv4 (Linux)

Les fichiers précompilés (`.deb`, AppImage, exécutable autonome et `SHA256SUMS-linux.txt`) sont dans les [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) du dépôt, sous une étiquette `Linux-v*`. Ils sont bâtis sur Debian 12 (glibc 2.36, x86-64).

```bash
# Vérifier les fichiers téléchargés (facultatif)
sha256sum -c SHA256SUMS-linux.txt
```

## Paquet `.deb` (Debian, Ubuntu, Linux Mint)

```bash
sudo apt install ./calculateur-masques_1.0.1_amd64.deb
calculateur-masques
```

L'installation n'ajoute aucune icône : au premier lancement, une fenêtre propose d'ajouter l'icône du menu et du bureau. Désinstaller :

```bash
sudo apt remove calculateur-masques
```

## AppImage

```bash
chmod +x CalculateurMasques-1.0.1-x86_64.AppImage
./CalculateurMasques-1.0.1-x86_64.AppImage
```

Sans FUSE : `./CalculateurMasques-1.0.1-x86_64.AppImage --appimage-extract-and-run`.

## Exécutable autonome

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

## Depuis les sources

```bash
# Debian / Ubuntu / Linux Mint
sudo apt install python3 python3-tk

# Fedora / RHEL
sudo dnf install python3 python3-tkinter

# Arch Linux
sudo pacman -S python tk

chmod +x lancer.sh
./lancer.sh
```

## Installation système à la main (optionnel)

```bash
# Copier les fichiers dans /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Ajouter au menu des applications
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database
```

## Construire les paquets (PyInstaller, appimagetool)

```bash
pip3 install pyinstaller

# l'exécutable autonome seul
pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
# L'exécutable sera dans ./dist/CalculateurMasquesIPv4

# le .deb et l'AppImage (dans dist/)
python3 packaging/build_linux_packages.py
```

Détails, icône du menu et du bureau, polices : voir [`README-LINUX.md`](README-LINUX.md).
