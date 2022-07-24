from app.formatter import LogFormatter

import logging
from pathlib import Path
from os import path, scandir, curdir, mkdir

path_project = path.abspath(curdir)

'''
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
'''
def Start(app=None):
    logger = logging.getLogger(app)
    logger.setLevel(logging.DEBUG)
    _path_logs = path.join(path_project, 'logs')
    _path_app = path.join(_path_logs, app)

    try:
        if Path(_path_logs).is_dir() == False:
            err_msg = _path_logs
            mkdir(_path_logs)

        fh = logging.FileHandler(f"{_path_app}.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)")
        fh.setFormatter(formatter)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(LogFormatter())

        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger
    except Exception as e:
        exit(f'Can\'t create folder: {e}')
