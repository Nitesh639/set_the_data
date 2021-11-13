import pandas as pd
data = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\set_the_data\melb_data.csv')
print(data.shape)
#print(data.head())

print(data.info())


l=data.isnull().sum()
print(l)