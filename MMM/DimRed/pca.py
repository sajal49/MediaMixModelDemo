from sklearn.decomposition import PCA
import pandas as pd

def get_pcs(X: pd.DataFrame = None, n_components: int = 2):
    # check X
    if X is None:
        raise ValueError("X cannot be None")
    
    # variables to store outputs
    # principal components
    pcs = None
    # explained variance
    exp_vars = None

    # fit PCA
    pca_obj = PCA(n_components = n_components)
    pca_obj.fit(X)

    # assign variables
    pcs = pca_obj.transform(X)
    exp_vars = pca_obj.explained_variance_ratio_

    # return transformation
    return pcs, exp_vars