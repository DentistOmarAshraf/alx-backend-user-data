#!/usr/bin/env python3
"""
Class Auth
"""
from flask import request
from typing import TypeVar, List
from os import path as PATH
import fnmatch


class Auth:
    """
    Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Chech if path require path
        Return - bool
            - false if path in execuleded_path
            - true if it is not
        """
        if not path or not excluded_paths:
            return True
        path_to_check = PATH.normpath(path)
        paths = [PATH.normpath(p) for p in excluded_paths]
        check = False
        for path in paths:
            if fnmatch.fnmatch(path_to_check, path):
                check = True
                break
        if check:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Check Authrization header in the request
        """
        if not request or not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """used_later
        """
        return None
