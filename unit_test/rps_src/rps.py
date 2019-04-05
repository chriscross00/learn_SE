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


rps_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

def player_choice():
	player = int(input('\nPlease choose your weapon:'
				   '\nRock: 1'
				   '\nPaper: 2'
				   '\nScissors:3'
				   '\ntest: '))
	if player in rps_dict:
		return player
		print('Your weapon is: ',rps_dict[player])
	else:
		print('Please choose one of the weapons\n')
		player_choice()
		
def game(player, computer):

	diff = player - computer
	
	if diff in [-2, 1]:
		print('Player wins!')
	elif diff in [-1, 2]:
		print('Computer wins!')
	else:
		print('Draw!')
		

if name == __main__:
	player_choice()

