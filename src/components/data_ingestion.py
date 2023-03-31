#The process of absorbing information (ingestion)
import os
import sys
from src.exception import CustomException
from src.exception import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #initializing the path

    def initiate_data_ingestion(self): #working on dataset
        logging.info("Entered the data ingestion component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as df")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path)) #making directory
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Initiating train test split")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=23) #creating training and testing sets

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #converting them to csv file
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()