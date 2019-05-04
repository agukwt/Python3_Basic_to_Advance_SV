import os
import sys

from cx_Freeze import setup, Executable


os.environ['TCL_LIBRARY'] = 'C:\\ProgramData\\Anaconda3\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\ProgramData\\Anaconda3\\tcl\\tk8.6'

build_exe_options = {}

base = None
if sys.platform == "win32":
        base = "Win32GUI"

directory_table = [
(
    "ProgramMenuFolder",
    "TARGETDIR",
    ".",
),
(
    "CalMyProgramMenu",
    "ProgramMenuFolder",
    "Calculator",
),
                ]

msi_data = {
    "Directory": directory_table,
}

setup(
    name = "calculator",
    version = "1.0.0",
    description = "My Calculator",
    options = {"build_exe": build_exe_options,
               'bdist_msi': { 'data': msi_data } },
    executables = [
        Executable(
            "calculator.py", 
            base=base,
            shortcutName="Calculator",
            shortcutDir="CalMyProgramMenu",
            )
        ])
