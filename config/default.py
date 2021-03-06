# -*- code: utf-8 -*-
"""
	Módulo que establece la configuracion del sistema
	This file contains most of the configuration variables that your app needs.
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """docstring for Config"""

    # Secret key for signing cookies
    SECRET_KEY = os.urandom(16)

    def __init__(self, arg):
        super(Config, self).__init__()
        self.arg = arg


class DevelopmentConfig(Config):
    SERVER_NAME = "PiHome_dev.com"

    # Todo: Modificar los parámetros necesarios para adaptarlos a tu proyecto

    # Las direcciones de verdad se encuentran en instace/config
    __debugURLUser = 'mysql+pymysql://test:test@localhost/debug'
    __mailUserName = 'name@domain.com'
    __defaultUserName = 'name+surname@domain.com'
    __mailPassword = 'password'

    """
        Parámetros de conexión a la BD
    """

    # Statement for enabling the development environment
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = __debugURLUser
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    """
        Parámetros para la conguración del WebMailServer
    """
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = __mailUserName
    DEFAULT_MAIL_SENDER = __defaultUserName
    MAIL_PASSWORD = __mailPassword  # os.environ.get('PASSWORD_EMAIL_DEBUG') # $ export PASSWORD_EMAIL_DEBUG = ''

    """
        Parámetros de conexión del módulo ZigBee
    """
    XBEE_PORT = '/dev/ttyUSB1'  # Puerto en el que se encuentra el ZigBee
    XBEE_BAUDRATE = 9600  # Frecuencia de emisión
    XBEE_REMOTE_ADDRESS = 5526146537043477  # 0013a20041513615
    XBEE_LOCAL_ADDRES = 5526146537043399  # 0013a200415135c7

    """docstring for DevelopmentConfig"""

    def __init__(self, arg):
        super(DevelopmentConfig, self).__init__()
        self.arg = arg


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True
