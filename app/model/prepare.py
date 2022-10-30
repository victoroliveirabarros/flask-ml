import pickle
import pandas as pd
from sklearn import linear_model

# Read the data
data = pd.read_csv('prices.csv')

y = data['Value']
x = data[['Rooms', 'Distance']]

# Build a linear model
lm = linear_model.LinearRegression()
lm.fit(x,y)

# Predict
lm.predict([[15, 61]])

pickle.dump(lm, open('model.pkl','wb'))



