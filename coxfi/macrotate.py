import os
import re
import subprocess
import string
import random

pln = '[\033[36;1m*\033[m] ' # Plain message (blue)

def generate():
    uppa = ''.join(set(string.hexdigits.upper()))
    mac = ''
    for fullcombo in range(6):
        for pairing in range(2):
            if fullcombo == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppa)
        mac += ":"
    return mac.strip(":")

def fetch(iface):
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def rotate(iface, newmac):
    subprocess.check_output(f"sudo ifconfig {iface} down", shell=True)
    subprocess.check_output(f"sudo ifconfig {iface} hw ether {newmac}", shell=True)
    subprocess.check_output(f"sudo ifconfig {iface} up", shell=True)

def roulette():
    iface = 'wlp4s0'
    oldmac = fetch(iface)
    newmac = generate()
    rotate(iface, newmac)
    print(pln + 'Old MAC: ' + str(oldmac.upper()) + '\n' + pln + 'New MAC: ' + str(newmac))
