"""
Practice: Logging Setup
"""
import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # File handler with rotation
    file_handler = RotatingFileHandler("app.log", maxBytes=1000, backupCount=2)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    log = setup_logging()
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning")
    log.error("This is an error")
    print("Logs written to app.log (and console)")
