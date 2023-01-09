import configparser
import json
import os


config = configparser.ConfigParser()
config.read("mission config/config.conf")
JSON_FILE = config["user_list"]["JSON_FILE"]


def get_option(section, option):
    return config.get(section, option)


def set_option(section, option, value):
    config.set(section, option, value)
    with open("mission config/config.conf", "w") as configfile:
        config.write(configfile)


def read_json_file(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
