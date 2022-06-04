import sys
from socket import socket, AF_INET, SOCK_STREAM
from time import time
from common.utils import get_message, send_message
from common.variables import DEFAULT_PORT, DEFAULT_ADDRESS


def presence(account_name='Ars'):
    json_object = {
        'action': 'presence',
        'time': time(),
        'user': {
            'account_name': account_name
        }

    }
    return json_object


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
    except IndexError:
        server_address = DEFAULT_ADDRESS
        server_port = DEFAULT_PORT
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.connect((server_address, server_port))
    message_to_server = presence()
    # print(message_to_server)
    send_message(server_socket, message_to_server)
    from_the_server = get_message(server_socket)
    print(from_the_server)
    # json_response = DATA.decode('utf-8')

    # response = json.loads(json_response)
    # print(response)
    server_socket.close()


if __name__ == '__main__':
    main()
