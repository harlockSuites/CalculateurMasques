import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import ipaddress
import csv
import datetime
import sys
import os
import shutil
import hashlib
import subprocess
import threading
import unicodedata
import urllib.request
from translations import T, LANGUAGES


def resource_path(filename):
    """Retourne le chemin absolu vers une ressource (fonctionne en script et en exe PyInstaller)."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, filename)

# ── Palette ────────────────────────────────────────────────────────────────────
DARK_BG  = "#1e1e2e"
PANEL_BG = "#2a2a3e"
ACCENT   = "#7c3aed"
ACCENT2  = "#a78bfa"
TEXT     = "#e2e8f0"
SUBTEXT  = "#94a3b8"
SUCCESS  = "#22c55e"
ERROR    = "#ef4444"
BORDER   = "#3f3f5a"
ROW_A    = "#2a2a3e"
ROW_B    = "#252535"

# ── Polices adaptées Linux ─────────────────────────────────────────────────────
# Priorité : Noto Sans > DejaVu Sans > Liberation Sans > sans-serif système
def best_font(size, bold=False, italic=False):
    weight = "bold"   if bold   else "normal"
    slant  = "italic" if italic else "roman"
    for family in ("Noto Sans", "DejaVu Sans", "Liberation Sans", "Ubuntu", "sans-serif"):
        try:
            f = tk.font.Font(family=family, size=size, weight=weight, slant=slant)
            if f.actual("family").lower() not in ("helvetica", "fixed", "courier"):
                return (family, size, weight) if not italic else (family, size, weight, "italic")
        except Exception:
            pass
    return ("sans-serif", size, weight)

def mono_font(size, bold=False):
    weight = "bold" if bold else "normal"
    for family in ("DejaVu Sans Mono", "Liberation Mono", "Noto Mono",
                   "Ubuntu Mono", "Courier New", "monospace"):
        try:
            f = tk.font.Font(family=family, size=size, weight=weight)
            if f.actual("family").lower() not in ("helvetica", "fixed"):
                return (family, size, weight)
        except Exception:
            pass
    return ("monospace", size, weight)


# ── Langue de départ et libellés de la liste ──────────────────────────────────
# Le coréen est écrit « Korean » dans la liste : sans police coréenne, « 한국어 » s'afficherait en carrés.
LANG_LABELS = {"ko": "Korean"}

def lang_label(code):
    return LANG_LABELS.get(code, LANGUAGES[code])

def lang_from_argv(argv=None):
    """Option --lang <code> (ou --lang=<code>) : langue de départ, utilisée par « Restart now » après l'installation d'une police."""
    args = sys.argv[1:] if argv is None else list(argv)
    for i, arg in enumerate(args):
        if arg == "--lang" and i + 1 < len(args) and args[i + 1] in LANGUAGES:
            return args[i + 1]
        if arg.startswith("--lang=") and arg[7:] in LANGUAGES:
            return arg[7:]
    return None


# ── État global ────────────────────────────────────────────────────────────────
current_lang    = lang_from_argv() or "fr"
history         = []
MAX_SUBNETS     = 65536   # plafond du tableau de découpage (au-delà, l'interface se fige)
_label_bindings = []


def t(key):
    return T[current_lang].get(key, T["fr"].get(key, f"[{key}]"))


def register(widget, key, attr="text"):
    _label_bindings.append((widget, key, attr))


def apply_language():
    for widget, key, attr in _label_bindings:
        try:
            widget.config(**{attr: t(key)})
        except Exception:
            pass
    lbl_header_title.config(text=t("app_title"))
    lbl_header_sub.config(text=t("app_subtitle"))
    notebook.tab(tab_calc,  text=t("tab_calc"))
    notebook.tab(tab_split, text=t("tab_split"))
    notebook.tab(tab_hist,  text=t("tab_hist"))

    split_col_keys = ["col_num","col_network","col_cidr","col_mask",
                      "col_first","col_last","col_broadcast","col_hosts"]
    for col_id, key in zip(COLS_SPLIT, split_col_keys):
        split_tree.heading(col_id, text=t(key))

    hist_col_keys = ["col_time","col_ip","col_res_network","col_mask",
                     "col_cidr","col_res_broadcast","col_res_hosts"]
    for col_id, key in zip(COLS_HIST, hist_col_keys):
        hist_tree.heading(col_id, text=t(key))

    lbl_status.config(text="")
    lbl_member_result.config(text="")
    lbl_split_status.config(text="")
    lbl_lang.config(text=t("lang_label"))
    _apply_result_conv_labels()


def set_language(lang_code):
    global current_lang
    current_lang = lang_code
    apply_language()


# ── Utilitaires ────────────────────────────────────────────────────────────────
def ip_to_bin(ip):
    return ".".join(f"{int(o):08b}" for o in str(ip).split("."))

def ip_to_hex(ip):
    return "0x" + "".join(f"{int(o):02X}" for o in str(ip).split("."))

def ip_to_decimal(ip):
    val = 0
    for o in str(ip).split("."):
        val = val * 256 + int(o)
    return str(val)

def is_wildcard_mask(text):
    """Vrai pour un masque inversé (ex. 0.0.0.255) : octets décimaux dont les 1 sont
    contigus en bas. 0.0.0.0 et 255.255.255.255 restent des masques normaux (/0 et /32)."""
    try:
        v = int(ipaddress.IPv4Address(text.strip()))
    except ValueError:
        return False
    inv = ~v & 0xFFFFFFFF
    if inv & (inv + 1) == 0:      # masque normal : 1 contigus en haut
        return False
    return v & (v + 1) == 0       # 0 contigus en haut, 1 en bas

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def make_copyable(widget, get_text):
    def show_menu(e):
        menu = tk.Menu(root, tearoff=0, bg=PANEL_BG, fg=TEXT,
                       activebackground=ACCENT, activeforeground="white",
                       font=best_font(9))
        menu.add_command(label=f"{t('menu_copy')}  « {get_text()} »",
                         command=lambda: copy_to_clipboard(get_text()))
        menu.tk_popup(e.x_root, e.y_root)
    widget.bind("<Button-3>", show_menu)


# ── Police du coréen (Linux) ───────────────────────────────────────────────────
# Sans police coréenne, le texte s'affiche en carrés. Quand on choisit le coréen, le logiciel regarde (fontconfig)
# si les caractères de l'interface sont couverts ; sinon une boîte de dialogue, en anglais (la langue n'est pas encore
# lisible), propose la commande à copier ou un téléchargement automatique (Noto Sans KR, licence SIL OFL, version
# figée, SHA-256 vérifié, dossier de polices de l'utilisateur : aucun droit administrateur), puis un redémarrage :
# un Tk déjà ouvert ne voit pas une police installée après son démarrage.
FONT_COMMIT   = "f8d157532fbfaeda587e826d4cd5b21a49186f7c"   # dépôt notofonts/noto-cjk
FONT_BASE_URL = f"https://raw.githubusercontent.com/notofonts/noto-cjk/{FONT_COMMIT}/Sans/"
FONT_PACKS = {
    "ko": {"family": "Noto Sans KR", "path": "SubsetOTF/KR/NotoSansKR-Regular.otf", "size": 4644748,
           "sha256": "69975a0ac8472717870aefeab0a4d52739308d90856b9955313b2ad5e0148d68"},
}
FONT_LICENSE = {"path": "LICENSE", "name": "LICENSE-OFL.txt", "size": 4301,
                "sha256": "6a73f9541c2de74158c0e7cf6b0a58ef774f5a780bf191f2d7ec9cc53efe2bf2"}
FONT_MISSING_THRESHOLD = 0.01   # au-delà de 1 % de caractères sans police, on propose la police
FONT_INSTALL_COMMANDS = (       # (outil du gestionnaire de paquets, commande pour tous les utilisateurs)
    ("apt-get", "sudo apt install fonts-noto-cjk"),
    ("dnf",     "sudo dnf install google-noto-sans-cjk-fonts"),
    ("pacman",  "sudo pacman -S noto-fonts-cjk"),
)

class FontInstallError(Exception):
    """Échec du téléchargement ou de l'installation d'une police (message en anglais, affiché tel quel)."""

def fonts_dir():
    data = os.environ.get("XDG_DATA_HOME") or os.path.join(os.path.expanduser("~"), ".local", "share")
    return os.path.join(data, "fonts", "calculateur-masques")

def font_install_command():
    """Commande à copier dans un terminal pour installer la police pour tous les utilisateurs, ou None."""
    for tool, command in FONT_INSTALL_COMMANDS:
        if shutil.which(tool):
            return command
    return None

def parse_fc_charsets(text):
    """Sortie de `fc-list --format '%{charset}\\n'` (plages hexadécimales « 20-7e a0-ff 3000 ») -> plages triées et fusionnées."""
    ranges = []
    for token in text.split():
        low, _, high = token.partition("-")
        try:
            ranges.append((int(low, 16), int(high or low, 16)))
        except ValueError:
            continue
    ranges.sort()
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    return merged

def missing_glyphs(code):
    """(caractères sans police, total) pour cette langue d'après fontconfig, ou None si `fc-list` est indisponible.
    Les polices installées se complètent : un caractère est couvert si l'une d'elles le contient."""
    import bisect
    chars = {c for v in T[code].values() for c in v if ord(c) > 127 and unicodedata.category(c)[0] == "L"}
    if not chars:
        return 0, 0
    try:
        done = subprocess.run(["fc-list", "--format", "%{charset}\n"], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    if done.returncode != 0 or not (done.stdout or "").strip():
        return None
    ranges = parse_fc_charsets(done.stdout)
    def covered(cp):
        i = bisect.bisect_right(ranges, (cp, float("inf"))) - 1
        return i >= 0 and ranges[i][0] <= cp <= ranges[i][1]
    return sum(1 for c in chars if not covered(ord(c))), len(chars)

def language_needs_font(code):
    """Vrai si une police est proposée pour cette langue et que trop de ses caractères n'en ont aucune.
    Si fontconfig est indisponible, on ne dérange pas l'utilisateur."""
    if code not in FONT_PACKS:
        return False
    result = missing_glyphs(code)
    return bool(result) and result[1] > 0 and result[0] / result[1] > FONT_MISSING_THRESHOLD

