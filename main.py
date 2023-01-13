import pyautogui
import os

# CHANGE THIS VALUE PER EXPERIMENT
### these two values MUST be larger than 2500 (the max must be at least 1 unit larger)
minThresholdValue = '2500'
maxThresholdValue = '3000'

def runAnalysis():
  # initial move to stage images
  pyautogui.moveTo(1033, 131)
  pyautogui.click()
  pyautogui.hotkey('ctrl', 'shift', 't')

  # write in minValue
  pyautogui.press('tab')
  pyautogui.press('right', presses=4)
  pyautogui.press('backspace', presses=4)
  pyautogui.write(minThresholdValue)
  pyautogui.press('enter')
  pyautogui.PAUSE = 0.5

  # write in maxValue
  pyautogui.press('tab')
  pyautogui.press('right', presses=5)
  pyautogui.press('right', presses=5)
  pyautogui.press('backspace', presses=5)
  pyautogui.write(maxThresholdValue)
  pyautogui.press('enter')
  pyautogui.PAUSE = 0.5

  # click back onto image window
  pyautogui.moveTo(1033, 131)
  pyautogui.click()
  pyautogui.PAUSE = 1

  # run analysis
  pyautogui.press('m')

  # close image
  pyautogui.moveTo(1404, 136)
  pyautogui.click()

### if we ever want to automate further
def exportResults():
  print('Saved you some time')


dirPath = r'C:\Users\JacAnderson\Dropbox\1_Naik Lab\Protocols\Cell Culturing Mesen ECs\IF - Cholesterol Manipulation by ATR101\2022NOV28 - ATR101 and Probucol\Rat Mesenteric endothelial cells - Filipin- Probucol\automated'
fileCount = 0

for path in os.listdir(dirPath):
  if (os.path.isfile(os.path.join(dirPath, path))):
    runAnalysis()
    fileCount += 1

# export results
exportResults()
