import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from dataclasses import dataclass
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_file_as_pickle
from sklearn.impute import SimpleImputer


@dataclass
class DataTransformationConfig:
    transformation_config = os.path.join("artifacts/pickle", "transformation.pkl")


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def transforming_data(self):
        try:
            numerical_columns = ["votes", "cost_for_two", "number_of_cuisines_offered"]
            categorical_columns = ["online_order", "book_table", "location", "type", "city", "restaurant_type",
                                   "cuisines"]

            numerical_columns_pipeline = Pipeline(steps=[
                ("impute", SimpleImputer(strategy="median")),
                ("standardscaler", StandardScaler())
            ])

            categorical_column_pipeline = Pipeline(steps=[
                ("impute", SimpleImputer(strategy="most_frequent")),
                ("encoder", OrdinalEncoder()),
                ("standardscaler", StandardScaler())
            ])

            transforming = ColumnTransformer([
                ("numerical_column_pipeline", numerical_columns_pipeline, numerical_columns),
                ("categorical_column_pipeline", categorical_column_pipeline, categorical_columns)
            ])
            return transforming
        except Exception as e:
            raise e

    def initiate_transformation(self, train_dataset, test_dataset):
        try:
            train_dataset = pd.read_csv(train_dataset)
            test_dataset = pd.read_csv(test_dataset)

            column_to_drop = "rating"
            target_column = "rating"

            xtrain = train_dataset.drop(columns=column_to_drop, axis=1)
            ytrain = train_dataset[target_column]
            print(xtrain.shape)
            print(ytrain.shape)

            xtest = test_dataset.drop(columns=column_to_drop, axis=1)
            print(xtest.shape)
            ytest = test_dataset[target_column]
            print(ytest.shape)
            transform = self.transforming_data()

            xtrain_transformed = transform.fit_transform(xtrain)
            xtest_transformed = transform.transform(xtest)

            transform_train = np.c_[xtrain_transformed, np.array(ytrain)]
            transform_test = np.c_[xtest_transformed, np.array(ytest)]

            save_file_as_pickle(self.config.transformation_config, transform)

            return transform_train, transform_test

        except Exception as e:
            raise e