def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()

def _download_pinned(url, item, dest, progress=None):
    """Télécharge `url` vers `dest` et vérifie la somme SHA-256 fixée ; le fichier est supprimé si elle diffère."""
    part = dest + ".part"
    with urllib.request.urlopen(url, timeout=30) as resp, open(part, "wb") as out:
        total = int(resp.headers.get("Content-Length") or item["size"])
        done = 0
        for block in iter(lambda: resp.read(1 << 16), b""):
            out.write(block)
            done += len(block)
            if progress:
                progress(min(100, done * 100 // max(total, 1)))
    if _sha256_file(part) != item["sha256"]:
        os.remove(part)
        raise FontInstallError("The downloaded file does not match its expected checksum: it was deleted.")
    os.replace(part, dest)

def install_font(code, progress=None):
    """Télécharge la police de la langue (et sa licence) dans le dossier des polices de l'utilisateur, puis actualise
    fontconfig. Retourne True si le système voit maintenant la police, False sinon, None s'il ne peut pas le dire.
    FontInstallError (message en anglais) en cas d'échec."""
    import urllib.error
    pack = FONT_PACKS[code]
    folder = fonts_dir()
    try:
        os.makedirs(folder, exist_ok=True)
        for item, name, report in ((pack, os.path.basename(pack["path"]), progress),
                                   (FONT_LICENSE, FONT_LICENSE["name"], None)):
            dest = os.path.join(folder, name)
            if os.path.isfile(dest) and _sha256_file(dest) == item["sha256"]:
                continue   # déjà installée, intacte
            _download_pinned(FONT_BASE_URL + item["path"], item, dest, report)
    except FontInstallError:
        raise
    except urllib.error.URLError as exc:
        reason = str(getattr(exc, "reason", exc))
        if isinstance(exc, urllib.error.HTTPError):
            reason = f"HTTP {exc.code} {reason}"
        raise FontInstallError(f"Download failed: {reason}")
    except OSError as exc:
        if exc.filename:
            raise FontInstallError(f"Could not write the font: {exc.strerror or exc}")
        raise FontInstallError(f"Download failed: {exc}")
    try:
        subprocess.run(["fc-cache", "-f", folder], capture_output=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        pass
    result = missing_glyphs(code)
    if result is None:
        return None
    return not (result[1] and result[0] / result[1] > FONT_MISSING_THRESHOLD)

def relaunch_command(code):
    """Commande qui relance le logiciel dans la langue `code` (script Python ou exécutable PyInstaller)."""
    if getattr(sys, "frozen", False):
        return [sys.executable, "--lang", code]
    return [sys.executable, os.path.abspath(sys.argv[0]), "--lang", code]

def relaunch(code):
    env = dict(os.environ)
    env["PYINSTALLER_RESET_ENVIRONMENT"] = "1"   # exécutable « onefile » : le nouveau processus se déballe lui-même
    try:
        subprocess.Popen(relaunch_command(code), env=env, start_new_session=True)
    except OSError as exc:
        messagebox.showerror("Restart", f"Could not restart the software: {exc}")
        return
    root.destroy()

def show_font_dialog(code):
    """Boîte « Font needed » : explication, commande à copier, installation automatique, redémarrage."""
    pack     = FONT_PACKS[code]
    language = lang_label(code)
    win = tk.Toplevel(root)
    win.title("Font needed")
    win.configure(bg=DARK_BG)
    win.resizable(False, False)
    win.transient(root)

    def text(msg, fg=TEXT, font=None, pady=(0, 8)):
        lbl = tk.Label(win, text=msg, bg=DARK_BG, fg=fg, font=font or best_font(10),
                       wraplength=540, justify="left", anchor="w")
        lbl.pack(fill="x", padx=24, pady=pady)
        return lbl

    text(f"{language} needs a font that is not installed on this computer.", font=best_font(12, bold=True), pady=(20, 4))
    text("Without it, the text appears as empty squares.")

    command = font_install_command()
    status  = None
    if command:
        text("To install it for every user of this computer, run this command in a terminal:", fg=SUBTEXT, pady=(8, 4))
        row = tk.Frame(win, bg=DARK_BG)
        row.pack(fill="x", padx=24, pady=(0, 8))
        entry = tk.Entry(row, bg=PANEL_BG, fg=TEXT, readonlybackground=PANEL_BG, relief="flat",
                         font=mono_font(10), highlightthickness=1, highlightbackground=BORDER)
        entry.insert(0, command)
        entry.config(state="readonly")
        entry.pack(side="left", fill="x", expand=True, ipady=4)
        def copy_command():
            copy_to_clipboard(command)
            status.config(text="Command copied: paste it into a terminal.", fg=SUCCESS)
        tk.Button(row, text="Copy", command=copy_command, bg=PANEL_BG, fg=TEXT, font=best_font(9),
                  relief="flat", padx=10, pady=3, cursor="hand2",
                  activebackground=BORDER, activeforeground=TEXT).pack(side="left", padx=(8, 0))
    else:
        text("To install it for every user of this computer, install the \"Noto Sans CJK\" font package "
             "of your distribution.", fg=SUBTEXT, pady=(8, 8))

    mb = f"{pack['size'] / 1e6:.1f}"
    text(f"Or let the software download {pack['family']} ({mb} MB, SIL Open Font License) for your user only: "
         "no administrator rights are needed, and the file is checked against its SHA-256 checksum.", fg=SUBTEXT)
    text("The software must restart before it can use the font. The language is applied when it starts again.",
         fg=SUBTEXT)

    status = tk.Label(win, text="", bg=DARK_BG, fg=SUBTEXT, font=best_font(10, italic=True),
                      wraplength=540, justify="left", anchor="w")
    status.pack(fill="x", padx=24, pady=(0, 8))

    state = {"percent": 0, "result": "running", "error": None}

    def poll():
        if not win.winfo_exists():
            return
        if state["result"] == "running":
            status.config(text=f"Downloading… {state['percent']}%", fg=SUBTEXT)
            win.after(100, poll)
            return
        btn_install.config(state="normal")
        if state["error"]:
            status.config(text=state["error"], fg=ERROR)
        elif state["result"] is False:
            status.config(text="Font installed, but the system does not list it yet. Restart the software; "
                               "if the text still shows squares, log out and back in.", fg=ERROR)
            btn_restart.config(bg=ACCENT)
        else:
            status.config(text="Font installed. Restart the software to use it: the language is applied "
                               "when it starts again.", fg=SUCCESS)
            btn_restart.config(bg=ACCENT)

    def run_install():
        try:
            state["result"] = install_font(code, lambda p: state.__setitem__("percent", p))
        except FontInstallError as exc:
            state["error"], state["result"] = str(exc), "failed"
        except Exception as exc:
            state["error"], state["result"] = f"Install failed: {exc}", "failed"

    def start_install():
        btn_install.config(state="disabled")
        state.update(percent=0, result="running", error=None)
        threading.Thread(target=run_install, daemon=True).start()
        poll()

    buttons = tk.Frame(win, bg=DARK_BG)
    buttons.pack(pady=(0, 20))
    btn_install = tk.Button(buttons, text="Install automatically", command=start_install, bg=ACCENT, fg="white",
                            font=best_font(10, bold=True), relief="flat", padx=14, pady=5, cursor="hand2",
                            activebackground=ACCENT2, activeforeground="white")
    btn_install.pack(side="left", padx=6)
    btn_restart = tk.Button(buttons, text="Restart now", command=lambda: relaunch(code), bg=PANEL_BG, fg="white",
                            font=best_font(10, bold=True), relief="flat", padx=14, pady=5, cursor="hand2",
                            activebackground=ACCENT2, activeforeground="white")
    btn_restart.pack(side="left", padx=6)
    tk.Button(buttons, text="Close", command=win.destroy, bg=PANEL_BG, fg=SUBTEXT, font=best_font(10),
              relief="flat", padx=14, pady=5, cursor="hand2",
              activebackground=BORDER, activeforeground=TEXT).pack(side="left", padx=6)
    win.bind("<Escape>", lambda e: win.destroy())
    win._state, win._btn_install, win._btn_restart, win._status = state, btn_install, btn_restart, status

    win.update_idletasks()
    x = root.winfo_rootx() + (root.winfo_width()  - win.winfo_width())  // 2
    y = root.winfo_rooty() + (root.winfo_height() - win.winfo_height()) // 2
    win.geometry(f"+{max(x, 0)}+{max(y, 0)}")
    win.focus_set()
    return win


# ── Calcul principal ───────────────────────────────────────────────────────────
def do_calculate(event=None):
    ip_str   = entry_ip.get().strip()
    mask_str = entry_mask.get().strip()
    cidr_str = entry_cidr.get().strip()

    for lbl in result_values.values():
        lbl.config(text="—", fg=SUBTEXT)
    for lbl in conv_values.values():
        lbl.config(text="—", fg=SUBTEXT)
    lbl_status.config(text="", fg=TEXT)
    lbl_member_result.config(text="", fg=SUBTEXT)

    if is_wildcard_mask(mask_str):
        lbl_status.config(text=t("status_err_wildcard"), fg=ERROR)
        return

    cidr = None
    if cidr_str:
        try:
            cidr = int(cidr_str)
            if not 0 <= cidr <= 32:
                raise ValueError
        except ValueError:
            lbl_status.config(text=t("status_err_cidr"), fg=ERROR)
            return
    elif mask_str:
        try:
            net_test = ipaddress.IPv4Network(f"0.0.0.0/{mask_str}", strict=False)
            cidr = net_test.prefixlen
            entry_cidr.delete(0, tk.END)
            entry_cidr.insert(0, str(cidr))
        except ValueError:
            lbl_status.config(text=t("status_err_mask"), fg=ERROR)
            return
    else:
        lbl_status.config(text=t("status_err_prefix"), fg=ERROR)
        return

    try:
        ipaddress.IPv4Address(ip_str)
    except ValueError:
        lbl_status.config(text=t("status_err_ip"), fg=ERROR)
        return

    try:
        network = ipaddress.IPv4Network(f"{ip_str}/{cidr}", strict=False)
    except ValueError as e:
        lbl_status.config(text=str(e), fg=ERROR)
        return

    mask      = network.netmask
    wildcard  = network.hostmask
    net_addr  = network.network_address
    broadcast = network.broadcast_address

    if cidr == 32:
        first_host, last_host, num_hosts = net_addr, net_addr, 1
    elif cidr == 31:
        first_host, last_host, num_hosts = net_addr, broadcast, 2
    else:
        first_host = net_addr + 1
        last_host  = broadcast - 1
        num_hosts  = network.num_addresses - 2

    data = {
        "adresse_reseau": str(net_addr),
        "masque":         str(mask),
        "cidr":           f"/{cidr}",
        "wildcard":       str(wildcard),
        "premiere_hote":  str(first_host),
        "derniere_hote":  str(last_host),
        "broadcast":      str(broadcast),
        "nb_hotes":       f"{num_hosts:,}".replace(",", " "),
    }
    for key, val in data.items():
        result_values[key].config(text=val, fg=ACCENT2)
    result_values["broadcast"].config(fg=SUCCESS)

    lbl_plage.config(text=f"{net_addr}  —  {broadcast}", fg=ACCENT2)
    lbl_status.config(text=t("status_ok"), fg=SUCCESS)

    entry_mask.delete(0, tk.END)
    entry_mask.insert(0, str(mask))

    conv_values["dotted"].config( text=ip_str,             fg=ACCENT2)
    conv_values["binaire"].config(text=ip_to_bin(ip_str),  fg=ACCENT2)
    conv_values["hex"].config(    text=ip_to_hex(ip_str),  fg=ACCENT2)
    conv_values["decimal"].config(text=ip_to_decimal(ip_str), fg=ACCENT2)

    entry = {
        "_raw": {
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "ip": ip_str, "cidr": str(cidr),
            "net": str(net_addr), "mask": str(mask),
            "broadcast": str(broadcast), "hosts": str(num_hosts),
        }
    }
    history.append(entry)
    refresh_history()
    root._active_network = network


def do_clear():
    for w in (entry_ip, entry_cidr, entry_mask):
        w.delete(0, tk.END)
    for lbl in result_values.values():
        lbl.config(text="—", fg=SUBTEXT)
    for lbl in conv_values.values():
        lbl.config(text="—", fg=SUBTEXT)
    lbl_status.config(text="", fg=TEXT)
    lbl_plage.config(text="—", fg=SUBTEXT)
    lbl_member_result.config(text="", fg=SUBTEXT)
    root._active_network = None
    entry_ip.focus()


def on_cidr_change(*args):
    val = cidr_var.get()
    try:
        cidr = int(val)
        mask = str(ipaddress.IPv4Network(f"0.0.0.0/{cidr}").netmask)
        lbl_mask_preview.config(text=mask, fg=ACCENT2)
        if not entry_mask.get():
            entry_mask.delete(0, tk.END)
            entry_mask.insert(0, mask)
    except Exception:
        lbl_mask_preview.config(text="", fg=SUBTEXT)


def on_mask_change(*args):
    val = mask_var.get()
    if is_wildcard_mask(val):
        lbl_mask_preview.config(text="", fg=SUBTEXT)
        lbl_status.config(text=t("status_err_wildcard"), fg=ERROR)
        return
    if lbl_status.cget("text") == t("status_err_wildcard"):
        lbl_status.config(text="")   # le masque a été corrigé : on retire l'erreur
    try:
        net = ipaddress.IPv4Network(f"0.0.0.0/{val}", strict=False)
        lbl_mask_preview.config(text=f"/{net.prefixlen}", fg=ACCENT2)
        entry_cidr.delete(0, tk.END)
        entry_cidr.insert(0, str(net.prefixlen))
    except Exception:
        pass


# ── Appartenance ───────────────────────────────────────────────────────────────
def check_member():
    net = getattr(root, "_active_network", None)
    if net is None:
        lbl_member_result.config(text=t("member_no_calc"), fg=ERROR)
        return
    test_ip = entry_member.get().strip()
    try:
        ip = ipaddress.IPv4Address(test_ip)
        net_str = f"{net.network_address}/{net.prefixlen}"
        if ip in net:
            lbl_member_result.config(
                text=t("member_in").format(ip=test_ip, net=net_str), fg=SUCCESS)
        else:
            lbl_member_result.config(
                text=t("member_out").format(ip=test_ip, net=net_str), fg=ERROR)
    except ValueError:
        lbl_member_result.config(text=t("member_err_ip"), fg=ERROR)


# ── Découpage ──────────────────────────────────────────────────────────────────
def do_split():
    for row in split_tree.get_children():
        split_tree.delete(row)
    lbl_split_status.config(text="", fg=TEXT)

    net = getattr(root, "_active_network", None)
    if net is None:
        lbl_split_status.config(text=t("split_no_calc"), fg=ERROR)
        return

    val_str = entry_split_val.get().strip()
    try:
        val = int(val_str)
        if val < 1:
            raise ValueError
    except ValueError:
        lbl_split_status.config(text=t("split_err_val"), fg=ERROR)
        return

    try:
        import math
        if split_mode.get() == "subnets":
            bits_needed = math.ceil(math.log2(val)) if val > 1 else 0
            new_prefix  = net.prefixlen + bits_needed
            if new_prefix > 30:
                lbl_split_status.config(text=t("split_too_many"), fg=ERROR)
                return
        else:
            bits = math.ceil(math.log2(val + 2)) if val > 0 else 1
            new_prefix = 32 - bits
            if new_prefix < net.prefixlen:
                lbl_split_status.config(text=t("split_too_small"), fg=ERROR)
                return

        if 2 ** (new_prefix - net.prefixlen) > MAX_SUBNETS:
            lbl_split_status.config(
                text=t("split_cap").format(max=f"{MAX_SUBNETS:,}".replace(",", " ")),
                fg=ERROR)
            return

        subnets = list(net.subnets(new_prefix=new_prefix))
        for i, sn in enumerate(subnets):
            bc = sn.broadcast_address
            fh = sn.network_address + 1 if sn.prefixlen < 31 else sn.network_address
            lh = bc - 1 if sn.prefixlen < 31 else bc
            nh = sn.num_addresses - 2 if sn.prefixlen < 31 else sn.num_addresses
            tag = "even" if i % 2 == 0 else "odd"
            split_tree.insert("", "end", values=(
                i + 1, str(sn.network_address), f"/{sn.prefixlen}",
                str(sn.netmask), str(fh), str(lh), str(bc),
                f"{nh:,}".replace(",", " "),
            ), tags=(tag,))

        lbl_split_status.config(
            text=t("split_ok").format(n=len(subnets), p=subnets[0].prefixlen if subnets else "?"),
            fg=SUCCESS)
    except Exception as e:
        lbl_split_status.config(text=str(e), fg=ERROR)


# ── Historique ─────────────────────────────────────────────────────────────────
def refresh_history():
    for row in hist_tree.get_children():
        hist_tree.delete(row)
    for i, entry in enumerate(reversed(history)):
        r = entry["_raw"]
        tag = "even" if i % 2 == 0 else "odd"
        hist_tree.insert("", "end", values=(
            r["time"],
            r["ip"], r["net"], r["mask"],
            f"/{r['cidr']}", r["broadcast"], r["hosts"],
        ), tags=(tag,))


def hist_click(event):
    item = hist_tree.focus()
    if not item:
        return
    idx   = len(history) - 1 - hist_tree.index(item)
    entry = history[idx]
    r     = entry["_raw"]
    entry_ip.delete(0, tk.END)
    entry_ip.insert(0, r["ip"])
    entry_cidr.delete(0, tk.END)
    entry_cidr.insert(0, r["cidr"])
    notebook.select(tab_calc)
    do_calculate()


def clear_history():
    if not history:
        return
    if messagebox.askyesno(t("clear_hist_title"), t("clear_hist_msg")):
        history.clear()
        refresh_history()


# ── Export ─────────────────────────────────────────────────────────────────────
def _hist_rows():
    return [{
        t("col_time"):          e["_raw"]["time"],
        t("col_ip"):            e["_raw"]["ip"],
        t("col_res_network"):   e["_raw"]["net"],
        t("col_mask"):          e["_raw"]["mask"],
        t("col_cidr"):          f"/{e['_raw']['cidr']}",
        t("col_res_broadcast"): e["_raw"]["broadcast"],
        t("col_res_hosts"):     e["_raw"]["hosts"],
    } for e in history]

def export_csv():
    if not history:
        messagebox.showinfo(t("dlg_export"), t("export_empty"))
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV", "*.csv"), ("*", "*.*")],
        title=t("export_title_csv"))
    if not path:
        return
    rows = _hist_rows()
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    messagebox.showinfo(t("dlg_export"), t("export_ok").format(path=path))

def export_txt():
    if not history:
        messagebox.showinfo(t("dlg_export"), t("export_empty"))
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[(t("ft_text"), "*.txt"), ("*", "*.*")],
        title=t("export_title_txt"))
    if not path:
        return
    rows = _hist_rows()
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write("=" * 50 + "\n")
            for k, v in row.items():
                f.write(f"  {k:<26}: {v}\n")
        f.write("=" * 50 + "\n")
    messagebox.showinfo(t("dlg_export"), t("export_ok").format(path=path))


# ── À propos ───────────────────────────────────────────────────────────────────
def show_about():
    """Fenêtre « À propos » : bannière et message, dans la langue courante."""
    win = tk.Toplevel(root)
    win.title(t("btn_about"))
    win.configure(bg=DARK_BG)
    win.resizable(False, False)
    win.transient(root)

    try:
        win._banner = tk.PhotoImage(file=resource_path("banner.png"))
        tk.Label(win, image=win._banner, bg=DARK_BG).pack(padx=30, pady=(24, 10))
    except Exception:
        pass   # bannière absente : la fenêtre reste utilisable

    tk.Label(win, text=t("about_msg"), bg=DARK_BG, fg=TEXT,
             font=best_font(11), wraplength=520, justify="center"
             ).pack(padx=30, pady=(6, 16))

    btn_close = tk.Button(win, text=t("about_close"), command=win.destroy,
                          bg=ACCENT, fg="white", font=best_font(10),
                          relief="flat", padx=16, pady=4, cursor="hand2",
                          activebackground=ACCENT2, activeforeground="white")
    btn_close.pack(pady=(0, 22))
    win.bind("<Escape>", lambda e: win.destroy())

    win.update_idletasks()
    x = root.winfo_rootx() + (root.winfo_width()  - win.winfo_width())  // 2
    y = root.winfo_rooty() + (root.winfo_height() - win.winfo_height()) // 2
    win.geometry(f"+{max(x, 0)}+{max(y, 0)}")
    win.focus_set()
    try:
        win.grab_set()
    except tk.TclError:
        pass


# ══════════════════════════════════════════════════════════════════════
# CONSTRUCTION DE LA FENÊTRE
# ══════════════════════════════════════════════════════════════════════
root = tk.Tk()
import tkinter.font as tk_font  # noqa — nécessaire pour best_font()

root.title("IPv4 Subnet Calculator")
root.configure(bg=DARK_BG)
root.resizable(True, True)
root.minsize(620, 440)
root._active_network = None

# Icône de la fenêtre — iconphoto avec PIL pour conserver la pleine résolution
try:
    from PIL import Image, ImageTk
    _img = Image.open(resource_path("icon.png")).resize((512, 512), Image.LANCZOS)
    _icon = ImageTk.PhotoImage(_img)
    root.iconphoto(True, _icon)
except Exception:
    try:
        _icon = tk.PhotoImage(file=resource_path("icon.png"))
        root.iconphoto(True, _icon)
    except Exception:
        pass

w, h = 740, 680
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

# Style ttk
style = ttk.Style()
# Préférer un thème sombre disponible sur Linux
for theme in ("clam", "alt", "default"):
    if theme in style.theme_names():
        style.theme_use(theme)
        break

style.configure("TNotebook",       background=DARK_BG,  borderwidth=0)
style.configure("TNotebook.Tab",   background=PANEL_BG, foreground=SUBTEXT,
                padding=[14, 6],   font=best_font(10))
style.map("TNotebook.Tab",
          background=[("selected", ACCENT)],
          foreground=[("selected", "white")])
style.configure("Treeview",
                background=PANEL_BG, fieldbackground=PANEL_BG,
                foreground=TEXT, rowheight=26, font=mono_font(10))
style.configure("Treeview.Heading",
                background=BORDER, foreground=TEXT,
                font=best_font(9, bold=True))
style.map("Treeview",
          background=[("selected", ACCENT)],
          foreground=[("selected", "white")])

# ── En-tête ────────────────────────────────────────────────────────────────────
frame_header = tk.Frame(root, bg=ACCENT, pady=10)
frame_header.pack(fill="x")

lbl_header_title = tk.Label(frame_header, text=t("app_title"),
                             bg=ACCENT, fg="white", font=best_font(15, bold=True))
lbl_header_title.pack()
lbl_header_sub = tk.Label(frame_header, text=t("app_subtitle"),
                           bg=ACCENT, fg="#ddd6fe", font=best_font(9))
lbl_header_sub.pack()

# Sélecteur de langue
frame_lang = tk.Frame(frame_header, bg=ACCENT)
frame_lang.pack(pady=(6, 0))

lbl_lang = tk.Label(frame_lang, text=t("lang_label"),
                    bg=ACCENT, fg="#ddd6fe", font=best_font(9))
lbl_lang.pack(side="left", padx=(0, 6))

lang_names = [lang_label(c) for c in LANGUAGES]
lang_codes = list(LANGUAGES.keys())
lang_var   = tk.StringVar(value=lang_label(current_lang))

combo_lang = ttk.Combobox(frame_lang, textvariable=lang_var,
                           values=lang_names, state="readonly",
                           width=17, font=best_font(9))
combo_lang.pack(side="left")

btn_about = tk.Button(frame_lang, text=t("btn_about"), command=show_about,
                      bg="#6d28d9", fg="white", font=best_font(9),
                      relief="flat", padx=10, pady=1, cursor="hand2",
                      activebackground=ACCENT2, activeforeground="white")
btn_about.pack(side="left", padx=(12, 0))
register(btn_about, "btn_about")

def on_lang_change(event=None):
    name = lang_var.get()
    code = lang_codes[lang_names.index(name)]
    if language_needs_font(code):
        lang_var.set(lang_label(current_lang))   # la langue ne change pas tant que la police manque
        show_font_dialog(code)
        return
    set_language(code)

combo_lang.bind("<<ComboboxSelected>>", on_lang_change)

# ── Onglets ────────────────────────────────────────────────────────────────────
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab_calc  = tk.Frame(notebook, bg=DARK_BG)
tab_split = tk.Frame(notebook, bg=DARK_BG)
tab_hist  = tk.Frame(notebook, bg=DARK_BG)

notebook.add(tab_calc,  text=t("tab_calc"))
notebook.add(tab_split, text=t("tab_split"))
notebook.add(tab_hist,  text=t("tab_hist"))


# ══════════════════════════════════════════════════════════════════════
# ONGLET 1 — CALCULATEUR
# ══════════════════════════════════════════════════════════════════════

def make_scrollable(parent):
    container = tk.Frame(parent, bg=DARK_BG)
    container.pack(fill="both", expand=True)
    vscroll = tk.Scrollbar(container, orient="vertical",
                           bg=PANEL_BG, troughcolor=DARK_BG,
                           activebackground=ACCENT2)
    vscroll.pack(side="right", fill="y")
    canvas = tk.Canvas(container, bg=DARK_BG, highlightthickness=0,
                       yscrollcommand=vscroll.set)
    canvas.pack(side="left", fill="both", expand=True)
    vscroll.config(command=canvas.yview)
    inner  = tk.Frame(canvas, bg=DARK_BG)
    win_id = canvas.create_window((0, 0), window=inner, anchor="nw")

    def on_inner_cfg(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(win_id, width=max(canvas.winfo_width(), inner.winfo_reqwidth()))
    def on_canvas_cfg(e):
        canvas.itemconfig(win_id, width=max(e.width, inner.winfo_reqwidth()))

    inner.bind("<Configure>", on_inner_cfg)
    canvas.bind("<Configure>", on_canvas_cfg)

    # Molette souris : X11 émet Button-4 / Button-5, Wayland et Tk 8.7+ émettent MouseWheel.
    # L'événement va au widget sous le curseur (étiquette, cadre, champ), jamais au canevas lui-même :
    # on écoute donc partout (bind_all) et on ne réagit que pour les widgets posés dans ce canevas.
    def on_wheel(e):
        if not str(e.widget).startswith(str(canvas)):
            return                                 # tableaux, fenêtres « À propos » : à eux la molette
        if canvas.yview() == (0.0, 1.0):
            return                                 # tout tient dans la fenêtre : rien à défiler
        if e.num == 4:
            step = -1
        elif e.num == 5:
            step = 1
        else:
            step = -1 if e.delta > 0 else 1
        canvas.yview_scroll(step, "units")
    for seq in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
        canvas.bind_all(seq, on_wheel, add="+")
    return inner

inner_calc = make_scrollable(tab_calc)

# Saisie
frame_input = tk.Frame(inner_calc, bg=DARK_BG, pady=14, padx=30)
frame_input.pack(fill="x")

def lbl_e(parent, key, row, width=18):
    lbl = tk.Label(parent, text=t(key), bg=DARK_BG, fg=SUBTEXT,
                   font=best_font(10))
    lbl.grid(row=row, column=0, sticky="e", padx=(0, 10), pady=5)
    register(lbl, key)
    var = tk.StringVar()
    e = tk.Entry(parent, textvariable=var, width=width,
                 bg=PANEL_BG, fg=TEXT, insertbackground=TEXT,
                 font=mono_font(11), relief="flat",
                 highlightthickness=1, highlightbackground=BORDER,
                 highlightcolor=ACCENT)
    e.grid(row=row, column=1, sticky="w", pady=5)
    return e, var

entry_ip,   _        = lbl_e(frame_input, "lbl_ip",   0)
entry_cidr, cidr_var = lbl_e(frame_input, "lbl_cidr", 1)
entry_mask, mask_var = lbl_e(frame_input, "lbl_mask", 2, width=16)

lbl_mask_preview = tk.Label(frame_input, text="", bg=DARK_BG, fg=ACCENT2,
                             font=mono_font(10))
lbl_mask_preview.grid(row=1, column=2, sticky="w", padx=8)

lbl_hint = tk.Label(frame_input, text=t("hint_mask"),
                    bg=DARK_BG, fg=BORDER, font=best_font(8, italic=True))
lbl_hint.grid(row=2, column=2, sticky="w", padx=8)
register(lbl_hint, "hint_mask")

cidr_var.trace_add("write", on_cidr_change)
mask_var.trace_add("write", on_mask_change)

# Boutons
frame_btn = tk.Frame(inner_calc, bg=DARK_BG)
frame_btn.pack(pady=4)

btn_calc = tk.Button(frame_btn, text=t("btn_calculate"), command=do_calculate,
                     bg=ACCENT, fg="white", font=best_font(11, bold=True),
                     relief="flat", padx=14, pady=6, cursor="hand2",
                     activebackground=ACCENT2, activeforeground="white")
btn_calc.pack(side="left", padx=8)
register(btn_calc, "btn_calculate")

btn_clr = tk.Button(frame_btn, text=t("btn_clear"), command=do_clear,
                    bg=PANEL_BG, fg=SUBTEXT, font=best_font(11),
                    relief="flat", padx=14, pady=6, cursor="hand2",
                    activebackground=BORDER, activeforeground=TEXT)
btn_clr.pack(side="left", padx=8)
register(btn_clr, "btn_clear")

root.bind("<Return>", do_calculate)

lbl_status = tk.Label(inner_calc, text="", bg=DARK_BG, fg=TEXT,
                      font=best_font(9, italic=True))
lbl_status.pack()

# Résultats réseau
frame_res = tk.Frame(inner_calc, bg=PANEL_BG, padx=24, pady=14,
                     highlightthickness=1, highlightbackground=BORDER)
frame_res.pack(fill="x", padx=24, pady=(8, 4))

lbl_res_title = tk.Label(frame_res, text=t("res_title"), bg=PANEL_BG, fg=ACCENT2,
                          font=best_font(10, bold=True))
lbl_res_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 6))
register(lbl_res_title, "res_title")

