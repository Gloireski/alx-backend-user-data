#!/usr/bin/env python3
"""
hash pass
"""
import bcrypt


def hash_password(password: str) -> str:
    """ def hash """
    password = b"my secret password"
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
