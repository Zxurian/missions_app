from log import logger

# store the name of the character in a file


def save_character_name(account_name):
    try:
        with open(
            "user_list_progression/character_name.txt", "w", encoding="UTF-8"
        ) as file:
            file.write(account_name)

    except Exception as e:
        logger.error(f"save_character_name: {e}")
    else:
        return
