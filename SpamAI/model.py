import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder


def train_model():
    data = pd.read_csv("dataset.csv")
    x, y = data["text"], data["label_num"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    vectorizer = CountVectorizer()
    count = vectorizer.fit_transform(x_train.values)

    clf = LogisticRegression(max_iter=10000)
    targets = y_train.values
    clf.fit(count, targets)

    # Save trained model and vectorizer object
    pickle.dump(clf, open("TrainedModel.pkl", "wb"))
    pickle.dump(vectorizer, open("Vectorizer.pkl", "wb"))


def make_prediction(user_input, clf, vectorizer):
    transformed_input = vectorizer.transform([user_input])
    prediction = clf.predict_proba(transformed_input)
    return prediction

if __name__ == "__main__":
    
    # Load trained model and vectorizer object
    clf = pickle.load(open("TrainedModel.pkl", "rb"))
    vectorizer = pickle.load(open("Vectorizer.pkl", "rb"))
    user_input = "Free money! Click now to claim your prize"

    prediction = make_prediction(user_input, clf, vectorizer)
    print(prediction[0][1])
