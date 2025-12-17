from tensorflow import keras

def build_mlp(input_shape):
    model = keras.Sequential([
        keras.layers.Dense(128, activation="relu", input_shape=input_shape),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(64, activation="relu"),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model