import pandas as pd
data = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\set_the_data\melb_data.csv')

#dropna is used for the row subset used for perticuler column
data.dropna(axis=0 , subset=['Price'],inplace=True)
# print(data.dtypes)

s = data.dtypes == object
s = list(s[s].index)
print(s)

# we have first option is to drop the object columns
# but it's not the good idea we lose the information of our data
data1 = data.copy()
data2 = data.copy()
data1= data1.drop(s,axis=1)
#Or we can use select_dtypes()
data2 = data2.select_dtypes(exclude=['object'])
print(data1.shape)
print(data2.shape)

#now we use OrdinalEncoder
from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder()
data3 = data.copy()
#But in this method it's not heandle any missing values
data3.fillna(method='ffill',inplace=True)
data3.fillna(method='bfill',inplace=True)
data4 = data3.copy()
data3[s] = encoder.fit_transform(data3[s])

print(data3.shape)


# now we use OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

onehot = OneHotEncoder()
data4 = onehot.fit_transform()