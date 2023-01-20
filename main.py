import utilities
from log import logger
import config
from automate_characters import automate_users


def main():
    while True:
        # Initiate time tracking for full run of all characters
        main_counter = utilities.Stopwatch(True)

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
        main_counter.stop()
        logger.info(f"Time Elapsed Cycles: {main_counter.get_total_time():.2f} seconds")
        print(f"Time Elapsed: {main_counter.get_total_time():.2f} seconds")


if __name__ == "__main__":
    main()
