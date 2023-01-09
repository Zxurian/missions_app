from log import logger
import pyautogui as pygui
import img_page as ip
from is_window_active import is_window_active
from verify_img import check_for_screen


def search_menu():
    print("Working on: search_menu()")
    is_window_active()
    search_icon = check_for_screen(
        'Search Icon', ip.needle_search, 0.9, True)
    if search_icon != None:
        pygui.click(search_icon)

    else:
        search_yellow_icon = check_for_screen(
            'Yellow Search Icon', ip.needle_selected_searchYellow, 0.9, True)
        pygui.click(search_yellow_icon)
    return
