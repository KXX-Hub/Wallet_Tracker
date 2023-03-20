"""This python will handle some extra functions."""
from datetime import datetime
import sys
from os.path import exists

import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | MEI_HSING_Auto_Video             |
# | Made by KXX (MIT License)        |
# ++--------------------------------++
# 輸入你的Etherscan api key :          
ether_api_key : ''
#-------------------------------------
# 輸入你的錢包地址
wallet_address : ''
#-------------------------------------
# 輸入你的line_notify_token
line_notify_token: ''
#-------------------------------------
"""
                )
    sys.exit()


def read_config():
    """Read config file.
    Check if config file exists, if not, create one.
    if exists, read config file and return config with dict type.
    :rtype: dict
    """
    if not exists('./config.yml'):
        print("Config file not found, create one by default.\nPlease finish filling config.yml")
        with open('config.yml', 'w', encoding="utf8"):
            config_file_generator()

    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            config = {
                'ether_api_key': data['ether_api_key'],
                'wallet_address': data['wallet_address'],
                'line_notify_token': data['line_notify_token']
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()


def convert_timestamp(timestamp):
    """Convert timestamp to time.
    :param int timestamp: Timestamp to convert.
    :rtype: str
    """
    import time
    time_local = time.localtime(timestamp)
    time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return time


def convert_timestamp_to_past_time(timestamp):
    """Convert timestamp to time.
    :param int timestamp: Timestamp to convert.
    :rtype: str
    """
    dt_object = datetime.fromtimestamp(timestamp)
    # Calculate the time difference from current time
    time_difference = datetime.now() - dt_object
    # Convert the time difference to days, hours and minutes
    days, seconds = time_difference.days, time_difference.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    time_past = f"{hours}hr{minutes}min ago"
    return time_past


def convert_gas_price(gas_price_in_wei):
    # Convert gas price from wei to Gwei
    gas_price_in_gwei = round(gas_price_in_wei / 1000000000)
    # Return gas price in Gwei
    return gas_price_in_gwei


def convert_value_to_ether(value_in_wei):
    value_in_ether = value_in_wei / 10 ** 18
    return value_in_ether
