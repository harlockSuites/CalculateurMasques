# Calculateur de Masques IPv4

**Français** · [English](README.en.md) · [Español](README.es.md) · [Português](README.pt.md) · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

Utilitaire graphique **hors-ligne**, gratuit et open-source, pour calculer les masques de sous-réseau IPv4, découper un réseau en sous-réseaux, garder un historique et l'exporter. Interface en **15 langues**.

Dépôt : <https://github.com/harlockSuites/CalculateurMasques>

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
- Touche **Entrée** pour déclencher le calcul

### Onglet Découpage
- Division d'un réseau en N sous-réseaux égaux
- Ou recherche du CIDR minimal pour contenir N hôtes
- Tableau des sous-réseaux avec réseau, masque, hôtes, broadcast (plafonné à 65 536 lignes, avec un message dans la langue choisie au-delà)
- Clic droit sur une cellule pour copier la valeur

### Onglet Historique
- Chaque calcul est enregistré automatiquement, avec l'heure du calcul
- Double-clic sur une entrée pour la recharger dans le calculateur
- Export **CSV** (encodage UTF-8 avec BOM, compatible Excel)
- Export **TXT** (format lisible)

### Sélecteur de langue
15 langues disponibles, accessibles depuis l'en-tête de l'application :

| Groupe | Langues |
|---|---|
| Romanes | Français · English · Español · Português · Italiano |
| Centre/Est Europe | Српски · Polski · Magyar · Русский |
| Asie du Sud/Est | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

Le changement de langue est instantané, sans redémarrage.

### Bouton À propos
À côté du sélecteur de langue, le bouton **À propos** ouvre une fenêtre avec la bannière de l'auteur (`banner.png`) et le message « Ce logiciel utilitaire hors-ligne est gratuit et open-source. », traduit dans les 15 langues.

---

## Prérequis

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- Module `tkinter` (inclus dans l'installation standard de Python)

Aucune dépendance externe requise pour lancer le script. [Pillow](https://pypi.org/project/pillow/) est optionnel : il sert uniquement à afficher l'icône de fenêtre en pleine résolution.

---

## Lancement

### Via Python
```
python calculateur_masques.py
```

### Via l'exécutable compilé
Double-cliquez sur `dist\CalculateurMasquesIPv4.exe`. L'exécutable est autonome, sans installation. Il n'est pas versionné dans ce dépôt : compilez-le (voir ci-dessous).

---

## Compiler l'exécutable

Le dépôt fournit une spec PyInstaller (`CalculateurMasquesIPv4.spec`) qui embarque l'icône, la bannière et les traductions. Depuis ce dossier :

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

L'exécutable est généré dans le dossier `dist\`. L'icône (`icon.ico`) est intégrée à l'exe.

---

## Structure des fichiers

```
CalculateurMasques\
├── calculateur_masques.py        # Application principale
├── translations.py               # Dictionnaire des 15 langues
├── CalculateurMasquesIPv4.spec   # Spécification PyInstaller
├── icon.ico                      # Icône de l'exe (Windows)
├── icon.png                      # Icône de fenêtre (512 px)
├── banner.png                    # Bannière de la fenêtre À propos (600 px)
├── LICENSE                       # Licence MIT
└── README.md
```

---

## Cas particuliers gérés

| Préfixe | Comportement |
|---|---|
| `/31` | Liaison point-à-point (RFC 3021) — 2 adresses, pas de broadcast conventionnel |
| `/32` | Hôte unique — première = dernière = adresse réseau |
| `/0` | Réseau universel `0.0.0.0` |

---

## Licence

Distribué sous licence [MIT](LICENSE) — © 2026 Harlock S.
