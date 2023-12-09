from flask import Blueprint
from http import HTTPStatus

health_api = Blueprint('health_api', __name__)

@health_api.route('/health', methods = ['GET'])
def health():
    return "OK", HTTPStatus.OK