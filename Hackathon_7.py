"""
7 - Write a function that will take as an
input a person’s forename, surname, age, marital status and gender,
and the output an appropriate salutation.
For instance, if the input is [“Osamu”, “Dazai”, 21, “single”, “male”],
it should output “Dear Mr Osamu Dazai”.
If the input is [“Lucy Maud”, “Montgomery”, 50, “married”, “female”],
it should output “Dear Mrs Lucy Maud Montgomery”.
The full list of possible titles are [“Miss”, “Master”, “Mrs”, “Mr”].
"""

def title(input_list):
    forename = input_list[0]
    surname = input_list[1]
    age = input_list[2]
    marital_status = input_list[3]
    gender = input_list[4]
    personal_title = ""
    if age < 18 and gender == "male":
        personal_title = "Master"
    elif age >= 18 and gender == "male":
        personal_title = "Mr"
    elif marital_status == "single" and gender == "female":
        personal_title = "Miss"
    elif marital_status == "married" and gender == "female":
        personal_title = "Mrs"
    print(f"Dear {personal_title} {forename} {surname}")    
    
personal_info =  ['Osamu', 'Dazai', 21, 'single', 'male']
title(personal_info)
lady_info = ['Lucy Maud', 'Montgomery', 50, 'married', 'female']
title(lady_info)