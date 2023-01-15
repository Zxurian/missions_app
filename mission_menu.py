import pyautogui as pygui
import pydirectinput as pydir

import img_page as ip

from verify_img import check_for_screen
from log import logger


def menu():
    print("Working on: mission()")

    # Press F8 Key to enter Mission Menu
    pydir.press("f8")

    # get the screen coordinates of the yellow home icon
    yellow_home_icon_coords = check_for_screen(
        "Yellow Home Icon", ip.needle_home_iconYellow, 0.9, True
    )

    # check if the yellow home icon was found
    if yellow_home_icon_coords != None:
        # if the yellow home icon was found, click on it
        pygui.click(yellow_home_icon_coords)
        return

    # call the check_for_screen() function and get the screen coordinates of the home icon
    else:
        home_icon = check_for_screen(
            "Reg Home Icon", ip.needle_unselected_home_icon, 0.9, True
        )
        pygui.click(home_icon)
        return
