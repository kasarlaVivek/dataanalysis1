import pandas as pd
import numpy as np
from scipy import stats
data=pd.read_csv('/content/01.Data Cleaning and Preprocessing.csv')
type(data)
print(data.info)
data.describe()
data=data.drop_duplicates()
print(data)
print(data.isnull())
print(data.isnull().sum())
print(data.notnull())
print(data.isnull().sum().sum())
data=data.fillna(value=0)
print(data)
data_fwd=data
print(data_fwd.columns)
data_fwd.drop(['Observation'],axis=1,inplace=True)
print(data_fwd.columns)
q1=data_fwd.quantile(0.25)
q2=data_fwd.quantile(0.75)
iqr=q2-q1
print(iqr)
data_fwd=data_fwd[~((data_fwd<(q1-1.5*iqr))|(data_fwd>(q2+1.5*iqr))).any(axis=1)]
print(data_fwd)
