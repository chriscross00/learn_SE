# Create a rock paper scissors game that you can play against a computer.

import logging
import random


logging.basicConfig(filename='rps.log', level=logging.DEBUG,
					format='%(asctime)s:%(levelname)s:%(message)s')

rps_dict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}


def player_choice():
    player = input('\nPlease choose your weapon:'
				   '\nRock'
				   '\nPaper'
				   '\nScissors'
				   '\nPlayer: ')
    if player in rps_dict:
        return player
    else:
        print('Please choose one of the weapons\n')
        player_choice()

#a = player_choice()
#print(a)

def game(player):

    computer = random.choice(list(rps_dict.keys()))
    diff = rps_dict[player] - rps_dict[computer]

	print('\n\nComputer chose', computer)
	if diff in [-2, 1]:
		print('Player wins!')
		logging.debug('Player')
	elif diff in [-1, 2]:
		print('Computer wins!')
		logging.debug('Computer')
	else:
		print('Draw!')
		logging.debug('Draw')

    if diff in [-2, 1]:
        print('Player wins!')
    elif diff in [-1, 2]:
        print('Computer wins!')
    else:
        print('Draw!')

if __name__ == '__main__':
    game(player_choice())
