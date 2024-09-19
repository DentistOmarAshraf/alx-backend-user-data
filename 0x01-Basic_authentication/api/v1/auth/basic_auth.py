#!/usr/bin/env python3
"""
Class BasicAuth
"""
from flask import request
from api.v1.auth.auth import Auth
import base64


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
