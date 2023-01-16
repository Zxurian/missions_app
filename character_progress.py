from load_progress import load_progress
from login_credentials import login_with_credentials
from save_progress import save_progress
from config import JSON_FILE, read_json_file


def character_progress():
    # load the character progress from the file
    current_character = load_progress()

    # load the list of characters from the json file
    characters = read_json_file(JSON_FILE)["characters"]
    # if the current_character is not set, start from the beginning of the list
    if current_character is None:
        current_character = 0
    else:
        # find the index of the current character in the list
        current_character = [
            i for i, c in enumerate(characters) if c["name"] == current_character
        ][0]

    # loop over the characters in the list
    for character in characters[current_character:]:
        # log in to the character
        login_with_credentials(character["email"], character["pwd"])

        # do other stuff here

        # save the progress after each character
        save_progress(character["name"])
