from ..utils.main import *

def phpInstall():
    version = float(input('Qual a versão deseja instalar do php? '))

    php_input=f"sudo apt-get install php{version}-fpm php{version}-cli php{version}-cgi php{version}-bcmath php{version}-bz2 php{version}-curl php{version}-dba php{version}-gd php{version}-imap php{version}-intl php{version}-json php{version}-mbstring php{version}-mysql php{version}-odbc php{version}-opcache php{version}-pgsql php{version}-snmp php{version}-soap php{version}-tidy php{version}-xml php{version}-zip"

    system('sudo add-apt-repository ppa:ondrej/php')
    system('sudo apt-get update')
    system(php_input)
