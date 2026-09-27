import numpy as np
from sklearn.ensemble import RandomForestClassifier

# X = Age, Tenure, Monthly Bill
X = np.array([
    [22, 2, 500],
    [25, 5, 600],
    [30, 1, 800],
    [35, 8, 550],
    [40, 10, 500],
    [28, 3, 900],
    [45, 12, 650],
    [32, 2, 850]
])
# y = Churn
y = np.array([1, 0, 1, 0, 0, 1, 0, 1])


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


prediction = model.predict([[30, 4, 700]])
if prediction[0] == 1:
    print("Churn: Yes")
else:
    print("Churn: No")
