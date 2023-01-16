import logging
import os
import config

# Create a logger
logging.basicConfig(
    level=logging.INFO,
    filename="logs/mission.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s: %(module)s:: %(funcName)s - %(name)s - %(message)s  ",
)
logger = logging.getLogger(__name__)

handler = logging.FileHandler("logs/mission.log")
formatter = logging.Formatter("%(name)s -  %(funcName)s - %(module)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


try:
    # Set the maximum size of the log file in bytes
    MAX_SIZE = int(config.get_option("log", "MAX_SIZE"))
except Exception as e:
    logger.debug("The value of MAX_SIZE is not a valid integer.")
else:
    # Open the log file in append mode
    with open("logs/mission.log", "a") as log_file:
        # Get the current size of the log file
        log_file_size = os.stat("logs/mission.log").st_size

        # If the log file is larger than the maximum size, truncate it
        if log_file_size > MAX_SIZE:
            log_file.truncate(MAX_SIZE)
