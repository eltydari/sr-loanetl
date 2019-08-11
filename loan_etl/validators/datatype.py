# -- FILE: loan_etl/validators/datatype.py
'''
Validates & converts cell data
'''
import sys
import re

ERROR = "_error"

def getValidator(vtype):
    try:
        return getattr(sys.modules[__name__], "_validate_{}".format(vtype))
    except AttributeError:
        raise KeyError("No validators exist for data type \"{}\"".format(vtype))

def _validate_string(input):
    return input

def _validate_integer(input):
    return int(input) if input is not None else input

def _validate_float(input):
    return float(input) if input is not None else input

def _validate_currency(input):
    return input

def _validate_date(input):
    return input