from utils import *
from softwares import *

clear()
title("LINUX")
print("# 0 - Sair          #")
print("# 1 - Novo sistema  #")
print("# 2 - Expecífico    #")
print("# 3 - Atualizar     #")
print("# 4 - NoiseReduction#")
print("#####################")
print("\n")
option = input("Opção: ")

clear()

if option == '0' :
    exit()

if option == '1' :
    installCurl()
    installGit()
    installNode()
    installMake()
    installWget()
    installPacSnap()
    installGimp()
    installSpotify()
    installBrave()
    installVim()
    installNeovim()
    installLunarVim()
    installFlatRemix()
    installFlatRemixLockScreen()
    installFlatRemixGTK()
    installFlatRemixIcons()

if option == '2' :
    title("Expecífico")
    print("# 0 - Sair               #")
    print("# 1 - Curl               #")
    print("# 2 - Git                #")
    print("# 3 - Node               #")
    print("# 4 - Make               #")
    print("# 5 - Snap               #")
    print("# 6 - Wget               #")
    print("# 7 - Gimp               #")
    print("# 8 - Spotify            #")
    print("# 9 - Brave Browser      #")
    print("# 10 - Vim               #")
    print("# 11 - Neovim            #")
    print("# 12 - Tema Flat Remix   #")
    print("# 13 - Tema Flat Remix GTK")
    print("# 14 - Tema Flat Remix Icon")
    print("# 15 - Flat Remix Lockscreen")
    print("# 16 - Lunarvim          #")
    print("##########################")
    print("\n")

    command = input("Selecione algum software que deseja baixar: ")

    if command == '0' :
        exit()

    if command == '1' :
        installCurl()

    if command == '2' :
        installGit()

    if command == '3' :
        installNode()

    if command == '4' :
        installMake()

    if command == '5' :
        installPacSnap()

    if command == '6' :
        installWget()

    if command == '7' :
        installGimp()

    if command == '8' :
        installSpotify()

    if command == '9' :
        installBrave()

    if command == '10' :
        installVim()

    if command == '11' :
        installNeovim()

    if command == '12' :
        installFlatRemix()

    if command == '13' :
        installFlatRemixGTK() 

    if command == '14' :
        installFlatRemixIcons()

    if command == '15' :
        installFlatRemixLockScreen()

    if command == '16' :
        installLunarVim()

if option == '3' :
    os.system('sudo apt-get update && sudo apt-get upgrade -y')

if option == '4' :
    try :
        os.system('pactl load-module module-echo-cancel aec_method=webrtc sink_properties=device.description="Noise_Reduction" aec_args="analog_gain_control=0\digital_gain_control=0"')
        print('Redução de ruído ativo')
    except :
        print('Não foi possivel')

clear()
