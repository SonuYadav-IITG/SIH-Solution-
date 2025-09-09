
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def create_lstm(input_shape=(10, 1)):
    model = Sequential()
    model.add(LSTM(16, input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

if __name__ == "__main__":
    model = create_lstm()
    data = np.random.rand(5, 10, 1)
    preds = model.predict(data)
    print("Predictions shape:", preds.shape)
