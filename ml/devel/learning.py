from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Conv3D,Conv2D, MaxPooling2D
from keras.models import load_model
import numpy as np
from keras import backend
print(backend.backend())
num_classes = 5
X_train, X_test, Y_train, Y_test = np.load('./sound_data.npy',allow_pickle=True)
print("len:",len(X_train.shape))
print(X_train.ndim)
img_rows=X_train[0].shape[0]
img_cols=X_train[0].shape[1]
train_shape = X_train.shape
X_train=X_train.reshape((img_rows*img_cols,X_train.shape[0]))

X_test=X_test.reshape((img_rows*img_cols*X_test.shape[0]))
print (X_train.ndim)
print(X_train.shape)
# Construct model
model = Sequential()
model.add(Dense(,activation='relu',input_dim=X_train.ndim))
model.compile(optimizer='adam',loss='categorical_crossentropy')
model.save('Gersang.h5')
model.fit(X_train,Y_train)