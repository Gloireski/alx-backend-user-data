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

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if b64_auth_header is None or type(b64_auth_header) is not str:
            return None
        try:
            b64 = base64.b64decode(b64_auth_header)
            b64_decode = b64.decode('utf-8')
        except Exception:
            return None
        return b64_decode
