import os

def ct():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')