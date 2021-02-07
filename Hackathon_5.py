"""
5 - Write a function that can take a date input and a person’s date of birth,
and then calculate how old they are.
An example input may be “18/02/2020” and “13/06/1981” (returning “38 years old”.
"""

today_date = "14/07/2020"
#today_date = "18/02/2020"
b_day_date = "13/06/1981"
#today_date = "12/06/2020"
#today_date = "14/06/2020"
# today_date = "20/08/2020"

def format_input(date):
    '''
    extracting time from the input format assuming that all is a string return a tuple
    '''
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[6:10])
    return day, month, year

today = format_input(today_date)
b_day = format_input(b_day_date)
print(today)
print(b_day)

age = today[2]-b_day[2] #year
print(age)
if today[1]>b_day[1]: # month
	print(age)
elif today[1]<b_day[1]:#month
	age =age-1
	print(age)
else: # month
	if today[0] > b_day[0]:
		print(age)
		print(today[0])
	elif today[0] < b_day[0]:
		age = age-1
		print(age)
	else:
		print(age)
		print(" Happy birthday!")
	
print(f" You're {age} years old")

