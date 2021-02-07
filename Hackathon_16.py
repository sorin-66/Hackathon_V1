"""
16 - Write a program that can take two strings as an input. The program should swap around
every other letter in each string, and return both as an output. For instance, if the input is
“Osamu” and “Dazai”, the output should be “Oaaau” and “Dszmi”. If the two input strings are not
the same length, the outputs should be the length of the shortest string.
"""

string_1 = "Writing"
string_2 = "input"
string_1_swaped = ""
string_2_swaped = ""

counter = 0
if len(string_1) >= len(string_2):
    counter = len(string_2)
else:
    counter = len(string_2)
    
for i in range(counter):
    if i%2==0:
        string_1_swaped = string_1_swaped + string_2[i]
        string_2_swaped = string_2_swaped + string_1[i]
    else:
        string_1_swaped = string_1_swaped + string_1[i]
        string_2_swaped = string_2_swaped + string_2[i]
 
print(string_1)
print(string_2)
print(string_1_swaped)
print(string_2_swaped)