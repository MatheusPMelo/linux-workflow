from ..utils.main import *

def showMenu(error:bool = False):
    clear()
    if error:
        print("Valor inválido! Tente novamente.\n")

    print('Menu de instalação')
    print('1 - Instalação completa do workflow')
    print('2 - Instalar PHP')
    print('3 - Instalar Laravel')
    print('4 - Instalar ASDF-VM')
    print('5 - Apache')

def menu(error:bool = False) :
    showMenu(error)    

    command:int = int(input('Digite uma opção: '))
    
    if command not in [1, 2, 3, 4] :
        return menu(True)

    return command
