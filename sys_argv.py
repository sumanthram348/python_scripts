import sys

"""
print(sys.argv)
print(sys.argv[0])
"""
"""
usr_str = sys.argv[1]
usr_cnf = sys.argv[2]

if usr_cnf == 'lower':
    print(usr_str.lower())
elif usr_cnf == 'upper':
    print(usr_str.upper())
elif usr_cnf == 'title':
    print(usr_str.title())
else:
    print("invalid option")
"""

if len(sys.argv) != 3 :
    print("usage:")
    print(f'{sys.argv[0]} <yuor_req_string> <lower|upper|title>')
    sys.exit()

usr_str = sys.argv[1]
usr_cnf = sys.argv[2]

if usr_cnf == 'lower':
    print(usr_str.lower())
elif usr_cnf == 'upper':
    print(usr_str.upper())
elif usr_cnf == 'title':
    print(usr_str.title())
else:
    print("invalid option")

