import os 
from src.datascience import logger
from src.datascience.entity.config_entity import DataTransforamtionConfig
from sklearn.model_selection import train_test_split
import pandas as pd


class DataTransforamtion:
    def __init__(self, config: DataTransforamtionConfig):
        self.config = config
    
    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        ## Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index=False)

        logger.info("Splitted data into training and test splits")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)