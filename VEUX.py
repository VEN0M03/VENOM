import os
import platform
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    import NE12
    
elif b == '32bit':
    import NE12
