#!/usr/bin/env python3
"""
obscure log messages
"""
import logging
import re
from typing import List
PII_FIELDS = ["email", "phone", "ssn", "password", "ip"]


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Returns the log message obfuscated"""
        return self.filter_datum(self.REDACTION,
                                 super().format(record), self.SEPARATOR)

    def filter_datum(self, redaction: str,
                     message: str, separator: str) -> str:
        """Returns the log message obfuscated"""
        for field in self.fields:
            message = re.sub(fr'{field}=.*?{separator}',
                             f'{field}={redaction}{separator}', message)
        return message


def get_logger() -> logging.Logger:
    """Returns a logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger
