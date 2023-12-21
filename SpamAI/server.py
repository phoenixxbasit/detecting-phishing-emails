from flask import Flask, jsonify, request
import pickle
from model import make_prediction
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model and vectorizer
clf = pickle.load(open("TrainedModel.pkl", "rb"))
vectorizer = pickle.load(open("Vectorizer.pkl", "rb"))


@app.route("/predict", methods=["GET"])
def predict():
    user_input = request.args.get("q")
    prediction = make_prediction(user_input, clf, vectorizer)
    score = prediction[0][1]

    return jsonify({"prediction": score})

@app.route("/predict", methods=["POST"])
def predictP():
    # Get the input data from the request body
    request_data = request.get_json(force=True)
    user_input = request_data['text']
    
    # Make the prediction and get the score
    prediction = make_prediction(user_input, clf, vectorizer)
    score = prediction[0][1]

    # Return the prediction score as JSON
    return jsonify({"prediction": score})

if __name__ == "__main__":
    app.run(debug=True)
