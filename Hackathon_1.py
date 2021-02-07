"""
1 - Write a program that will take multiple user inputs, the first being the user's name, followed by
the user's location and finally take something the user likes. Then output a string that contains
this information. e.g.
Output > Hello my name is Jordan, I live in the UK and I like classical music.

"""

user_name = input("Enter your name: \n")
user_location = input("Where are you from? \n")
user_like = input("What do you like? (music, sports, movies, or other hobbies) : \n")

print(f"Hello my name is {user_name}, I live in {user_location} and I like {user_like}. ")