RESULT_FIELDS_TOP = [
    ("adresse_reseau", "res_network"),
    ("masque",         "res_mask"),
    ("cidr",           "res_cidr"),
    ("wildcard",       "res_wildcard"),
    ("premiere_hote",  "res_first"),
    ("derniere_hote",  "res_last"),
]
RESULT_FIELDS_BOT = [
    ("broadcast", "res_broadcast"),
    ("nb_hotes",  "res_hosts"),
]

result_values = {}
result_labels = {}

def add_result_field(parent, data_key, trans_key, row):
    lbl = tk.Label(parent, text=t(trans_key) + " :", bg=PANEL_BG, fg=SUBTEXT,
                   font=best_font(10), anchor="e", width=30)
    lbl.grid(row=row, column=0, sticky="e", padx=(0, 12), pady=2)
    result_labels[data_key] = (lbl, trans_key)
    val_lbl = tk.Label(parent, text="—", bg=PANEL_BG, fg=SUBTEXT,
                       font=mono_font(11, bold=True), anchor="w", width=20)
    val_lbl.grid(row=row, column=1, sticky="w", pady=2)
    make_copyable(val_lbl, lambda l=val_lbl: l.cget("text"))
    result_values[data_key] = val_lbl

for i, (dk, tk_) in enumerate(RESULT_FIELDS_TOP):
    add_result_field(frame_res, dk, tk_, i + 1)

