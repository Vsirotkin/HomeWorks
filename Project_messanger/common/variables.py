''' Константы '''


# порт по умолчанию
DEFAULT_PORT = 7777
# ip адрес по умолчанию
DEFAULT_IP_ADDRESS = '127.0.0.1'
# максимальная очередь подключений
MAX_CONNECTIONS = 5
# максильная длина сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# кодировка проекта
ENCODING = 'utf-8'

# протокол JIM, основные ключи
ACTION          = 'action'
TIME            = 'time'
USER            = 'user'
ACCOUNT_NAME    = 'account_name'

# прочие ключи для протокола
PRESENCE    = 'presence'
RESPONSE    = 'response'
ERROR       = 'error'
