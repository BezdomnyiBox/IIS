from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)

app.json.ensure_ascii = False
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'student':
        return 'dvfu'
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 401


@app.route("/")
def hello_world():
    return jsonify({"app": "Самые высокие здания и сооружения"})


if __name__ == "__main__":
    app.run(debug=True)
        
import structures.views
        