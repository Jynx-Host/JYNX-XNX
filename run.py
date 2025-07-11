import os, platform, time, sys
os.system('xdg-open https://t.me/jynxhub')
try:
 import requests
except:os.system("pip install requests")
print('\u001b[37m \x1b[38;5;196m->\033[1;97mChecking For Update...')
os.system('git pull --quiet ')
bit = platform.architecture()[0]
if bit == "64bit":
 print('\u001b[37m \x1b[38;5;196m->\033[1;97m64Bit Found')
 time.sleep(2)
 from ruth64 import __RUTHXJYNX__
 __RUTHXJYNX__().__MENU__()
 
 
 
if bit == "32bit":
 print('\u001b[37m \x1b[38;5;196m-> \033[1;97m32Bit Found')
 time.sleep(2)
 from ruth64 import MENU
 MENU()
