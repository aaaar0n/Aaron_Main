Assignment #1
# 1. Ask for interger input: 
# Condition:
# pag naglagay ng hnd intereger, back to start with 
# 2. Print Wrong input
# 3. If odd integer = print Fuzzy
# 4. If even integer = print Wuzzy
# 5. If divisible by 2 and 3 = FuzzyWuzzy

x = 1
while x <= 1:
    number = input("Integer Input: ")
    try:
        number = int(number)
        x += 1
    except:
        print("Please input an integer!!")

number = int(number)
if number >= 0 or number < 0:
    if number % 2 > 0:
        print("Fuzzy")
    elif number % 2 == 0:
        if number % 2 == 0 and number % 3 == 0:
            print("FuzzyWuzzy")
        else:
            print("Wuzzy")


# Assignment #2
# 1. put 2 integer input
# 2. Print even numbers in between
# Condition
# pag naglagay ng hnd intereger, back to start with 

x = 1
while x <= 1:
    number1 = input("Integer 1: ")
    number2 = input("Integer 2: ")
    try:
        number1 = int(number1)
        number2 = int(number2)
        number3 = list(range(number1, number2))
        c = number3.pop(0)
        x += 1
    except:
        print("Please input an integer!!")
for item in number3:
    if item % 2 == 0:
        print(item)