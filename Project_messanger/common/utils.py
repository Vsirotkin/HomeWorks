'''Утилиты'''

import json
from common.variables import MAX_PACKAGE_LENGTH, ENCODING

def get_message(sock):
    '''
    утилита приема и декодирования сообщения
    принимает байты, выдает словарь или ошибку
    :param sock:
    :return:
    '''
    encoded_response = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    '''утилита кодирования и отправки сообщения
        принимает словать и отправляет его
        :param sock:
        :param message:
        :return:

    '''
    js_message = json.dump(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
