#!/usr/bin/env bash
# Lanceur — Calculateur de Masques IPv4
# Place ce fichier dans le même répertoire que calculateur_masques.py

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Vérifier que Python 3 est disponible
if ! command -v python3 &>/dev/null; then
    echo "Erreur : python3 n'est pas installé."
    echo "Installez-le avec : sudo apt install python3 python3-tk"
    exit 1
fi

# Vérifier que tkinter est disponible
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "Erreur : le module tkinter est manquant."
    echo "Installez-le avec : sudo apt install python3-tk"
    exit 1
fi

exec python3 "$DIR/calculateur_masques.py" "$@"
