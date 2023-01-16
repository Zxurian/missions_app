import time

from log import logger
import config
from automate_characters import automate_users


def main():
    # Initiate time tracking for full run of all characters
    start_time = time.perf_counter()

    # Check for existence of user accounts to run automation on
    try:
        account_list = config.read_json_file(
            config.get_option("user_list", "JSON_FILE")
        )
    except Exception as e:
        logger.error(e)
    else:
        automate_users(account_list)

    # Stop time tracking for full run of all characters and output
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    logger.info(f"Time Elapsed Cycles: {elapsed_time:.2f} seconds")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
