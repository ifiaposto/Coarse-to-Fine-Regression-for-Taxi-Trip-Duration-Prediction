import numpy as np
import pandas as pd
from datetime import datetime


#load csv with the training dataset
train_dataset = pd.read_csv("data/train.csv")

#check that there are no missing values (same number of entries per col)
train_dataset.info()


#Datetyping the dates so we can work with it
train_dataset['tpep_pickup_datetime'] = pd.to_datetime(train_dataset.tpep_pickup_datetime)
train_dataset['dayofyear'] = train_dataset.tpep_pickup_datetime.dt.dayofyear
train_dataset['week'] = train_dataset.tpep_pickup_datetime.dt.week
train_dataset['weekday'] = train_dataset.tpep_pickup_datetime.dt.weekday
train_dataset['pickup_hour'] = train_dataset.tpep_pickup_datetime.dt.hour
print('hours, weekdays, day of year extracted')
#compute the hour of the dropoff from the travel time and the pickup time
train_dataset['dropoff_hour'] =(train_dataset.pickup_hour+ (train_dataset.travel_time // 60)%24)
print('dropoff hour extracted')


##################### compute the traffic level for each location per hour
#count the number of pickups at each location and time of the day
df1=train_dataset.groupby(['PULocationID', 'pickup_hour']).size().reset_index().rename(columns={0:'nof_trips'})
df1.rename(index=str, columns={"PULocationID": "LocationID"}, inplace=True)
df1.rename(index=str, columns={"pickup_hour": "hour"}, inplace=True)

#count the number of dropoffs at each location and time of the day
df2=train_dataset.groupby(['DOLocationID', 'dropoff_hour']).size().reset_index().rename(columns={0:'nof_trips'})
df2.rename(index=str, columns={"DOLocationID": "LocationID"}, inplace=True)
df2.rename(index=str, columns={"dropoff_hour": "hour"}, inplace=True)

#sum the total number of drop-offs and pick-ups at each location and time of the day
df1=df1.append(df2, ignore_index=True)
df_traffic_per_hour = df1.groupby(['LocationID', 'hour']).agg({'nof_trips': ['sum']}).reset_index()
df_traffic_per_hour.columns = ["_".join(x) for x in df_traffic_per_hour.columns.ravel()]
#compute percentiles  of the traffic level for each location
df_traffic_per_hour['traffic_level'] = pd.cut(df_traffic_per_hour['nof_trips_sum'], 6, labels=False)
print('traffic levels per hour and location were discretized:')
print(df_traffic_per_hour['traffic_level'].value_counts())
#binarize the traffic level feature
def discretize_traffic(row):
    return (row['traffic_level'] >=4)#it will keep the busiest 20% hours of the day for the region
df_traffic_per_hour['bin_traffic_level']=df_traffic_per_hour.apply(discretize_traffic, axis=1)
print('traffic levels per hour and location were binarized')
df_traffic_per_hour.rename(index=str, columns={"LocationID_": "LocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"hour_": "hour"}, inplace=True)
df_traffic_per_hour.to_csv('traffic_location_hour.csv', index=False)

#################### compute the traffic level for each location per day of the week
#count the number of pickups at each location and time of the day
df1=train_dataset.groupby(['PULocationID', 'weekday']).size().reset_index().rename(columns={0:'nof_trips'})
df1.rename(index=str, columns={"PULocationID": "LocationID"}, inplace=True)

#count the number of dropoffs at each location and time of the day
df2=train_dataset.groupby(['DOLocationID', 'weekday']).size().reset_index().rename(columns={0:'nof_trips'})
df2.rename(index=str, columns={"DOLocationID": "LocationID"}, inplace=True)

#sum the total number of drop-offs and pick-ups at each location and time of the day
df1=df1.append(df2, ignore_index=True)
df_traffic_per_weekday = df1.groupby(['LocationID', 'weekday']).agg({'nof_trips': ['sum']}).reset_index()
df_traffic_per_weekday.columns = ["_".join(x) for x in df_traffic_per_weekday.columns.ravel()]
#compute percentiles  of the traffic level for each location
df_traffic_per_weekday['traffic_level'] = pd.cut(df_traffic_per_weekday['nof_trips_sum'], 6, labels=False)
print('traffic levels per day of week and location were discretized:')
print(df_traffic_per_weekday['traffic_level'].value_counts())
#binarize the traffic level feature
def discretize_traffic(row):
    return (row['traffic_level'] >=4)
df_traffic_per_weekday['bin_traffic_level']=df_traffic_per_weekday.apply(discretize_traffic, axis=1)
df_traffic_per_weekday.rename(index=str, columns={"LocationID_": "LocationID"}, inplace=True)
df_traffic_per_weekday.rename(index=str, columns={"weekday_": "weekday"}, inplace=True)
print('traffic levels per day of week and location were binarized')
df_traffic_per_weekday.to_csv('traffic_location_weekday.csv', index=False)


#################### compute the traffic level for each location per dayofyear
#count the number of pickups at each location and day of the year
df1=train_dataset.groupby(['PULocationID', 'dayofyear']).size().reset_index().rename(columns={0:'nof_trips'})
df1.rename(index=str, columns={"PULocationID": "LocationID"}, inplace=True)

#count the number of dropoffs at each location day of the year
df2=train_dataset.groupby(['DOLocationID', 'dayofyear']).size().reset_index().rename(columns={0:'nof_trips'})
df2.rename(index=str, columns={"DOLocationID": "LocationID"}, inplace=True)

#sum the total number of drop-offs and pick-ups at each location and day of year
df1=df1.append(df2, ignore_index=True)
df_traffic_per_dayofyear = df1.groupby(['LocationID', 'dayofyear']).agg({'nof_trips': ['sum']}).reset_index()
df_traffic_per_dayofyear.columns = ["_".join(x) for x in df_traffic_per_dayofyear.columns.ravel()]
#compute percentiles  of the traffic level for each location
df_traffic_per_dayofyear['traffic_level'] = pd.cut(df_traffic_per_dayofyear['nof_trips_sum'], 6, labels=False)
print('traffic levels per day of dayof year and location were discretized:')
print( df_traffic_per_dayofyear['traffic_level'].value_counts())
#binarize the traffic level feature
def discretize_traffic(row):
    return (row['traffic_level'] >=4)
df_traffic_per_dayofyear['bin_traffic_level']=df_traffic_per_dayofyear.apply(discretize_traffic, axis=1)
print('traffic levels per day of dayof year and location were binarized')
df_traffic_per_dayofyear.rename(index=str, columns={"LocationID_": "LocationID"}, inplace=True)
df_traffic_per_dayofyear.rename(index=str, columns={"dayofyear_": "dayofyear"}, inplace=True)




