import os
import platform
import argparse
from compiler.compile import compile
import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python kedi.py <dosya.kedi>")
        sys.exit(1)

    kedi_file = sys.argv[1]
    if not kedi_file.endswith(".kedi"):
        print("Lütfen bir .kedi dosyası girin!")
        sys.exit(1)
    compile(kedi_file,"program.c")


if __name__ == "__main__":
    main()