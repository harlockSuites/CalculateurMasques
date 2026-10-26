"""Construit le paquet Debian (.deb) et l'AppImage du Calculateur de Masques IPv4 (version Linux).

Usage (sous Linux, depuis le dossier du projet ; PyInstaller et appimagetool dans le PATH) :
    python3 packaging/build_linux_packages.py            # tout
    python3 packaging/build_linux_packages.py --only deb # ou : --only appimage

Étapes : PyInstaller (dossier, pas « onefile » : démarrage immédiat, rien à déballer à chaque lancement) -> dist/ :
    calculateur-masques_<version>_<amd64|arm64>.deb
    CalculateurMasques-<version>-<x86_64|aarch64>.AppImage       fichier unique à rendre exécutable

Contenu du .deb :
    /usr/lib/calculateur-masques/        le programme (dossier PyInstaller)
    /usr/bin/calculateur-masques         lien vers le programme
    /usr/share/applications/             lanceur MASQUÉ (NoDisplay) : aucune icône d'elle-même, voir ci-dessous
    /usr/share/icons/hicolor/512x512/apps/   icône
    /usr/share/doc/calculateur-masques/  licence (copyright) et journal des modifications
    /usr/share/man/man1/                 page de manuel
Aucun script de maintenance. Le paquet n'ajoute aucune icône au menu : c'est le logiciel qui l'ajoute sur demande (entrée de
menu et raccourci du Bureau dans le dossier de l'utilisateur, avec TryExec : elles disparaissent si le paquet est retiré)
et, pour la police coréenne, ~/.local/share/fonts/calculateur-masques ; le paquet n'y touche pas.
"""
import argparse
import gzip
import hashlib
import os
import platform
import shutil
import stat
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
BUILD = os.path.join(ROOT, "build")
LINUX_FILES = os.path.join(ROOT, "packaging", "linux")
SCRIPT = os.path.join(ROOT, "calculateur_masques.py")
PACKAGE = "calculateur-masques"
VERSION = "1.0.1"
LIB_DIR = "usr/lib/calculateur-masques"
DEB_ARCHES = {"x86_64": "amd64", "amd64": "amd64", "aarch64": "arm64", "arm64": "arm64"}
APPIMAGE_ARCHES = {"x86_64": "x86_64", "amd64": "x86_64", "aarch64": "aarch64", "arm64": "aarch64"}
MAINTAINER = "harlockSuites <harlockSuites@users.noreply.github.com>"
HOMEPAGE = "https://github.com/harlockSuites/CalculateurMasques/tree/Linux"
# Dépendances système : PyInstaller embarque Tcl/Tk, X11, freetype, fontconfig, OpenSSL… ; hors du dossier il ne reste
# que la bibliothèque C (la plus récente utilisée : GLIBC_2.36) et libxcb (mesuré avec ldd sur le dossier, voir --show-deps).
DEPENDS = "libc6 (>= 2.36), libxcb1"
RECOMMENDS = "fontconfig"


def machine():
    return platform.machine().lower()


def build_bundle():
    """PyInstaller : dossier dist/pyinstaller/calculateur-masques/ ."""
    out = os.path.join(BUILD, "pyinstaller-dist")
    work = os.path.join(BUILD, "pyinstaller-work")
    for folder in (out, work):
        shutil.rmtree(folder, ignore_errors=True)
    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", "--onedir", "--windowed",
           "--name", PACKAGE, "--distpath", out, "--workpath", work, "--specpath", work]
    for data in ("translations.py", "icon.png", "banner.png"):
        cmd += ["--add-data", f"{os.path.join(ROOT, data)}:."]
    cmd.append(SCRIPT)
    print("->", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT)
    app_dir = os.path.join(out, PACKAGE)
    if not os.path.isfile(os.path.join(app_dir, PACKAGE)):
        raise SystemExit("PyInstaller n'a pas produit le programme")
    return app_dir


