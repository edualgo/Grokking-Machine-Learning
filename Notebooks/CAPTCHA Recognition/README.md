# Captcha Recognition

Dataset Used : https://www.kaggle.com/fournierp/captcha-version-2-images

We have used the following custom Convolution Structure :

```python

captcha = Input(shape=(50,200,channels))
x = Conv2D(32, (5,5),padding='valid',activation='relu')(captcha)
x = MaxPooling2D((2,2),padding='same')(x)
x = Conv2D(64, (3,3),padding='same',activation='relu')(x)
x = MaxPooling2D((2,2),padding='same')(x)
x = Conv2D(128, (3,3),padding='same',activation='relu')(x)
maxpool = MaxPooling2D((2,2),padding='same')(x)
outputs = []
for i in range(5):
    x = Conv2D(256, (3,3),padding='same',activation='relu')(maxpool)
    x = MaxPooling2D((2,2),padding='same')(x)
    x = Flatten()(x)
    x = Dropout(0.5)(x)
    x = BatchNormalization()(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = BatchNormalization()(x)
    x = Dense(len_symbols , activation='softmax' , name=f'char_{i+1}')(x)
    outputs.append(x)

```

Overall Accuracy : 0.98
