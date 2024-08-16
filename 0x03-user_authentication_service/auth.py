#!/usr/bin/env python#
"""define _hash_password
"""
import bcrypt


def _hash_password(password: str) -> str:
    """Takes in password string argument
    Returns bytes (salted_hashed)
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
