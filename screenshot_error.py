import pyautogui
import datetime


def screen_shot_error(save_file_as):
    image = pyautogui.screenshot()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image.save(f"assets/screen_shot_error/{save_file_as}_{timestamp}.png")
