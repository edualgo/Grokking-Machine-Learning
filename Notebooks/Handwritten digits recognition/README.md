# Handwritten Digits Recognition

This Project is based on ***Convolutional Neural Networks***. Python Programming language has been used to train and test the model. It recognizes handwritten digits with an accuracy of **97.68%**. I have used Google Colab to train and test the model as we can train the model using GPU in Colab and that is very fast as compared to CPU. The more number of epochs takes more time in training the model. A **convolution** multiplies a matrix of pixels with a filter matrix or ***‘kernel’*** and sums up the multiplication values. Then the convolution slides over to the next pixel and repeats the same process until all the image pixels have been covered.

## Dataset
I have used **MNIST Dataset** for training the model. This dataset consists of **70,000 images of handwritten digits from 0–9**. We will identify them using a CNN model on google colab.It consists of **mnist_train_small.csv" and mnist_test.csv"**. In Google colab, MNIST dataset is pre uploaded there, we can import it from `keras.dataset`.

## Required Python Libraries (Installation using pip command)
- numpy : `pip install numpy`
- keras : `pip install keras`
- matplotlib : `pip install matplotlib`

## About the Model

<img src ="https://user-images.githubusercontent.com/62782231/103486357-3e3dee00-4e23-11eb-8fb7-c8f74df2b622.png">

- **Sequential** : Sequential is the easiest way to build a model in Keras. It allows us to build a model layer by layer. Each layer has weights that correspond to the layer the follows it. We use the `.add()` function to add layers to our model. We will add two layers and an output layer.
- **Conv2D layers** : These are convolution layers that will deal with our input images, which are seen as 2-dimensional matrices.
- **kernel size** : It is the size of the filter matrix for our convolution.
- **Activation** : It is the activation function for the layer. The activation function we will be using for our first 2 layers is the ***ReLU, or Rectified Linear Activation***.
- **Flatten layer** : It is used to flatten the input. It is a connection between Convolutional and dense layers.
- **Dense layer** : It is the layer type we will use in for our output layer. Dense is a standard layer type that is used in many cases for neural networks.
- **Softmax** : It makes the output sum up to 1 so the output can be interpreted as probabilities. The model will then make its prediction based on which option has the highest probability.

## Conclusion
This model has gained accuracy of **97.68 %**. It recognizes digits with high efficiency. I have trained the model by taking number of epochs as three. I haven't faced any problem of overfitting, underfitting etc while training the model.
