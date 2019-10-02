# Predict the total ride duration of taxi trips in New York City

This tutorial develops a prediction model for the New York City Taxi Trip Duration on [Kaggle](https://www.kaggle.com/c/10-718-2019s). You may refer to the `trip_time_prediction.pdf` for a detailed description of the model and features used for this task.



## Setting-up the tutorial
1. Clone the repo

```
git clone https://github.com/ifiaposto/Taxi-Trip-Duration-Prediction.git
```
2. Install the requirements

```
pip install -r requirements.txt
```
3. Download the data

You can download the data from [Kaggle](https://www.kaggle.com/c/10-718-2019s). After downloading, unzip and save the CSV files to a directory called `data` in the root of this repository.

## Running the tutorial
For a detailed description of the files mentioned below, you may refer to the   report `trip_time_prediction.pdf` provided in the repository.

### 1. Traffic Level Computation

```
python3 traffic_binarization.py
```
This step computes the discretized traffic level per location and hour of the day and per location and day of the week. It generates the files:

traffic_location_hour.csv

traffic_location_weekday.csv

### 2. Zone Popularity Computation

```
python3 zone_popularity.py
```
This step computes the discretized popularity level of each sub-area. It generates the files:

zone_populariy.csv

### 3. Graph Location Construction

```
python3 graph_part.py
```
This step constructs the location graphs, partitions the graph given their popularity and computes the distance between each pair of sub areas. The discretization information used for the graph is provided in the directory called `NYC_Maps` in the root of this repository.  It generates the files:

taxi_zones_clusters.csv

distances.csv

### 4. Location Features Construction

```
python3 location_features.py
```

This step keeps the most popular clusters and locations that will be used as features for the regressor, and it creates the one hot representation for each subarea. It generates the generates the files:

popular_taxi_zones_binary_clusters.csv

one_hot_popular_taxi_zones_lookup.csv

### 5. Features Construction for the Testing Data

```
python3 test_features.py
```

This step computes the features for the testing dataset. It generates the file:

X_test.csv

### 6. Training and Validation Dataset formation, Model Training.

```
python3 split_learn_features.py
```

This file splits the dataset in the validation/ training dataset. It computes the traffic and location features for them. Subsequently, a random  forest regressor is fitted. Finally, it predicts the trip duration for the testing dataset. It prints a log file with the importance of the features, the validation error achieved and the learning time.


## Contact

Any questions and requests for access to the data can be directed to iapostol@andrew.cmu.edu







