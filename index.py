from src.components.menu import menu
from src.components.php import phpInstall
from src.components.composer import composerInstall
from src.components.asdf import installAsdf
from src.components.apache import apacheInstall

command = menu()

if command == 0 :
    exit()

if command == 2 :
    phpInstall()

if command == 3 :
    composerInstall()

if command == 4 :
    installAsdf()

if command == 5 :
    apacheInstall()
