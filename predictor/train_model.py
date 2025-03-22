import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Generate training data (simple increasing sequences)
X = np.array([[i, i + 1, i + 2] for i in range(1, 100)])  # Input: [1,2,3], [2,3,4], ...
y = np.array([i + 3 for i in range(1, 100)])  # Output: [4,5,6, ...]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, "predictor/number_model.pkl")
print("Model saved successfully!")
