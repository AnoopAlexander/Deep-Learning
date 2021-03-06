# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:06:28 2018

@author: anoop
"""

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Data preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1=LabelEncoder()
X[:,1]=labelencoder_X_1.fit_transform(X[:,1])
labelencoder_X_2=LabelEncoder()
X[:,2]=labelencoder_X_2.fit_transform(X[:,2])
onehotencoder=OneHotEncoder(categorical_features=[1])
X=onehotencoder.fit_transform(X).toarray()
X=X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#importing libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# creating the ANN
classifier=Sequential()

# adding input and hidden layers
classifier.add(Dense(input_dim=11,activation='relu',kernel_initializer="uniform",units=6))
classifier.add(Dense(activation='relu',kernel_initializer="uniform",units=6))

#output layer
classifier.add(Dense(activation='sigmoid',kernel_initializer="uniform",units=1))

#compig the ANN-apply stochastic gradient descent
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Fitting ANN to the training set
classifier.fit(X_train,y_train,batch_size=10,epochs=100)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred=(y_pred>0.5)

#checking confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

# using logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

ypredlr=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cmlr = confusion_matrix(y_test, ypredlr)

#Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_predNB = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cmNB = confusion_matrix(y_test, y_predNB)



