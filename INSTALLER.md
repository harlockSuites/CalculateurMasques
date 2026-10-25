# Installation — Calculateur de Masques IPv4 (Linux)

## Prérequis

```bash
# Debian / Ubuntu / Linux Mint
sudo apt install python3 python3-tk

# Fedora / RHEL
sudo dnf install python3 python3-tkinter

# Arch Linux
sudo pacman -S python tk
```

## Lancement direct

```bash
chmod +x lancer.sh
./lancer.sh
```

## Installation système (optionnel)

```bash
# Copier les fichiers dans /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Ajouter au menu des applications
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database
```

## Compiler un exécutable autonome (PyInstaller)

```bash
pip3 install pyinstaller
pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
# L'exécutable sera dans ./dist/CalculateurMasquesIPv4
```
