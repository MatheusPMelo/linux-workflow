from utils import *
from softwares import *

clear()
title("LINUX")
print("# 0 - Sair          #")
print("# 1 - Novo sistema  #")
print("# 2 - Expecífico    #")
print("# 3 - Atualizar     #")
print("#####################")
print("\n")
option = input("Opção: ")

clear()

if option == '0' :
    exit()

if option == '1' :
    print("Faz Isso")

if option == '2' :
    title("Expecífico")
    print("# 0 - Sair               #")
    print("# 1 - Gimp               #")
    print("# 2 - Spotify            #")
    print("# 3 - Brave Browser      #")
    print("##########################")
    print("\n")

    command = input("Selecione algum software que deseja baixar: ")
    
    if command == '0' :
        exit()

    if command == '1' :
        installGimp()

    if command == '2' :
        installSpotify()

    if command == '3' :
        installBrave()

if option == '3' :
    os.system('sudo apt-get update && sudo apt-get upgrade -y')
