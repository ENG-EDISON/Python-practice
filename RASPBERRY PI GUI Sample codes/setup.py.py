import sys
from cx_Freeze import setup, Executable
executables = [
    Executable('makingfiles.py', base=base)
]

setup(name='makingfiles',
      version='0.1',
      description='Sample makingfiles',
      executables=executables
      )
