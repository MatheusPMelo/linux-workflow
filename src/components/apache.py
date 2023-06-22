from os import system


def apacheInstall():
    system('sudo apt-get install apache2')
    system('sudo chomod -R 777 /var/www/html')
