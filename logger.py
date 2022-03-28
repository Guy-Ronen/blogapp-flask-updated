import logging
from pathlib import Path

def get_logger(folder,logging_level=logging.WARNING):
    # create logger
    logger = logging.getLogger(folder)
    logger.setLevel(logging_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # create console handler and set level to debug
    file_handler = logging.FileHandler(f"./flask_blog/{folder}/{folder}.log")
    file_handler.setLevel(logging_level)
    file_handler.setFormatter(formatter)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    
    return logger
        
    