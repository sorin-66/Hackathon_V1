'''
11 - Create a nested dictionary of modules. This should include a code, a module title, and the
number of teaching hours per lecturer involved. These lecturers should also be in a separate
nested dictionary of lecturers that also includes their ID and hourly rate of pay. Using both
dictionaries calculate how much each lecturer will be paid once all the modules are delivered and
print these to screen. There should be at least 4x lecturers and 4x modules.
'''

modules = {
    "French":{"code":1, "title":"Learn French","hours":10,"Teacher":"Monsieur Rovet"},
    "German":{"code":2, "title":"Learn German","hours":15,"Teacher":"Fur Elize"},
    "Spanish":{"code":3, "title":"Learn Spanish","hours":20,"Teacher":"Senor Sanchez"},
    "Japanese":{"code":4, "title":"Learn Japanese","hours":22,"Teacher":"Hirohito san"}
    }

lecturer = {
    "Monsieur Rovet":{"ID": 25, "pay_hour": 55},
    "Fur Elize":{"ID": 32, "pay_hour": 50},
    "Senor Sanchez":{"ID": 41, "pay_hour": 40},
    "Hirohito san":{"ID": 28, "pay_hour": 55},    
    }
    
# modules["French"]["Teacher"] - this is the key for lecturer dict to access the hour payment
# modules["French"]["hours"] - this is the amount of hours
# lecturer[modules["French"]["Teacher"]]["pay_hour"] - this is the payment per hour

for key in modules:
    total = modules[key]["hours"]*lecturer[modules[key]["Teacher"]]["pay_hour"]
    teacher_name = modules[key]["Teacher"]
    print(f"{teacher_name} was paid ${total}")
    
    
    
#print(modules["French"]["Teacher"])
#print(lecturer[modules["French"]["Teacher"]]["pay_hour"])
