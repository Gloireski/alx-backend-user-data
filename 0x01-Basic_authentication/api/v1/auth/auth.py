#!/usr/bin/env python3
"""
auth class def
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path and excluded_paths
        """
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path is None:
            return True

        if path[-1] != '/':
            path += '/'

        if excluded_paths[-1] != '/':
            excluded_paths += '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ returns None - request
        request is flask object
        """
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None - request
        request will be the Flask request object
        """
        pass
