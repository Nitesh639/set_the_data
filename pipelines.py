import pandas as pd
from sklearn.pipeline import Pipeline
data = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\set_the_data\melb_data.csv')

miss = []
                                                                # n = [col for col in data.columns if data[col].isnull().any()]
for col in data.columns:
    if data[col].isnull().any():
        miss.append(col)

st_pipeline = Pipeline([('drop',data.dropna(axis=0 , inplace=True)),
                        ()])
print(st_pipeline)