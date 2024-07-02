from sensor.exception.exception import CustomException
import os
import sys
from sensor.logging.logger import logging

def test():
    try:
        logging.info("Entered in try block....")
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":

    try:
        test()
    except Exception as e:
        logging.info(e)