import os,time
bit = os.uname().machine
os.system('git checkout -- . && git pull')
os.system('chmod 777 *')
if '64' in bit:
  print(' YOUR SYSTEM IS 64 BIT SO SUCCESS RUN')
  time.sleep(2)
  from jnx64 import key
else:
  os.system('clear')
  print(' YOUR SYSTEM IS 32 BIT NOT SUPPORTED')
