import os
import subprocess
# clear

def clear() :
    os.system('clear')

def title(title) :
    print("###### ", title," ######")

def checkInstall(soft, command) :
    try :
        subprocess.check_output([soft, command])
        print(soft, " está instalado")
        next = input("Proceguir [s/n]: ")

        if next == 'n' or next == 'N' :
            exit()

    except subprocess.CalledProcessError :
        print(soft," não está instalado")
