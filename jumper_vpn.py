import os
import random
from time import sleep
from bot import main

codeList = ["AT", "BE", "BG", "CA", "CA-W", "US", "US-C", "US-W", "FI", "FR", "TR", "DE", "NL", "CH", "GB"]

try:
  os.system("windscribe connect ")
  while True:
    codeChoice = random.choice(codeList)
    print("#Changing the IP Address...")
    os.system("windscribe connect " + codeChoice)
    sleep(10)
    main()
    sleep(10)
    os.system("windscribe disconnect")
except:
  os.system("windscribe disconnect")
  print("Error occured")