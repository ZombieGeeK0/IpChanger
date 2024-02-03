# importamos las librerías necesarias
from colorama import Fore, Back
import os, sys

# definimos los colores de colorama
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# hacemos las funciones principales
def salir():
    print(Fore.RESET + Back.RESET)
    os.system('clear')
    sys.exit()

def volver_menu():
    print(Fore.BLUE + Back.RESET + '\n[#] Presiona ENTER para volver al menú.')
    choice = input(Fore.RED + Back.RESET + '[#] ====>  ')
    menu()

def error():
    print(Fore.BLUE + Back.RESET + '\n[#] Error. Presiona ENTER para volver al menú.')
    choice = input(Fore.RED + Back.RESET + '[#] ====>  ')
    menu()

def cambiar_ip():
    os.system('clear')
    title = '''
\033[31m ▄████▄   ██░ ██  ▄▄▄       ███▄    █ \033[34m  ▄████ ▓█████  ██▓ ██▓███  
\033[31m▒██▀ ▀█  ▓██░ ██▒▒████▄     ██ ▀█   █ \033[34m ██▒ ▀█▒▓█   ▀ ▓██▒▓██░  ██▒
\033[31m▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒\033[34m▒██░▄▄▄░▒███   ▒██▒▓██░ ██▓▒
\033[31m▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒\033[34m░▓█  ██▓▒▓█  ▄ ░██░▒██▄█▓▒ ▒
\033[31m▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░\033[34m░▒▓███▀▒░▒████▒░██░▒██▒ ░  ░
\033[31m░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ \033[34m ░▒   ▒ ░░ ▒░ ░░▓  ▒▓▒░ ░  ░
\033[31m  ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░\033[34m  ░   ░  ░ ░  ░ ▒ ░░▒ ░     
\033[31m░         ░  ░░ ░  ░   ▒      ░   ░ ░ \033[34m░ ░   ░    ░    ▒ ░░░       
\033[31m░ ░       ░  ░  ░      ░  ░         ░ \033[34m      ░    ░  ░ ░           
\033[31m░                                                                 
'''
    print(title)

    print(Fore.RED + Back.RESET + '\n[#] Ingresa tu IP.')
    ip = input(Fore.BLUE + Back.RESET + '[#] ====>  ')

    print(Fore.RED + Back.RESET + '\n[#] Ingresa la IP  a cambiar.')
    ip_change = input(Fore.BLUE + Back.RESET + '[#] ====>  ')

    print(Fore.RED + Back.RESET + '\n[#] El DNS se cambiará a 8.8.8.8.')
    print(Fore.BLUE + Back.RESET + '[#]> -------------------------------------------------------------- <[#]')
    os.system('cd .. && cd ..')
    os.system('auto lo')
    os.system('iface lo inet loopback')
    os.system('allow-hotplug eth0')
    os.system('iface eth0 inet static')
    os.system(f'address {ip}')
    os.system(f'gateway {ip_change}')
    os.system('service networking restart')
    os.system('nano /etc/resolv.conf')
    os.system('nameserver 8.8.8.8')
    print(Fore.BLUE + Back.RESET + '[#]> -------------------------------------------------------------- <[#]')
    print(Fore.RED + Back.RESET + '\n[#] Proceso finalizado.')

    print(Fore.BLUE + Back.RESET + '\n[#] Presiona ENTER para volver al menú.')
    choice = input(Fore.RED + Back.RESET + '[#] ====>  ')
    menu()

    

# hacemos el menú
def menu():
    os.system('clear')
    title = '''
    \033[31m ██▓ ██▓███   ▄████▄   ██░ ██  ▄▄▄     \033[34m  ███▄    █   ▄████ ▓█████  ██▀███  
    \033[31m▓██▒▓██░  ██▒▒██▀ ▀█  ▓██░ ██▒▒████▄   \033[34m  ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
    \033[31m▒██▒▓██░ ██▓▒▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄ \033[34m ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
    \033[31m░██░▒██▄█▓▒ ▒▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██\033[34m ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
    \033[31m░██░▒██▒ ░  ░▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██\033[34m▒▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
    \033[31m░▓  ▒▓▒░ ░  ░░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█\033[34m░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    \033[31m ▒ ░░▒ ░       ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ \033[34m░░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
    \033[31m ▒ ░░░       ░         ░  ░░ ░  ░   ▒  \033[34m    ░   ░ ░ ░ ░   ░    ░     ░░   ░ 
    \033[31m ░           ░ ░       ░  ░  ░      ░  \033[34m░         ░       ░    ░  ░   ░     
    \033[31m             ░                         \033[34m                                    
    '''
    print(title)

    options = '''
[00]: Salir.
[01]: Volver al menú.
[02]: Cambiar IP y DNS. (ASEGÚRATE DE EJECUTAR EL PROGRAMA DESDE SU CARPETA EN LA CARPETA HOME DE LINUX).
'''
    print(Fore.BLUE + Back.RESET + options)

    choice = input(Fore.RED + Back.RESET + '[#] ====>  ')

    if choice == '00':
        salir()

    elif choice == '01':
        volver_menu()

    elif choice == '02':
        cambiar_ip()

    else:
        error()

menu()