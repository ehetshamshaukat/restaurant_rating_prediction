import os
import pickle


def save_file_as_pickle(path, obj_name, ):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as path:
        pickle.dump(obj_name, path)



def load_pickle(path):
    with open(path,"rb") as path_obj:
        return pickle.load(path_obj)