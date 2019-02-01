import pandas as pd
import numpy as numpy

import keras
from keras.models import Sequential, save_model, load_model
from keras.layers import Dense

from sklearn.model_selection import  cross_val_score, cross_val_predict
from sklearn.metrics import r2_score

X_train = pd.read_hdf('ML_data/champ_X_train.h5', 'X_train')
X_test = pd.read_hdf('ML_data/champ_X_test.h5', 'X_test')

y_train = pd.read_hdf('ML_data/champ_y_train.h5', 'y_train')
y_test = pd.read_hdf('ML_data/champ_y_test.h5', 'y_test')


classifier = Sequential()

classifier.add(Dense(
    units=6,
    kernel_initializer='uniform',
    activation='relu',
    input_dim=18
    ))

# classifier.add(Dense(
#     units=9,
#     kernel_initializer='uniform',
#     activation='relu'
#     ))

classifier.add(Dense(
    units=6,
    kernel_initializer='uniform',
    activation='relu'
    ))

classifier.add(Dense(
    units=1,
    kernel_initializer='uniform',
    activation='sigmoid'
    ))

classifier.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
    )


classifier.fit(X_train, y_train, batch_size=10, epochs=10)

# y_pred = classifier.predict(X_test)
# y_pred = (y_pred > 0.5)
# print(y_pred)

# Making the Confusion Matrix
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, y_pred)

ann_predictions = classifier.predict(X_test)
ann_accuracy = r2_score(y_test, ann_predictions)
print(ann_accuracy)

classifier.save('RL_neural.h5')

del classifier

new_cla = load_model('RL_neural.h5')

ann_predictions = new_cla.predict(X_test)
ann_accuracy = r2_score(y_test, ann_predictions)
print(ann_accuracy)