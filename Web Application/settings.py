# app-wide production settings can go in this file
STATIC = "/static"
MIN = ""

try:
    # use localsettings.py to create development settings
    # e.g. local database connection, file paths, log settings
    from localsettings import *
except ImportError:
    pass
