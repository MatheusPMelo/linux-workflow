from src.components.menu import menu
from src.components.php import phpInstall
from src.components.lavarel import installLaravel
from src.components.asdf import installAsdf
command = menu()

if command == 2 :
    phpInstall()

if command == 3 :
    installLaravel()

if command == 4 :
    installAsdf()