def show_deps(app_dir):
    """Bibliothèques système que le dossier PyInstaller utilise sans les embarquer, avec leur paquet Debian."""
    libs = set()
    for folder, _dirs, files in os.walk(app_dir):
        for name in files:
            path = os.path.join(folder, name)
            if name == PACKAGE or ".so" in name:
                out = subprocess.run(["ldd", path], capture_output=True, text=True).stdout
                for line in out.splitlines():
                    if "=>" in line and app_dir not in line and "not found" not in line:
                        libs.add(line.split("=>")[1].split("(")[0].strip())
    owners = {}
    for lib in sorted(libs):
        r = subprocess.run(["dpkg", "-S", os.path.realpath(lib)], capture_output=True, text=True)
        owners.setdefault(r.stdout.split(":")[0] if r.returncode == 0 else "?", []).append(os.path.basename(lib))
    for pkg, names in sorted(owners.items()):
        print(f"  {pkg}: {', '.join(names)}")


def _normalize_modes(root):
    """Dossiers 755 ; fichiers 755 s'ils sont exécutables dans le dossier PyInstaller, sinon 644 ; les bibliothèques
    (.so) en 644 : le chargeur dynamique n'a pas besoin du droit d'exécution (lintian : shared-library-is-executable)."""
    for folder, _dirs, files in os.walk(root):
        os.chmod(folder, 0o755)
        for name in files:
            path = os.path.join(folder, name)
            if os.path.islink(path):
                continue
            is_lib = ".so" in name and name != PACKAGE
            os.chmod(path, 0o755 if (os.stat(path).st_mode & stat.S_IXUSR and not is_lib) else 0o644)


def _dir_size_kib(root):
    total = 0
    for folder, _dirs, files in os.walk(root):
        for name in files:
            path = os.path.join(folder, name)
            if not os.path.islink(path):
                total += os.path.getsize(path)
    return (total + 1023) // 1024


