import sys
from typing import Optional

import numpy as np
import pandas as pd
import json
from sensor.config.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception.exception import CustomException
from sensor.logging.logger import logging

class SensorData:
    '''
    This class help to export entire mongo DB record as pandas dataframe
    '''

    def __init__(self):
        
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise CustomException(e,sys)
        
    def save_csv_file(self,file_path,collection_name: str, database_name: Optional[str] = None):
        try:
            logging.info("entered in sensor_data save_csv_file function")
            data_frame = pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise CustomException(e,sys)
        
    def export_collection_as_dataframe(self,collection_name:str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            '''
            export entire collection as dataframe:
            return pd.DataFrame of collection
            '''
            logging.info("Entered in export_collection_as_dataframe function")
            
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
  
            df = pd.DataFrame(list(collection.find()))

            logging.info("DataFrame created successfully")
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            logging.info("Exited from export_collection_as_dataframe function")

            return df
        except Exception as e:
            raise CustomException(e,sys)
        