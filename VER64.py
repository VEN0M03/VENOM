import os, platform, time, sys
os.system('xdg-open https://t.me/toolstermuxi')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('[*] Loeading Chacking Update.')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('[✓] Found 64 Bit Device')
 import VER64
elif bit == '32bit':
 print('\033[1;97m[✓] SORRY BRO YOUR DEVIS IS 32 BIT ')
 print('\033[1;97m[✓] PLEASE USE 4=64 DEVIS ')
