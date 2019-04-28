# Create a rock paper scissors game that you can play against a computer.

# Requirements:
#     Create dict of rps
#     Human input
#         -Ask for input from player
#         -Convert string to int
#     Computer choice
#         -randomly choice between 1-3
#         -1:rock
#         -2:paper
#         -3:scissors
#	Game
#		- Computer wins: {-1, 2}
#		- Person wins: {-2, 1}
#		- Draw: {0}

import random

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

def game(player):

	computer = random.choice(list(rps_dict.keys()))
	diff = rps_dict[player] - rps_dict[computer]

	print('\n\nComputer chose', computer)
	if diff in [-2, 1]:
		print('Player wins!')
	elif diff in [-1, 2]:
		print('Computer wins!')
	else:
		print('Draw!')

def play_game():
	game(player_choice())

play_game()
