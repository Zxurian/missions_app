import pydirectinput as pydir

from time import sleep

from flight_complete import check_img_to_land
import img_page as ip

from verify_img import check_for_screen


def market_12_drop():
    print("Working on: market_12_drop()")

    attempts = 60
    count = 0
    while count <= attempts:

        market_drop = check_for_screen(
            "market_drop", ip.needle_Market12Drop, 0.8, True)

        if market_drop:
            pydir.keyDown("alt")
            pydir.press("4")
            sleep(0.25)
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
    return
