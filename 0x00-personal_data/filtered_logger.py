#!/usr/bin/env python3
"""
This module contains the function filter_datum, which obfuscates sensitive fields in a log message.
"""
import re
import logging
import os
import mysql.connector



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

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

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

def get_logger() -> logging.Logger:
    """ Returns a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    target_handler = logging.StreamHandler()
    target_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))

    target_handle.setFormatter(formatter)

    logger.addHandler(target_handler)
    return logger

def get_db() -> mysql.connector.connection.MYSQLConnection:
    """get the database credentials from the environment variables"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    """create a connection to the MySQL database using mysql.connector"""
    conn = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )

    return conn

def hash_password(password):
    """ generate a random salt using bcrypt.gensalt and return the hashed password as a byte string"""
    salt = bcrypt.gensalt()
    
    hashed = bcrypt.hashpw(password.encode(), salt)
    """return the hashed password as a byte string"""
    return hashed

def is_valid(hashed_password, password):
    """ use bcrypt.checkpw to compare the hashed password and the password
    # return True if they match, False otherwise"""
    return bcrypt.checkpw(password.encode(), hashed_password)

