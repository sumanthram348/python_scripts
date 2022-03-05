>>> import os
>>> print(o.sep)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'o' is not defined
>>> print(os.sep)
/
>>> path="/home/ec2-user"
>>> os.getcwd()
'/home/ec2-user/Automation'
>>> os.chdir("/home/ec2-user")
>>> os.getcwd()
'/home/ec2-user'
>>> os.chdir("/home/ec2-user/Automatiom")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/home/ec2-user/Automatiom'
>>> os.chdir("/home/ec2-user/Automation")
>>> od.getcwd()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'od' is not defined
>>> os.getcwd()
'/home/ec2-user/Automation'
>>> os.listdir()
['__pycache__', 'sample.py', 'type_cast.py', 'string_formatting.py', 'io_eval.py', 'case_conversion.py', 'conditions.py', 'math_module.py', 'platform_module.py', 'getpass.py', 'sys.py', 'sys_argv.py', 'different_string_operation.py', 'data_structures.py', 'operators.py']
>>> os.mkdir("sumanth")
>>> os.listdir()
['__pycache__', 'sumanth', 'sample.py', 'type_cast.py', 'string_formatting.py', 'io_eval.py', 'case_conversion.py', 'conditions.py', 'math_module.py', 'platform_module.py', 'getpass.py', 'sys.py', 'sys_argv.py', 'different_string_operation.py', 'data_structures.py', 'operators.py']
>>> os.makedirs("sumanth/xyz/x")
>>> os.listdir("sumanth")
['xyz']
>>> os.remove("sumanth/xyz/x")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IsADirectoryError: [Errno 21] Is a directory: 'sumanth/xyz/x'
>>> os.rmdir("sumanth/xyz/x")
>>> os.getuid()
1000
>>>
>>> os.getpid()
7172
>>> os.environ
environ({'XDG_SESSION_ID': '1456', 'HOSTNAME': 'ip-172-31-91-67.ec2.internal', 'TERM': 'xterm', 'SHELL': '/bin/bash', 'HISTSIZE': '1000', 'SSH_CLIENT': '49.37.221.87 49227 22', 'SSH_TTY': '/dev/pts/0', 'USER': 'ec2-user', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:', 'MAIL': '/var/spool/mail/ec2-user', 'PATH': '/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/ec2-user/.local/bin:/home/ec2-user/bin', 'PWD': '/home/ec2-user/Automation', 'LANG': 'en_US.UTF-8', 'HISTCONTROL': 'ignoredups', 'SHLVL': '1', 'HOME': '/home/ec2-user', 'LOGNAME': 'ec2-user', 'SSH_CONNECTION': '49.37.221.87 49227 172.31.91.67 22', 'LESSOPEN': '||/usr/bin/lesspipe.sh %s', 'XDG_RUNTIME_DIR': '/run/user/1000', 'OLDPWD': '/home/ec2-user', '_': '/usr/local/bin/python3'})