tk.Frame(frame_res, bg=BORDER, height=1).grid(
    row=len(RESULT_FIELDS_TOP) + 1, column=0, columnspan=2,
    sticky="ew", padx=4, pady=(6, 6))

for j, (dk, tk_) in enumerate(RESULT_FIELDS_BOT):
    add_result_field(frame_res, dk, tk_, len(RESULT_FIELDS_TOP) + 2 + j)

# Plage
frame_plage = tk.Frame(inner_calc, bg=DARK_BG, pady=4)
frame_plage.pack()
lbl_plage_title = tk.Label(frame_plage, text=t("lbl_range"), bg=DARK_BG, fg=SUBTEXT,
                            font=best_font(10))
lbl_plage_title.pack(side="left", padx=(0, 8))
register(lbl_plage_title, "lbl_range")
lbl_plage = tk.Label(frame_plage, text="—", bg=DARK_BG, fg=SUBTEXT,
                     font=mono_font(11, bold=True))
lbl_plage.pack(side="left")
make_copyable(lbl_plage, lambda: lbl_plage.cget("text"))

# Conversions
frame_conv = tk.Frame(inner_calc, bg=PANEL_BG, padx=24, pady=14,
                      highlightthickness=1, highlightbackground=BORDER)
frame_conv.pack(fill="x", padx=24, pady=(6, 4))

