import time
import requests
import line_notify
import utilities as utils
from datetime import datetime

config = utils.read_config()
address = config.get('wallet_address')
ether_apikey = config.get('ether_api_key')
counter = {
    'balance': 0,
    'transaction': 0
}
common_contract = {
    '0x000000000000ad05ccc4f10045630fb830b95127': 'Blur.Marketplace',
    '0x0000000000A39bb272e79075ade125fd351887Ac': 'Blur.Bidding',
}


def get_wallet_balance():
    # URL for the API endpoint to get the balance of a given wallet address
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ether_apikey}"

    # Send a GET request to the API endpoint and parse the response as JSON
    response = requests.get(url).json()

    # Get the balance of the wallet address in Ether
    balance_in_wei = int(response["result"])
    balance_in_ether = balance_in_wei / 10 ** 18

    # Print the balance
    print(f"The balance of your wallet onw is {balance_in_ether} Ether.")
    print("--------------------------------------------------------------")
    message = f"\nThe balance of your wallet  now is {balance_in_ether} Ether."
    line_notify.send_message(message)


def get_the_latest_transaction():
    # URL for the API endpoint to get the latest transaction for a given wallet address
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={ether_apikey}"

    # Send a GET request to the API endpoint and parse the response as JSON
    response = requests.get(url).json()

    # Get the details of the latest transaction
    latest_tx = response["result"][0]
    gas_price_in_gwei = int(latest_tx["gasPrice"])
    gas_used = int(latest_tx["gasUsed"])
    from_address = latest_tx["from"]
    to_address = latest_tx["to"]
    value_in_wei = int(latest_tx["value"])
    timestamp = int(latest_tx["timeStamp"])
    if from_address.lower() == address.lower():
        from_address = 'You'
    else:
        pass
    if to_address.lower() == address.lower():
        to_address = 'You'
    else:
        pass
    if from_address in common_contract:
        from_address = common_contract[from_address]
    else:
        pass
    if to_address in common_contract:
        to_address = common_contract[to_address]
    else:
        pass
    # Convert the gas price from Gwei to Wei
    gas_price_in_wei = gas_price_in_gwei * 10 ** 9

    # Convert the timestamp to a human-readable date string
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Convert the values from Wei to Ether
    gas_price_in_ether = gas_price_in_wei / 10 ** 18
    value_in_ether = value_in_wei / 10 ** 18

    # Print the details of the latest transaction
    print(f"The Most Recent Transaction :")
    print("")
    print(f"Gas price: {gas_price_in_ether} Gwei")
    print(f"From address: {from_address}")
    print(f"To address: {to_address}")
    print(f"Value: {value_in_ether} Ether")
    print(f"Date: {date}")
    print("----------------------------------------------------------")
    message = "\nThe Most Recent Transaction :" \
              "\n" \
              f"\nGas price: {gas_price_in_ether} Gwei" \
              f"\nFrom address: {from_address}" \
              f"\nTo address: {to_address}" \
              f"\nValue: {value_in_ether} Ether" \
              f"\nDate: {date}"
    line_notify.send_message(message)


def track_newest_transaction():
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={ether_apikey}"
    latest_timestamp = int(time.time())
    while True:
        # Initialize the latest transaction timestamp to the current time
        response = requests.get(url).json()
        latest_tx = response["result"][0]
        timestamp = int(latest_tx["timeStamp"])
        if timestamp > latest_timestamp:
            latest_timestamp = timestamp
            gas_price_in_gwei = int(latest_tx["gasPrice"])
            gas_used = int(latest_tx["gasUsed"])
            from_address = latest_tx["from"]
            to_address = latest_tx["to"]
            value_in_wei = int(latest_tx["value"])
            if from_address.lower() in common_contract:
                from_address = common_contract[from_address]
            else:
                pass
            if to_address.lower() in common_contract:
                to_address = common_contract[to_address]
            else:
                pass
            # Convert the gas price from Gwei to Wei
            gas_price_in_wei = gas_price_in_gwei * 10 ** 9

            # Convert the timestamp to a human-readable date string
            date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            # Convert the values from Wei to Ether
            gas_price_in_ether = gas_price_in_wei / 10 ** 18
            value_in_ether = value_in_wei / 10 ** 18
            transaction_fee_in_ether = gas_price_in_ether * gas_used
            print("--------------------------------------------------------"
                  "New transaction"
                  f"From address: {from_address}\n"
                  f"To address: {to_address}\n"
                  f"Transaction fee: {transaction_fee_in_ether} Ether\n"
                  f"Value: {value_in_ether} Ether\n"
                  f"Date: {date}"
                  "---------------------------------------------------------")

            message = "\nNew transaction!"
            line_notify.send_message(message)
            message = f"\nFrom address: {from_address}\n"
            message += f"To address: {to_address}\n"
            message += f"Transaction fee: {transaction_fee_in_ether} Ether\n"
            message += f"Value: {value_in_ether} Ether\n"
            message += f"Date: {date}"
            line_notify.send_message(message)
            get_wallet_balance()
            continue
        else:
            time.sleep(60)
            continue


def run_app():
    print("+-----------------------------+")
    print("Welcome to wallet tracker!    |")
    print("+-----------------------------+")
    message = "\nWelcome to wallet tracker!"
    line_notify.send_message(message)
    get_wallet_balance()
    get_the_latest_transaction()
    message = "\nInitial information done!" \
              "\nStart tracking your wallet"
    line_notify.send_message(message)
    track_newest_transaction()


if __name__ == '__main__':
    run_app()
