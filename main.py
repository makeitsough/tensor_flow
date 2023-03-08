## single neuron test (from Moroney 2021)

import tensorflow as tf
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

## Sequential determines layer struct # Dense specified 'fully connected' neurons
model = Sequential([Dense(units=1, input_shape=[1])]) 
## optimizer: stochastic gradient descent measures loss function
model.compile(optimizer='sgd', loss='mean_squared_error')

## input numpy arrays
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

## learning process 'fit Xys to the Ys 500 times'
model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))


## with output display

import tensorflow as tf
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

l0 = Dense(units=1, input_shape=[1])
model = Sequential(l0)
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

## Outputs weight and bias: Y = WX + B
print(model.predict([10.0]))
print("Here is what I learned: {}".format(l0.get_weights()))
