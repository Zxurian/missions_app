import json

from log import logger


def save_progress(character):
    # create a dictionary with the character name as the key
    # and the character data as the value
    # characters = {character["name"]: character}
    try:
        with open(
            "user_list_progression/character_progress.json", "w", encoding="UTF-8"
        ) as progress_file:
            json.dump({"character": character}, progress_file)
    except Exception as e:
        logger.error(f" save_progress: {e}")
    else:
        return
