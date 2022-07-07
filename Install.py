import os
import subprocess
import sys
#import update

def install():
    package = "dice"
    package2 = "discord"
    package3 = "sqlite3"
    package4 = "GitPython"
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    subprocess.check_call([sys.executable, "-m", "pip", "install", package2])
    subprocess.check_call([sys.executable, "-m", "pip", "install", package3])
    subprocess.check_call([sys.executable, "-m", "pip", "install", package4])
    #subprocess.check_call([sys.executable, "-m", "python", "update.py"])

install()

#try:
#    update.Update()
#except:
#z    install()