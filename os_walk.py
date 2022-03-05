"""
import os

path = "/home/ec2-user/Automation"
print(path)

#for each in os.walk(path):
#    print(each)

for p,d,f in os.walk(path):
    print(p,f)
   # print(d)
   # print(f)
"""
"""
for p,d,f in os.walk(path):
    if len(f) != 0:
        print(d,f)
"""
"""
for p,d,f in os.walk(path):
    if len(f) != 0:
        print(p)
        for each in f:
            print(each)
            print(os.path.join(p,each))
"""
"""
import os
import platform
import string

req_file = input("Enter the file to search:")

if platform.system() == "Windows":
    pd_names = string.ascii_uppercase
    vd_names = []
    for each in pd_name:
        if os.path.exists(each+":\\"):
            vd_names.append(each+":\\")
    print(vd_names)
    for each_d in vd_names:
        for r,d,f in os.walk(each_d):
            for each_f in f:
                if each_f == req_file:
                    print(os.path.join(r,each_f))

else:
    for r,d,f in os.walk("/"):
        for each_f in f:
            if each_f == req_file:
                print(os.path.join(r,each_f))
"""

import os

path = input("Enter your path:")

if os.path.exists(path):
    print(f"Given path {path} is a valid path")
    if os.path.isfile(path):
        print(f" the {path} is a file path")
    else:
        print(f" the {path} is directory path")
else:
    print(f" the {path} is not existing path")

