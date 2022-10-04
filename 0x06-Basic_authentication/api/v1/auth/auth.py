#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar
"""
This module contains the Auth class
"""


class Auth():
    """
    auth.py
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        return True if the path is not in the list of strings excluded_paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user
        """
        return None
