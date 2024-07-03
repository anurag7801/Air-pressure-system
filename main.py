from sensor.exception.exception import CustomException
import os
import sys
from sensor.logging.logger import logging
from sensor.utils.utils import dump_csv_file_to_mongodb_collection

def test():
    try:
        logging.info("Entered in try block....")
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    file_path = r'D:\Github Projects\Air-pressure-system\aps_failure_training_set1.csv'
    database_name = "air-pressure-system"
    collection_name = "sensor"
    dump_csv_file_to_mongodb_collection(filepath=file_path,database_name=database_name,collection_name=collection_name)