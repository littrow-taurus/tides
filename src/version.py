# coding: utf-8

import conf_logging
import logging

logger=logging.getLogger(__name__)

MAJOR=0
MINOR=0
BUILD=6

def get_version() -> str:
    return f"{MAJOR}.{MINOR}.{BUILD}"