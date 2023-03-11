import requests
import utilities as utils
from datetime import datetime

config = utils.read_config()
address = config.get('wallet_address')
ether_apikey = config.get('ether_api_key')


def get_internal_transactions():
    # URL for the API endpoint to get the balance of a given wallet address
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ether_apikey}"

    # Send a GET request to the API endpoint and parse the response as JSON
    response = requests.get(url).json()

    # Get the balance of the wallet address in Ether
    balance_in_wei = int(response["result"])
    balance_in_ether = balance_in_wei / 10 ** 18

    # Print the balance
    print("----------------------------------------------------------")
    print(f"The balance of your wallet is {balance_in_ether} Ether.")
    print("----------------------------------------------------------")



def check_the_latest_transaction():
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

    # Convert the gas price from Gwei to Wei
    gas_price_in_wei = gas_price_in_gwei * 10 ** 9

    # Convert the timestamp to a human-readable date string
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Convert the values from Wei to Ether
    gas_price_in_ether = gas_price_in_wei / 10 ** 18
    value_in_ether = value_in_wei / 10 ** 18

    # Print the details of the latest transaction
    print(f"Latest transaction :")
    print("")
    print(f"Gas price: {gas_price_in_ether} Ether")
    print(f"From address: {from_address}")
    print(f"To address: {to_address}")
    print(f"Value: {value_in_ether} Ether")
    print(f"Date: {date}")
    print("----------------------------------------------------------")


if __name__ == '__main__':
    get_internal_transactions()
    check_the_latest_transaction()