lbl_conv_title = tk.Label(frame_conv, text=t("conv_title"), bg=PANEL_BG,
                           fg=ACCENT2, font=best_font(10, bold=True))
lbl_conv_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 6))
register(lbl_conv_title, "conv_title")

CONV_FIELDS = [
    ("dotted",  "conv_dotted"),
    ("binaire", "conv_bin"),
    ("hex",     "conv_hex"),
    ("decimal", "conv_dec"),
]
conv_values = {}
conv_labels = {}

for i, (ck, tk_) in enumerate(CONV_FIELDS):
    lbl = tk.Label(frame_conv, text=t(tk_) + " :", bg=PANEL_BG, fg=SUBTEXT,
                   font=best_font(10), anchor="e", width=30)
    lbl.grid(row=i+1, column=0, sticky="e", padx=(0, 12), pady=2)
    conv_labels[ck] = (lbl, tk_)
    val_lbl = tk.Label(frame_conv, text="—", bg=PANEL_BG, fg=SUBTEXT,
                       font=mono_font(11, bold=True), anchor="w", width=38)
    val_lbl.grid(row=i+1, column=1, sticky="w", pady=2)
    make_copyable(val_lbl, lambda l=val_lbl: l.cget("text"))
    conv_values[ck] = val_lbl

# Appartenance
frame_member = tk.Frame(inner_calc, bg=PANEL_BG, padx=24, pady=14,
                        highlightthickness=1, highlightbackground=BORDER)
