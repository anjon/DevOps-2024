import logging, logging.handlers
import sys


class clusterLinkConfig():
    def __init__(self) -> None:
        pass

def initializeLogger():
    logger = logging.getLogger('cluster_link')
    logger.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(loglevel)s - %(messgae)s')
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)
    logger.addHandler(logging.FileHandler('cluster_link.log'))
    return logger

try:
    logger = initializeLogger()
    print('Hello World!')
except:
    e = sys.exc_info()[0]
    logger.exception(e)