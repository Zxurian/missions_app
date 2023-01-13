import mission_config
import win32gui
import win32process
import logging
from screenshot_error import screen_shot_error
from start_game import start_game

logger = logging.getLogger(__name__)

client = mission_config.get_option("client_title", "CLIENT")


def is_window_active():
    hwnd = win32gui.FindWindow(None, client)
    if hwnd:
        pid = get_window_pid(hwnd)
        activate_window(hwnd)
        screen_shot_error("activate_window")
        logger.info(f"{client} was activated")
    else:
        start_game()


def activate_window(hwnd):
    win32gui.SetForegroundWindow(hwnd)


def get_window_pid(hwnd):
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid
