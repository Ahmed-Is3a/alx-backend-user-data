#!/usr/bin/env python3
""" logging module
"""
import re


def filter_datum(fields, redaction, message, separator):
    """loging with regex
    """
    result = re.sub(rf'({"|".join(fields)})=[^{separator}]*',
                    lambda m: f"{m.group(1)}={redaction}", message)
    return result
