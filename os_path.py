>>> import os
>>> path="/home/ec2-user/Automation"
>>> os.path.basename(path)
'Automation'
>>> os.path.dirname(path)
'/home/ec2-user'
>>> path="/home"
>>> path1="ec2-user"
>>> print(os.path.join(path,path1))
/home/ec2-user
>>> path="/home/ec2-user/Automation/os_simple.py"
>>> os.path.split(path)
('/home/ec2-user/Automation', 'os_simple.py')
>>> os.path.getsize(path)
3792
>>> os.path.isfile(path)
True
>>> os.path.exists(path)
True
>>> os.path.islink(path)
False
>>> exit()



