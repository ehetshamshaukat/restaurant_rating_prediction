# Project: Restaurant Rating
## Problem statement
### 1. Goal
```
To predict the rating of restaurant    
```
### 2. About 
```
To increase user satisfaction and visibility 
```
## Description
### 1. Dataset
```
1. Unclean data
1. Regression problem 
2. Dataset available on kaggle 
```

### 2. Features
``` 
Input features = [online_order, book_table, votes, location, cost_for_two, type, city, restaurant_type, cuisines,
                 number_of_cuisines_offered]
Target feature = [rating]
```
### 3. Pipeline Structure
```requirements
Google define pipeline 
```
# Requirements
### 1. Language
```
Python 3.10
```
### 2. Libraries
```
1. numpy
2. pandas
3. scikit-learn
4. pickle
5. os 
6. streamlit 
 ```
# code
### 1. Enviroment
```requirements
conda create -p venv python==3.10 -y 
```
### 2. Activate enviroment
```requirements
conda activate venv/
```
### 3. Setup
```
The setup.py is a Python script typically included with Python-written libraries or apps. Its objective is to ensure that the program is installed correctly. 
```
### 4. Components
- Data ingestion
```
reading data from different source and splitting data into train and test
```
- Data transformation
```
  reading train and test dataset and apply different transformation and save transformation setting in pickle format
```
- Model training
```requirements
transformed dataset and using different machine learning model and save the best model in pickle format
```
### 5. Pipeline
- Training pipeline
```
using components and creating pipeline for model training
```
- Prediction pipeline
```
taking data from user transform for model and predict 
```

## Run
#### 1. Download repository
```
git clone https://github.com/ehetshamshaukat/restaurantrating.git
```
#### 2. create virtual enviroment
```
conda create -p venv python==version -y
```
#### 3. Install dependences
```requirements
pip install -r requirements.txt
```
#### 4. Transformation and training
- data transformation and model training
  ```
  For model training, which will also save tranformation and model in pickle format
  python src/pipeline/training_pipeline.py
  ```
- Prediction
  ```
  For Prediction on new data
  python src/pipeline/prediction_pipeline.py
  ```
#### 5. Streamlit
```
to predict
streamlit run application.py
```
## Deployment
```
Deploy on AWS using Github actions which is CI CD technique
```
## Image
<img width="1501" alt="Screenshot 2024-08-25 at 2 43 55 PM" src="https://github.com/user-attachments/assets/e1fc85cb-fa3e-4df7-8afd-a3c4679240c3">

