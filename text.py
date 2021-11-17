import sys
import argparse
from twilio.rest import Client
from decouple import config


def send_message(message_body):

    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    to_number = input('Enter the 10 digit number to send the message\n')
    message = client.messages \
                    .create(
                        body=message_body,
                        from_=config('TWILIO_PHONE_NUM'),
                        to=f'+1{to_number}'
                    )

    print(message.sid)


def create_parser():
    parser = argparse.ArgumentParser(
        description='''Send a text/sms message using command line
        arguments'''
    )

    parser.add_argument('-s', '--send', help='''Enter the message you
        would like to send then follow the prompts to send the message''',
                        type=str)

    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        print(ns)
        sys.exit(1)

    send = ns.send

    if send:
        print(ns)
        send_message(send)


if __name__ == '__main__':
    main(sys.argv[1:])
