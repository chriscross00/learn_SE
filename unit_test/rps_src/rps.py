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
#     Game
#         -ifelse statements
#         -p==1 and c==2:
#             c wins
#         -p==1 and c==3:
#             p wins
#         -p==2 and c==3:
#             c wins
#         -p==2 and c==1:
#             p wins
#         -p==3 and c==2:
#             p wins
#         -p==3 and c==1:
#             c wins
#         -p==c:
#             draw

rps_dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

print(rps_dict.keys()[2])

def player_choice():
    player = input('Please choose your weapon:'
                   '\nRock: 1'
                   '\nPaper: 2'
                   '\nScissors: 3'
                   
                   '\ntest:')
    return print('Your weapon is:', player)

