import os

def get_environment_variable(secret_name, default="") -> str:
    value = os.getenv(secret_name)
    if value is None or len(value) == 0:
        value = default
    return str(value)