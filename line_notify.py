import requests
import utilities as utils

config = utils.read_config()
token = config.get('line_notify_token')


def send_message(message):
    """Send message to LINE Notify.
    :param int sub_num: Subscribed sync channels num.
    :param str message: Message to send.
    """
    headers = {"Authorization": "Bearer " + token}
    data = {'message': message}
    requests.post("https://notify-api.line.me/api/notify",
                  headers=headers, data=data, timeout=5)


def send_transaction_message(from_address, to_address, transaction_fee_in_ether, function, value_in_ether, time_past):
    """Send message to LINE Notify.
    :param int sub_num: Subscribed sync channels num.
    :param str message: Message to send.
    """
    headers = {"Authorization": "Bearer " + token}
    data = {'message': "\nThe Most Recent Transaction :"
                       "\n"
                       f"\nFrom address: {from_address}\n"
                       f"To address: {to_address}\n"
                       f"Transaction fee: {transaction_fee_in_ether} Ether\n"
                       f"Function: {function}\n"
                       f"Value: {value_in_ether} Ether\n"
                       f"Time: {time_past}"}
    requests.post("https://notify-api.line.me/api/notify",
                  headers=headers, data=data, timeout=5)
