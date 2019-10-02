import numpy as np
import pandas as pd
import time
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn import ensemble
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_log_error



############################################################################# split to training and validation set   ############################################################################
X_train = pd.read_csv("data/train.csv")
print(X_train.info(verbose=True))
#get the last entries of the data for validation
X_val=X_train.tail(5000000)
#get a fraction of the first entries of the data for training
X_train=X_train.head(55000000)
X_train=X_train.sample(frac=0.2)

print('training dataset computed')
print(X_train.head(100))
print(X_train.info(verbose=True))


print('validation dataset computed')

############################################################################# compute features for the training dataset  ############################################################################

######################## compute traffic features for training dataset
print(X_train.info())
#Datetyping the dates so we can work with it
X_train['tpep_pickup_datetime'] = pd.to_datetime(X_train.tpep_pickup_datetime)
X_train['dayofyear'] = X_train.tpep_pickup_datetime.dt.dayofyear
X_train['week'] = X_train.tpep_pickup_datetime.dt.week
X_train['weekday'] = X_train.tpep_pickup_datetime.dt.weekday
X_train['pickup_hour'] = X_train.tpep_pickup_datetime.dt.hour
X_train['pickup_p1_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+1)%24)
X_train['pickup_p2_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+2)%24)
X_train['pickup_p3_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+3)%24)
X_train['pickup_p4_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+4)%24)
X_train['pickup_p5_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+5)%24)
X_train['pickup_p6_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+6)%24)
X_train['pickup_p7_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+7)%24)
X_train['pickup_p8_hour'] = ((X_train.tpep_pickup_datetime.dt.hour+8)%24)
print('hours, weekdays, day of year extracted')

#load the traffic per location and hour of the day
df_traffic_per_hour=  pd.read_csv("traffic_location_hour.csv")

print('traffic per location and hour loaded!')

#rename the keys to perform the merging for the pick-up hour
df_traffic_per_hour.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"hour":"pickup_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['PULocationID', 'pickup_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_pickup_hour"}, inplace=True)
del X_train['bin_traffic_level']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_hour"}, inplace=True)
del X_train['bin_traffic_level']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_hour":"pickup_p1_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p1_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p1_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p1_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p1_hour":"pickup_p2_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p2_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p2_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p2_hour']


df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p2_hour":"pickup_p3_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p3_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p3_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p3_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p3_hour":"pickup_p4_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p4_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p4_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p4_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p4_hour":"pickup_p5_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p5_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p5_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p5_hour']


df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p5_hour":"pickup_p6_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p6_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p6_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p6_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p6_hour":"pickup_p7_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p7_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p7_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p7_hour']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_p7_hour":"pickup_p8_hour"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_hour, on=['DOLocationID', 'pickup_p8_hour'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_p8_hour"}, inplace=True)
del X_train['bin_traffic_level']
del X_train['pickup_p8_hour']

print('pickup hour traffic merged!')
print(X_train.info(verbose=True))

#load the traffic per location and  day of the week
df_traffic_per_weekday=  pd.read_csv("traffic_location_weekday.csv")

df_traffic_per_weekday.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_weekday, on=['PULocationID', 'weekday'])
X_train.rename(index=str, columns={"traffic_level": "traffic_pickup_weekday"}, inplace=True)
del X_train['bin_traffic_level']

df_traffic_per_weekday.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
X_train=pd.merge(X_train, df_traffic_per_weekday, on=['DOLocationID', 'weekday'])
X_train.rename(index=str, columns={"traffic_level": "traffic_dropoff_weekday"}, inplace=True)
del X_train['bin_traffic_level']

print('weekday traffic merged!')
print(X_train.info())



###################### compute location features
print(X_train.info())
#compute distance between pickup-drop-off location
distances = pd.read_csv("distances.csv")

#convert to unsigned int to save memory
X_train['traffic_pickup_hour'] =X_train['traffic_pickup_hour'].astype('uint8')
X_train['traffic_dropoff_hour'] = X_train['traffic_dropoff_hour'].astype('uint8')
X_train['traffic_dropoff_p1_hour'] = X_train['traffic_dropoff_p1_hour'].astype('uint8')
X_train['traffic_dropoff_p2_hour'] = X_train['traffic_dropoff_p2_hour'].astype('uint8')
X_train['traffic_dropoff_p3_hour'] = X_train['traffic_dropoff_p3_hour'].astype('uint8')
X_train['traffic_dropoff_p4_hour'] = X_train['traffic_dropoff_p4_hour'].astype('uint8')
X_train['traffic_dropoff_p5_hour'] = X_train['traffic_dropoff_p5_hour'].astype('uint8')
X_train['traffic_dropoff_p6_hour'] = X_train['traffic_dropoff_p6_hour'].astype('uint8')
X_train['traffic_dropoff_p7_hour'] = X_train['traffic_dropoff_p7_hour'].astype('uint8')
X_train['traffic_dropoff_p8_hour'] = X_train['traffic_dropoff_p8_hour'].astype('uint8')
X_train['traffic_dropoff_weekday'] = X_train['traffic_dropoff_weekday'].astype('uint8')
X_train['traffic_pickup_weekday'] = X_train['traffic_pickup_weekday'].astype('uint8')

X_train=pd.merge(X_train, distances, on=['PULocationID', 'DOLocationID'])
X_train['distance'] =X_train['distance'].astype('uint8')

print('distance feature added')
print(X_train.info())

#load the file with the clustering of the taxi zones
#location_features = pd.read_csv(path+"popular_taxi_zones_binary_clusters.csv")
location_features = pd.read_csv("popular_taxi_zones_binary_clusters.csv")

location_features.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
location_features.columns=location_features.columns.str.replace('level', 'pickup_level')
X_train=pd.merge(X_train, location_features, on=['PULocationID'])
print('pickup location features merged!')

location_features.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
location_features.columns=location_features.columns.str.replace('pickup_level', 'dropoff_level')
X_train=pd.merge(X_train, location_features, on=['DOLocationID'])
print('dropoff location features merged!')
print(X_train.info(verbose=True))

#load the file with the one hot representation of most popular zones
zones = pd.read_csv("one_hot_popular_taxi_zones_lookup.csv")

zones.rename(index=str, columns={"LocationID_":"PULocationID"}, inplace=True)
zones.columns=zones.columns.str.replace('zone', 'pickup_zone')
X_train=pd.merge(X_train, zones, on=['PULocationID'])
print('one hot pickup location merged!')

zones.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
zones.columns=zones.columns.str.replace('pickup_zone', 'dropoff_zone')
X_train=pd.merge(X_train, zones, on=['DOLocationID'])
print('one hot dropoff location merged!')
print(X_train.info(verbose=True))




print('location features added')

#delete uneccesary features to save memory
del X_train['week']
del X_train['passenger_count']




############################################################################ model features   ########################################################################

#features (independent variables to be used)
features=['distance', 'traffic_pickup_hour', 'pickup_hour', 'weekday','traffic_dropoff_hour', 'traffic_dropoff_p1_hour', 'traffic_dropoff_p2_hour', 'traffic_dropoff_p3_hour', 'traffic_dropoff_p4_hour', 'traffic_dropoff_p5_hour', 'traffic_dropoff_p6_hour', 'traffic_dropoff_p7_hour', 'traffic_dropoff_p8_hour', 'traffic_pickup_weekday','traffic_dropoff_weekday', 'PULocationID','DOLocationID']+[col for col in X_train.columns if 'level' in col]+[col for col in X_train.columns if 'zone' in col]


print(X_train.info())
y_train= X_train['travel_time'].tolist()
X_train=X_train[features]

print('features extracted')
print(X_train.info(verbose=True))


############################################################################ compute features for the validation dataset  ########################################################################
print('validation dataset loaded')
print(X_val.info())
#
####################### compute traffic features
#Datetyping the dates so we can work with it
X_val['tpep_pickup_datetime'] = pd.to_datetime(X_val.tpep_pickup_datetime)
X_val['dayofyear'] = X_val.tpep_pickup_datetime.dt.dayofyear
X_val['week'] = X_val.tpep_pickup_datetime.dt.week
X_val['weekday'] = X_val.tpep_pickup_datetime.dt.weekday
X_val['pickup_hour'] = X_val.tpep_pickup_datetime.dt.hour
X_val['pickup_p1_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+1)%24)
X_val['pickup_p2_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+2)%24)
X_val['pickup_p3_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+3)%24)
X_val['pickup_p4_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+4)%24)
X_val['pickup_p5_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+5)%24)
X_val['pickup_p6_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+6)%24)
X_val['pickup_p7_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+7)%24)
X_val['pickup_p8_hour'] = ((X_val.tpep_pickup_datetime.dt.hour+8)%24)
print('hours, weekdays, day of year extracted')

#load the traffic per location and hour of the day
df_traffic_per_hour=  pd.read_csv("traffic_location_hour.csv")

print('traffic per location and hour loaded!')

#rename the keys to perform the merging for the pick-up hour
df_traffic_per_hour.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"hour":"pickup_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['PULocationID', 'pickup_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_pickup_hour"}, inplace=True)
del X_val['bin_traffic_level']

df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_hour"}, inplace=True)
del X_val['bin_traffic_level']

#df_traffic_per_hour.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
df_traffic_per_hour.rename(index=str, columns={"pickup_hour":"pickup_p1_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p1_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p1_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p1_hour']

df_traffic_per_hour.rename(index=str, columns={"pickup_p1_hour":"pickup_p2_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p2_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p2_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p2_hour']

df_traffic_per_hour.rename(index=str, columns={"pickup_p2_hour":"pickup_p3_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p3_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p3_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p3_hour']

df_traffic_per_hour.rename(index=str, columns={"pickup_p3_hour":"pickup_p4_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p4_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p4_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p4_hour']

df_traffic_per_hour.rename(index=str, columns={"pickup_p4_hour":"pickup_p5_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p5_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p5_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p5_hour']

df_traffic_per_hour.rename(index=str, columns={"pickup_p5_hour":"pickup_p6_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p6_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p6_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p6_hour']

df_traffic_per_hour.rename(index=str, columns={"pickup_p6_hour":"pickup_p7_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p7_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p7_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p7_hour']


df_traffic_per_hour.rename(index=str, columns={"pickup_p7_hour":"pickup_p8_hour"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_hour, on=['DOLocationID', 'pickup_p8_hour'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_p8_hour"}, inplace=True)
del X_val['bin_traffic_level']
del X_val['pickup_p8_hour']


print('pickup hour traffic merged!')
print(X_val.info(verbose=True))

#load the traffic per location and  day of the week
df_traffic_per_weekday=  pd.read_csv("traffic_location_weekday.csv")

df_traffic_per_weekday.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_weekday, on=['PULocationID', 'weekday'])
X_val.rename(index=str, columns={"traffic_level": "traffic_pickup_weekday"}, inplace=True)
del X_val['bin_traffic_level']

df_traffic_per_weekday.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
X_val=pd.merge(X_val, df_traffic_per_weekday, on=['DOLocationID', 'weekday'])
X_val.rename(index=str, columns={"traffic_level": "traffic_dropoff_weekday"}, inplace=True)
del X_val['bin_traffic_level']

print('weekday traffic merged!')
print(X_val.info())



###################### compute location features

#convert to unsigned int to save memory
X_val['traffic_pickup_hour'] =X_val['traffic_pickup_hour'].astype('uint8')
X_val['traffic_dropoff_hour'] = X_val['traffic_dropoff_hour'].astype('uint8')
X_val['traffic_dropoff_p1_hour'] = X_val['traffic_dropoff_p1_hour'].astype('uint8')
X_val['traffic_dropoff_p2_hour'] = X_val['traffic_dropoff_p2_hour'].astype('uint8')
X_val['traffic_dropoff_p3_hour'] = X_val['traffic_dropoff_p3_hour'].astype('uint8')
X_val['traffic_dropoff_p4_hour'] = X_val['traffic_dropoff_p4_hour'].astype('uint8')
X_val['traffic_dropoff_p5_hour'] = X_val['traffic_dropoff_p5_hour'].astype('uint8')
X_val['traffic_dropoff_weekday'] = X_val['traffic_dropoff_weekday'].astype('uint8')
X_val['traffic_pickup_weekday'] = X_val['traffic_pickup_weekday'].astype('uint8')

print(X_train.info())

#compute distance between pickup-drop-off location

X_val=pd.merge(X_val, distances, on=['PULocationID', 'DOLocationID'])
X_val['distance'] =X_val['distance'].astype('uint8')



print('distance feature added')
print(X_val.info())

#load the file with the clustering of the taxi zones
location_features = pd.read_csv("popular_taxi_zones_binary_clusters.csv")

location_features.rename(index=str, columns={"LocationID":"PULocationID"}, inplace=True)
location_features.columns=location_features.columns.str.replace('level', 'pickup_level')
X_val=pd.merge(X_val, location_features, on=['PULocationID'])
print('pickup location features merged!')

location_features.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
location_features.columns=location_features.columns.str.replace('pickup_level', 'dropoff_level')
X_val=pd.merge(X_val, location_features, on=['DOLocationID'])
print('dropoff location features merged!')
print(X_val.info(verbose=True))

#load the file with the one hot representation of most popular zones
zones = pd.read_csv("one_hot_popular_taxi_zones_lookup.csv")

zones.rename(index=str, columns={"LocationID_":"PULocationID"}, inplace=True)
zones.columns=zones.columns.str.replace('zone', 'pickup_zone')
X_val=pd.merge(X_val, zones, on=['PULocationID'])
print('one hot pickup location merged!')

zones.rename(index=str, columns={"PULocationID":"DOLocationID"}, inplace=True)
zones.columns=zones.columns.str.replace('pickup_zone', 'dropoff_zone')
X_val=pd.merge(X_val, zones, on=['DOLocationID'])
print('one hot dropoff location merged!')
print(X_train.info(verbose=True))




print('location features added')

#delete uneccesary features to save memory
del X_val['week']
del X_val['passenger_count']

print(X_val.info())
y_val= X_val['travel_time'].tolist()
X_val=X_val[features]
print('features extracted')
print(X_val.info(verbose=True))

X_val = X_val[X_train.columns]

########################################################################### load the testing dataset   ############################################################################

#load from file
print('load testing!')
#X_test= pd.read_csv(path+"X_test.csv")
X_test= pd.read_csv("X_test.csv")
#make sure the order of the entries is preserved!
X_test=X_test.sort_values(by=['Id'])
print(X_test.info(verbose=True))
#make sure the order of the features is the same with the order of the features in the training dataset
X_test = X_test[X_train.columns]


#convert the types of the traffic features
X_test['traffic_pickup_hour'] = X_test['traffic_pickup_hour'].astype('uint8')
X_test['traffic_dropoff_hour'] = X_test['traffic_dropoff_hour'].astype('uint8')
X_test['traffic_dropoff_p1_hour'] = X_test['traffic_dropoff_p1_hour'].astype('uint8')
X_test['traffic_dropoff_p2_hour'] = X_test['traffic_dropoff_p2_hour'].astype('uint8')
X_test['traffic_dropoff_p3_hour'] = X_test['traffic_dropoff_p3_hour'].astype('uint8')
X_test['traffic_dropoff_p4_hour'] = X_test['traffic_dropoff_p4_hour'].astype('uint8')
X_test['traffic_dropoff_p5_hour'] = X_test['traffic_dropoff_p5_hour'].astype('uint8')
X_test['traffic_dropoff_p6_hour'] = X_test['traffic_dropoff_p6_hour'].astype('uint8')
X_test['traffic_dropoff_p7_hour'] = X_test['traffic_dropoff_p7_hour'].astype('uint8')
X_test['traffic_dropoff_p8_hour'] = X_test['traffic_dropoff_p8_hour'].astype('uint8')
X_test['traffic_pickup_weekday'] = X_test['traffic_pickup_weekday'].astype('uint8')
X_test['traffic_dropoff_weekday'] = X_test['traffic_dropoff_weekday'].astype('uint8')

print('testing dataset loaded!')
print(X_test.info(verbose=True))


############################################################################ start fitting   ############################################################################

#location precision
tree_depth=6
n_estimators=100
max_depth=30
max_features=0.5

print('start fitting')
random_forest=True
print(tree_depth)
if random_forest:
    #fit random forest
    params = {'n_estimators': n_estimators, 'max_depth': max_depth, 'max_features':max_features ,'n_jobs': 10}
    regr = RandomForestRegressor(**params)
    print(params)
    start_time = time.time()
    regr.fit(X_train, y_train)
    learn_time=time.time() - start_time
    print('training random forest finished')
    #predict and copmpute loss functions
    y_pred = regr.predict(X_val)
   
    paramstr=str(tree_depth)+'_'+str(n_estimators)+'_'+str(max_depth)+'_'+str(max_features)
    loss=np.sqrt(mean_squared_log_error(y_val,y_pred))
    print(loss)
    y_test = regr.predict(X_test)
    
    with open('learn_'+paramstr+'.txt', mode='w') as learn_file:
        learn_file.write('learning time '+str(learn_time)+'\n')
        learn_file.write('tree depth '+str(tree_depth)+'\n')
        learn_file.write('n_estimators '+str(n_estimators)+'\n')
        learn_file.write('max_depth '+str(max_depth)+'\n')
        learn_file.write('max_features '+str(max_features)+'\n')
        learn_file.write('val error '+str(loss)+'\n')
        learn_file.write('features')
        i=0;
        for item in features:
            learn_file.write("%s %f\n" % (item,regr.feature_importances_[i]))
            i=i+1
        learn_file.write('feature importance')

    
    #<depth in cluster tree of locatuons >_<number of popular zones>_<number of popular clusters>_<nof estimators/ decision trees>_<max decision tree depth>_<sampling ratio of the features>
    with open('prediction_'+paramstr+'.csv', mode='w') as prediction_file:
        prediction_writer = csv.writer(prediction_file, delimiter=',')
        cols=['Id', 'travel_time']
        prediction_writer.writerow(cols)
        for i in range(len(y_test)):
            prediction_writer.writerow([i+1, y_test[i]])


else:

    params = {'n_estimators': 200, 'max_depth': 3, 'min_samples_split': 2,
    'learning_rate': 0.1, 'loss': 'ls', 'subsample':0.5}
    regr = ensemble.GradientBoostingRegressor(**params)
  
    print(params)
    regr.fit(X_train, y_train)
    print('training gradient boosting finished ')
    y_pred = regr.predict(X_val)
    loss=np.sqrt(mean_squared_log_error(y_val,y_pred))
    print(loss)


print(regr.feature_importances_)
