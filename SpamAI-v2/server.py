from flask import Flask, jsonify, request
import pickle
from model import make_prediction
from keras.models import load_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model and vectorizer
lb = pickle.load(open("labels", "rb"))
model = load_model("model.h5")


@app.route("/predict", methods=["GET"])
def predict():
    user_input = request.args.get("q")
    prediction = make_prediction(user_input, lb, model)
    score = prediction[0][0]

    return jsonify({"prediction": float(score)})

@app.route("/predict", methods=["POST"])
def predictP():
    # Get the input data from the request body
    request_data = request.get_json(force=True)
    user_input = request_data['text']
    
    # Make the prediction and get the score
    prediction = make_prediction(user_input, lb, model)
    score = prediction[0][0]

    # Return the prediction score as JSON
    return jsonify({"prediction": float(score)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
