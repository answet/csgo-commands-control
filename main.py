import pyperclip as pc
from colorama import init,Fore
from pyfiglet import Figlet
from os import system

init(autoreset=True)


def clear():
    system('cls')


def mapPeek():

    clear()
    selected = None    
    maps = [
        'de_cache','de_dust2','de_mirage',
        'de_overpass','de_nuke','de_inferno',
        'de_train','de_cbble'
        ]

    while not selected in maps:
        clear()
        print(Fore.YELLOW + 'Mapas')
        for map in maps:
            print(map)
        
        selected = input('\nEscribir nombre del mapa: ')

    clear()
    return 'map ' + selected + ';'


def DM(mapa):

    load_mode = f'game_type 1; game_mode 2;{mapa}'
    dm = 'mp_ignore_round_win_conditions 1;bot_kick;mp_limitteams 0;mp_autoteambalance 0;'

    clear()
    difficulty = 0
    print(Fore.YELLOW + 'BOTS')
    ct = int(input('Cantidad de ' + Fore.CYAN + 'CTs' + Fore.RESET + ': '))
    tt = int(input('Cantidad de ' + Fore.RED + 'TTs' + Fore.RESET + ': '))

    while not difficulty in range(1,5):
        clear()
        print(Fore.CYAN + 'CTs' + Fore.RESET + f': {ct}     ' + Fore.RED + 'TTs' + Fore.RESET + f': {tt}')
        print('\n0 = easy  1 = normal  2 = hard  3 = expert')
        difficulty = int(input('Dificultad: '))

    cmd = 'alias ok "' + dm + 'bot_add ct;'*ct + 'bot_add t;'*tt + f'bot_difficulty {difficulty}' + '";'

    clear()
    return cmd + load_mode


def Practica(): #TODO
    pass


def main():
    modos = ['Deathmatch']
    mode = 0
    f = Figlet()

    while not mode in range(1,(len(modos)+1)):
        clear()
        print(f.renderText('CSGO Control'))
        print(Fore.YELLOW + 'Select mode: ')

        for m in modos:
            print(f'{modos.index(m)+1} - {m}' )
        
        mode = int(input())
    
    mapa = mapPeek()

    if mode == 1:
        command = DM(mapa)
    else:
        return

    pc.copy(command)


main()

print(Fore.GREEN + '# Comando copiado')
print(Fore.YELLOW + '- Pegar en la consola de CSGO')
print(Fore.YELLOW + '- Esperar que cargue el mapa')
print(Fore.YELLOW + '- Escribir ok en consola')
input('\nEnter para finalizar...')