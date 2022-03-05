"""
>>> import os
>>> os.system("ls")
case_conversion.py  data_structures.py             getpass.py  math_module.py  os_path.py    os_system.py        __pycache__  string_formatting.py  sys_argv.py  type_cast.py
conditions.py       different_string_operation.py  io_eval.py  operators.py    os_simple.py  platform_module.py  sample.py    sumanth               sys.py
0
>>> os.system("mkdir jyothsna")
0
>>> os.system("ls")
case_conversion.py  data_structures.py             getpass.py  jyothsna        operators.py  os_simple.py  platform_module.py  sample.py             sumanth      sys.py
conditions.py       different_string_operation.py  io_eval.py  math_module.py  os_path.py    os_system.py  __pycache__         string_formatting.py  sys_argv.py  type_cast.py
0
>>> os.system("pwd")
/home/ec2-user/Automation
0
"""

import os
"""
cmd = "date"
rt = os.system(cmd)

if rt == 0:
    print("Your command was successful")
else:
    print("Your command was not successful")
"""

import os
import platform

usr_str = platform.system()

if usr_str == "Windows":
    os.system("cls")
else:
    os.system("clear")

