import time
from log import logger
from login_to_characters import automate_character


def main():
    start_time = time.perf_counter()
    automate_character()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    logger.info(f"Time Elapsed Cycles: {elapsed_time:.2f} seconds")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
