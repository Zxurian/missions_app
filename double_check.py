from time import sleep
import pyautogui as pygui

def double_check(image_to_compare, confidence):
    attempts = 3
    count = 0
    while (count < attempts):
        sleep(1)
        img_check = pygui.locateCenterOnScreen(
            image_to_compare, confidence=confidence)
        if img_check != None:
            pygui.click(img_check)
            count += 1
            continue
        else:
            return
