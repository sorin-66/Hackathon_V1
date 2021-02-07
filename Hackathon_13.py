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
    # deal the cards to the players
    for i in range(len(cards)-1):
        player_1.append(cards[i])
        player_2.append(cards[i+1])
        
    for i in range(26):
        print("Player 1  |   Player 2 ")
        print(f"    {player_1[i]}     |       {player_2[i]}")
        if player_1[i] == player_2[i]:
            print('Snap!')
            return
        else:
            input("Press enter to continue:")
    
snap()                  
