import pyautogui
from pynput import keyboard

def captureMouseCursorPosition():
    x, y = pyautogui.position()
    print(str(x) + ", " + str(y), end='')
    print('\b')

def killProgram():
    raise KeyboardInterrupt

with keyboard.GlobalHotKeys({
        '<ctrl>+x': captureMouseCursorPosition,
        '<ctrl>+c': killProgram
    }) as h:
    h.join()