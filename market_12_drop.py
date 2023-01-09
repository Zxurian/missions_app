from time import sleep
import pydirectinput as pydir
from flight_complete import landed_img
import img_page as ip
from is_window_active import is_window_active
from verify_img import check_for_screen


def market_12_drop():
    print("Working on: market_12_drop()")
    is_window_active()
    attempts = 60
    count = 0
    while (count <= attempts):

        market_drop = check_for_screen(
            'market_drop', ip.needle_Market12Drop, 0.8, True)

        if market_drop:
            pydir.keyDown('alt')
            pydir.press('4')
            sleep(0.25)
            pydir.keyUp('alt')
            sleep(0.25)
            pydir.press('ctrl')
            pydir.middleClick()
            landed_img()
            pydir.keyDown('f')
            sleep(4)
            pydir.keyUp('f')
            return
        else:
            pydir.keyDown('alt')
            pydir.press('2')
            pydir.keyUp('alt')
            count += 1
    return
