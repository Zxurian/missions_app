import pyautogui as pygui

from time import sleep

from log import logger


def check_for_screen(screen_name, image_to_compare, confidence, skip_sleep=False):
    is_on_screen = False
    check_count = 4
    max_checks = 15
    while not is_on_screen and check_count < max_checks:
        if skip_sleep != True:
            sleep(check_count)
            print(f"searching for {screen_name}: sleeping for {check_count}")
            logger.info(f"searching for {screen_name}: sleeping for {check_count}")
        screen_coords = pygui.locateCenterOnScreen(
            image_to_compare, confidence=confidence
        )

        if screen_coords != None:
            print(f"checking: {screen_name} found")
            logger.info(f"checking: {screen_name} found")
            return screen_coords

        check_count += 1
    if not is_on_screen:
        print(f"checking: {screen_name} Not found")
        logger.info(f"checking: {screen_name} Not found")
        return None
