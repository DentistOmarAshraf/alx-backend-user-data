#!/usr/bin/env python3
"""
Class BasicAuth
"""
from flask import request as FLASK_REQ
from models.user import User
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """
    Class BasicAuth
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """extract_base64_authorization_header
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """decode_base64_authorization_header
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(base)
            info = decoded.decode('utf-8')
            return info
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """extract_user_credentials
        """
        if not decoded_base64_authorization_header:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        result = decoded_base64_authorization_header.split(':')
        if len(result) > 2:
            email = result[0]
            password = ":".join(result[1:])
            return (email, password)
        return (result[0], result[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """User_object_from credentials
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        try:
            list_of_user = User.search({'email': user_email})
        except KeyError:
            return None

        if not list_of_user:
            return None
        the_user: User = list_of_user[0]
        if not the_user.is_valid_password(user_pwd):
            return None
        return the_user

    def current_user(self, request=None) -> TypeVar('User'):
        """use all methods to check user
        """
        auth_header = self.authorization_header(request)
        header_b64 = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(header_b64)
        user = self.extract_user_credentials(decoded)
        if user == (None, None):
            return None
        user_obj = self.user_object_from_credentials(user[0], user[1])
        return user_obj
