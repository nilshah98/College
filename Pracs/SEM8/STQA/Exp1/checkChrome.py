import pyautogui
import time
pyautogui.keyDown('ctrl')
pyautogui.keyDown('alt')
pyautogui.press('t')
pyautogui.keyUp('alt')
pyautogui.keyUp('ctrl')
pyautogui.typewrite('google-chrome\n', interval=0.2)

# waiting for chrome to load
time.sleep(5)

# checking for somaiya website details
pyautogui.typewrite('somaiya\n', interval=0.2)
time.sleep(10)

# check full screen
pyautogui.keyDown('fn')
pyautogui.press('f11')
pyautogui.keyUp('fn')

time.sleep(10)

# exit full screen
pyautogui.keyDown('fn')
pyautogui.press('f11')
pyautogui.keyUp('fn')

time.sleep(5)

# move cursor to cross button
pyautogui.moveTo(1900,40)
time.sleep(2)
pyautogui.click()

