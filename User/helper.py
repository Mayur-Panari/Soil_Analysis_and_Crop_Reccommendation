from urllib import request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from django.contrib import messages

import os
from django.conf import settings

class GETDATA:

    def __init__(self):
        data_path = os.path.join(settings.BASE_DIR,'static','C_R.csv')

        self.crop_data= pd.read_csv(data_path)
        

    def get_prediction(self,input_data):
        crop_data=self.crop_data.copy()

        X= crop_data.drop(columns=['label'])
        Y=crop_data['label']


        x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=2)

        from sklearn.preprocessing import MinMaxScaler
        mx = MinMaxScaler()
        x_train = mx.fit_transform(x_train)
        x_test = mx.transform(x_test)


        model = LogisticRegression()

        model.fit(X_train,y_train)


        input_data = mx.transform([input_data])
        prediction = model.predict(input_data)
        return {"prediction": prediction[0]}
