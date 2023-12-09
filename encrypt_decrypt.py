import base64, os, time
import werkzeug
from flask import Blueprint, render_template, flash, request, send_file, after_this_request, Response
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from http import HTTPStatus
from tools.encdec import generate_enckey, encrypt_encfile, decrypt_encfile
from common import constants
from typing import Any

homepage = Blueprint('home', __name__)
encryptpage = Blueprint('encryption', __name__)
decryptpage = Blueprint('decryption', __name__)

@homepage.route('/', methods = ['GET'])
def home() -> str:
    return render_template("index.html")

@encryptpage.route('/encrypt', methods = ['GET', 'POST'])
def encrypt() -> Response:
    file = request.files.get('input_file')
    password = request.form.get('encyption_key')
    filename = file.filename
    mime = file.content_type
    input = file.read()
    key = generate_enckey(password=password,salt=constants.salt)
    output = encrypt_encfile(key=key, input=input)
    response = Response(response=output, content_type=mime)
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response

@decryptpage.route('/decrypt', methods = ['GET', 'POST'])
def decrypt() -> Response:
    file = request.files.get('input_file')
    password = request.form.get('encyption_key')
    filename = file.filename
    mime = file.content_type
    input = file.read()
    key = generate_enckey(password=password,salt=constants.salt)
    output = decrypt_encfile(key=key,input=input)
    response = Response(response=output, content_type=mime)
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response