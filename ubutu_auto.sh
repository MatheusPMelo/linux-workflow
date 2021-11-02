#!bin/bash
clear
sudo apt-get update && sudo apt-get upgrade -y
#Comando para atualizar os repostitórios e os softwares.
clear
sudo apt install snap -y
#Comando para baixar o pacote snap.
clear
sudo apt install gimp -y
#Comando para baixar gimp.
clear
sudo snap install spotify -y
#Comando para baixar Spotify
clear
sudo apt install apt-transport-https curl gnupg -y
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser -y
#Comando para baixar o Brave
clear
sudo apt-get install flat-remix -y
sudo add-apt-repository ppa:daniruiz/flat-remix -y && sudo apt-get update && sudo apt-get install flat-remix-gtk -y && sudo apt-get install flat-remix -y
#Comando para baixar o tema flat remix
clear
uname -m
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo apt-get update
sudo apt-get install google-chrome-stable -y
#Comando para baixar o Google Chrome
clear
sudo snap install code --classic -y
#comando para baixar o VSCode
clear
sudo snap install sublime-text --classic -y
#Comando para baixar o Sublime Text
clear
sudo snap install pycharm-professional --classic -y
#Comando para baixar o PyCharm
clear
sudo snap install intellij-idea-ultimate --classic -y
#Comando para baixar o intelij IDEA
clear
sudo snap install android-studio --classic -y
#Comando para baixar o Android Studio
clear
sudo sh -c "echo 'deb http://linux.teamviewer.com/deb stable main' >> /etc/apt/sources.list.d/teamviewer.list"
sudo sh -c "echo 'deb http://linux.teamviewer.com/deb preview main' >> /etc/apt/sources.list.d/teamviewer.list"
wget -q https://download.teamviewer.com/download/linux/signature/TeamViewer2017.asc -O- | sudo apt-key add -
sudo apt-get update -y
sudo apt-get install teamviewer -y
#Comando para baixar o team Viewer
clear
sudo apt install gnome-tweak-tool -y
#Comando para baixar o gnome tweak tool
clear
sudo apt-get install git-all -y
#Comando para baixar o GIT
sudo apt-get update && sudo apt-get upgrade -y
clear