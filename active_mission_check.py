import pyautogui as pygui
import pydirectinput as pydir

from log import logger

import img_page as ip
from double_check import double_check
from is_window_active import is_window_active
from verify_img import check_for_screen


def active_aileron_check():
    """searches for the coresponding image file from img_page.py for the aileron mission check

    Returns:
        x, y | None: cordinates if image is found, or None if image is not found.

    """
    print("Working on: active_aileron_check()")
    is_window_active()
    try:
        aileron_parts = check_for_screen(
            "active aileron mission", ip.aileron_parts, 0.9, True
        )
    except Exception as e:
        logger.error(e)
        pass

    if aileron_parts != None:
        pygui.click(aileron_parts)
        double_check(ip.aileron_parts, 0.9)
        return True
    else:
        return False
