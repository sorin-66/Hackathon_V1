'''
6 - Write a function that will round a float in reverse.
If the input has a decimal greater than or
equal to .5 then in should round down. If the decimal is less than .5 it should round up.
'''

number_2 = 1.2345
number_1 = 9.8765
# transform the float in a string
num1_str = str(number_1)
# find the index of the floating point in the string
floatpoint = num1_str.index(".")
# get the first character after the floating point and transform in an integer
first_decimal = int(num1_str[floatpoint+1])
if first_decimal >= 5:
    rounded_number = int(num1_str[:floatpoint])
else:
    rounded_number = int(num1_str[:floatpoint])+1
    
print(rounded_number)