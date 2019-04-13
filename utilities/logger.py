'''
Module for logging the information
'''
import os
import sys
import logging
import logging.config
from constants import LOG_FOLDER

class Logger(object):
    def __init__(self):
        if not os.path.exists(LOG_FOLDER):
            os.makedirs(LOG_FOLDER)
        self.logfile = os.path.join(LOG_FOLDER, "logs.txt")
        # Setting the baseConfig for logging
        self.set_basic_config()

    def set_basic_config(self):
        try:
            multiple_stream_handler = True
            loglevel = "DEBUG"
            formatter = "%(asctime)s [%(module)s]:[%(funcName)s]:%(lineno)d [%(levelname)s] | %(message)s"
            logging.basicConfig(filename=self.logfile, disable_existing_loggers=False, filemode='a',
                                format=formatter, datefmt='%Y-%m-%d %H:%M:%S', level=loglevel)

            if multiple_stream_handler == "True":
                display_formatter = logging.Formatter(formatter)
                # log to stdout
                stdout_stream = logging.StreamHandler(sys.stdout)
                stdout_stream.setLevel(logging.getLevelName(loglevel))
                stdout_stream.setFormatter(display_formatter)
                logging.getLogger().addHandler(stdout_stream)
        except Exception as err:
            logging.exception("Exception is raised: " + str(err.args))
            raise

class ConsoleLogger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)