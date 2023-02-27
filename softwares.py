from utils import *
import os

def installGit() :
    clear()
    try :
        os.system("sudo apt-get install git -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação do git: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()

def installPacSnap() :
    clear()
    try :
        os.system("sudo apt-get install snapd -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()

def installVim() :
    clear()
    try :
        os.system("sudo apt-get install vim -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installNeovim() :
    clear()
    try :
        os.system("cd ~")
        os.system("wget -O neovim.deb https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.deb")
        os.system("sudo apt install ./neovim.deb")
        os.system("rm -rf ~/neovim.deb")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()



def installCurl() :
    clear()
    try:
        os.system("sudo apt-get install curl -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installNode() :
    clear()
    try:
        os.system("sudo apt-get install nodejs -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installMake() :
    clear()
    try :
        os.system("sudo apt-get install make -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installWget() :
    clear()
    try :
        os.system("sudo apt-get install wget -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installGimp() :
    clear()
    try :
        os.system("sudo apt-get install gimp -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installSpotify() :
    clear()
    try:
        os.system("sudo apt-get install spotify -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installBrave() :
    clear()
    try :
        os.system("sudo apt install apt-transport-https curl gnupg -y")
        os.system("curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -")
        os.system("sudo apt-get update")
        os.system("sudo apt install brave-browser -y")
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installFlatRemix() :
    clear()
    try :
        os.system('sudo add-apt-repository ppa:daniruiz/flat-remix -y')
        os.system('sudo apt update -y')
        os.system('sudo apt install flat-remix-gnome -y')
        os.system('gsettings set org.gnome.shell.extensions.user-theme name "Flat-Remix-Violet-Dark"')
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installFlatRemixGTK() : 
    clear()
    try :
        os.system('sudo add-apt-repository ppa:daniruiz/flat-remix -y && sudo apt-get update && sudo apt-get install flat-remix-gtk -y')
        os.system('gsettings set org.gnome.desktop.interface gtk-theme "Flat-Remix-GTK-Violet-Dark"')
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installFlatRemixIcons() :
    clear()
    try :
        os.system('cd ~')
        os.system('wget -O flat-remix-master.zip https://github.com/daniruiz/flat-remix/archive/master.zip')
        os.system('unzip flat-remix-master.zip')
        os.system('cd flat-remix-master')
        os.system('mv * ~/.local/share/icons/')
        os.system('gsettings set org.gnome.desktop.interface icon-theme "Flat-Remix-Violet-Dark"')
        os.system('rm -rf flat-remix-master')
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installFlatRemixLockScreen() :
    clear()
    try :
        os.system('sudo apt install libglib2.0-dev-bin imagemagick -y')
        os.system('git clone https://github.com/daniruiz/flat-remix-gnome')
        os.system('cd flat-remix-gnome')
        os.system('make && sudo make install -y')
    except Exception as e :
        print(f"Opss! Houve um erro na instalação: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


def installLunarVim() :
    clear()
    try :
        os.system("LV_BRANCH='release-1.2/neovim-0.8' bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/fc6873809934917b470bff1b072171879899a36b/utils/installer/install.sh)")
    except Exception as e :
        print(f"Opss! Houve um problema na instalação do lunarvim: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()

def installPhp() :
    clear()

    try :
        os.system('sudo add-apt-repository ppa:ondrej/php')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install php7.4-fpm php7.4-cli php7.4-bcmath php7.4-bz2 php7.4-curl php7.4-dba php7.4-gd php7.4-imap php7.4-intl php7.4-json php7.4-mbstring php7.4-mysql php7.4-odbc php7.4-opcache php7.4-pgsql php7.4-snmp php7.4-soap php7.4-tidy php7.4-xml php7.4-zip')
    except Exception as e :
        print(f"Opss! Houve um problema na instalação do lunarvim: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()

def installComposer() :
    clear()

    try :
        os.system(`php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"`)
        os.system(`php -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"`)
        os.system("php composer-setup.php")
        os.system(`php -r "unlink('composer-setup.php');"`)
    except Exception as e :
        print(f"Opss! Houve um problema na instalação do lunarvim: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()


