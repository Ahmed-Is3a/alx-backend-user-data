#!/usr/bin/env python3
""" logging module
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """loging with regex
    """
    for field in fields:
        result = re.sub(field+'=.*?'+separator,
                        field+'='+redaction+separator, message)
    return result