def _write_md5sums(root):
    lines = []
    for folder, dirs, files in os.walk(root):
        dirs.sort()
        if os.path.relpath(folder, root) == "DEBIAN":
            continue
        for name in sorted(files):
            path = os.path.join(folder, name)
            if os.path.islink(path):
                continue
            h = hashlib.md5()   # format imposé par dpkg (md5sums), sans rôle de sécurité
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(1 << 20), b""):
                    h.update(chunk)
            lines.append(f"{h.hexdigest()}  {os.path.relpath(path, root).replace(os.sep, '/')}")
    with open(os.path.join(root, "DEBIAN", "md5sums"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def control_text(arch, installed_size_kib):
    return "\n".join([
        f"Package: {PACKAGE}",
        f"Version: {VERSION}",
        f"Architecture: {arch}",
        f"Maintainer: {MAINTAINER}",
        f"Installed-Size: {installed_size_kib}",
        f"Depends: {DEPENDS}",
        f"Recommends: {RECOMMENDS}",
        "Section: net",
        "Priority: optional",
        f"Homepage: {HOMEPAGE}",
        "Description: IPv4 subnet mask calculator",
        " Offline graphical utility to calculate IPv4 subnet masks, split a network",
        " into subnets, keep a history and export it as CSV or text. The interface is",
        " available in 15 languages.",
        " .",
        " The program is bundled (PyInstaller): no Python or Tk package is needed.",
        " This is a pre-release of the Linux version.",
        ""])


def build_deb(app_dir):
    arch = DEB_ARCHES.get(machine())
    if not arch:
        raise SystemExit(f"architecture non prise en charge : {machine()}")
    if not shutil.which("dpkg-deb"):
        raise SystemExit("dpkg-deb introuvable : à construire sous Debian ou Ubuntu.")
    root = os.path.join(BUILD, "deb-root")
    shutil.rmtree(root, ignore_errors=True)
    shutil.copytree(app_dir, os.path.join(root, *LIB_DIR.split("/")), symlinks=True)
    os.makedirs(os.path.join(root, "usr", "bin"))
    os.symlink("../lib/calculateur-masques/calculateur-masques", os.path.join(root, "usr", "bin", PACKAGE))
    apps = os.path.join(root, "usr", "share", "applications")
    os.makedirs(apps)
    # lanceur MASQUÉ (NoDisplay) : le paquet n'ajoute aucune icône au menu de lui-même ; le logiciel (bouton de la fenêtre
    # « À propos » ou invitation de la première ouverture) écrit l'entrée visible dans le dossier de l'utilisateur, qui
    # remplace celle-ci (même nom de fichier, dossier prioritaire). `gtk-launch calculateur-masques` fonctionne quand même.
    with open(os.path.join(LINUX_FILES, "calculateur-masques.desktop"), encoding="utf-8") as src:
        hidden = src.read().replace("[Desktop Entry]\n", "[Desktop Entry]\nNoDisplay=true\n", 1)
    with open(os.path.join(apps, "calculateur-masques.desktop"), "w", encoding="utf-8", newline="\n") as dst:
        dst.write(hidden)
    icons = os.path.join(root, "usr", "share", "icons", "hicolor", "512x512", "apps")
    os.makedirs(icons)
    shutil.copy2(os.path.join(ROOT, "icon.png"), os.path.join(icons, "calculateur-masques.png"))
    doc = os.path.join(root, "usr", "share", "doc", PACKAGE)
    os.makedirs(doc)
    shutil.copy2(os.path.join(ROOT, "LICENSE"), os.path.join(doc, "copyright"))
    with open(os.path.join(LINUX_FILES, "changelog.Debian"), "rb") as src, \
            open(os.path.join(doc, "changelog.gz"), "wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as gz:
            gz.write(src.read())
    man = os.path.join(root, "usr", "share", "man", "man1")
    os.makedirs(man)
    with open(os.path.join(LINUX_FILES, "calculateur-masques.1"), "rb") as src,             open(os.path.join(man, "calculateur-masques.1.gz"), "wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as gz:
            gz.write(src.read())
    _normalize_modes(root)
    debian = os.path.join(root, "DEBIAN")
    os.makedirs(debian)
    with open(os.path.join(debian, "control"), "w", encoding="utf-8", newline="\n") as f:
        f.write(control_text(arch, _dir_size_kib(root)))
    _write_md5sums(root)
    os.chmod(debian, 0o755)
    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, f"{PACKAGE}_{VERSION}_{arch}.deb")
    if os.path.exists(out):
        os.remove(out)
    cmd = ["dpkg-deb", "--root-owner-group", "-Zxz", "--build", root, out]
    print("->", " ".join(cmd))
    subprocess.run(cmd, check=True)
    return out


def build_appimage(app_dir):
    arch = APPIMAGE_ARCHES.get(machine())
    if not arch:
        raise SystemExit(f"architecture non prise en charge : {machine()}")
    tool = os.environ.get("APPIMAGETOOL") or shutil.which("appimagetool")
    if not tool:
        raise SystemExit("appimagetool introuvable (https://github.com/AppImage/appimagetool)")
    appdir = os.path.join(BUILD, "AppDir")
    shutil.rmtree(appdir, ignore_errors=True)
    shutil.copytree(app_dir, os.path.join(appdir, *LIB_DIR.split("/")), symlinks=True)
    apprun = os.path.join(appdir, "AppRun")
    shutil.copy2(os.path.join(LINUX_FILES, "AppRun"), apprun)
    os.chmod(apprun, os.stat(apprun).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    shutil.copy2(os.path.join(LINUX_FILES, "calculateur-masques.desktop"), os.path.join(appdir, "calculateur-masques.desktop"))
    shutil.copy2(os.path.join(ROOT, "icon.png"), os.path.join(appdir, "calculateur-masques.png"))
    shutil.copy2(os.path.join(ROOT, "icon.png"), os.path.join(appdir, ".DirIcon"))
    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, f"CalculateurMasques-{VERSION}-{arch}.AppImage")
    if os.path.exists(out):
        os.remove(out)
    env = dict(os.environ, ARCH=arch, APPIMAGE_EXTRACT_AND_RUN="1")   # l'outil est lui-même un AppImage : pas de FUSE
    cmd = [tool, "--no-appstream", appdir, out]
    print("->", " ".join(cmd))
    subprocess.run(cmd, check=True, env=env)
    os.chmod(out, 0o755)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", choices=("deb", "appimage"), help="ne construire qu'un des deux")
    ap.add_argument("--show-deps", action="store_true", help="afficher les bibliothèques système utilisées, puis s'arrêter")
    args = ap.parse_args(argv)
    if not sys.platform.startswith("linux"):
        raise SystemExit("Ce script construit des paquets Linux : à lancer sous Linux.")
    app_dir = build_bundle()
    if args.show_deps:
        show_deps(app_dir)
        return
    outputs = []
    if args.only in (None, "deb"):
        outputs.append(build_deb(app_dir))
    if args.only in (None, "appimage"):
        outputs.append(build_appimage(app_dir))
    for path in outputs:
        print("->", path)
    print("Terminé.")


if __name__ == "__main__":
    main()
