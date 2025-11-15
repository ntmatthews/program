# PyInstaller spec for building a single-file, GUI binary
# Build with: pyinstaller portable_database.spec

block_cipher = None

import sys
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('tkinter')

a = Analysis(
    ['portable_database.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PortableDB',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # GUI app
    disable_windowed_traceback=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PortableDB'
)

app = BUNDLE(
    coll,
    name='PortableDB.app',
    icon=None,
    bundle_identifier='com.portable.db',
)
