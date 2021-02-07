"""
15 - Write a function that can take two numbers as an input. The function should divide the first
number by the second number and establish if the output is an integer (whole number) or decimal.
For instance, if the input is “4” and “2”, the output should be “integer” (the answer is 2). If the
input is “3” and “2” the output should be “decimal” (the answer is 1.5).
"""

def normal(n1,n2):
    nr_1 = n1
    nr_2 = n2
    result = nr_1/nr_2

    if nr_1%nr_2 == 0:
        print(int(result))
    else:
        print(result)


normal(10,2)