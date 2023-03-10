from log import logger
from time import sleep
import pyautogui as pygui

from time import sleep

import img_page as ip
from double_check import double_check
from verify_img import check_for_screen
from log import logger


def exit_game():

    logger.info("working of exit_game()")
    exit_game = check_for_screen("exit game menu", ip.exit_game, 0.9)
    if exit_game != None:
        pygui.click(exit_game)
        double_check(ip.exit_game, 0.9)
    dismiss_screen = pygui.locateOnScreen(
        ip.dismiss_screen, confidence=0.8, minSearchTime=2
    )
    if dismiss_screen:
        dismiss_btn = check_for_screen("Dismiss Btn", ip.dismiss_btn, 0.8, True)
        pygui.click(dismiss_btn, clicks=2)
    sleep(60)
