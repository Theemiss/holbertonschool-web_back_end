#!/usr/bin/env python3
"""
# 7-to_kv module"""


def make_multiplier(multiplier: float) -> callable:
    """
    make_multiplier function"""
    def multiplier(multiplier):
        return multiplier * multiplier
    return multiplier
