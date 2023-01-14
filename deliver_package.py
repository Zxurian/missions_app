import pyautogui as pygui

from log import logger

import img_page as ip
from double_check import double_check
from verify_img import check_for_screen


def deliver_package():

    deliver_package = check_for_screen(
        "deliver_package", ip.needle_mission_deliver_package, 0.8, True
    )
    logger.info(f"checking for retrieve_package {deliver_package}")

    if deliver_package != None:
        logger.info(f"deliver_package found {deliver_package}")
        pygui.click(deliver_package)
        double_check(ip.needle_mission_deliver_package, 0.8)
        return True
    else:
        return False
