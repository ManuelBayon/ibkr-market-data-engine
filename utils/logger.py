import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

def get_logger(name, log_path, debug=False, use_timestamp=False):

    os.makedirs(log_path, exist_ok=True)

    if use_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        log_file = f"{log_path}\\{name}_{timestamp}.log"
    else:
        log_file = f"{log_path}\\{name}.log"

    # Get a logger
    logger = logging.getLogger(name)
    # Sets the threshold for this logger to level
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # read-only - ist of handlers directly attached to this logger instance
    if not logger.handlers:
        handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=1_000_000,
            backupCount=5,
            encoding=None,
            delay=False
        )
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


