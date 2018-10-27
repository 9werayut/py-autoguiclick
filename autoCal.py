#run calc
#######################
import subprocess

cmd = "C:/Windows/System32/calc.exe"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)
process.wait()
#######################




# you can send any text or Keyboard Shortcuts Combinations - pyautogui.hotkey('ctrl', 'c')
# send "5", "+", "8", "/", "2"
# send "Enter" 
#######################
import pyautogui
import time

time.sleep(.500)
pyautogui.press(['5','+','8','/','2']) 
pyautogui.hotkey('enter')
#######################