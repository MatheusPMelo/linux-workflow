#!bin/bash

clear

echo "=======MENU======="
echo "1 - atualização geral"
echo "2 - Baixar o Snap"
echo "3 - Baixar o Gimp"
echo "4 - Baixar o Spotify"
echo "5 - Baixar o Navegador Brave"
echo "6 - Baixar o tema Flat Remix"
echo "7 - Baixar o Google Chrome"
echo "8 - Baixar o VS Code"
echo "9 - Baixar o Sublime Text"
echo "10 - Baixar o PyCharm"
echo "11 - Baixar o InteliJ IDEA"
echo "12 - Baixar o Android Studio"
echo "13 - Baixar o Tema Viewer"
echo "14 - Baixar o Tweak Tool"
echo "15 - Baixar o GIT"

read menu

clear

if [ $menu = 1 ]; then
		clear
		sudo apt-get update && sudo apt-get upgrade 
		#Comando para atualizar os repostitórios e os softwares.

elif [ $menu = 2 ]; then
		clear
		sudo apt install snap 
		#Comando para baixar o pacote snap.

elif [ $menu = 3 ]; then
		clear
		sudo apt install gimp 
		#Comando para baixar gimp.

elif [ $menu = 4 ]; then
		clear
		sudo snap install spotify 
		#Comando para baixar Spotify

elif [ $menu = 5 ]; then
		clear
		sudo apt install apt-transport-https curl gnupg

		curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -

		echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list

		sudo apt update

		sudo apt install brave-browser
	
		#Comando para baixar o Brave

elif [ $menu = 6 ]; then
		clear
		sudo apt-get install flat-remix -y

		sudo add-apt-repository ppa:daniruiz/flat-remix -y && sudo apt-get update && sudo apt-get install flat-remix-gtk -y && sudo apt-get install flat-remix -y

		#Comando para baixar o tema flat remix

elif [ $menu = 7 ]; then
		clear
		uname -m

		sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

		wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

		sudo apt-get update

		sudo apt-get install google-chrome-stable

		#Comando para baixar o Google Chrome

elif [ $menu = 8 ]; then
		clear
		sudo snap install code --classic

		#comando para baixar o VSCode

elif [ $menu = 9 ]; then
		clear
		
		sudo snap install sublime-text --classic
		#Comando para baixar o Sublime Text

elif [ $menu = 10 ]; then
		clear

		sudo snap install pycharm-professional --classic
		#Comando para baixar o PyCharm

elif [ $menu = 11 ]; then
		clear

		sudo snap install intellij-idea-ultimate --classic
		#Comando para baixar o intelij IDEA

elif [ $menu = 12 ]; then
		clear

		sudo snap install android-studio --classic
		#Comando para baixar o Android Studio

elif [ $menu = 13 ]; then
		clear

		sudo sh -c "echo 'deb http://linux.teamviewer.com/deb stable main' >> /etc/apt/sources.list.d/teamviewer.list"

		sudo sh -c "echo 'deb http://linux.teamviewer.com/deb preview main' >> /etc/apt/sources.list.d/teamviewer.list"

		wget -q https://download.teamviewer.com/download/linux/signature/TeamViewer2017.asc -O- | sudo apt-key add -

		sudo apt-get update

		sudo apt-get install teamviewer
		#Comando para baixar o team Viewer


elif [ $menu = 14 ]; then
		clear

		sudo apt install gnome-tweak-tool
		#Comando para baixar o gnome tweak tool

elif [ $menu = 15 ]; then
		clear

		sudo apt-get install git-all
		#Comando para baixar o GIT

else

	clear

fi