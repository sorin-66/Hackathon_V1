"""
10 - Create a function that takes time in the 24-hour clock (e.g. “23:30”) and
converts to the 12-
hour clock (e.g. “11:30 PM”). Print the result to screen. 
"""
from random import randint

def hour_convert(h,m):
    if h > 12:
        print(f"{h-12}:{m} P.M.")
    elif h == 12:
        print(f"12:{m} P.M.")
    else:
        print(f"{h}:{m} A.M.")
        
    
    

# generate a random hour
hour = randint(0,24)
minutes = randint(0,60)
time_to_convert = str(hour)+':'+str(minutes)
print(time_to_convert)
hour_convert(hour,minutes)


