# Calculateur de Masques IPv4 — Linux

**Français** · [English](docs/README-LINUX.en.md) · [Español](docs/README-LINUX.es.md) · [Português](docs/README-LINUX.pt.md) · [Italiano](docs/README-LINUX.it.md) · [Српски](docs/README-LINUX.sr.md) · [Polski](docs/README-LINUX.pl.md) · [Magyar](docs/README-LINUX.hu.md) · [Русский](docs/README-LINUX.ru.md) · [हिन्दी](docs/README-LINUX.hi.md) · [中文](docs/README-LINUX.zh.md) · [Tiếng Việt](docs/README-LINUX.vi.md) · [한국어](docs/README-LINUX.ko.md) · [日本語](docs/README-LINUX.ja.md) · [Filipino](docs/README-LINUX.fil.md)

> **Branche `Linux`** : version Linux du logiciel. La branche `main` est réservée à la distribution Windows ; ne pas fusionner l'une dans l'autre.

Utilitaire graphique de calcul de masques de sous-réseau IPv4, avec support de 15 langues, découpage de sous-réseaux, historique et export.

Dépôt : <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

---

## Aperçu

L'application est organisée en trois onglets :

| Onglet | Contenu |
|---|---|
| **Calculateur** | Calcul principal, conversions IP, vérification d'appartenance |
| **Découpage** | Division automatique d'un réseau en sous-réseaux |
| **Historique** | Journalisation des calculs, export CSV / TXT |

---

## Fonctionnalités

### Onglet Calculateur
- Saisie par **préfixe CIDR** (`/24`) ou **masque décimal** (`255.255.255.0`) — les deux se synchronisent automatiquement
- Résultats affichés :
  - Adresse réseau
  - Masque de sous-réseau
  - Notation CIDR
  - Masque générique (wildcard)
  - Première / Dernière adresse hôte
  - Adresse de broadcast
  - Nombre d'hôtes utilisables
  - Plage réseau complète
- **Conversions** de l'adresse IP saisie : décimale pointée, binaire, hexadécimal, décimal 32 bits
- **Vérification d'appartenance** : teste si une IP donnée appartient au réseau calculé
- **Clic droit** sur n'importe quelle valeur pour la copier dans le presse-papiers
- Un **masque inversé** (wildcard, ex. `0.0.0.255`) est refusé avec un message traduit : saisissez un masque de sous-réseau (`255.255.255.0`)
- **Molette de la souris** : fait défiler la page, quel que soit l'élément survolé (X11 : `Button-4`/`Button-5` ; Wayland : `MouseWheel`)
- Touche **Entrée** pour déclencher le calcul

### Onglet Découpage
- Division d'un réseau en N sous-réseaux égaux
- Ou recherche du CIDR minimal pour contenir N hôtes
- Tableau des sous-réseaux avec réseau, masque, hôtes, broadcast
- Plafond de 65 536 sous-réseaux par découpage (au-delà, un message l'indique au lieu de figer l'interface)
- Clic droit sur une cellule pour copier la valeur

### Onglet Historique
- Chaque calcul est enregistré automatiquement, avec l'heure à laquelle il a été fait (conservée à l'affichage et à l'export)
- Double-clic sur une entrée pour la recharger dans le calculateur
- Export **CSV** (encodage UTF-8)
- Export **TXT** (format lisible)

### Sélecteur de langue
15 langues disponibles, accessibles depuis l'en-tête de l'application :

| Groupe | Langues |
|---|---|
| Romanes | Français · English · Español · Português · Italiano |
| Centre/Est Europe | Српски · Polski · Magyar · Русский |
| Asie du Sud/Est | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

Le changement de langue est instantané, sans redémarrage.

### Bouton « À propos »
À côté du sélecteur de langue, il ouvre une fenêtre avec la bannière et le message « Ce logiciel utilitaire hors-ligne est gratuit et open-source. », traduit dans les 15 langues. La touche Échap ou le bouton Fermer la referme.

