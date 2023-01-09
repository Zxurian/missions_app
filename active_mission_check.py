from log import logger
import pyautogui as pygui
import pydirectinput as pydir
from double_check import double_check
import img_page as ip
from is_window_active import is_window_active
from verify_img import check_for_screen

# aileron_parts = mission_config.get_option('mission1', 'aileron')


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
    # If aileron_parts Coords
    if aileron_parts != None:
        pygui.click(aileron_parts)
        try:
            double_check(
                ip.aileron_parts,
                0.9,
            )
            return True
        except Exception as e:
            logger.error(e)
    else:
        return False
