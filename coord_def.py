#%%
import pyautogui
import time
while True:
    time.sleep(0.1)
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")