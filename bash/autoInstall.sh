#/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

# Dependencies
sudo apt-get install git make nodejs python pip

# Install Theme
sudo add-apt-repository ppa:daniruiz/flat-remix -y
sudo apt update -y
sudo apt install flat-remix-gnome -y
gsettings set org.gnome.shell.extensions.user-theme name "Flat-Remix-Violet-Dark"

# Install GTK theme
sudo add-apt-repository ppa:daniruiz/flat-remix -y && sudo apt-get update && sudo apt-get install flat-remix-gtk -y
gsettings set org.gnome.desktop.interface gtk-theme "Flat-Remix-GTK-Violet-Dark"

# Install Icons
cd ~
wget -O flat-remix-master.zip https://github.com/daniruiz/flat-remix/archive/master.zip
unzip flat-remix-master.zip
cd flat-remix-master
mv * ~/.local/share/icons/ 
gsettings set org.gnome.desktop.interface icon-theme "Flat-Remix-Violet-Dark"
rm -rf flat-remix-master# Install Login theme

# ????
sudo apt install libglib2.0-dev-bin imagemagick -y
git clone https://github.com/daniruiz/flat-remix-gnome
cd flat-remix-gnome
make && sudo make install -y
