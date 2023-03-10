import pyautogui as pygui
import pydirectinput as pydir

from time import sleep

import img_page as ip
from verify_img import check_for_screen


def logout_of_account():
    print("Working on: logout()")
    count = 0
    at_esc_menu = False
    while not at_esc_menu:
        if count >= 10:
            break

        sleep(2)
        pydir.press("esc")
        at_esc_coordinates = check_for_screen(
            "at ESC menu", ip.needle_logout, 0.9, True
        )
        if not at_esc_coordinates:
            count += 1
            continue
        at_esc_menu = True

    if not at_esc_menu:
        print("ESC Menu Not found")
        sleep(0.5)
    pygui.click(at_esc_coordinates, clicks=2)
    return
