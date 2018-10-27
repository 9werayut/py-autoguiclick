#run calc
#######################
import subprocess

cmd = "C:/Windows/System32/mspaint.exe"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)
#process.wait()
#######################

import pyautogui
import time

distance = 200
time.sleep(5)

pyautogui.moveTo(100, 200)

while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.1)   # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.1)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.1)  # move up