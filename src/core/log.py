"""File for core logger of the application."""

import logging
import sys

# flake8: noqa E501
LOG_FORMAT = "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(LOG_FORMAT)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
