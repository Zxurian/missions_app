import pyautogui as pygui
import img_page as ip
from log import logger
from is_window_active import is_window_active
from verify_img import check_for_screen


def welcome_back():
    is_window_active()
    logger.info("looking for welcome back reward:")
    welcome_back_coordinates = check_for_screen(
        "Welcome Back Reward", ip.needle_welcomeBack, 0.7, True
    )
    # check if the OK Btn was found
    if welcome_back_coordinates != None:
        # if the OK Btn was found, click on it
        pygui.click(welcome_back_coordinates)
        logger.info("Another 100k")
    return
