from collections.abc import Callable
import logging, threading, os, signal, traceback
from views.health_check import health_api
from views.encrypt_decrypt import homepage, encryptpage, decryptpage
from time import sleep
from common import constants
from util.flask_util import initialize_flask
from util.environment_util import get_environment_variable
from threads.custom_threadpool import CustomThreadPool


audit_logger = logging.getLogger('audit')
app_logger = logging.getLogger('app')

class Agent(threading.Thread):

    def __init__(self, thread_name, thread_id):

        self.thread_name = thread_name
        self.thread_ID = thread_id

        self.host = get_environment_variable(constants.ENV_PARAMETER_HOST_NAME, constants.ENV_DEFAULT_HOST)
        self.port = get_environment_variable(constants.ENV_PARAMETER_PORT, constants.ENV_DEFAULT_PORT)
        self.flask_secret_key = get_environment_variable(constants.ENV_PARAMETER_FLASK_SECRET_KEY, constants.ENV_DEFAULT_FLASK_SECRET_KEY)
        self.environment = get_environment_variable(constants.ENV_PARAMETER_ENVIRONMENT, constants.ENV_DEFAULT_ENVIRONMENT)
        self.key_file = get_environment_variable(constants.ENV_PARAMETER_HTTPS_KEY_FILE, constants.ENV_DEFAULT_KEY_FILE)
        self.cert_file = get_environment_variable(constants.ENV_PARAMETER_HTTPS_CERT_FILE, constants.ENV_DEFAULT_CERT_FILE)


    def start_flask(self) -> None:
        initialize_flask(
            name=constants.APP_NAME,
            blueprints=[health_api, homepage, encryptpage, decryptpage],
            host=self.host,
            port=int(self.port),
            keyfile=self.key_file,
            certfile=self.cert_file,
            addhoc=True,
            production=(self.environment.lower() == 'prod'),
            debug=False,
            secret_key=self.flask_secret_key
        )
