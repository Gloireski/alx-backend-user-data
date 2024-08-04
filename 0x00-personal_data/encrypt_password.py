#!/usr/bin/env python3
"""
hash pass
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ def hash """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
