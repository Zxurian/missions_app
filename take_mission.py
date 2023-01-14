from log import logger
import pyautogui as pygui
from double_check import double_check
import img_page as ip

from verify_img import check_for_screen


def take_mission():
    print("Working on: take_mission()")

    # Now we are looking for the take_mission btn to finish the process of getting the mission
    mission_details = check_for_screen(
        "mission details", ip.needle_mission_details, 0.8
    )
    take_mission_btn = check_for_screen(
        "take_mission_btn", ip.needle_mission_details_takeMission, 0.8
    )

    if mission_details != None:
        pygui.click(take_mission_btn)

        # After clicking on the first take mission Btn another screen will pop up and
        # ask for a confirmation to take the mission hinch another take Btn to click
        confirm_mission = check_for_screen(
            "confirmation take Btn", ip.needle_mission_confirmation_title, 0.8
        )
        take_confirmation_btn = check_for_screen(
            "take_mission_btn", ip.needle_mission_confirmation_takeMission, 0.8, True
        )

        if confirm_mission != None:
            pygui.click(take_confirmation_btn, clicks=2)
            double_check(ip.needle_mission_confirmation_takeMission, 0.8)
            double_check(ip.highlighted_confirm_take_btn, 0.8)
            print("mission taken!")
            return True  # if this is true then we need to move to logout_of_account() and proceed to next character
    else:
        print("Not able to retrieve package")
        logger.info("not able to retrieve package")
        return False  # if this is false then we need to logout and go to next account because something went wrong and con not resolve it
