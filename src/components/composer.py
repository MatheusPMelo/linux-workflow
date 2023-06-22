from ..utils.main import *
from .php import phpInstall
import subprocess

def composerInstall() :
    try:
        subprocess.check_call(['php', '--version'])
        system("wget https://raw.githubusercontent.com/composer/getcomposer.org/76a7060ccb93902cd7576b67264ad91c8a2700e2/web/installer -O - -q | php -- --quiet")
        system("sudo mv composer.phar /usr/local/bin/composer")
        print("Composer instalado com sucesso!!!")
        sleep(3)
        clear()
        exit()

    except subprocess.CalledProcessError:

        command:str = str(input("Deseja instalar PHP? [S/N]"))

        if command in ['S', 's', 'Y', 'y'] :
            phpInstall()
            composerInstall()
        else :
            exit()
        print("PHP não está instalado.")

