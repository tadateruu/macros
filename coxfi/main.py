# Script to get free CoxWiFi anywhere you go.
# Make sure to encrypt your network traffic for privacy!
# To do: add IP checker, add loop success/fail counter

# For timings and timestamps
import schedule
import time
from datetime import datetime

# For macros
import pyautogui as auto

# Ping test
import os
import subprocess
from requests import get

clear = lambda: os.system('clear')
clear()
loopnum = 0
dip = '[\033[32;1m+\033[m] ' # Good to go (green)
pln = '[\033[36;1m*\033[m] ' # Plain message (blue)
err = '[\033[31;1m-\033[m] ' # Error message (red)
war = '[\033[31;1m!\022[m] ' # Warning or exit (yellow)

print(dip + 'Script initialized.\n')

def enter():
    auto.press('enter')
def pingtest():
    with open(os.devnull, 'w') as DEVNULL:
        global is_up
        try:
            subprocess.check_call(
                ['ping', '-c', '1', 'vid.puffyan.us'],
                stdout=DEVNULL,  # suppress output
                stderr=DEVNULL)
            is_up = True
        except subprocess.CalledProcessError:
            is_up = False
def runbrowser():
    with open(os.devnull, 'w') as DEVNULL:
        subprocess.Popen(['librewolf', '--new-window', '192.168.0.1'], stdout=DEVNULL, stderr=DEVNULL)
    #os.system('librewolf --new-window 192.168.0.1')

def macro():
    #print(auto.position())
    
    # Input sudo password automatically (insecure)
    subprocess.Popen(['python3', 'passwd.py'])

    # Console MAC rotation
    time.sleep(0.3)
    import macrotate
    macrotate.roulette()
    time.sleep(0.3)
    time.sleep(1)
    
    # Have to turn off wifi manually because buggy mess
    auto.moveTo(0, 925, duration=0.2)
    auto.click()
    time.sleep(0.5)
    auto.press('tab')
    auto.press('tab')
    enter()
    time.sleep(0.15)
    auto.hotkey('shift', 'tab')
    auto.press('tab')
    enter()
    auto.click(1, 925)
    auto.moveTo(40,925)
    time.sleep(0.1)
    print(dip + "MAC address rotated.")
    time.sleep(10)

    # Open browser for CoxWiFi login.
    runbrowser()
    print(pln + "Browser opened.")
    time.sleep(25)
    print(pln + "CoxWiFi login screen should be open.")
    
    # Fullscreen onto the login page to quickly log in.
    auto.press('f11')
    time.sleep(1)
    auto.press('tab')
    auto.press('tab')
    enter()
    time.sleep(10)
    # Spam credentials.
    auto.press('tab')
    auto.typewrite('lol')
    auto.press('tab')
    auto.typewrite('o')
    auto.press('tab')
    auto.typewrite('o')
    auto.press('tab')
    auto.typewrite('l@....')
    # Finished!
    auto.click(x=680, y=436)
    time.sleep(0.5)
    auto.click(x=1193, y=469)
    time.sleep(5)
    auto.hotkey('ctrl', 'w')
    
    # Count loops and generate timestamp
    global loopnum
    loopnum = loopnum + 1
    now = datetime.now()
    looptime = now.strftime("%H:%M:%S")
    print(pln + "Did it work? Loop #" + str(loopnum) + " at " + looptime + '.')
    time.sleep(0.5)
    # Connection test/ping
    print(pln + "Testing the connection...")
    time.sleep(0.5)
    pingtest()
    if is_up is True:
        print(dip + "Connected to the web ^-^\n")
    else:
        print(err + "Something's wrong... O_o")
        print(err + "Most likely a macro error?\n")

def pavlov():
    auto.alert('MAC rotation about to start.\n\nClick OK to continue.')
    time.sleep(120)
    macro()

#pavlov()
macro()
#schedule.every(5).seconds.do(macro)
schedule.every(59).minutes.do(macro)
#schedule.every(59).minutes.do(pavlov)

while 1:
    schedule.run_pending()
    time.sleep(1)
