from log import logger

from active_mission_check import active_aileron_check
from deliver_package import deliver_package
from end_of_characters import end_of_characters
from exit_game import exit_game
from logout import logout_of_account
from market_12_drop import market_12_drop
from mission_menu import menu
from mission_packages import reward_aileron
from origin_180k import origin_180k
from retrieve_package import retrieve_package
from search_menu import search_menu
from start_game import start_game
from take_mission import take_mission
from welcome_back import welcome_back


def call_list():
    """runs through the list of actions that it
    takes to complete a mission pre character

    Returns back to login_to_character
    """
    welcome_back()
    menu()
    active_results = active_aileron_check()
    if active_results:
        deliver_results = deliver_package()
        if deliver_results:
            logout_of_account()
            # check if at end of character list
            character_results = end_of_characters()
            if character_results:
                # if end_of_characters is true then goto origin_180k()
                origin_180k()
                logout_of_account()
                exit_game()
                start_game()
                return
        else:
            retrieve_package()
            logout_of_account()
            # check if at end of character list
            character_results = end_of_characters()
            if character_results:
                # if end_of_characters is true then goto market_12_drop()
                market_12_drop()
                logout_of_account()
                return
    else:
        search_menu()
        reward_aileron_results = reward_aileron()
        if reward_aileron_results:
            take_results = take_mission()
            if take_results:
                retrieve_package()
                logout_of_account()
                # check if at end of character list
                character_results = end_of_characters()
                if character_results:
                    market_12_drop()
                    logout_of_account()
                    return
