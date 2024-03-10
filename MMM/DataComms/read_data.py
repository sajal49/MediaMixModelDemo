import pandas as pd
from typing import List

def return_data(path: str = None) -> pd.DataFrame:
    """
    TO BE COMPLETED
    Given path(str), return a pandas dataframe
    """
    if path is None:
        raise ValueError("Path cannot be None")
    data = None
    
    # <your code goes here>
    data = pd.read_csv(path)

    return data

def return_text_data(path: str = None) -> List[str]:
    """
    TO BE COMPLETED
    Given path(str), returns a list of strings
    """
    if path is None:
        raise ValueError("Path cannot be None")
    data = None
    
    # <your code goes here>

    return data
