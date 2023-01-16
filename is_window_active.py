import config
import win32gui
import win32process

import logging
from start_game import start_game
import mission_config

logger = logging.getLogger(__name__)

client = config.get_option("client_title", "CLIENT")


def is_window_active():
    hwnd = win32gui.FindWindow(None, client)
    if hwnd:
        pid = get_window_pid(hwnd)
        activate_window(hwnd)
        logger.info(f"{client} was activated")
    else:
        start_game()


def activate_window(hwnd):
    win32gui.SetForegroundWindow(hwnd)


def get_window_pid(hwnd):
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid
