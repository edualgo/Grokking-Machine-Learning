# CONCRETE STRENGTH

Predicting the compressive strength of concrete using ML methods and Deep Nueral Networks.

<h3> EXISTING SOCIETAL ISSUE: </h3>

In earlier days, the concrete strength is measure through other traditional methods like using drill holes, weight spring, or using sensors. But that requires a significant destruction of test sample and thereby increasing the cost. The recommended wait time for testing the cylinder is 28 days to ensure correct results. This consumes a lot of time and requires a lot of labour to prepare different prototypes and test them. Also, this method is prone to human error and one small mistake can cause the wait time to drastically increase.

<h3> PROPOSED SOLUTION: </h3>
   
The focus of this project is the application of machine learning process,Artificial nueral networks and their suitability to model concrete compressive strength compared with early models obtained from the literature and compared with some conventional approaches and also a recoomendation system is developed by applying various ML methods,Deep nueral network methods to predict the concrete strength from its components accurately and then looking for the optimal combination of components which increases the strength.

<h3> ARCHITECTURE DIAGRAM: </h3>

![Picture4](https://user-images.githubusercontent.com/53599318/99866749-c486d380-2bd9-11eb-8ee3-abbc60f646cb.jpg)

<h3>  DATA DESCRIPTION: </h3>
   
Data is obtained from UCI Machine Learning Repository and this dataset is used for all ML Algorithms. https://archive.ics.uci.edu/ml/datasets/Concrete+Compressive+Strength

Number of instances - 1030
Number of Attributes - 9
Attribute breakdown - 8 quantitative inputs, 1 quantitative output

<h4> Attribute information: </h4>

Inputs:
Cement,
Blast Furnace Slag,
Fly Ash,
Water,
Superplasticizer,
Coarse Aggregate,
Fine Aggregate,
All above features measured in kg/$m^3$,
Age (in days),

Output:
Concrete Compressive Strength (Mpa)

Dataset used for Deep Nueral Network is https://www.kaggle.com/maajdl/yeh-concret-data

<h3> MODELLING AND EVALUATION: </h3>

ML Algorithms used:
Linear regression,
Lasso regression,
Ridge regression,
Decision Trees,
Random Forests,
Deep Nueral Nework

Metric - Since the target variable is a continuous variable, regression evaluation metric RMSE (Root Mean Squared Error) and R2 Score (Coefficient of Determination) have been used.
And a recommendation system is developed as which algorithm is best choice for predicting accurate concrete strength.

<h3> CONCLUSION: </h3>
Analysed the Compressive Strength and used Machine Learning to Predict the Compressive Strength of Concrete. We have used Linear Regression and its variations, Decision Trees and Random Forests to make predictions and compared their performance. Random Forest Regressor has the lowest RMSE and is a good choice for this problem. Also, we can further improve the performance of the algorithm by tuning the hyperparameters by performing a grid search or random search.

NN approaches combine the complexity of many statistical techniques with machine learning techniques and attributed as a black-box which allows NN to be applied in all engineering disciplines. It comes out as the best possible model for the prediction of compressive strength of concrete. It has predicted with high accuracy for all the curing ages, that is, 28, 56, and 91 days.

<h4> For ML code please refer to my kaggle link:</h4>

https://www.kaggle.com/nityasreepaladugu/predicting-concrete-compressive-strength-with-ml


