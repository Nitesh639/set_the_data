import pandas as pd
data = pd.read_csv(r'C:\Users\Lenovo\PycharmProjects\set_the_data\melb_data.csv')

#dropna is used for the row subset used for perticuler column
data.dropna(axis=0 , subset=['Price'],inplace=True)

#In this code we drop the all missing columns
miss = []
                                                                # n = [col for col in data.columns if data[col].isnull().any()]
for col in data.columns:
    if data[col].isnull().any():
        miss.append(col)            #all columns with the drop values
data1 = data.drop(miss , axis=1)        #now we drop the missing values
print(data1.shape)

#We use the fillna method to add the data
data2 = data.copy()
data2.fillna(method='ffill',inplace=True)
data2.fillna(method="bfill",inplace=True)
print(data2.shape)

#It's Extension of last one
data3 = data.copy()
for col in miss:
    data3[col+'_was_missing'] = data3[col].isnull()

data3.fillna(method='ffill',inplace=True)
data3.fillna(method="bfill",inplace=True)
print(data3.shape)

from sklearn.impute import SimpleImputer
data4 = data.copy()
mean_imputer = SimpleImputer(strategy='constant')
data5 = pd.DataFrame(mean_imputer.fit_transform(data4))

#When we use to SimpleImputer all columns name remove then we put the columns name
data5.columns = data.columns
print(data5.columns)
# print(data5.groupby('car'))

# print(n)