import pandas
from sklearn.linear_model import LinearRegression

import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#scikit-learn - for our model
#pandas Imports data into python from csv can do more
data = pandas.read_csv('etf5002.csv')
#5 rows of data - data.head()
#print(data.head())
#diagram scatter x to z [x], a y [y]
#plt.scatter(data['version'], data['price'])
#Show me this plt
#plt.show()

model = LinearRegression()
#Do modelu dopasuj dane
model.fit(data[['data']], data[['kurs']])
#Predict future model 14 tylko
print(model.predict([[2504]]))
print(model.predict([[2505]]))
