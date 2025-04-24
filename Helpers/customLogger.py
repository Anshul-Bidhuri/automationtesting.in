import logging
import inspect
import os
import datetime

now = datetime.datetime.now()


def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        log_folder_path = os.path.abspath(__file__ + '/../../')
        log_file_name = now.strftime("%d-%m-%Y_%I-%M-%S-%p")
        log_file_path = os.path.join(log_folder_path, "LogFiles", f'Logs_{log_file_name}.log')
        fileHandler = logging.FileHandler(log_file_path, mode='w')
        fileHandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        streamHandler = logging.StreamHandler()  # to print the logs in console
        streamHandler.setLevel(logging.INFO)
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)
    return logger