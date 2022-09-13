#!/usr/bin/env python3
"""
obscure log messages
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(fr'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
