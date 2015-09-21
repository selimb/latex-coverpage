import os
import shutil
import subprocess
import sys

def compile():
    """Compile into PDF."""
    cmd = ['pdflatex', '-halt-on-error', 'main.tex']
    rc = subprocess.call(cmd)
    if rc != 0:
        print('An error occurred')
        sys.exit(rc)

def main():
    compile()
    shutil.copy('main.pdf', '../cover.pdf')
if __name__ == '__main__':
    main()

