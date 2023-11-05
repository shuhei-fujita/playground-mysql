# logger_config.py
import logging
import os
from logging.handlers import RotatingFileHandler


# loggerの設定関数
def get_logger():
    if "logger" not in globals():
        logger = logging.getLogger("uvicorn")
        os.makedirs("logs", exist_ok=True)

        handler = RotatingFileHandler("logs/api.log", maxBytes=10000000, backupCount=5)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.ERROR)

    return logger
