import json
from log import logger


def load_progress():
    try:
        with open("character files/character_progress.json", "r", encoding="UTF-8") as progress_file:
            progress = json.load(progress_file)
        return progress["character"]
    except Exception as e:
        logger.error(f" load_progress: {e}")
        return None
