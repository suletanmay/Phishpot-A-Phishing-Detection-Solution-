import numpy as np
import pandas as pd
import keras
from keras import models
from keras import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import pickle as pkl

data = pd.read_csv('PhisingWebsite_datset.csv')


def prepare_data(data):
    y = data['Result']
    x = data.drop('Result',axis =1) 
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.3, random_state=42)
    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = prepare_data(data=data)


forest = RandomForestClassifier(n_estimators=50)
forest.fit(x_train,y_train)
y_pred = forest.predict(x_test)


rf_acc = accuracy_score(y_true=y_test, y_pred= y_pred)
print("Accuracy of random forest model using test-set is : %f" %(rf_acc*100))


rf_filename = 'rfmodel.pkl'
pkl.dump(forest, open(rf_filename, 'wb')) 







