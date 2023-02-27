from utils import *
import os

def installGit() :
    clear()
    try :
        os.system("sudo apt-get install git -y")
    except Exception as e :
        print(f"Opss! Houve um erro: na instalação do git: {e}")
        next = input("Proceguir? [s/n]")

        if next == 'N' or next == 'n' :
            return exit()

def installPacSnap() :
    clear()
    os.system("sudo apt-get install snapd -y")

def installVim() :
    clear()
    os.system("sudo apt-get install vim -y")

def installNeovim() :
    clear()
    os.system("cd ~")
    os.system("wget -O neovim.deb https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.deb")
    os.system("sudo apt install ./neovim.deb")
    os.system("rm -rf ~/neovim.deb")

def installCurl() :
    clear()
    os.system("sudo apt-get install curl -y")

def installNode() :
    clear()
    os.system("sudo apt-get install nodejs -y")

def installMake() :
    clear()
    os.system("sudo apt-get install make -y")

def installWget() :
    clear()
    os.system("sudo apt-get install wget -y")

def installGimp() :
    clear()
    os.system("sudo apt-get install gimp -y")

def installSpotify() :
    clear()
    os.system("sudo apt-get install spotify -y")

def installBrave() :
    clear()
    os.system("sudo apt install apt-transport-https curl gnupg -y")
    os.system("curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -")
    os.system("sudo apt-get update")
    os.system("sudo apt install brave-browser -y")

def installFlatRemix() :
    clear()
    os.system('sudo add-apt-repository ppa:daniruiz/flat-remix -y')
    os.system('sudo apt update -y')
    os.system('sudo apt install flat-remix-gnome -y')
    os.system('gsettings set org.gnome.shell.extensions.user-theme name "Flat-Remix-Violet-Dark"')

def installFlatRemixGTK() : 
    clear()
    os.system('sudo add-apt-repository ppa:daniruiz/flat-remix -y && sudo apt-get update && sudo apt-get install flat-remix-gtk -y')
    os.system('gsettings set org.gnome.desktop.interface gtk-theme "Flat-Remix-GTK-Violet-Dark"')

def installFlatRemixIcons() :
    clear()
    os.system('cd ~')
    os.system('wget -O flat-remix-master.zip https://github.com/daniruiz/flat-remix/archive/master.zip')
    os.system('unzip flat-remix-master.zip')
    os.system('cd flat-remix-master')
    os.system('mv * ~/.local/share/icons/')
    os.system('gsettings set org.gnome.desktop.interface icon-theme "Flat-Remix-Violet-Dark"')
    os.system('rm -rf flat-remix-master')

def installFlatRemixLockScreen() :
    clear()
    os.system('sudo apt install libglib2.0-dev-bin imagemagick -y')
    os.system('git clone https://github.com/daniruiz/flat-remix-gnome')
    os.system('cd flat-remix-gnome')
    os.system('make && sudo make install -y')

def installLunarVim() :
    clear()
    os.system("LV_BRANCH='release-1.2/neovim-0.8' bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/fc6873809934917b470bff1b072171879899a36b/utils/installer/install.sh)")
