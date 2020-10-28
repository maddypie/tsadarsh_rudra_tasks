from twilio.rest import Client
import sys


def main(account_sid, auth_token, message: str, ph_no: str):
    client = Client(account_sid, auth_token)

    send_message = client.messages \
    		.create(body=message,
    				from_="+12072908941", to=f"+91{ph_no}")

    print(send_message.sid)
    return

def check_valid_number(number):
    if len(number) == 10 and number.isnumeric():
        return True
    return False


if __name__ == "__main__":
    guide = "\nFormat: <message> <10-digit phone number>"
    message = ' '.join(sys.argv[1:-1])
    ph_no = sys.argv[-1]
    assert message, "Message Required{guide}"
    assert check_valid_number(ph_no), f"Invalid phone number{guide}"

    with open('private_keys.txt', 'r') as file:
        account_sid = file.readline().rstrip('\n')
        auth_token = file.readline().rstrip('\n')

    main(account_sid, auth_token, message, ph_no)

