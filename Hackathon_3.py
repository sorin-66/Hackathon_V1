"""
3 - Write a function that can take as an input a date/time in UTC
(https://en.wikipedia.org/wiki/Coordinated_Universal_Time)
and a desired timezone to change the time to
(this should include the main four US timezones,  Pacific, Mountain,
Central and Eastern; China time; and British Summer Time.
An example input may be “18/02/2020 23:30” and “ET”.
"""

def date_change(date,offset):
    hour = int(date[0])
    day = date[2]
    month = date[3]
    year = date[4]
    new_hour = hour + offset
    if new_hour < 0:
        # this will be the previous day form UTC point of view
        final_hour = 24 + new_hour
        new_day = int(day)-1
        if day == "01":
            # here is month changing too
            new_day = days_back(month,year)
            new_month = int(month)-1
            new_year = year
            if month == "01":
                # here they waiting for the new year
                new_day = '31'
                new_month = '12'
                new_year = int(year)-1
    elif new_hour > 24:
        final_hour = new_hour - 24
        new_year = year
        if day == 28 and month == 2:
            if leap_year(year):
                new_day = int(day)+1
                new_month = 2
            else:
                new_day = 1
                new_month = 3
        if day == 29 and month == 2:            
            new_day = 1
            new_month = 3
        if day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
            new_day = day + 1
            new_month = month + 1
        else:
            new_day = day + 1
            new_month = month + 1
        if day == 31 and month !=12:
            new_day = 1
            new_month = month + 1
        elif day == 31 and month == 12:
            new_day = 1
            new_month = 1
            new_year = year +1

    else:
        final_hour = new_hour
        new_day = day
        new_month = month
        new_year = year
        print("no date change")
    return final_hour,new_day, new_month, new_year

def day_ahead():
    # intented to reduce de code on the date_change function
    pass

def days_back(month,year):
    global day_back
    nr_month = int(month)
    nr_year = int(year)
    new_day = day_back[nr_month]
    if nr_month == 3:
        if leap_year(nr_year):
            new_day = new_day + 1
    return new_day

def leap_year(year):
    #year = Which year do you want to check?

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# extracting time from the input format assuming that all is a string

def format_input(date_time):
    '''
    extracting date/time from the input format assuming that all is a string return a tuple
    '''
    hour = int(date_time[-5:-3])
    minutes = int(date_time[-2:])
    day = int(date_time[:2])
    month = int(date_time[3:5])
    year = int(date_time[6:10])
    return hour, minutes, day, month, year

# initial data
time_date_start = "31/12/2019 17:30"
time_zone_to_end = "CST"
# the above variables to change to play with the program
time_zone_offset = {"ET":-5, "CT":-6, "MT":-7, "PT":-8, "CST":8, "BST":1}
day_back = {1:31, 2:31, 3:28, 4:31, 5:30, 6:31, 7:30, 8:31, 9:31, 10:30, 11:31, 12:30}
# offset from the dictionary
print(time_date_start)
print(time_zone_to_end)

new_date_time = format_input(time_date_start)


# calculating time for specificated time zone

#time_in_time_zone = new_date_time[0] + time_zone_offset[time_zone_to_end]
#print(time_in_time_zone)
final = date_change(new_date_time,time_zone_offset[time_zone_to_end])
print(f" The new date and time is: {final[0]}:{new_date_time[1]}/{final[1]}/{final[2]}/{final[3]}")

