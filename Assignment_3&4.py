# Assignment #3
# 1. 5 employees in list firstname lastname age. User will input above input
# 2. print first/last name of age above 20. 
# function
# pagkuha ng age
# pagbuo ng name

employee_list = [
    {'firstname': "Aaron", 'lastname': "dela Cruz", 'age': 12},
    {'firstname': "Joelle", 'lastname': "Villanueva", 'age': 18},
    {'firstname': "Edward", 'lastname': "Domingo", 'age': 21},
    {'firstname': "Miguel", 'lastname': "Santos", 'age': 26},
    {'firstname': "Joelo", 'lastname': "Villanueva", 'age': 23},
]

x = 0
y = 0
for index in employee_list:
    y += 1
def print_name():
    employee_firstname = employee_list[x]['firstname']
    employee_lastname = employee_list[x]['lastname']
    employee_fullname = str(employee_firstname) + " " + str(employee_lastname) + " "
    print(employee_fullname + str(employee_list[x]['age']))

while True:
    user_input = input("Minimum age limit: ")
    try:
        number = int(user_input)
        break
    except:
        print("Please input a valid integer!!")

while x < y:
    employee_age = employee_list[x]['age']
    if int(user_input) < int(employee_age):
        print_name()
    x += 1

##while x < y:
    #employee_age = employee_list[0 + x]['age']
    #if int(employee_age) > int(user_input):
    #    print(employee_list[0 + x]['firstname'] + " " + employee_list[0 + x]['lastname'] + " " + str(employee_age))
    #x += 1

# Assignment #4
# 1. same 5 employee list
# 2. print according to age ascending order

employee_list = [
    {'firstname': "Aaron", 'lastname': "dela Cruz", 'age': 12},
    {'firstname': "Joelle", 'lastname': "Villanueva", 'age': 18},
    {'firstname': "Edward", 'lastname': "Domingo", 'age': 21},
    {'firstname': "Miguel", 'lastname': "Santos", 'age': 26},
    {'firstname': "Joelo", 'lastname': "Villanueva", 'age': 23},
]
from operator import itemgetter
while True:
    user_input = input("Arrange age to ascending order? (Y/N)").upper()
    try:
        answer = str(user_input)
        pass
    except:
        print("Please type Y or N only")
    if answer == 'Y':
        sorted_employee_list = sorted(employee_list, key=itemgetter('age'))
        ascending = True
        break
    elif answer == 'N':
        ascending = False
        break
    else:
        print("Please type Y or N only")
x = 0
y = 0

for index in employee_list:
    y += 1
def print_normal_name():
    employee_firstname = employee_list[x]['firstname']
    employee_lastname = employee_list[x]['lastname']
    employee_fullname = str(employee_firstname) + " " + str(employee_lastname) + " "
    print(employee_fullname + str(employee_list[x]['age']))

def print_sorted_name():
    employee_firstname = sorted_employee_list[x]['firstname']
    employee_lastname = sorted_employee_list[x]['lastname']
    employee_fullname = str(employee_firstname) + " " + str(employee_lastname) + " "
    print(employee_fullname + str(sorted_employee_list[x]['age']))

while True:
    user_input = input("Minimum age limit: ")
    try:
        number = int(user_input)
        break
    except:
        print("Please input a valid integer!!")

if ascending == True:
    while x < y:
        employee_age = sorted_employee_list[x]['age']
        if int(user_input) < int(employee_age):
            print_sorted_name()
        x += 1
elif ascending == False:
    while x < y:
        employee_age = employee_list[x]['age']
        if int(user_input) < int(employee_age):
            print_normal_name()
        x += 1
