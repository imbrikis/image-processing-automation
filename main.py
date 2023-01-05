import pyautogui
# To find file count in a directory
import os

def doStuffHere():
  pyautogui.moveTo(-1307, 217)
  pyautogui.click()
  pyautogui.moveTo(-854, 402, duration=0.5)
  pyautogui.dragTo(-553, 399, 0.5)
  pyautogui.dragTo(-854, 402, 0.5)
  pyautogui.PAUSE = 1
  # pyautogui.write('The best anno', .1)
  print('found a file')

dirPath = r'C:\Users\imbrikis\Downloads\TEMP'
count = 0

for path in os.listdir(dirPath):
  if (os.path.isfile(os.path.join(dirPath, path))):
    doStuffHere()
    # count += 1