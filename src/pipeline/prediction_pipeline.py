import pandas as pd
import os

from src.utils import load_pickle


class Prediction:
    def __init__(self):
        pass

    def initiate_prediction(self, features):
        try:
            preprocessing_path = os.path.join("artifacts/pickle", "transformation.pkl")
            model_path = os.path.join("artifacts/pickle", "model.pkl")

            preprocessing = load_pickle(preprocessing_path)
            model = load_pickle(model_path)

            processed_data = preprocessing.transform(features)
            result = model.predict(processed_data)
            return result

        except Exception as e:
            raise e


class Features:
    def __init__(self, online_order, book_table, votes, location, cost_for_two, type, city, restaurant_type, cuisines,
                 number_of_cuisines_offered):
        self.online_order = online_order
        self.book_table = book_table
        self.votes = votes
        self.location = location
        self.cost_for_two = cost_for_two
        self.type = type
        self.city = city
        self.restaurant_type = restaurant_type
        self.cuisines = cuisines
        self.number_of_cuisines_offered = number_of_cuisines_offered
    def to_dataframe(self):
        try:
            data_in_dict = {
                "online_order": [self.online_order],
                "book_table": [self.book_table],
                "votes": [self.votes],
                "location": [self.location],
                "cost_for_two": [self.cost_for_two],
                "type": [self.type],
                "city": [self.city],
                "restaurant_type": [self.restaurant_type],
                "cuisines": [self.cuisines],
                "number_of_cuisines_offered": [self.number_of_cuisines_offered]
            }
            data_in_df = pd.DataFrame(data_in_dict)
            return data_in_df
        except Exception as E:
            raise E
