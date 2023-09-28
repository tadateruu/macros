import pyautogui as auto
import time

def enter():
    auto.press('enter')
time.sleep(0.5)
auto.typewrite('your password here')
enter()
