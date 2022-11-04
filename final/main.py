from gameplay import *
import os
from time import sleep
from sys import *

def mapping_hands(hand):
    if hand == 0:
        return 'Rock'
    elif hand == 1:
        return 'Paper'
    elif hand == 2:
        return 'Scizor'
    else:
        'undefined hand error, please correct code'

def clear_screen(wait):
        print(f'\n(Screen will be cleared in {wait} seconds)')
        sleep(wait) # Waiting for 4 seconds to clear the screen
        os.system('clear') # Clearing the Screen


def get_older_name():
    #to be done
    return 'teste'

def aplly_name(args):
    if args['name'] != False:
        return args['name']

    print(f'Before start playing choose your name:')
    name =  input()

    if name == '':
        name = get_older_name()

    return name

def read_args():
    args = list(argv)
    arg = {'name': False, 'score': False}

    for a in range(1, len(args)):
        if args[a].isnumeric() and arg['score'] == False:
            arg['score'] = int(args[a])
            if arg['score'] > 100:
                arg['score'] = 100
        elif arg['name'] == False:
            arg['name'] = args[a]

    return arg

def play(player, computer):
    win = player.show_winner(computer)
    my_hand = player.show_play()
    pc_hand = computer.show_play()
    if win == 'W':
        print(f'You won!!! Your hand ({mapping_hands(my_hand)}) is stronger then the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    elif win == 'L':
        print(f'You lost!!! Your hand ({mapping_hands(my_hand)}) is weaker then the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    else:
        print(f'You draw!!! Your hand ({mapping_hands(my_hand)}) is equal to the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)

def instructions():
    print("\nWinning Rules of the Rock paper scissor game as follows: \n"
                                    +"rock vs paper->paper wins \n"
                                    + "rock vs scissor->rock wins \n"
                                    +"paper vs scissor->scissor wins \n")
    clear_screen(10)


def read_input():
    while True:
        print("Enter choice \n 0 for rock \n 1 for paper \n 2 for scissor \n 3 for instructions \n 4 for exit ")

        players_choice =  input()

        if players_choice == '0' or players_choice == '1' or players_choice == '2' or players_choice == '3' or players_choice == '4':
            return int(players_choice)
        else:
            print('please choose from one of the valid options')



player = Gameplay()
computer = Gameplay()
args = read_args()
name = aplly_name(args)
print(f"""Your name is: {name} and the max score is: {args['score']}""")

while True:
    print('Welcome:')
    option = read_input()
    computer.set_play_random()

    if option == 0 or option == 1 or option == 2:
        player.set_play(option)
        play(player, computer)
    elif option == 3:
        instructions()
    else:
        break



'''
clears
mostrar pontuacao a cada jogada
alterar 0 1 2 3 para nomes starts with

nomes e ler args
mostrar a nossa jogada
funcao q fecha o jogo se score max for atingido

'''

