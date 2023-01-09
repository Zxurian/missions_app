import time
from log import logger
from login_to_characters import login_to_character


while True:
    start_time = time.perf_counter()
    login_to_character()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    logger.info(f"Time Elapsed Cycles: {elapsed_time:.2f} seconds")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")