frame_member.pack(fill="x", padx=24, pady=(6, 4))

lbl_member_title = tk.Label(frame_member, text=t("member_title"), bg=PANEL_BG,
                             fg=ACCENT2, font=best_font(10, bold=True))
lbl_member_title.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 6))
register(lbl_member_title, "member_title")

lbl_member_lbl = tk.Label(frame_member, text=t("member_lbl"), bg=PANEL_BG,
                           fg=SUBTEXT, font=best_font(10))
lbl_member_lbl.grid(row=1, column=0, sticky="e", padx=(0, 10))
register(lbl_member_lbl, "member_lbl")

entry_member = tk.Entry(frame_member, width=18, bg=DARK_BG, fg=TEXT,
                        insertbackground=TEXT, font=mono_font(11),
                        relief="flat", highlightthickness=1,
                        highlightbackground=BORDER, highlightcolor=ACCENT)
entry_member.grid(row=1, column=1, sticky="w", padx=(0, 10))

btn_check = tk.Button(frame_member, text=t("btn_check"), command=check_member,
                      bg=ACCENT, fg="white", font=best_font(10),
                      relief="flat", padx=10, pady=3, cursor="hand2",
                      activebackground=ACCENT2, activeforeground="white")
btn_check.grid(row=1, column=2)
register(btn_check, "btn_check")

