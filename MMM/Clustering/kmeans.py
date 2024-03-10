from sklearn.cluster import KMeans
import pandas as pd

def get_clusters(X: pd.DataFrame = None, n_clusters: int = 2):
    """
    TO BE COMPLETED
    Given 'X', a pandas datframe and 'n_clusters', number of clusters
    your code create 'n_clusters' in 'X'
    """
    if X is None:
        raise ValueError("X cannot be None")
    
    # variables to return
    # labels: cluster labels is saved here
    # centers: cluster centers is saved here
    labels = None 
    centers = None

    # < your code goes here >
    
    return labels, centers