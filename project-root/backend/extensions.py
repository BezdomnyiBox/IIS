from flask import Flask
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app)
api = Api(app)
auth = HTTPBasicAuth() 