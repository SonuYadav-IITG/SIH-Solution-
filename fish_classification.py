
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

def create_fish_classifier(num_species=50):
    base_model = ResNet50(weights='imagenet', include_top=False)
    x = GlobalAveragePooling2D()(base_model.output)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_species, activation='softmax')(x)
    model = tf.keras.Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model

if __name__ == "__main__":
    model = create_fish_classifier()
    print("Fish image classifier model loaded.")
