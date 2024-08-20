import pandas as pd
from sklearn.model_selection import train_test_split
import os
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train = os.path.join("artifacts/train_test_dataset", "train.csv")
    test = os.path.join("artifacts/train_test_dataset", "test.csv")

class DataIngestion:
    def __init__(self):
        self.dataset = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv("dataset/cleaned_zomato.csv")

            os.makedirs(os.path.dirname(self.dataset.train), exist_ok=True)

            train_dataset, test_dataset = train_test_split(df, test_size=0.25, random_state=69)

            train_dataset.to_csv(self.dataset.train, index=False, header=True)
            test_dataset.to_csv(self.dataset.test, index=False, header=True)

            return self.dataset.train, self.dataset.test

        except Exception as e:
            raise e
