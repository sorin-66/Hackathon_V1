"""
13 - Write a function that simulates a rubbish version of the game of snap! (https://
en.wikipedia.org/wiki/Snap_(card_game). There are two players each of
whom receives half a
deck of cards each (at random) and then plays one card at a time.
If the two players play a card
with the same value (e.g. two Kings or two 4’s) then the phrase “Snap!”
should be printed to
screen and the game ends.
"""

from random import shuffle

def snap():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    shuffle(cards)

    player_1 = []
    player_2 = []
    score_1 = 0
    score_2 = 0
    # deal the cards to the players
    for i in range(26):
        player_1.append(cards[2*i])
        player_2.append(cards[2*i+1])
        
    for i in range(26):
        print("Player 1  |   Player 2 ")
        print(f"    {player_1[i]}     |       {player_2[i]}")
        if player_1[i] == player_2[i]:
            print('Snap!')
            if score_1 > score_2:
                print(f" Player 1 win with {score_1} - {score_2}")
            elif score_1 < score_2:
                print(f" Player 2 win with {score_2} - {score_1}")
            else:
                print(f" Snap-Snap! nobody wins equal score: {score_1}")
            return
        else:
            if player_1[i] > player_2[i]:
                score_1 +=1
            else:
                score_2 +=1
            input("Press enter to continue:")
    
snap()                  

