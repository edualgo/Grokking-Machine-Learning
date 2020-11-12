import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
import seaborn as sns
import pickle

data = pd.read_csv("car_price_assignment.csv")
car_company = data['CarName'].apply(lambda x : x.split(' ')[0])
data.insert(3,"car_company",car_company)

def correct_name(a,b):
    data['car_company'].replace(a,b,inplace=True)

correct_name('maxda','mazda')
correct_name('Nissan','nissan')
correct_name('porsche','porcshce')
correct_name('toyouta','toyota')
correct_name('vokswagen','volkswagen')
correct_name('vw','volkswagen')

reg_features = ['wheelbase','carlength', 'carwidth','curbweight','enginesize','horsepower','citympg','highwaympg']
reg_target = ['price']

X = data[reg_features]
y = data[reg_target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm = LinearRegression()
lm.fit(X_train,y_train)
pickle.dump(lm,open('linear_model.pkl','wb'))

# poly = PolynomialFeatures(degree = 2)
# X_poly = poly.fit_transform(X_train)
# X_poly_test = poly.fit_transform(X_test)
#
# poly.fit(X_poly, y_train)
# lin2 = LinearRegression()
# lin2.fit(X_poly, y_train)
#
# y_train_predicted = lin2.predict(X_poly)
# y_test_predict = lin2.predict(poly.fit_transform(X_test))
#
regressor = DecisionTreeRegressor(random_state = 2)
regressor.fit(X_train, y_train)
pickle.dump(lm,open('decision_tree_model.pkl','wb'))
