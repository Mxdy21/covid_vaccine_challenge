import os
import pandas as pd
import rampwf as rw
from itertools import combinations_with_replacement
from sklearn.model_selection import ShuffleSplit

problem_title = 'Covid Vaccince Prediction'

_target_names = ['Vaccine', 'Business']

_prediction_label_ = combinations_with_replacement(
                                ['Completely disagree', 
                                'Somewhat disagree', 
                                'No opinion', 
                                'Completely agree', 
                                'Somewhat agree'],2)

Predictions = rw.prediction_types.make_regression(label_names=_target_names)
workflow = rw.workflows.Regressor()

score_types = rw.score_types.Accuracy(name= 'acc')

def get_cv(X, y):
    cv = ShuffleSplit(n_splits=10, test_size=0.25, random_state=57)
    return cv.split(X, y)

def _get_data(path, split):
    split_path = os.path.join(path, "data", split, "data.csv")
    data = pd.read_csv(split_path, encoding='iso-8859-1', index_col=0)  # XXX rmv index_col=0 if ever needed
    data = data.reset_index(drop=True)  # if index_col=0 in read_csv above

    X = data.drop(['Vaccine','Business2'], axis=1)
    Y = data[['Vaccine','Business2']]
    return X, Y

def get_train_data(path):
    return _get_data(path, 'train')

def get_test_data(path):
    return _get_data(path, 'test')




