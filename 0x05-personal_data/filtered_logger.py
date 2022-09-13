#!/usr/bin/env python3
"""
obscure log messages
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str):
    """
    filters a messages
    """
    for field in fields:
        message = re.sub(field + "=.*?" + separator, field +
                         "=" + redaction + separator, message)
    return message
