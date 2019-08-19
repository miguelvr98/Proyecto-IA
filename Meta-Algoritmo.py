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

print((btg.random_forest_algorithm(train,n_trees =8 , n_bootstrap =10 , n_features = 10, dt_max_depth= 3)))

