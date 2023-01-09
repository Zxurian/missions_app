from log import logger
import img_page as ip
from verify_img import check_for_screen


def at_login_screen():
    # check if we're at the login screen
    at_login_screen = check_for_screen("Login Screen", ip.needle_login, 0.8)
    if at_login_screen == None:
        logger.info(f"Not at at_login_screen")
        return False
