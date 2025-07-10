import os,time
RED = "\033[91m"    # Bright Red
WHITE = "\033[97m"  # Bright White
bit = os.uname().machine
os.system('chmod 777 *')
if '64' in bit:
  print(f' {RED}>> {WHITE}64 BIT DETECTED')
  time.sleep(1)
  print(f' {RED}>> {WHITE}CHECKING UPDATE')
  time.sleep(2)
  os.system('git checkout -- . && git pull')
  print(f' {RED}>> {WHITE}UPDATE IS CHECKED')
  time.sleep(2)
  import ruth64
else:
  os.system('clear')
  print(' {RED}>> {WHITE}32 BIT NOT SUPPORTED')
