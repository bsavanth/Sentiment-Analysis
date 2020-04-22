import pandas as pd
import numpy as np
from sklearn import preprocessing

my_data = pd.read_csv('word2vec.txt', sep=',')

X = my_data.iloc[:,0:].values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(X)
df_normalized = pd.DataFrame(x_scaled)

df_normalized.to_csv('dataset.txt', header=None, index=None, sep=',', mode='a')



Training_X = df_normalized.iloc[0:5221,:].values
Testing_X = df_normalized.iloc[5281:5331,:].values
Training_Y = df_normalized.iloc[5331:10611,:].values
Testing_Y = df_normalized.iloc[10611:10662,:].values


df1=pd.DataFrame(data=Training_X)
df2=pd.DataFrame(data=Testing_X)
df3=pd.DataFrame(data=Training_Y)
df4=pd.DataFrame(data=Testing_Y)

frames = [df1, df3]
Training = pd.concat(frames)

print(Training.shape)

frames1 = [df2, df4]
Testing = pd.concat(frames1)
print(Testing.shape)


Training.to_csv('Training.txt', header=None, index=None, sep=',', mode='a')
Testing.to_csv('Testing.txt', header=None, index=None, sep=',', mode='a')








