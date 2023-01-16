import json
from log import logger
import sys
from time import sleep
import pydirectinput as pydir
import img_page as ip

from is_window_active import is_window_active
from loading_screen import at_loading_screen
from login_credentials import login_with_credentials
from logout import logout_of_account
from respawn import respawn
from verify_img import check_for_screen
from config import JSON_FILE, read_json_file, get_option

PILOT = get_option("end_of_characters", "PILOT")


def end_of_characters():
    print("working on end_of_characters()")
    try:
        data = read_json_file(JSON_FILE)
    except (FileNotFoundError, KeyError):
        logger.error(FileNotFoundError, KeyError)
        print("error loading user.json file")
    else:
        characters = data["characters"]

    num_characters = len(characters)
    print(f"number of characters: {num_characters}")

    try:
        with open("character files/character_name.txt", encoding="UTF-8") as file:
            file_contents = file.read()
    except (FileNotFoundError, KeyError):
        logger.error(FileNotFoundError, KeyError)
        print("error loading character_name.txt file")
    else:

        # last_key is the name of the last character in the list & num_character is the index of
        # that character
        # subtract 1 to get the last index
        last_key = list(characters.keys())[num_characters - 1]
        print(f"last character is: {last_key}")
        # email/pwd  |  listOfChar | NameOfLast Char
        # last_character = characters[last_key]

        if last_key == file_contents:
            print("At end of character list.")
            #  if on the last character login to Barron and start of flight part
            # global PILOT
            character = PILOT
            try:
                account_list = read_json_file(JSON_FILE)
            except Exception as e:
                logger.error(e)
                print("error loading character_name.txt file")
            else:

                # retrieve email and password for the specified character
                email = account_list["characters"][character]["email"]
                pwd = account_list["characters"][character]["pwd"]

                # perform login actions
                logger.info(f"loggin into {character} with: {email}")
                print(f"logging into {character}")
                print(email)
                # print(pwd)

                is_window_active()
                login_with_credentials(email, pwd)

                print("done entering custom info")

                at_loading_screen()

                respawn()

                pilot_seat = check_for_screen(
                    "pilot_seat", ip.needle_pilotseat, 0.5, True
                )

                if pilot_seat != None:
                    pydir.keyDown("f")
                    sleep(4)
                    pydir.keyUp("f")
                    return True

                else:
                    logger.info(
                        "could not find pilot seat: sleeping for 120s then quiting"
                    )
                    print("could not find pilot seat: sleeping for 120s then quiting")
                    sleep(120)
                    logout_of_account()
                    sys.exit(0)

        else:
            print("Have not reached the end of the character list yet.")
            print(f"Last character: {last_key}, current character {file_contents}")
            return False
