import pyperclip as pc
from colorama import init,Fore
from pyfiglet import Figlet
from os import system

init(autoreset=True)

f = Figlet()


def clear():
    system('cls')


def mapPeek():

    selected = None    
    maps = [
        'de_cache','de_dust2','de_mirage',
        'de_overpass','de_nuke','de_inferno',
        'de_train','de_cbble'
        ]

    while not selected in maps:
        clear()
        print(f.renderText('Deathmatch'))
        print(Fore.YELLOW + 'Mapas')
        for map in maps:
            print(map)
        
        selected = input('\nEscribir nombre del mapa: ')

    return 'map ' + selected + ';'


def DM():

    clear()
    print(f.renderText('Deathmatch'))

    load_mode = f'game_type 1; game_mode 2;{mapPeek()}'
    dm = 'mp_ignore_round_win_conditions 1;mp_limitteams 0;mp_autoteambalance 0;bot_kick'

    clear()
    print(f.renderText('Deathmatch'))
    difficulty = 0
    print(Fore.YELLOW + 'BOTS')
    ct = int(input('Cantidad de ' + Fore.CYAN + 'CTs' + Fore.RESET + ': '))
    tt = int(input('Cantidad de ' + Fore.RED + 'TTs' + Fore.RESET + ': '))

    while not difficulty in range(1,5):
        clear()
        print(f.renderText('Deathmatch'))
        print(Fore.CYAN + 'CTs' + Fore.RESET + f': {ct}     ' + Fore.RED + 'TTs' + Fore.RESET + f': {tt}')
        print('\n0 = easy  1 = normal  2 = hard  3 = expert')
        difficulty = int(input('Dificultad: '))

    cmd = f'alias 1 "{dm}";' + 'alias 2 "' + 'bot_add_ct;'*ct + 'bot_add_t;'*tt + f'bot_difficulty {difficulty}' + '";'

    clear()
    return cmd + load_mode


def one_vs_one():

    vs = 'sv_cheats 1;sv_infinite_ammo 2;sv_alltalk 1;sv_deadtalk 1;bot_kick;mp_free_armor 1;mp_roundtime 60;mp_roundtime_defuse 60;mp_warmup_end 1;'

    clear()
    print(f.renderText('1 vs 1'))
    freezetime = int(input('Segundos de congelacion: '))
    delay = int(input('Segundos para comenzar la siguiente ronda: '))
    max_rounds = int(input('Rondas: '))
    overtime = int(input('Overtime (0 = no | 1 = si): '))

    cmd = vs + f'mp_freezetime {freezetime};' + f'mp_round_restart_delay {delay};' + f'mp_maxrounds {max_rounds};' + f'mp_overtime_enable {overtime};' + 'mp_restartgame 1;'

    clear()
    return cmd


def main():
    modos = ['Deathmatch','1v1']
    mode = 0
    f = Figlet()

    while not mode in range(1,(len(modos)+1)):
        clear()
        print(f.renderText('CSGO Control'))
        print(Fore.YELLOW + 'Select mode: ')

        for m in modos:
            print(f'{modos.index(m)+1} - {m}' )
        
        mode = int(input('\n'))

    if mode == 1:
        command = DM()
        print(f.renderText('Deathmatch'))
        print(Fore.GREEN + '# Comando copiado')
        print(Fore.YELLOW + '- Pegar en la consola de CSGO')
        print(Fore.YELLOW + '- Esperar que cargue el mapa')
        print(Fore.YELLOW + '- Escribir 1 en consola')
        print(Fore.YELLOW + '- Escribir 2 en consola')
        input('\nEnter para finalizar...')
    elif mode == 2:
        command = one_vs_one()
        print(f.renderText('1 vs 1'))
        print(Fore.GREEN + '# Comando copiado')
        print(Fore.YELLOW + '- Entrar a un mapa de CSGO')
        print(Fore.YELLOW + '- Pegar comando en consola')
        input('\nEnter para finalizar...')
    else:
        return

    pc.copy(command)
    clear()


main()
