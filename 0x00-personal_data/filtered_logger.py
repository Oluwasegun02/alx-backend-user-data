#!/usr/bin/env python3
"""
This module contains the function filter_datum, which obfuscates sensitive fields in a log message.
"""
import re

def filter_datum(fields, redaction, message, separator):
    """
    Obfuscate sensitive fields in a log message.

    Arguments:
    fields: A list of strings representing all fields to obfuscate.
    redaction: A string representing what the field will be obfuscated with.
    message: A string representing the log line.
    separator: A string representing the character separating all fields in the log line.

    Returns:
    The log message with sensitive fields obfuscated.
    """
    pattern = r"(" + "|".join(fields) + r")" + separator + r"[^" + separator + r"]*"
    
    return re.sub(pattern, r"\1" + separator + redaction, message)

