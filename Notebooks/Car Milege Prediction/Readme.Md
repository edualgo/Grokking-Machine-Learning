# CAR MILEGE PREDICTION
<h3>Summary</h3>
A Linear Regression model to predict car fuel economy (in mpg) given various specifications: {cylinders, displacement, horsepower, weight, acceleration, year, origin}. Currently, Root Mean Square error is around 3.7 mpg.


Dataset Descriptions

https://docs.google.com/spreadsheets/d/1viqrctQHNdJQigAwRfJxnN9h7jv0D48xKzITjA7138U/edit#gid=85281029

Variables that are available  in  the dataset are 
1. mpg:           continuous
2. cylinders:     multi-valued discrete
3. displacement:  continuous
4. horsepower:    continuous
5. weight:        continuous
6. acceleration:  continuous
7. model year:    multi-valued discrete
8. origin:        multi-valued discrete
9. car name:      string (unique for each instance)

Problem Statement

In this model you will investigate the impact of a number of automobile
engine factors on the vehicle's mpg. The dataset auto-mpg.data contains infor-
mation for 398 different automobile models. Information regarding the number
of cylinders, displacement, horsepower, weight, acceleration, model year, origin,
and car name as well as mpg are contained in the file.

Data Cleaning
1. Replace the null value of horsepower to mean value of horsepower.
2. We have to create dummy variable for variable car name.if we do it through pandas
   we create 9 column to 312 column. We are  only performing hot encoding for top 10 frequent 
   label.
 
MODELLING AND EVALUATION 

ML Algorithm Used :- Multiple linear regression is  the relationship between two or more features and response by fitting a linear equation to observed data.

Metrics :- Since the target (mpg) variable is a continuous variable, regression evaluation metric RMSE (Root Mean Squared Error) used.
           We tried  to reduce the rmse by selecting good features, so we can get better accuracy.

CONCLUSION:- We get 82% accracy on car milege prediction through muntiple Linear Regression.