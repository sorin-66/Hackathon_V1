'''
8 - Write a function that will play a rubbish version of the board game snakes and ladders
(https://en.wikipedia.org/wiki/Snakes_and_Ladders).
In this game, two players compete to get from square 1 to square 100.
Players take alternative turns, and move between 1 and 6 spaces based on a random
roll of the dice. If they land on a square that ends in 5 (e.g. 5, 15, 25, etc.),
they land on a ladder and move forward 9 spaces. If they land on a square that ends
in 0 (e.g. 10, 20, 30, etc.), they land on a snake and go back to the start. The game will be
explained using text commentary that you should print to the screen.
'''

from random import randint
player1_score = 0
player2_score = 0

print(
    '''
    In this game, two players compete to get from square 1 to square 100.
Players take alternative turns, and move between 1 and 6 spaces based on a random
roll of the dice. If they land on a square that ends in 5 (e.g. 5, 15, 25, etc.),
they land on a ladder and move forward 9 spaces. If they land on a square that ends
in 0 (e.g. 10, 20, 30, etc.), they land on a snake and go back to the start.
    ''')
player1 = input("Player 1 enter your name:  ")
print(f"Welcome {player1}")
player2 = input("Player 2 enter your name:  ")
print(f"Welcome {player2}")
user_input = input("Press any key to start! ")
game_on = True

def player_1(name1):
    global player1_score
    input(f"{name1}: roll the dice! ")
    dice_roll = randint(1,6)
    player1_score += dice_roll
    if player1_score%5 == 0 and player1_score%2 != 0:
        print(f"You've rolled {dice_roll} and you landed on square {player1_score} and that's a ladder you go ahead 9 squares and you're on square {player1_score+9} now")
        player1_score += 9
    elif player1_score%10 == 0:
        print(f"You've rolled {dice_roll} and you landed on square {player1_score} and that's a snake! Sorry you go back to start now")
        player1_score = 0
    else:
        print(f"You've rolled {dice_roll} and you're on square {player1_score}")
        
def player_2(name2):
    global player2_score
    input(f"{name2}: roll the dice! ")
    dice_roll = randint(1,6)
    player2_score += dice_roll
    if player2_score%5 == 0 and player2_score%2 != 0:
        print(f"You've rolled {dice_roll} and you landed on square {player2_score} and that's a ladder you go ahead 9 squares and you're on square {player2_score+9} now")
        player2_score += 9
    elif player2_score%10 == 0:
        print(f"You've rolled {dice_roll} and you landed on square {player2_score} and that's a snake! Sorry you go back to start now")
        player2_score = 0
    else:
        print(f"You've rolled {dice_roll} and you're on square {player2_score}")

while game_on:
    player_1(player1)
    if player1_score >= 100:
        print(f"Congratulation {player1} you won!")
        game_on = False
    player_2(player2)
    if player2_score >= 100:
        print(f"Congratulation {player2} you won!")
        game_on = False
    
    
