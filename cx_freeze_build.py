import os

from cx_Freeze import Executable, setup

build_exe_options = {
    "packages": ["pygame"],  
    "include_files": ["assets/"],
}

executables = [Executable("main.py")]

setup(
    name="StellarRepair",
    version="1.0.0",
    description="Stellar Repair sokoban odissei",
    options={"build_exe": build_exe_options},
    executables=executables,
    author="Wesley Benvindo"
)