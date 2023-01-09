import json
from log import logger
from time import sleep
from is_window_active import is_window_active
from loading_screen import at_loading_screen
from login_credentials import login_with_credentials
from login_screen import at_login_screen
from logout import logout_of_account
from mission_config import read_json_file, JSON_FILE

# TODO want to incorprate this into the start and ask for user input


def character_link():
    """Logs in a character from user.json file"""
    is_window_active()
    print("Working on: login()")
    try:
        account_list = read_json_file(JSON_FILE)
    except Exception as e:
        logger.error(e)
    else:
        # loop over all the accounts
        for account_name, account_info in account_list["characters"].items():
            at_login_screen()
            # log in to the account
            print(f"logging in as: {account_name}")

            login_creds = login_with_credentials(
                account_info["email"], account_info["pwd"]
            )
            logger.info(f"logging in as {account_name}")

            if login_creds:
                continue

            # check to see if the login has completed and we're on the loading screen
            at_loading_screen()
            # wait a bit before trying to logout

            sleep(15)

            logout_of_account()
            continue


character_link()
