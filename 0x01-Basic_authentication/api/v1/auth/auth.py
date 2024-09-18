#!/usr/bin/env python3
"""
Class Auth
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """
    Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """used later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """used_later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """used_later
        """
        return None
