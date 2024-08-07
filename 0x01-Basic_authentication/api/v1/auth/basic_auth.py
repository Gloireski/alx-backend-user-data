#!/usr/bin/env python3
""" Basic authentification """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ basic auth class """
    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """the Base64 part of the Authorization header for a
        Basic Authentication:
        """
        if auth_header is None or type(auth_header) is not str:
            return None
        if not auth_header.startswith('Basic '):
            return None
        return auth_header[6:]
