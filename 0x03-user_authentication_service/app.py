#!/usr/bin/env python3
""" entry app """
from auth import Auth
from flask import Flask, jsonify, request, abort
from flask.helpers import make_response

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    return jsonify(message="Bienvenue")


@app.route('/users', methods=['POST'], strict_slashes=False)
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    response = make_response(jsonify({"email": email,
                                      "message": "logged in"}))
    response.set_cookie('session_id', AUTH.create_session(email))
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
