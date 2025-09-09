
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Input
from tensorflow.keras.models import Model

def build_cnn(input_shape=(64, 64, 3), num_classes=5):
    inputs = Input(shape=input_shape)
    x = Conv2D(16, (3,3), activation='relu')(inputs)
    x = Flatten()(x)
    outputs = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs, outputs)
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model

if __name__ == "__main__":
    model = build_cnn()
    print("Crop stress/disease CNN built.")
