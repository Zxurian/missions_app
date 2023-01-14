from is_window_active import is_window_active
from log import logger
import img_page as ip
from verify_img import check_for_screen


def at_loading_screen():

    # check to see if the login has completed and we're on the loading screen
    at_loading_screen = check_for_screen("Loading Complete", ip.loading_complete, 0.6)
    logger.info("Loading Complete")
    if at_loading_screen != None:
        return True
    else:
        logger.info(f" Not at {at_loading_screen}")
        return False
