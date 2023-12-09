import logging
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from health_check import health_api
from encrypt_decrypt import homepage, encryptpage, decryptpage
from gevent import pywsgi

web_logger = logging.getLogger('web')
audit_logger = logging.getLogger('audit')
app_logger = logging.getLogger('app')

SECRET_KEY:str = "a18b63c8-3b74-4e9d-abf4-9df0c7d2e45d"
HOST:str = "0.0.0.0"
PORT:str = "8585"
DEBUG:bool = False
CERT_FILE:str = "./certs/cert.pem"
KEY_FILE:str = "./certs/key.pem"
LOG_FORMAT = f"%(asctime)s | %(levelname)s | app | %(name)s | %(threadName)s | %(message)s"

def initialize_logs() -> None:

    logging.basicConfig(
        level=getattr(logging, "INFO"),
        format = LOG_FORMAT,
        handlers=[logging.StreamHandler()]
    )

def initialize() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["WTF_CSRF_SSL_STRICT"] = False
    csrf = CSRFProtect(app)
    return app

def register_blueprints(app:Flask) -> None:
    app.register_blueprint(health_api)
    app.register_blueprint(homepage)
    app.register_blueprint(encryptpage)
    app.register_blueprint(decryptpage)

def run_app_server(app:Flask) -> None:
    audit_logger.info(f"Starting server in production mode {HOST}:{PORT}")
    server = pywsgi.WSGIServer((HOST, int(PORT)), app, keyfile = KEY_FILE, certfile = CERT_FILE, log = web_logger)

    server.serve_forever()

    # app.run(host=HOST, ssl_context = 'adhoc', port= PORT, debug=DEBUG)

if __name__=="__main__":
    app = initialize()
    register_blueprints(app)
    run_app_server(app)