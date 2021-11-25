from flask import Flask, jsonify, request
from services import dbservices

app = Flask(__name__)

@app.route('/people', methods=["GET"])
def get_people():
    #add servicelayer function (business logic) that executes db_controller
    people = dbservices.getdata('people')
    return jsonify(people)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    app.run()
