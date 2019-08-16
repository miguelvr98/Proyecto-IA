import pandas as pd
import numpy as np

import random

from decision_tree_functions import decision_tree_algorithm, decision_tree_predictions
from helper_functions import train_test_split, calculate_accuracy

adults_train = pd.read_csv('adult_train.csv', header=None,
                       names=['age', 'capital-gain', 'capital-loss', 'hours-per-week',
                              'workClass', 'education', 'marital-status','occupation',
                              'relationship','race','sex','native-country','inconme'])

print(adults_train.shape)  # El metodo shape muestra el numero de filas y columnas del .csv