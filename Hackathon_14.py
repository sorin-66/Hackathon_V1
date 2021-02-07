"""
14 - Write a program that can take a list of numbers. If a number in the list is an even number it
should be added to a running total, if the number is odd it should be ignored. After processing all
the numbers in the list it should output the total (i.e. the sum of all the even numbers in the list).
"""

list_of_numbers =  [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]
sum = 0

for num in list_of_numbers:
    if num%2 == 0:
        sum += num

print(sum)