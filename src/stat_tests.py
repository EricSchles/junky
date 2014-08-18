import pandas as pd
import numpy as np
#expects a pandas dataframe
def z_score(df):
    scores = {}
    cols = dict(df)
    for col in cols.keys():
        scores[col] = {'zscore': (cols[col] - cols[col].mean())/cols[col].std(ddof=0) }
    return scores
