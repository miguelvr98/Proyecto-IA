import numpy as np
from decision_tree_functions import decision_tree_algorithm

def bootstrapping(train, n):

    indices = np.random.randint(low=0, high=len(train), size=n)
    result = train.iloc[indices]
    
    return result

def methodBootstrapping(adults_train,num_bootstrap,num_trees, num_features, dt_max_depth) :

    forest = []
    for _ in range(num_trees):
        b = bootstrapping(adults_train,num_bootstrap)
        tree = decision_tree_algorithm(b,max_depth=dt_max_depth,random_subspace=num_features)
        forest.append(tree)
        indice = indice + 1
    return forest