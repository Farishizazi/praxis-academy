from flask import Flask
from flask_cors import CORS
# from hashlib import md5

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

from app import routes

# password = "rahasia"
# salt = "rahasiaaaa"
# passwordHash = (md5((password+salt).encode())).hexdigest()
# print(passwordHash.hexdigest())