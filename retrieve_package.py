from log import logger
import pyautogui as pygui
from double_check import double_check
import img_page as ip
from verify_img import check_for_screen


def retrieve_package():

    retrieve_package = check_for_screen(
        "retrieve_package", ip.needle_mission_retrieveBtn, 0.8, True
    )
    logger.info(f"checking for retrieve_package {retrieve_package}")

    if retrieve_package != None:
        logger.info(f"retrieve_package found {retrieve_package}")
        pygui.click(retrieve_package)
        double_check(ip.needle_mission_retrieveBtn, 0.8)
        return
