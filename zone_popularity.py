import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime


#load csv
train_dataset = pd.read_csv("data/train.csv")

#check that there are no missing values (same number of entries per col)
train_dataset.info()


##################### compute the traffic level for each location per hour
#count the number of pickups at each location and time of the day
df1=train_dataset.groupby(['PULocationID']).size().reset_index().rename(columns={0:'nof_trips'})
df1.rename(index=str, columns={"PULocationID": "LocationID"}, inplace=True)

#count the number of dropoffs at each location and time of the day
df2=train_dataset.groupby(['DOLocationID']).size().reset_index().rename(columns={0:'nof_trips'})
df2.rename(index=str, columns={"DOLocationID": "LocationID"}, inplace=True)

#sum the total number of drop-offs and pick-ups at each location and time of the day
df1=df1.append(df2, ignore_index=True)
df2 = df1.groupby(['LocationID']).agg({'nof_trips': ['sum']}).reset_index()
df2.columns = ["_".join(x) for x in df2.columns.ravel()]
df2['popularity'] = pd.cut(df2['nof_trips_sum'], 10, labels=False)

#unknown areas
df2 = df2.append({'LocationID_': 264, 'nof_trips_sum' : 0, 'popularity' : 0}, ignore_index=True)
df2 = df2.append({'LocationID_': 265, 'nof_trips_sum' : 0, 'popularity' : 0}, ignore_index=True)


line = pd.DataFrame({'LocationID_': 103, 'nof_trips_sum' : 0, 'popularity' : 0}, index=[102])
df3 = pd.concat([df2.iloc[:101], line, df2.iloc[102:]]).reset_index(drop=True)

df3.to_csv('zone_popularity.csv', index=False)
