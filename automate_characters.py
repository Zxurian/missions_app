import time
from call_list import call_list
from log import logger
import random
from time import sleep

from is_window_active import is_window_active
from loading_screen import at_loading_screen
from login_credentials import login_with_credentials
from login_screen import at_login_screen
from save_character_name import save_character_name
from save_progress import save_progress


def automate_users(account_list):
    """Runs through automation actions fo reach character.

    This is the main function class that will run through all applicable actions for each character

    Parameters
    __________
    account_list : object
        The array of accounts, including credentials, to loop through for character automations

    """
    is_window_active()

    for account_name, account_info in account_list["characters"].items():
        char_start_time = time.perf_counter()

        # # save the name of the character to a file
        save_character_name(str(account_name))
        logger.info(f"save_character_name: {account_name}")
        # used to save current character to load in if program is stopped
        save_progress(account_name)
        logger.info(f"save_progress: {account_name}")

        # check if we're at the login screen
        at_login_screen()

        # log in to the account
        print(f"Logging in as: {account_name}")

        login_creds = login_with_credentials(
            account_info["email"], account_info["pwd"]
        )
        logger.info(f"logger in as {account_name}")

        if login_creds:
            continue

        # check to see if the login has completed and we're on the loading screen
        at_loading_screen()

        # wait a bit before trying to logout
        sleep(random.randint(3, 6))
        call_list()
        char_end_time = time.perf_counter()
        elapsed_time = char_end_time - char_start_time
        logger.info(f"Time Elapsed {account_name}: {elapsed_time:.2f} seconds")
        print(f"Time Elapsed {account_name}: {elapsed_time:.2f} seconds")
