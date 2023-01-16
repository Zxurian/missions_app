import pyautogui as pygui
import pydirectinput as pydir

import sys
import re
import logging

import mission_config
from double_check import double_check
import img_page as ip
from verify_img import check_for_screen
import config
import re

logger = logging.getLogger(__name__)


def start_game():
    client = config.get_option("client_title", "CLIENT")

    # Define the regular expressions for title1 and title2
    pattern1 = r"^Dual Universe$"
    pattern2 = r"^Dual Universe on GeForce NOW$"

    # Check if client matches its regular expression
    match1 = re.match(pattern1, client)
    match2 = re.match(pattern2, client)

    if match1 and not match2:
        pygui.hotkey("win", "d")
        du_icon = check_for_screen("DU Icon 1", ip.du_shortcut, 0.6, True)
        if du_icon != None:
            pygui.click(du_icon, clicks=2)
        else:
            du_icon_2 = check_for_screen("DU Icon 2", ip.du_shortcut_2, 0.6, True)
            pygui.click(du_icon_2, clicks=2)

    elif match2 and not match1:
        geforce_home_du = check_for_screen("GeForce home du", ip.geforce_home_du, 0.7)
        if geforce_home_du:
            pygui.moveTo(geforce_home_du)
            pydir.click()

    du_window = check_for_screen("DU Play Btn", ip.DU_start, 0.9)
    if du_window != None:
        pygui.click(du_window, clicks=2)
        double_check(ip.DU_start, 0.9)
        return
    else:
        # wait and try again
        logger.info("Client window and Game window not found")
        # TODO Send notification here
        sys.exit(0)
