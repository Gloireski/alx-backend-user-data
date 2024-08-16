#!/usr/bin/env python#
"""define _hash_password
"""
import bcrypt


def _hash_password(password: str) -> str:
    """ hash function"""
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd, salt)
