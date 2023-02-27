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
sudo apt install gnome-tweak-tool -y

#Comando para baixar o gnome tweak tool
clear
sudo apt-get install git-all -y

#Comando para baixar o GIT
sudo apt-get update && sudo apt-get upgrade -y
clear

#baixando nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
nvm install 16.14.2
clear

#baixando vuejs
cd ~
npm install -g @vue/cli
clear

#baixando composer 
sudo apt-get install composer -y
clear

#baixando lampp
sudo apt-get install lamp-server^
sudo chmod 777 /var/www/html
cd /var/www/html
wget https://files.phpmyadmin.net/phpMyAdmin/5.1.3/phpMyAdmin-5.1.3-all-languages.zip
unzip phpMyAdmin-5.1.3-all-languages.zip
mv phpMyAdmin-5.1.3-all-languages phpmyadmin
rm -rf phpMyAdmin-5.1.3-all-languages.zip
cd ~

#Baixando Filezilla
clear
sudo apt install filezilla -y

clear
sudo apt-get update && sudo apt-get upgrade -y
sudo apt autoremove

clear
echo 'TUDO PRONTO!'

