import time
import random
from time import sleep


from call_list import call_list
from is_window_active import is_window_active
import logging
import random
from time import sleep


from loading_screen import at_loading_screen
from login_credentials import login_with_credentials
from login_screen import at_login_screen
from mission_config import read_json_file, JSON_FILE
from save_character_name import save_character_name
from save_progress import save_progress

logger = logging.getLogger(__name__)


def login_process():
    """Logs in a character from manifest.json file"""

    print("Working on: login()")

    try:
        account_list = read_json_file(JSON_FILE)
    except Exception as e:
        logger.error(e)
    else:
        # loop over all the accounts
        for account_name, account_info in account_list["characters"].items():
            is_window_active()
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
            logger.info(f"logged in as {account_name}")

            if login_creds:
                continue

            # check to see if the login has completed and we're on the loading screen
            result_loading = at_loading_screen()
            if result_loading == False:
                continue

            # wait a bit before moving on
            sleep(random.randint(3, 6))
            call_list()
            char_end_time = time.perf_counter()
            elapsed_time = char_end_time - char_start_time
            logger.info(f"Time Elapsed {account_name}: {elapsed_time:.2f} seconds")
            print(f"Time Elapsed {account_name}: {elapsed_time:.2f} seconds")
            continue
