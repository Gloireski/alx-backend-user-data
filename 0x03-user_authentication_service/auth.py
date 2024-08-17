#!/usr/bin/env python3
"""Auth Class for user attributes validation
"""
import bcrypt
import uuid


def _hash_password(password: str) -> str:
    """Takes in password string argument
    Returns bytes (salted_hashed)
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Returns string repr of a new UUID
    Use uuid module
    """
    return str(uuid.uuid4())
