from sklearn.neighbors import LocalOutlierFactor
import pandas as pd
import numpy as np
from ..DataComms import read_data
from typing import List

def identify_outlier(X: pd.DataFrame = None, colnm: List[str] = None, n_neighbors: int = 10):
    # check X
    if X is None:
        raise ValueError("X cannot be None")
    
    # subset
    if colnm is None:
        colnm = X.columns
    
    # find outliers
    lof = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=0.1)
    out_list = []
    for i in colnm:
        lof.fit(X[[i]])
        score = lof.negative_outlier_factor_
        score = np.round(score)
        out_list.append(np.where(score < -5)[0])
    
    # return sample indices
    return out_list
