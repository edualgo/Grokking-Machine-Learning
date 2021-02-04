<h1 align="center">GANS on MNIST Handwritten Digits</h1>

Generative Adversarial Networks (GAN) are deep neural net architectures comprising of a set of two networks which compete against the other, hence the name “adversarial”.
The two networks are called Generator and Discriminator. A generator ("the artist") learns to create images that look real, while a discriminator ("the art critic") learns to tell real images apart from fakes.
<p align="center">
<img src="https://github.com/madhurima99/Grokking-Machine-Learning/blob/main/Notebooks/MNIST%20GAN/Outputs/gan.png" alt="model">
</p>

<h2>Model Architecture</h2>

<b>The notebook <i>DCGAN_MNIST.ipynb</i> implements GAN on mnist handwritten digits dataset. <br>
The dataset has been loaded from <a href="https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data">tf.keras.datasets.mnist.load_data</a> module.</b><br>
<br>The architecture of Generator and Discriminator models are as follows:

<p align="center">
<img src="https://github.com/madhurima99/Grokking-Machine-Learning/blob/main/Notebooks/MNIST%20GAN/Outputs/model.png" alt="model">
</p>

>Further details has been documented inside the notebook itself.


<h2>Model training</h2>

The model has been trained on Google Colab using GPU.<br>
Animated gif using the images saved during training.
<p align="center">
<img src="https://github.com/madhurima99/Grokking-Machine-Learning/blob/main/Notebooks/MNIST%20GAN/Outputs/dcgan_mnist.gif" alt="dcgan-mnist">
</p>

<h2>Examples of generated images</h2>
<p align="center">
<img src="https://github.com/madhurima99/Grokking-Machine-Learning/blob/main/Notebooks/MNIST%20GAN/Outputs/generated.png" alt="dcgan-mnist">
</p>

<h2>Requirements to run the notebook</h1>

>1. TensorFlow 2.0
>2. Keras
>3. Numpy
>4. Matplotlib
>5. Ipython
>6. Glob
>7. Imageio
>8. OS
>9. PIL
>10. Time