lbl_member_result = tk.Label(frame_member, text="", bg=PANEL_BG, fg=SUBTEXT,
                              font=best_font(10, italic=True))
lbl_member_result.grid(row=2, column=0, columnspan=3, sticky="w", pady=(6, 0))

lbl_footer = tk.Label(inner_calc, text=t("footer"), bg=DARK_BG, fg=BORDER,
                      font=best_font(8))
lbl_footer.pack(pady=(4, 10))
register(lbl_footer, "footer")


# ══════════════════════════════════════════════════════════════════════
# ONGLET 2 — DÉCOUPAGE
# ══════════════════════════════════════════════════════════════════════

frame_split_ctrl = tk.Frame(tab_split, bg=DARK_BG, padx=24, pady=16)
frame_split_ctrl.pack(fill="x")

lbl_split_title = tk.Label(frame_split_ctrl, text=t("split_title"),
                            bg=DARK_BG, fg=ACCENT2, font=best_font(12, bold=True))
lbl_split_title.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 6))
register(lbl_split_title, "split_title")

lbl_split_hint = tk.Label(frame_split_ctrl, text=t("split_hint"),
                           bg=DARK_BG, fg=SUBTEXT, font=best_font(9, italic=True))
lbl_split_hint.grid(row=1, column=0, columnspan=4, sticky="w", pady=(0, 10))
register(lbl_split_hint, "split_hint")

split_mode = tk.StringVar(value="subnets")
rb_subnets = tk.Radiobutton(frame_split_ctrl, text=t("split_radio_subnets"),
                             variable=split_mode, value="subnets",
                             bg=DARK_BG, fg=TEXT, selectcolor=PANEL_BG,
                             activebackground=DARK_BG, activeforeground=ACCENT2,
                             font=best_font(10))
rb_subnets.grid(row=2, column=0, sticky="w")
register(rb_subnets, "split_radio_subnets")

rb_hosts = tk.Radiobutton(frame_split_ctrl, text=t("split_radio_hosts"),
                           variable=split_mode, value="hosts",
                           bg=DARK_BG, fg=TEXT, selectcolor=PANEL_BG,
                           activebackground=DARK_BG, activeforeground=ACCENT2,
                           font=best_font(10))
rb_hosts.grid(row=3, column=0, sticky="w", pady=(4, 0))
register(rb_hosts, "split_radio_hosts")

lbl_split_val = tk.Label(frame_split_ctrl, text=t("split_lbl_val"),
                          bg=DARK_BG, fg=SUBTEXT, font=best_font(10))
lbl_split_val.grid(row=4, column=0, sticky="w", pady=(10, 0))
register(lbl_split_val, "split_lbl_val")

entry_split_val = tk.Entry(frame_split_ctrl, width=10, bg=PANEL_BG, fg=TEXT,
                            insertbackground=TEXT, font=mono_font(11),
                            relief="flat", highlightthickness=1,
                            highlightbackground=BORDER, highlightcolor=ACCENT)
entry_split_val.grid(row=4, column=1, sticky="w", padx=(8, 0), pady=(10, 0))

btn_split = tk.Button(frame_split_ctrl, text=t("btn_split"), command=do_split,
                      bg=ACCENT, fg="white", font=best_font(10, bold=True),
                      relief="flat", padx=12, pady=5, cursor="hand2",
                      activebackground=ACCENT2, activeforeground="white")
