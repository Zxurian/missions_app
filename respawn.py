from log import logger
import pyautogui as pygui
import pydirectinput as pydir
from double_check import double_check
import img_page as ip

from verify_img import check_for_screen


def respawn():
    print("Working on: respawn()")

    attempts = 30
    count = 0
    while count < attempts:
        pydir.press("esc")
        respawn_btn = check_for_screen(
            "at respawn_btn menu", ip.needle_respawn_btn, 0.9, True
        )
        if respawn_btn == None:
            count += 1
            continue

        else:
            print("respawn_btn Not found")
            pygui.leftClick(respawn_btn)

            respawn_yes_btn = check_for_screen(
                "at respawn_btn menu", ip.needle_respawn_yes_btn, 0.9, True
            )
            if respawn_yes_btn != None:
                pygui.click(respawn_yes_btn)
                double_check(ip.needle_respawn_yes_btn, 0.9)
                respawn_ok = check_for_screen(
                    "respawn_ok", ip.needle_respawn_ok, 0.9)
                if respawn_ok != None:
                    pygui.click(respawn_ok)
                    double_check(ip.needle_respawn_ok, 0.9)
                    return
