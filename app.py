from flask import Flask, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump, load

import json

app = Flask(__name__)

@app.route(/predict, method=['POST'])
def predict():
    values = json.loads(request.form["values"])
    model = load("model.joblib")
    prediction = model.predict(values)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

