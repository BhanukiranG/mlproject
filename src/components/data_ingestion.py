# #The process of absorbing information (ingestion)
# import os
# import sys
# from src.exception import CustomException
# from src.exception import logging
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass

# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTranformationConfig


# @dataclass #it will automatically add generated special methods such as init
# class DataIngestionConfig:
#     train_data_path: str=os.path.join('artifacts','train.csv')
#     test_data_path: str=os.path.join('artifacts','test.csv')
#     raw_data_path: str=os.path.join('artifacts','data.csv')

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config=DataIngestionConfig() #initializing the path

#     def initiate_data_ingestion(self): #working on dataset
#         logging.info("Entered the data ingestion component")
#         try:
#             df=pd.read_csv('notebook\data\stud.csv')
#             logging.info("Read the dataset as df")
#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path)) #making directory
#             df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

#             logging.info("Initiating train test split")
#             train_set,test_set=train_test_split(df,test_size=0.2,random_state=23) #creating training and testing sets

#             train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #converting them to csv file
#             test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
#             logging.info("Ingestion completed")

#             return(
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path
#             )
#         except Exception as e:
#             raise CustomException(e,sys)
# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.initiate_data_ingestion()

#     data_transformation=DataTransformation()
#     train_arr,test_arr=data_transformation.initiate_data_transformation(train_data,test_data)


import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTranformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



