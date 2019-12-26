#!/usr/bin/env python

from copy import copy
from logging import Formatter

MAPPING = {
    "DEBUG": 37,  # white
    "INFO": 36,  # cyan
    "WARNING": 33,  # yellow
    "ERROR": 31,  # red
    "CRITICAL": 41,  # white on red bg
}
# MAPPING_MODULE = {
#     'ws_thread':
# }

PREFIX = "\033["
SUFFIX = "\033[0m"


class ColoredFormatter(Formatter):
    def __init__(self, pattern):
        Formatter.__init__(self, pattern)

    def format(self, record):
        colored_record = copy(record)
        levelname = colored_record.levelname
        modulename = colored_record.module
        seq = MAPPING.get(levelname, 31)
        seq2 = 32 # default white
        colored_levelname = ("{0}{1}m{2}{3}").format(PREFIX, seq, levelname, SUFFIX)
        colored_modulename = ("{0}{1}m{2}{3}").format(PREFIX, seq2, modulename, SUFFIX)
        colored_record.levelname = colored_levelname
        colored_record.module = colored_modulename
        return Formatter.format(self, colored_record)
