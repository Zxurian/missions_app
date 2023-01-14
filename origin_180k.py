from time import sleep
import pydirectinput as pydir
from flight_complete import check_img_to_land
import img_page as ip

from verify_img import check_for_screen


def origin_180k():
    print("Working on: origin_180k()")

    attempts = 60
    count = 0

    while count <= attempts:

        # TODO need to move pilot seat to login barron

        i80k_origin = check_for_screen("i80k_origin", ip.I80kOrigin, 0.8, True)

        if i80k_origin:
            pydir.keyDown("alt")
            pydir.press("4")
            sleep(0.5)
            pydir.keyUp("alt")
            sleep(0.25)
            pydir.press("ctrl")
            pydir.middleClick()
            check_img_to_land()
            pydir.keyDown("f")
            sleep(4)
            pydir.keyUp("f")
            return
        else:
            pydir.keyDown("alt")
            pydir.press("2")
            pydir.keyUp("alt")
            count += 1
