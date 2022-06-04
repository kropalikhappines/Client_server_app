import sys
from time import ctime, time
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from common.variables import PRESENCE, ACTION, TIME, USER, \
    ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_PORT, DEFAULT_ADDRESS


def pars_client_message(message):
    print(message, 'func')
    if ACTION in message and message[ACTION] == PRESENCE \
            and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Ars':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    if '-a' in sys.argv:
        address = sys.argv[sys.argv.index('-a') + 1]
    else:
        address = DEFAULT_ADDRESS
    if '-p' in sys.argv:
        port = int(sys.argv[sys.argv.index('-p') + 1])
    else:
        port = DEFAULT_PORT
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind((address, port))
    server_sock.listen(3)
    while True:
        CLIENT, ADDR = server_sock.accept()
        print(f'Запрос на подключение от {ADDR}')

        message_from_client = get_message(CLIENT)
        message_to_client = pars_client_message(message_from_client)
        send_message(CLIENT, message_to_client)
        # print(p)
        # CLIENT.send(p)
        # print(p)
        CLIENT.close()


if __name__ == '__main__':
    main()
