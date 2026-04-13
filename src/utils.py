import sys
import termios
import tty
import os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')   # Windows
    else:
        os.system('clear') # Linux/Mac