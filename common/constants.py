# salt:list(bytes) = [b'f\x8b\xd3\xa4\xd0\xe6\x92\xd1G\x12~Q\x83\x07\x14_', b'\x9fU\xa0\x1c\x07\xecA\xc5y\xe5\xda4"9\xd3\xc9', b'\xad\xa0\x90)`\x16\xea\x86\x83;YO\xf6\xdb\xb9_']
salt:bytes = b'f\x8b\xd3\xa4\xd0\xe6\x92\xd1G\x12~Q\x83\x07\x14_'
DEFAULT_LOG_LEVEL:str = "INFO"
DEFAULT_LOG_FILE:str = "./encrypt_decrypt.log"
APP_NAME:str = "encrypt-decrypt"
DEFAULT_PRINT_TO_CONSOLE:str = "True"
DEFAULT_HANDLER_TRACE_ID_FIELD:str = "x-process-trace-id"
DEFAULT_APP_ID_FIELD:str = "x-app-id"


ENV_PARAMETER_HOST_NAME:str = "HOST"
ENV_PARAMETER_PORT:str = "PORT"
ENV_PARAMETER_FLASK_SECRET_KEY:str = "FLASK_SECRET_KEY"
ENV_PARAMETER_ENVIRONMENT:str = "ENVIRONMENT"
ENV_PARAMETER_HTTPS_KEY_FILE:str = "HTTPS_KEY_FILE"
ENV_PARAMETER_HTTPS_CERT_FILE:str = "HTTPS_CERT_FILE"


ENV_DEFAULT_HOST:str = "0.0.0.0"
ENV_DEFAULT_PORT:str = "8585"
ENV_DEFAULT_FLASK_SECRET_KEY:str = "a18b63c8-3b74-4e9d-abf4-9df0c7d2e45d"
ENV_DEFAULT_ENVIRONMENT:str = "prod"
ENV_DEFAULT_KEY_FILE:str="/usr/src/app/certs/key.pem"
ENV_DEFAULT_CERT_FILE:str="/usr/src/app/certs/cert.pem"