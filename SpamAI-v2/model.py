import pickle
import numpy as np
from keras.models import load_model


def make_prediction(user_input, lb, model, max_len=4000, num_classes=98):
    user_input = lb.transform(list(user_input))
    if len(user_input) < max_len:
        padding_vec = np.full((max_len - len(user_input), num_classes), -1)
        user_input = np.concatenate((user_input, padding_vec))
    user_input = user_input[:max_len]
    predictions = model.predict(user_input.reshape((1, 4000, 98)))
    return predictions


if __name__ == "__main__":
    with open("labels", "rb") as f:
        lb = pickle.load(f)
    model = load_model("model.h5")
    print(make_prediction("Hello", lb, model))