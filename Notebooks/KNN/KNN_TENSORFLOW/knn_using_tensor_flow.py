#IMPORT THE LIBRARIES
import tensorflow as tf


#READING THE FILE
file = 'iris.txt'
with open(file) as f:
    iris = f.readlines()

#GROUP BY CLASS
setosa = iris[:50]
versicolor = iris[50:100]
virginica = iris[100:]

#ORGANISING THE DATA IN ORDER TO BALANCE
samples = []
for i in range(0, 50):
    samples.append(setosa[i])
    samples.append(versicolor[i])
    samples.append(virginica[i])

#CREATE FEATURES AND LABELS 
features = []
labels = []
for sample in samples:
    aux = sample.split(",")
    sepal_length = float(aux[0])
    sepal_width = float(aux[1])
    petal_length = float(aux[2])
    petal_width = float(aux[3])
    label = aux[4].strip()
    features.append([sepal_length, sepal_width, petal_length, petal_width])
    labels.append(label)


percentual_samples_test = 0.7
features_train = features[: int(percentual_samples_test * len(features))]
labels_train = labels[: int(percentual_samples_test * len(features))]
features_test = features[int(percentual_samples_test * len(features)):]
labels_test = labels[int(percentual_samples_test * len(features)):]

features_train_placeholder = tf.placeholder("float", [None, 4])
features_test_placeholder = tf.placeholder("float", [4])

# NEAREST NEIGHBOUR USING L1 REGULARISATION
distance = tf.reduce_sum(tf.abs(tf.add(features_train_placeholder, tf.neg(features_test_placeholder))), reduction_indices=1)

accuracy = 0.


pred = tf.arg_min(distance, 0)

# INITIALISE VARIABLES
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    #LOOP OVER THE GIVEN TEST DATA
    for i in range(len(features_test)):
       
        nn_index = sess.run(pred, feed_dict={features_train_placeholder: features_train, features_test_placeholder: features_test[i]})
       
        print("Sample", i, " - Prediction:", labels_train[nn_index], " / True Class:", labels_test[i])
        #FINALLY CALCULATE THE ACCURACY
        if labels_train[nn_index] == labels_test[i]:
            accuracy += 1. / len(features_test)
print("Accuracy:", accuracy)
