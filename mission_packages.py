from log import logger
from time import sleep
import pyautogui as pygui
from double_check import double_check
import img_page as ip
from is_window_active import is_window_active


def mission_packages(mission_name, mission_pay):
    print("Working on: reward_aileron()")
    is_window_active()
    attempts = 20
    count = 0
    while count < attempts:
        package = pygui.locateCenterOnScreen(
            mission_name, confidence=0.9, minSearchTime=1.5
        )

        payout = pygui.locateCenterOnScreen(
            mission_pay, confidence=0.9, minSearchTime=1.5
        )

        if package and payout != None:
            sleep(0.5)
            pygui.click(package)
            double_check(package, 0.8)
            return True  # if this is true we need to goto take_mission()

        reward_icon = pygui.locateCenterOnScreen(
            ip.needle_reward_unsorted, confidence=0.9, minSearchTime=1
        )

        pygui.click(reward_icon)

        count += 1

    return False


def reward_aileron():
    print("Working on: reward_aileron()")
    is_window_active()
    attempts = 20
    count = 0
    while count < attempts:
        aileron_search_menu = pygui.locateCenterOnScreen(
            ip.needle_aileron_search, confidence=0.9, minSearchTime=1.5
        )

        payout_180kh = pygui.locateCenterOnScreen(
            ip.needle_180kh_mission, confidence=0.9, minSearchTime=1
        )

        if aileron_search_menu and payout_180kh != None:
            pygui.click(aileron_search_menu)
            double_check(ip.needle_aileron_search, 0.8)
            return True  # if this is true we need to goto take_mission()

        reward_icon = pygui.locateCenterOnScreen(
            ip.needle_reward_unsorted, confidence=0.9, minSearchTime=1
        )

        pygui.click(reward_icon)

        count += 1

    print("mission not found and logged out")
    return False
