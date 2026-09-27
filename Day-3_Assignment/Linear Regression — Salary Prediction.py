import numpy as np
from sklearn.linear_model import LinearRegression

# X = Years of Experience
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
# y = Salary
y = np.array([20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000])


model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[5]])
print("Predicted Salary:", prediction[0])

