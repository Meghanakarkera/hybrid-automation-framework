import logging

def get_logger():
    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("logs/test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger