#!/usr/bin/env python3
"""
This module contains the Auth class
"""
import re
from flask import request
from typing import List, TypeVar


class Auth():
    """
    auth.py module for the API
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        return True if the path is not in the list of strings excluded_paths
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

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
