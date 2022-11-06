'''
A baseline model is a naive implementation that helps with setting expectations for model performance
'''
import tensorflow as tf
from keras import layers
from keras.metrics import RootMeanSquared as RMSE

# avoid undefined value error
inputs = 0
feature_columns = 0
models = 0

dnn_inputs = layers.DenseFeatures(feature_columns.values())(inputs)
h1 = layers.Dense(32, activation='relu', name='h1')(dnn_inputs)
h2 = layers.Dense(8, activation='relu', name='h2')(h1)

output = layers.Dense(1, activation='linear', name='fare')(h2)
model = models.Model(inputs, output)
model.compile(optimizer='adam', loss='mse',
              metrics=[RMSE(name='rmse'), 'mse'])