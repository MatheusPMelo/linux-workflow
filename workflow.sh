#!bin/bash

clear

sudo apt-get update && sudo apt-get upgrade

clear

sudo apt install snap
sudo apt-get update

clear

sudo apt-get install tree
sudo apt-get update

clear

sudo apt-get install git
sudo apt-get update

clear

sudo apt-get install lamp-server^
sudo chmod 777 /var/www/html
sudo apt-get update

clear

sudo apt install apt-transport-https curl gnupg
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser
sudo apt-get update

clear

sudo snap install code --classic
sudo apt-get update

clear

sudo snap install sublime-text --classic
sudo apt-get update

clear

sudo add-apt-repository ppa:mattrose/terminator
sudo apt-get update
sudo apt install terminator
sudo apt-get update

clear

sudo apt-get install flat-remix -y
sudo add-apt-repository ppa:daniruiz/flat-remix -y && sudo apt-get update && sudo apt-get install flat-remix-gtk -y && sudo apt-get install flat-remix -y
sudo apt-get update