### Coréen et police
Le coréen apparaît sous le nom **Korean** dans la liste (en anglais, car « 한국어 » s'afficherait en carrés sans police coréenne). Si le système n'en a aucune, le choisir ouvre une boîte de dialogue **en anglais** (« Font needed ») qui explique le besoin et propose :
- une **commande à copier** dans un terminal (installation pour tous les utilisateurs) : `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — seule la commande Debian/Ubuntu a été vérifiée ;
- un bouton **Install automatically** : télécharge Noto Sans KR (4,6 Mo, licence SIL OFL, version figée, somme SHA-256 vérifiée) dans `~/.local/share/fonts/calculateur-masques/`, sans droits administrateur. C'est le seul cas où le logiciel utilise le réseau ; il reste hors-ligne le reste du temps ;
- un bouton **Restart now** : relance le logiciel (option `--lang ko`) pour qu'il voie la police ; la langue change au redémarrage. La langue n'est pas retenue d'une session à l'autre.

Pour retirer la police téléchargée : `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Les autres langues à écriture non latine (hindi, japonais, chinois…) n'ont pas de boîte de ce type : sans police adaptée, des carrés peuvent s'afficher. Pour le japonais et le chinois : `sudo apt install fonts-noto-cjk`.

---

## Prérequis

Python 3.8+ avec le module `tkinter`.

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

Aucune autre dépendance requise.

---

## Lancement

### Méthode rapide

```bash
chmod +x lancer.sh
./lancer.sh
```

Le script vérifie automatiquement la présence de Python et de tkinter, et affiche un message d'erreur explicite si une dépendance est manquante.

### Via Python directement

```bash
python3 calculateur_masques.py
```

### Via un exécutable autonome

Un exécutable autonome (PyInstaller) se compile en une commande (voir « Compiler un exécutable autonome » plus bas). Une version précompilée est publiée (en préversion) dans les [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) du dépôt, sous une étiquette `Linux-v*` ; elle est bâtie sur Debian 12 (glibc 2.36, Python 3.11, x86-64) :

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **Réserve glibc** : ce binaire est bâti sur Debian 12. Il est vérifié sur cette distribution ; il doit aussi fonctionner sur les distributions de glibc 2.36 ou plus récente, mais pas sur une plus ancienne. Dans ce cas, recompilez depuis les sources.

---

## Installation système (optionnel)

Pour intégrer l'application au menu de l'environnement de bureau (GNOME, KDE, XFCE…) :

```bash
# Copier les fichiers dans /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Modifier le chemin dans le fichier .desktop si nécessaire
# Exec=bash /opt/calculateur-masques/lancer.sh

# Ajouter au menu des applications
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# ou
sudo kbuildsycoca6              # KDE Plasma
```

---

## Compiler un exécutable autonome

PyInstaller permet de générer un binaire sans dépendance Python :

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

L'exécutable sera généré dans `./dist/CalculateurMasquesIPv4`. Les options `--add-data` embarquent l'icône de fenêtre (chargée au runtime via Pillow si présent, sinon par Tk) et la bannière de la fenêtre « À propos » ; Pillow est facultatif (`pip3 install pillow`).

> **Note :** un binaire Linux compilé sur Ubuntu ne fonctionnera pas nécessairement sur Arch ou Fedora en raison des différences de versions de glibc. Compilez sur la distribution cible ou utilisez une image Docker pour la distribution visée.

---

## Structure des fichiers

```
CalculateurMasques/            (branche Linux)
├── calculateur_masques.py      # Application principale (adaptée Linux)
├── translations.py             # Dictionnaire des 15 langues (identique à la branche main)
├── icon.png                    # Icône de fenêtre / menu (512 px)
├── banner.png                  # Bannière de la fenêtre « À propos » (600 x 200)
├── lancer.sh                   # Script de lancement avec vérification des dépendances
├── calculateur-masques.desktop # Entrée de menu pour environnements de bureau
├── INSTALLER.md                # Instructions d'installation détaillées (en français)
├── LICENSE                     # Licence MIT
├── README-LINUX.md             # Ce guide, en français
└── docs/README-LINUX.<code>.md # Traductions : en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Différences avec la version Windows

| Aspect | Windows | Linux |
|---|---|---|
| Polices | Segoe UI / Consolas | Détection automatique (Noto Sans, DejaVu Sans, Liberation…) |
| Molette souris | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Export CSV | UTF-8 avec BOM (Excel) | UTF-8 sans BOM (standard) |
| Exécutable | `.exe` autonome | Binaire ELF via PyInstaller (dépend de la distrib.) |
| Intégration bureau | Raccourci Windows | Fichier `.desktop` (XDG) |

---

## Cas particuliers gérés

| Préfixe | Comportement |
|---|---|
| `/31` | Liaison point-à-point (RFC 3021) — 2 adresses, pas de broadcast conventionnel |
| `/32` | Hôte unique — première = dernière = adresse réseau |
| `/0` | Réseau universel `0.0.0.0` |

---

## Licence

Licence MIT — voir le fichier `LICENSE`.
