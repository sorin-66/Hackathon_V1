"""
12 - Create a function that will take a string of text and return the index number of each letter in
the alphabet. For instance, if the input is “abc” it should return “1 2 3”; if the input is “xyz” it
should return “24 25 26”.
"""

def letter_to_number(string_input):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    nr =""
    for c in string_input.lower():
        if c != " ":
            nr = nr+str(alphabet.index(c)+1)+" "
        
    print(nr)

string = "Create a function"
letter_to_number(string)
