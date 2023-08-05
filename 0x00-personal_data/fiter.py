#!/usr/bin/env python3

import re

def filter_datum(fields, redaction, message, separator):
    """a list of strings representing all fields"""

  regex = separator.join(f"(?<=\\b{field}\\b{separator}).*?(?=\\b{separator}|$)" for field in fields)
  return re.sub(regex, redaction, message)

