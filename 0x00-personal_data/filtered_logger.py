#!/usr/bin/env python3
"""
This module contains the function filter_datum, which obfuscates sensitive fields in a log message.
"""
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """ add a fields attribute to store the list of strings to filter"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ use the filter_datum function to obfuscate the values in the record message"""
        record.msg = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        """ return the formatted record using the parent class method"""
        return super().format(record)

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

# if __name__ == '__main__':
#     main()
