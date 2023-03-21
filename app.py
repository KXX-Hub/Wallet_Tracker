import etherscan


def run_app():
    print("+-----------------------------+")
    print("Welcome to wallet tracker!    |")
    print("+-----------------------------+")
    message = "\nWelcome to wallet tracker!"
    etherscan.line_notify.send_message(message)
    etherscan.get_wallet_balance()
    etherscan.get_the_latest_transaction()
    message = "\nInitial information done!" \
              "\nStart tracking your wallet"
    etherscan.line_notify.send_message(message)
    etherscan.track_newest_transaction()


if __name__ == '__main__':
    run_app()
