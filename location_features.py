import numpy as np
import pandas as pd
import csv
from sklearn.ensemble import RandomForestRegressor
from sklearn import ensemble
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_log_error



#load the file with the taxi zones

#keep only the popular zones
popularity = pd.read_csv("zone_popularity.csv")

one_hot_zones = pd.get_dummies(popularity['LocationID_'], sparse=True).astype('bool')
one_hot_names=[]
for j in range(len(one_hot_zones.columns)):
 one_hot_names.append('zone_'+str(j+1))

one_hot_zones.columns=one_hot_names
one_hot_zones = popularity.join(one_hot_zones)


zone_popularity_arr=np.array(popularity['nof_trips_sum'].to_list())
L=40

popular_zones=zone_popularity_arr.argsort()[-L:][::-1] #get the rows/ zones of the L-most popular zones
print('popular zone')
print(popular_zones)
cols = [x+3 for x in popular_zones]
print('cols to be kept')
print(cols)
one_hot_zones=one_hot_zones[['LocationID_']+[one_hot_zones.columns[i] for i in cols ]]

one_hot_zones.to_csv("one_hot_popular_taxi_zones_lookup.csv", index=False)

location_features = pd.read_csv("taxi_zones_clusters.csv")

one_hot_location = pd.get_dummies(location_features['LocationID'], sparse=True).astype('bool')
one_hot_names=[]
for i in range(len(one_hot_location.columns)):
    one_hot_names.append('LocationID_'+str(i+1))


one_hot_location.columns=one_hot_names
one_hot_location_features =  location_features[['LocationID']].join(one_hot_location)


tree_depth=6
one_hot_names_all=[]
###get the one-hot representation for the clusters of the pickup locations
for i in range(tree_depth+1):
#    #print(i)
    one_hot_clusters = pd.get_dummies(location_features['level_'+str(i+1)], sparse=True).astype('bool')
    one_hot_names=[]
    for j in range(len(one_hot_clusters.columns)):
        one_hot_names.append('level_'+str(i+1)+'_'+str(j+1))
        one_hot_names_all.append('level_'+str(i+1)+'_'+str(j+1))
    one_hot_clusters.columns=one_hot_names
    del location_features['level_'+str(i+1)]
    location_features = location_features.join(one_hot_clusters)
#
one_hot_names_all=['LocationID']+one_hot_names_all
location_features=location_features[one_hot_names_all]
location_features.drop_duplicates(keep='first',inplace=False).to_csv('taxi_zones_binary_clusters.csv', index=False)

popular_location_features=location_features[['LocationID']]


zones=location_features['LocationID'].to_list()
del location_features['LocationID']
cluster_popularity=[]
for cluster in location_features: #each loop is processing a column/cluster: the corresponding row has 1 if zone belongs to the cluster
    
    index_list=location_features.index[location_features[cluster] == True].tolist()#zones contained in the cluster
    zones_in_cluster=[zones[i] for i in index_list] #get the zones/rows that belong to the cluster
    print(zones_in_cluster)
    c=popularity.loc[popularity['LocationID_'].isin(zones_in_cluster), 'nof_trips_sum'].sum() #add the popularity of zones in the cluster
    cluster_popularity.append(c) #add the popularity of the cluster
    print(c)

cluster_popularity_arr=np.array(cluster_popularity)
N=50

print('popular clusters')
popular_clusters=cluster_popularity_arr.argsort()[-N:][::-1] #get the N-most popular clusters
print(popular_clusters)

cols = [x for x in popular_clusters]
df2=location_features.iloc[: , cols] #keep only the popular clsuters
popular_location_features=popular_location_features.join(df2)#match each location with the flag that it belongs or not to each cluster
#popular_location_features.to_csv(path+'popular_taxi_zones_binary_clusters.csv', index=False)
popular_location_features.to_csv('popular_taxi_zones_binary_clusters.csv', index=False)

