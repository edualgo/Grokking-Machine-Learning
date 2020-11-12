import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('linear_model.pkl','rb'))
model2 = pickle.load(open('decision_tree_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    prediction2 = model2.predict(final_features)

    output = np.round(prediction[0],2)
    output2 = np.round(prediction2[0],2)

    return render_template('index.html',prediction_text = "The Car Price for Linear Regression Model = $ {} & Decision Tree Regression Model = $ {}".format(output,output2))

if __name__ == "__main__":
    app.run(debug=True)
