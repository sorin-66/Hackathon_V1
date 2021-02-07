'''
4 - Write a function that simulates a guessing game. Player two should pick a number between 1
and 10. Player one then should guess the number.
If they guess the right number they win. If they
guess the wrong number, Player two should say if their number is higher or lower. Player one
should guess again and keep guessing until they get the right number.
'''

player_2_nr = int(input("Player 2 choose a number to be guessed: "))
print("\n\n\n\n\n\n\n\n\n\n")

score = 0
guessed = False

while not guessed:
	guess= int(input("Player 1 enter your guess: "))
	if guess > player_2_nr:
		print("Your guess is too high. Guess again!")
		score += 1
	elif guess < player_2_nr:
		print("Your guess is too low. Guess again!")
		score +=1
	else:
		score += 1
		print(f"Yes you guessed. Your final score is {score}")
		guessed = True
		
		
