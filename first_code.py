# import numpy as np
import pandas as pd 
import json
# import bq_helper
from pandas.io.json import json_normalize
# import seaborn as sns
# import matplotlib.pyplot as plt
# from plotly.offline import init_notebook_mode  # iplot
# import plotly.graph_objs as go
# from plotly import tools
# init_notebook_mode(connected=True)

json_cols = ['device', 'geoNetwork', 'totals', 'trafficSource']


def load_df(filename):
    path = "/home/akeister/Data/Google Analytics Revenue/" + filename
    df = pd.read_csv(path, converters={column: json.loads for column in json_cols}, 
                     dtype={'fullVisitorId': 'str'})
    
    for column in json_cols:
        column_as_df = json_normalize(df[column])
        column_as_df.columns = [f"{column}_{subcolumn}" for subcolumn in column_as_df.columns]
        df = df.drop(column, axis=1).merge(column_as_df, right_index=True, left_index=True)
    return df


train = load_df("train_reduced.csv")
print("There are " + str(train.shape[0]) + " rows and " + str(train.shape[1]) + " raw columns in this dataset")

print("Snapshot: ")
train.head()
