
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset
data = pd.DataFrame({
    'Weather': ['Sunny', 'Sunny', 'Rainy', 'Rainy', 'Cloudy',
                'Cloudy', 'Sunny', 'Rainy'],
    'Temperature': ['Hot', 'Cool', 'Cool', 'Hot', 'Hot',
                    'Cool', 'Hot', 'Cool'],
    'Play': [0, 1, 1, 0, 1, 1, 0, 1]
})

weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()

data['Weather'] = weather_encoder.fit_transform(data['Weather'])
data['Temperature'] = temperature_encoder.fit_transform(data['Temperature'])

X = data[['Weather', 'Temperature']]
y = data['Play']

model = DecisionTreeClassifier()
model.fit(X, y)

new_data = [[
    weather_encoder.transform(['Sunny'])[0],
    temperature_encoder.transform(['Cool'])[0]
]]

prediction = model.predict(new_data)
print("Play Game:", prediction[0])