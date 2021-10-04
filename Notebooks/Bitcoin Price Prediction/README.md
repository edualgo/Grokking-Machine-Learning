# Predict bitcoin price

* The data collected from the CSV files for select bitcoin exchanges for the time period of Jan 2012 to December March 2021, with minute to minute updates of OHLC (Open, High, Low, Close), Volume in BTC and indicated currency, and weighted bitcoin price. Timestamps are in Unix time. Timestamps without any trades or activity have their data fields filled with NaNs. If a timestamp is missing, or if there are jumps, this may be because the exchange (or its API) was down, the exchange (or its API) did not exist, or some other unforeseen technical error in data reporting or gathering. All effort has been made to deduplicate entries and verify the contents are correct and complete to the best of my ability, but obviously trust at your own risk.  


* We created and trained a RNN model with one LSTM layer and one Dense Layer


* We find the root mean square error of our predicted values and consider this as the prediction metric


* We did the train test split using the train_test_split method which takes the input, output values as well as test_size


* The data is first imported from the dataset. We removed all the columns with missing values or the wrong timestamp. In addition to that, we also removed all the values before 2017 because the plot before 2017 is significantly different from the plot after 2017.


# Download the dataset 
[Link to the dataset](http://google.com)
