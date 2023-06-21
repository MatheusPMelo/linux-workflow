from os import system
from ..utils.main import *

def installAsdf() :
    system('sudo apt-get install curl')
    system('sudo apt-get install git')
    system("git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.12.0")
    clear()
    print("Cole esse código no seu PATH:")
    print(". '$HOME/.asdf/asdf.sh'")
