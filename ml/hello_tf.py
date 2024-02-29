import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

l0 = Dense(units=1, input_shape=[1])
model = Sequential([l0])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-3.0, 0.2, 1.0, 1.0, 2.0, 4.0], dtype=float)
ys = np.array([-2.0, -0.5, 1.0, 3.0, 4.0, 6.0], dtype=float)

plt.plot(xs, ys, 'ro')

model.fit(xs, ys, epochs=500)


new_value = [10.0, 20.0, 30.0]
predicted_ys = model.predict(new_value)
print("predicted values ", predicted_ys)
plt.plot(new_value, [y[0] for y in predicted_ys], 'bo')
plt.show()
print("Here is what I learned: {}".format(l0.get_weights()))