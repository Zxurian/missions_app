from log import logger
from time import sleep
import time

import pyautogui as pygui
import img_page as ip

# TODO landed_img hangs here waiting for img and when G is pressed within game and img is displayed again
# it is able to reconigze it again and procced.
# maybe put in a check to search for img again after a set amount of time without interfering with method.
def check_img_to_land():
    logger.info("Starting Flight")

    print("Starting Flight")

    start_time = time.perf_counter()

    # sleep here to give a delay between the time the ship takes off and the img will disapear.
    sleep(15)

    while True:
        img_region = pygui.locateOnScreen(ip.landed, minSearchTime=2, confidence=0.7)
        pygui.moveTo(img_region)
        if img_region == None:
            continue

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        logger.info(f"Time Elapsed: flight time {elapsed_time:.2f} seconds")
        print(f"Time Elapsed: flight time {elapsed_time:.2f} seconds")

        # gives time for ship to land before continuing
        sleep(10)
        return
