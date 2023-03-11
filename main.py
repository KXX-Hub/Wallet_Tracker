import requests
import utilities as utils

config = utils.read_config()
address = config.get('wallet_address')
token = config.get('line_notify_token')


def get_internal_transactions():
    result = requests.get(
        f'//https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={token}')


if __name__ == '__main__':
    get_internal_transactions()
