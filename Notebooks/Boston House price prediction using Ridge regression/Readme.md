### Predicting House prices 
Predicting house prices using Ridge Regression
### Dataset Description
The Dataset used here is Boston Housing Dataset The Boston Housing Dataset is a derived from information collected by the U.S. Census Service concerning housing in the area of Boston MA.In this problem we are trying to predict the price of houses using features like (tax,ptratio etc) using Ridge Regression. Kaggle link for dataset: https://www.kaggle.com/puxama/bostoncsv
### Ridge Regression
Ridge regression is used to solve regression problems just like Linear regression. But if we already had Linear regression then why do we need another regression model? This is because the problem with linear regression is that estimated coefficients of the model can become large, making the model sensitive to inputs and possibly unstable. This is particularly true for problems with few observations (samples) or less samples (n) than input predictors (p) or variables (so-called p >> n problems). Though the model performs best on training data, but fails badly on training data. This is called the problem of overfitting. Now,Ridge regression comes into picture. It adds additional parameter to SSR(sum of squared residuals) which makes the model fit better on test data. For better understanding watch this amazing video by Joshua Stammer: https://www.youtube.com/watch?v=Q81RR3yKn30&t=7s

### Model Evaluation Factors
R -square and regression coefficient for each feature

### Data Visualisation
Using Residuals plot from yellowbrick.regressor library




