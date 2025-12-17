import time

def train_model(model, X_train, y_train):
    start_time = time.time()
    history = model.fit(
        X_train, y_train,
        epochs=30,
        batch_size=32,
        validation_split=0.2,
        verbose=1
    )
    training_time = time.time() - start_time
    return history, training_time