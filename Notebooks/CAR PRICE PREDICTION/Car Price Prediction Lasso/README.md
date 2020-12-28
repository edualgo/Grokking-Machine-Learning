# Car Price Prediction

Prediction the Price of car using Lasso Regression ML Algorithm.


<h3> DATA DESCRIPTION: </h3>
<h4> Before Data Wrangling: </h4>

Number of instances - 205
Number of Attributes -26

<h4> After Data Wrangling: </h4>
Number of instances - 205
Number of Attributes -10
Attribute breakdown - 9 quantitative inputs, 1 quantitative output

<h4> Attribute Information: </h4>

Inputs:
wheelbase,
carlength,
carwidth,
horsepower,
curbweight,
enginesize
citympg,
highwaympg,
torque

Output:
Price(in dollars)

<h3>MODELLING AND EVALUATION: </h3>

ML Algorithm used :
Lasso Regression

Metric - Since the target variable is a continuous variable, regression evaluation metric RMSE (Root Mean Squared Error) and R2 Score (Coefficient of Determination) have been used.

<h3>CONCLUSION: </h3>
We have used Lasso Regression to make Predictions also used GridSearch to find the best parameter for Lasso algorithm.
