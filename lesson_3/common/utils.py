import json


def get_message(client):
    DATA = client.recv(1024)
    json_response = DATA.decode('utf-8')
    response = json.loads(json_response)
    return response


def send_message(sock, message):
    js_message = json.dumps(message)
    encode_message = js_message.encode('utf-8')
    sock.send(encode_message)
