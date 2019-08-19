import numpy as np
from decision_tree_functions import decision_tree_algorithm 

def bootstrapping(train, n_bootstrap):
    bootstrap_indices = np.random.randint(low=0, high=len(train), size=n_bootstrap)
    df_bootstrapped = train.iloc[bootstrap_indices]
    
    return df_bootstrapped

def random_forest_algorithm(train, n_trees, n_bootstrap, n_features, dt_max_depth):
    forest = []
<<<<<<< HEAD
    for _ in range(num_trees):
        b = bootstrapping(adults_train,num_bootstrap)
        tree = decision_tree_algorithm(b,max_depth=dt_max_depth,random_subspace=num_features)
=======
    for i in range(n_trees):
        df_bootstrapped = bootstrapping(train, n_bootstrap)
        tree = decision_tree_algorithm(df_bootstrapped, max_depth=dt_max_depth, random_subspace=n_features)
>>>>>>> 14e69b4685d970ee495e6d99f1364f027982b14f
        forest.append(tree)
    
    return forest