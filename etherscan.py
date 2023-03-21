import time

import requests

import line_notify
import utilities as utils

config = utils.read_config()
address = config.get('wallet_address')
ether_apikey = config.get('ether_api_key')
common_contract = {
    '0x000000000000ad05ccc4f10045630fb830b95127': 'Blur.Marketplace',
    '0x0000000000A39bb272e79075ade125fd351887Ac': 'Blur.Bidding',
}


def get_api_url(module, action, ether_apikey, address=None,
                start_block=None, end_block=None, sort=None, page=None, offset=None,
                contract_address=None, tag=None,
                use_goerli_testnet=config.get('use_goerli_testnet')):
    if use_goerli_testnet:
        url = f'https://api-goerli.etherscan.io/api?module={module}&action={action}&apikey={ether_apikey}'
    else:
        url = f'https://api.etherscan.io/api?module={module}&action={action}&apikey={ether_apikey}'

    if address:
        url += f'&address={address}'
    if start_block:
        url += f'&startblock={start_block}'
    if end_block:
        url += f'&endblock={end_block}'
    if sort:
        url += f'&sort={sort}'
    if page:
        url += f'&page={page}'
    if offset:
        url += f'&offset={offset}'
    if contract_address:
        url += f'&contractaddress={contract_address}'
    if tag:
        url += f'&tag={tag}'

    return url


def get_wallet_balance():
    # URL for the API endpoint to get the balance of a given wallet address
    url = get_api_url('account', 'balance', ether_apikey, address)

    # Send a GET request to the API endpoint and parse the response as JSON
    response = requests.get(url).json()

    # Get the balance of the wallet address in Ether
    balance_in_wei = int(response["result"])
    balance_in_ether = round(balance_in_wei / 10 ** 18, 2)

    # Print the balance
    print(f"There is {balance_in_ether} Ether in your wallet .")
    print("--------------------------------------------------------------")
    message = f"\nThere is {balance_in_ether} Ether in your wallet ."
    line_notify.send_message(message)


def get_the_latest_transaction():
    # URL for the API endpoint to get the latest transaction for a given wallet address
    url = get_api_url('account', 'txlist', ether_apikey, address, sort='desc', page=1, offset=1)
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
    function = str(latest_tx["functionName"].split('(')[0])
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
    cov_time = utils.convert_timestamp(timestamp)
    gas_price_in_ether = utils.convert_gas_price(gas_price_in_gwei)
    value_in_ether = utils.convert_value_to_ether(value_in_wei)
    # Print the details of the latest transaction
    print(f"The Most Recent Transaction :")
    print("")
    print(f"Gas price: {gas_price_in_ether} Gwei")
    print(f"From : {from_address}")
    print(f"To : {to_address}")
    print(f"Function : {function}")
    print(f"Value: {value_in_ether} Ether")
    print(f"Time: {cov_time}")
    print("----------------------------------------------------------")
    line_notify.send_transaction_message(from_address, to_address, gas_price_in_ether, function, value_in_ether,
                                         cov_time)


def track_newest_transaction():
    url = get_api_url('account', 'txlist', ether_apikey, address, sort='desc', page=1, offset=1)
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
            function = str(latest_tx["functionName"].split('(')[0])
            if from_address.lower() in common_contract:
                from_address = common_contract[from_address]
            else:
                pass
            if to_address.lower() in common_contract:
                to_address = common_contract[to_address]
            else:
                pass
            time_past = utils.convert_timestamp_to_past_time(timestamp)
            gas_price_in_ether = utils.convert_gas_price(gas_price_in_gwei)
            value_in_ether = utils.convert_value_to_ether(value_in_wei)

            print("\nNew transaction\n"
                  f"From: {from_address}\n"
                  f"To: {to_address}\n"
                  f"Transaction fee: {gas_price_in_ether} Ether\n"
                  f"Function: {function}\n"
                  f"Value: {value_in_ether} Ether\n"
                  f"Date: {time_past}"
                  "---------------------------------------------------------")
            message = "\nNew transaction!"
            line_notify.send_message(message)
            line_notify.send_transaction_message(from_address, to_address, gas_price_in_ether, function, value_in_ether,
                                                 time_past)
            get_wallet_balance()
            continue
        else:
            time.sleep(60)
            continue
