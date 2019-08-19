import pandas as pd
import numpy as np

import random

from decision_tree_functions import decision_tree_algorithm, decision_tree_predictions
from helper_functions import train_test_split, calculate_accuracy
import bootstrapping as btg

train = pd.read_csv('adult_train.csv', header=None,
                       names=['age', 'capital-gain', 'capital-loss', 'hours-per-week',
                              'workClass', 'education', 'marital-status','occupation',
                              'relationship','race','sex','native-country','inconme'])

print("¿Number of trees?")
n_trees = input()

print("Number of bootstrap")
n_bootstrap= input()

print("¿Number of features?")
n_features = input()

print("¿Max depth?")
dt_max_depth = input()

print((btg.random_forest_algorithm(train, int(n_trees) , int(n_bootstrap) , int(n_features), int(dt_max_depth))))

