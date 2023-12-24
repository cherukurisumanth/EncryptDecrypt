import logging

from flask import Flask
from gevent import pywsgi
from flask_wtf.csrf import CSRFProtect

audit_logger = logging.getLogger('audit')
app_logger = logging.getLogger('app')
web_logger = logging.getLogger('web')

class NoHealth(logging.Filter):
    def filter(self, record:logging.LogRecord) -> bool:
        return 'GET /health' not in record.getMessage()
    
def initialize_flask(
        name:str,
        blueprints:list=[],
        host:str="0.0.0.0",
        port:int=8585,
        keyfile:str="",
        certfile:str="",
        addhoc:bool=True,
        production:bool=False,
        debug:bool=False,
        secret_key:str=""
    ):

    app = Flask(name)
    app.config["SECRET_KEY"] = secret_key
    app.config["WTF_CSRF_SSL_STRICT"] = False
    logging.getLogger("werkzeug").addFilter(NoHealth())
    web_logger.addFilter(NoHealth())

    CSRFProtect(app)

    for blueprint in blueprints:
        app.register_blueprint(blueprint=blueprint)

    if production:
        audit_logger.info(f"Starting server in production mode {host}:{port}")
        server = pywsgi.WSGIServer(
            listener=(host,port),
            application=app,
            keyfile=keyfile,
            certfile=certfile,
            log=web_logger
            )
        server.serve_forever()
    else:
        if addhoc:
            audit_logger.info(f"Starting server in non-production mode - adhoc {host}:{port}")
            app.run(
                host=host,
                port=port,
                ssl_context = 'adhoc',
                debug = debug
            )
        else:
            audit_logger.info(f"Starting server in non-production mode - with certs {host}:{port}")
            app.run(
                host=host,
                port=port,
                ssl_context = (certfile, keyfile),
                debug = debug
            )