"""
2 - Write a function that takes in a user string input and reformats it into
A E S T H E T I C text.
Example:
Input > Hello World
Output > H e l l o W o r l d
"""

def aesthetic():
    string_input = input("Enter a string that will be formated in A E S T H E T I C text: \n")
    string_output = ""
    for character in string_input:
        string_output = string_output + character + " "
    print(string_output)

aesthetic()