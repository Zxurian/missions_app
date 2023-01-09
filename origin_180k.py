from time import sleep
import pydirectinput as pydir
from flight_complete import landed_img
import img_page as ip
from is_window_active import is_window_active
from verify_img import check_for_screen


def origin_180k():
    print("Working on: origin_180k()")
    is_window_active()
    attempts = 60
    count = 0

    while (count <= attempts):
        is_window_active()
        # TODO need to move pilot seat to login barron

        i80k_origin = check_for_screen(
            'i80k_origin', ip.I80kOrigin, 0.8, True)

        if i80k_origin:
            pydir.keyDown('alt')
            pydir.press('4')
            sleep(0.5)
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
