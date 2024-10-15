#!/usr/bin/env python3
"""Model of login view
"""
from flask import request, jsonify, make_response
from typing import List
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route("/auth_session/login",
                 strict_slashes=False, methods=['POST'])
def login() -> str:
    """login
    """
    email: str = request.form.get('email', None)
    if not email:
        return jsonify({"error": "email missing"}), 400

    passwd: str = request.form.get('password', None)
    if not passwd:
        return jsonify({"error": "password missing"}), 400

    user: List[User] = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    the_user = user[0]
    if not the_user.is_valid_password(passwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(the_user.id)

    response = make_response(the_user.to_json(), 200)
    response.headers['Content-type'] = 'application/json'
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)
    return response
