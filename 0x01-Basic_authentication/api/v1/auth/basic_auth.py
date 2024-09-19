#!/usr/bin/env python3
"""
Class BasicAuth
"""
from flask import request
from api.v1.auth.auth import Auth


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
