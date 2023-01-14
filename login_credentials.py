import pyautogui as pygui
import pydirectinput as pydir
from ahk import AHK

from time import sleep

import img_page as ip
from log import logger
from is_window_active import is_window_active
from verify_img import check_for_screen

ahk = AHK()


def login_with_credentials(username, password):

    print(username)
    # print(password)
    is_window_active()
    pydir.press("tab")
    pydir.press("backspace")
    pydir.press("tab")
    pydir.press("backspace")
    needle_email = pygui.locateCenterOnScreen(
        ip.needle_email_login, confidence=0.8, minSearchTime=1
    )
    pygui.click(needle_email, clicks=2)
    sleep(1)
    # pygui.write(username)
    ahk.send_input(username)
    needle_pwd = pygui.locateCenterOnScreen(
        ip.needle_pwd_login, confidence=0.8, minSearchTime=1
    )
    sleep(1)
    pygui.click(needle_pwd, clicks=2)
    sleep(1)
    # pygui.write(password)
    # sleep(1)
    ahk.send_input(password)
    pydir.press("enter")

    gametime_error = check_for_screen(
        "gametime_error", ip.needle_gametime_error, 0.9, True
    )

    if gametime_error:
        return True
    # TODO would like to have a notification sent when gametime_error found
    else:
        return False
