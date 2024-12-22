from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Initialize the Flask app
app = Flask(__name__)

# Load the saved model and scaler (ensure your model is saved and scaler is fitted)
model = pickle.load(open('saved_trained_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check')
def checkFunc():
    return render_template('check.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data from the user input
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])

    # Create an input array from the user input
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    # Get prediction from the model
    prediction = model.predict(input_data)

    # Return the prediction result
    if prediction[0] == 1:
        result = 'Heart Disease Detected'
    else:
        result = 'No Heart Disease'

    return render_template('check.html', prediction_text=result)


@app.route('/help')
def about():
    return render_template('help.html')


if __name__ == "__main__":
    app.run(debug=True)
