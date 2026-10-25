# -*- mode: python ; coding: utf-8 -*-
# Chemins relatifs : lancer depuis ce dossier avec
#   python -m PyInstaller CalculateurMasquesIPv4.spec

a = Analysis(
    ['calculateur_masques.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('translations.py', '.'),
        ('icon.ico', '.'),
        ('icon.png', '.'),
        ('banner.png', '.'),
    ],
    hiddenimports=['PIL', 'PIL.Image', 'PIL.ImageTk'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CalculateurMasquesIPv4',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
