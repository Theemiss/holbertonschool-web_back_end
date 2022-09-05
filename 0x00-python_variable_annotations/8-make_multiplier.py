#!/usr/bin/env python3
"""
# 7-to_kv module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier function"""
    return lambda x: x * multiplier
