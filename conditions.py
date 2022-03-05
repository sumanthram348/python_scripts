"""
import os

t_w = os.get_terminal_size().columns

given_str = input("Eneter the string:")
print(given_str)
usr_cnf = input("Enter if you want the string in title:")

if usr_cnf == "yes":
    print(given_str.title())
else:
    print(given_str)
"""
"""
my_list = [0, 2, 4, 6, 8, 10]
usr_num = eval(input("Enter the number between 1-10:"))

if usr_num in my_list:
    print(f'The entered num {usr_num} is in the list')
"""
"""
a = eval(input("Enter the number:"))
b = eval(input("Enter the number:"))

if (a > b):
    print(f'The number {a} is greter than {b}')
elif (a < b):
    print(f'The number {a} is lesser than {b}')
else:
    print(f'The number {a} is equal to {b}')
"""
"""
a = eval(input("Enter the number:"))
if a in [1,2,3,4,5,6,7,8,9,10]:
    if (a == 1):
        print("one")
    elif (a == 2):
        print("two")
    elif (a == 3):
        print("three")
    elif (a == 4):
        print("four")
    elif (a == 5):
        print("five")
    elif (a == 6):
        print("six")
    elif (a == 7):
        print("seven")
    elif (a == 8):
        print("eight")
    elif (a == 9):
        print("nine")
    else:
        print("ten")
else:
    print(f'The given {a} is out of range')
"""

a = eval(input("Enter the number:"))
d = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

if a in [1,2,3,4,5,6,7,8,9,10]:
    print(d.get(a))
else:
    print(f'The given {a} is out of range')
