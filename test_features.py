import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime


#load csv
#path2='cropped_taxi_data/'
#path='taxi_data/'


#load the testing dataset
#X_test = pd.read_csv(path2+"valid_unlab.csv")
X_test = pd.read_csv("data/valid_unlab.csv")
print(X_test.info())

#Datetyping the dates so we can work with it
X_test['tpep_pickup_datetime'] = pd.to_datetime(X_test.tpep_pickup_datetime)
X_test['dayofyear'] = X_test.tpep_pickup_datetime.dt.dayofyear
X_test['week'] = X_test.tpep_pickup_datetime.dt.week
X_test['weekday'] = X_test.tpep_pickup_datetime.dt.weekday
X_test['pickup_hour'] = X_test.tpep_pickup_datetime.dt.hour
X_test['pickup_p1_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+1)%24)
X_test['pickup_p2_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+2)%24)
X_test['pickup_p3_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+3)%24)
X_test['pickup_p4_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+4)%24)
X_test['pickup_p5_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+5)%24)
X_test['pickup_p6_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+6)%24)
X_test['pickup_p7_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+7)%24)
X_test['pickup_p8_hour'] = ((X_test.tpep_pickup_datetime.dt.hour+8)%24)
print('hours, weekdays, day of year extracted')
print(X_test.info(verbose=True))
#X_test.to_csv(path2+'X_test_0.csv', index=False)
X_test.to_csv('X_test_0.csv', index=False)
#print(X_test.head(10))

#load the traffic per location and hour of the day
#df_traffic_per_hour=  pd.read_csv(path+"traffic_location_hour.csv")
df_traffic_per_hour=  pd.read_csv("traffic_location_hour.csv")

print('traffic per location and hour loaded!')

#rename the keys to perform the merging for the pick-up hour
df_traffic_per_hour.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"hour":"pickup_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['PULocationID', 'pickup_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_pickup_hour"}, inplace=True)

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_hour"}, inplace=True)

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_hour":"pickup_p1_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p1_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p1_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p1_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p1_hour":"pickup_p2_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p2_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p2_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p2_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p2_hour":"pickup_p3_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p3_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p3_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p3_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p3_hour":"pickup_p4_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p4_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p4_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p4_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p4_hour":"pickup_p5_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p5_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p5_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p5_hour']


df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p5_hour":"pickup_p6_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p6_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p6_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p6_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p6_hour":"pickup_p7_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p7_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p7_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p7_hour']


df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p7_hour":"pickup_p8_hour"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_hour, on=['DOLocationID', 'pickup_p8_hour'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_p8_hour"}, inplace=True)
del X_test['bin_traffic_level']
del X_test['pickup_p8_hour']

print('pickup hour traffic merged!')
print(X_test.info(verbose=True))
#print(X_test.head(10))

#load the traffic per location and  day of the week
#df_traffic_per_weekday=  pd.read_csv(path+"traffic_location_weekday.csv")
df_traffic_per_weekday=  pd.read_csv("traffic_location_weekday.csv")

df_traffic_per_weekday.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_weekday, on=['PULocationID', 'weekday'])
X_test.rename(index=str, columns={"traffic_level": "traffic_pickup_weekday"}, inplace=True)

df_traffic_per_weekday.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
X_test=pd.merge(X_test, df_traffic_per_weekday, on=['DOLocationID', 'weekday'])
X_test.rename(index=str, columns={"traffic_level": "traffic_dropoff_weekday"}, inplace=True)


print(X_test.info())
print('weekday traffic merged!')

##load the traffic per location and  day of year
#df_traffic_per_dayofyear=  pd.read_csv(path+"traffic_location_dayofyear.csv")
#df_traffic_per_dayofyear =df_traffic_per_dayofyear[['LocationID','dayofyear','traffic_level']]
#print(df_traffic_per_dayofyear.head(10))
##add any missing values to make sure that all test entries will be merged!
#df_traffic_per_dayofyear.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
#common=pd.merge(X_test, df_traffic_per_dayofyear, on=['PULocationID', 'dayofyear'])
#diff=X_test[(~X_test.PULocationID.isin(common.PULocationID))&(~X_test.dayofyear.isin(common.dayofyear))]
#X_test=pd.merge(X_test, df_traffic_per_dayofyear, on=['PULocationID', 'dayofyear'])
#print(X_test.info(verbose=True))
#print(X_test[['Id','PULocationID', 'dayofyear']])
#print('what it could not be merged!')
##print(len(diff.index))
#print(diff.info(verbose=True))
#
#common.rename(index=str, columns={"traffic_level": "traffic_dayofyear"}, inplace=True)
#print(common.info(verbose=True))
#diff['traffic_dayofyear']=0
#X_test=pd.concat([common, diff])
#X_test.to_csv(path2+'X_test_1.csv', index=False)
#print(X_test.info())
#
#print('dayofyear traffic merged!')


#delete uneccessary features
del X_test['VendorID']
del X_test['passenger_count']
del X_test['tpep_pickup_datetime']
del X_test['payment_type']

del X_test['week']
#del X_test['weekday']
del X_test['dayofyear']
#del X_test['pickup_hour']
del X_test['nof_trips_sum_x']
del X_test['bin_traffic_level_x']
del X_test['nof_trips_sum_y']
del X_test['bin_traffic_level_y']
#del X_test['bin_traffic_level']


X_test['traffic_pickup_hour'] = X_test['traffic_pickup_hour'].astype('uint8')
X_test['traffic_dropoff_hour'] = X_test['traffic_dropoff_hour'].astype('uint8')
X_test['traffic_pickup_weekday'] = X_test['traffic_pickup_weekday'].astype('uint8')
X_test['traffic_dropoff_weekday'] = X_test['traffic_dropoff_weekday'].astype('uint8')
print('traffic features added!')
print(X_test.info(verbose=True))


##compute distance between pickup-drop-off location
#distances = pd.read_csv(path2+"distances.csv")
distances = pd.read_csv("distances.csv")

X_test=pd.merge(X_test, distances, on=['PULocationID', 'DOLocationID'])
X_test['distance'] =X_test['distance'].astype('uint8')
print('distances computed!')
print(X_test.info(verbose=True))


#compute one hot representation for the popular zones
#zones = pd.read_csv(path2+"one_hot_popular_taxi_zones_lookup.csv")
zones = pd.read_csv("one_hot_popular_taxi_zones_lookup.csv")

zones.rename(index=str, columns={"LocationID_":"PULocationID"}, inplace=True)
zones.columns=zones.columns.str.replace('zone', 'pickup_zone')
X_test=pd.merge(X_test, zones, on=['PULocationID'])
print('one hot pickup location merged!')

zones.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
zones.columns=zones.columns.str.replace('pickup_zone', 'dropoff_zone')
X_test=pd.merge(X_test, zones, on=['DOLocationID'])
print('one hot representations of taxi zones  added!')
print(X_test.info(verbose=True))


#location_features = pd.read_csv(path2+"popular_taxi_zones_binary_clusters.csv")
location_features = pd.read_csv("popular_taxi_zones_binary_clusters.csv")
location_features.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
location_features.columns=location_features.columns.str.replace('level', 'pickup_level')
X_test=pd.merge(X_test, location_features, on=['PULocationID'])
print('pickup location features merged!')
print(X_test.info(verbose=True))
location_features.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
location_features.columns=location_features.columns.str.replace('pickup_level', 'dropoff_level')
X_test=pd.merge(X_test, location_features, on=['DOLocationID'])
print('pickup location features merged!')
print(X_test.info(verbose=True))


X_test=X_test.sort_values(by=['Id'])
#X_test.to_csv(path2+'X_test.csv', index=False)
X_test.to_csv('X_test.csv', index=False)

print('all features added!')
print(X_test.info(verbose=True))

