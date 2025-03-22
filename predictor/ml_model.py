import joblib
import numpy as np

# Load the trained model
model = joblib.load("predictor/number_model.pkl")


def predict_next_number(sequence):
    if len(sequence) < 3:
        raise ValueError("Sequence must have at least 3 numbers.")

    # Convert input to NumPy array
    X_input = np.array(sequence[-3:]).reshape(1, -1)

    # Predict next number
    return round(model.predict(X_input)[0], 2)
