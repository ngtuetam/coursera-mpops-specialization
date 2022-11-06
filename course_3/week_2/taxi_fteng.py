import tensorflow as tf
from keras import layers
from keras.metrics import RootMeanSquared as RMSE
'''
Increasing model performance with Feature Engineering

Carefully craft features for the data types:
    -  Temporal (pickup date & time)
    - Geographical (latitude and longitude)
'''


# Handling temporal features
def parse_datetime(s):
    if type(s) is not str:
        s = s.numpy().decode('utf-8')
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S %Z")

def get_dayofweek(s):
    ts = parse_datetime(s)
    return DAYS[ts.weekday()]

@tf.function
def dayofweek(ts_in):
    return tf.map_fn(
        lambda s: tf.py_function(get_dayofweek, inp=[s],
            Tout=tf.string),
        ts_in)

# Geolocational features
def euclidean(params):
    lon1, lat1, lon2, lat2 = params
    londiff = lon2 - lon1
    latdiff = lat2 - lat1
    return tf.sqrt(londiff * londiff + latdiff * latdiff)

# Scaling latitude and longitude
def scale_longitude(lon_column):
    return (lon_column + 78)/8.
def scale_latitude(lat_column):
    return (lat_column - 37)/8.