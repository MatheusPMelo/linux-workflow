from utils import *
import os
import subprocess

def installGit() :
    os.system("sudo apt-get install git -y")

def installCurl() :
    os.system("sudo apt-get install curl -y")

def installGimp() :
    os.system("sudo apt-get install gimp -y")

def installSpotify() :
    os.system("sudo apt-get install spotify -y")

def installBrave() :
    checkInstall('curl', '--version')
    os.system("sudo apt install apt-transport-https curl gnupg -y")
    os.system("curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -")
    os.system("sudo apt-get update")
    os.system("sudo apt install brave-browser -y")
        