btn_split.grid(row=4, column=2, padx=(14, 0), pady=(10, 0))
register(btn_split, "btn_split")

lbl_split_status = tk.Label(tab_split, text="", bg=DARK_BG, fg=TEXT,
                             font=best_font(9, italic=True))
lbl_split_status.pack(anchor="w", padx=24, pady=(0, 2))

COLS_SPLIT = ("c1","c2","c3","c4","c5","c6","c7","c8")
frame_tree_split = tk.Frame(tab_split, bg=DARK_BG)
frame_tree_split.pack(fill="both", expand=True, padx=12, pady=(0, 10))

split_vsb = tk.Scrollbar(frame_tree_split, orient="vertical",  bg=PANEL_BG,
                          troughcolor=DARK_BG, activebackground=ACCENT2)
split_vsb.pack(side="right", fill="y")
split_hsb = tk.Scrollbar(frame_tree_split, orient="horizontal", bg=PANEL_BG,
                          troughcolor=DARK_BG, activebackground=ACCENT2)
split_hsb.pack(side="bottom", fill="x")

split_tree = ttk.Treeview(frame_tree_split, columns=COLS_SPLIT, show="headings",
                           yscrollcommand=split_vsb.set,
                           xscrollcommand=split_hsb.set)
split_vsb.config(command=split_tree.yview)
split_hsb.config(command=split_tree.xview)

split_col_keys = ["col_num","col_network","col_cidr","col_mask",
                  "col_first","col_last","col_broadcast","col_hosts"]
w_map_split = {"c1": 38, "c3": 52, "c8": 80}
for col_id, key in zip(COLS_SPLIT, split_col_keys):
    split_tree.heading(col_id, text=t(key))
    split_tree.column(col_id, width=w_map_split.get(col_id, 110),
                      anchor="center", stretch=True)
split_tree.tag_configure("even", background=ROW_A)
split_tree.tag_configure("odd",  background=ROW_B)
split_tree.pack(side="left", fill="both", expand=True)

def split_tree_copy(event):
    item = split_tree.identify_row(event.y)
    col  = split_tree.identify_column(event.x)
    if not item or not col:
        return
    val = split_tree.item(item, "values")[int(col.replace("#","")) - 1]
    menu = tk.Menu(root, tearoff=0, bg=PANEL_BG, fg=TEXT,
                   activebackground=ACCENT, activeforeground="white",
                   font=best_font(9))
    menu.add_command(label=f"{t('menu_copy')}  « {val} »",
                     command=lambda: copy_to_clipboard(val))
    menu.tk_popup(event.x_root, event.y_root)

split_tree.bind("<Button-3>", split_tree_copy)


# ══════════════════════════════════════════════════════════════════════
# ONGLET 3 — HISTORIQUE
# ══════════════════════════════════════════════════════════════════════

frame_hist_top = tk.Frame(tab_hist, bg=DARK_BG, padx=16, pady=10)
frame_hist_top.pack(fill="x")

lbl_hist_title = tk.Label(frame_hist_top, text=t("hist_title"),
                           bg=DARK_BG, fg=ACCENT2, font=best_font(12, bold=True))
lbl_hist_title.pack(side="left")
register(lbl_hist_title, "hist_title")

frame_hist_btns = tk.Frame(frame_hist_top, bg=DARK_BG)
frame_hist_btns.pack(side="right")

for lbl_key, cmd in [("btn_export_csv", export_csv),
                      ("btn_export_txt", export_txt),
                      ("btn_clear_hist", clear_history)]:
    btn = tk.Button(frame_hist_btns, text=t(lbl_key), command=cmd,
                    bg=PANEL_BG, fg=SUBTEXT, font=best_font(9),
                    relief="flat", padx=10, pady=4, cursor="hand2",
                    activebackground=BORDER, activeforeground=TEXT)
    btn.pack(side="left", padx=4)
    register(btn, lbl_key)

lbl_hist_hint = tk.Label(tab_hist, text=t("hist_hint"),
                          bg=DARK_BG, fg=SUBTEXT, font=best_font(8, italic=True))
lbl_hist_hint.pack(anchor="w", padx=16)
register(lbl_hist_hint, "hist_hint")

COLS_HIST = ("h1","h2","h3","h4","h5","h6","h7")
frame_hist_tree = tk.Frame(tab_hist, bg=DARK_BG)
frame_hist_tree.pack(fill="both", expand=True, padx=12, pady=(4, 10))

hist_vsb = tk.Scrollbar(frame_hist_tree, orient="vertical",  bg=PANEL_BG,
                         troughcolor=DARK_BG, activebackground=ACCENT2)
hist_vsb.pack(side="right", fill="y")
hist_hsb = tk.Scrollbar(frame_hist_tree, orient="horizontal", bg=PANEL_BG,
                         troughcolor=DARK_BG, activebackground=ACCENT2)
hist_hsb.pack(side="bottom", fill="x")

hist_tree = ttk.Treeview(frame_hist_tree, columns=COLS_HIST, show="headings",
                          yscrollcommand=hist_vsb.set,
                          xscrollcommand=hist_hsb.set)
hist_vsb.config(command=hist_tree.yview)
hist_hsb.config(command=hist_tree.xview)

hist_col_keys = ["col_time","col_ip","col_res_network","col_mask",
                 "col_cidr","col_res_broadcast","col_res_hosts"]
w_map_hist = {"h1": 70, "h5": 55}
for col_id, key in zip(COLS_HIST, hist_col_keys):
    hist_tree.heading(col_id, text=t(key))
    hist_tree.column(col_id, width=w_map_hist.get(col_id, 120), anchor="center")
hist_tree.tag_configure("even", background=ROW_A)
hist_tree.tag_configure("odd",  background=ROW_B)
hist_tree.pack(side="left", fill="both", expand=True)
hist_tree.bind("<Double-1>", hist_click)

def hist_tree_copy(event):
    item = hist_tree.identify_row(event.y)
    col  = hist_tree.identify_column(event.x)
    if not item or not col:
        return
    val = hist_tree.item(item, "values")[int(col.replace("#","")) - 1]
    menu = tk.Menu(root, tearoff=0, bg=PANEL_BG, fg=TEXT,
                   activebackground=ACCENT, activeforeground="white",
                   font=best_font(9))
    menu.add_command(label=f"{t('menu_copy')}  « {val} »",
                     command=lambda: copy_to_clipboard(val))
    menu.tk_popup(event.x_root, event.y_root)

hist_tree.bind("<Button-3>", hist_tree_copy)


# ── Mise à jour des étiquettes de résultats/conversions ───────────────────────
def _apply_result_conv_labels():
    for dk, (lbl, tk_) in result_labels.items():
        lbl.config(text=t(tk_) + " :")
    for ck, (lbl, tk_) in conv_labels.items():
        lbl.config(text=t(tk_) + " :")


entry_ip.focus()
if language_needs_font(current_lang):   # lancé avec --lang ko sans la police : on rouvre la boîte
    root.after(400, lambda: show_font_dialog(current_lang))
root.mainloop()
