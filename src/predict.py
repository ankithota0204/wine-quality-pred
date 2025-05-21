import joblib
import numpy as np

# Load model
model = joblib.load("model/wine_quality_model.pkl")

def predict_quality(input_data):
    """
    Predict wine quality from user input.
    input_data should be a list or array of 11 features.
    """
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]
