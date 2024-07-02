from sensor.exception.exception import CustomException
import os
import sys

def test():
    try:
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":

    try:
        test()
    except Exception as e:
        print(e)