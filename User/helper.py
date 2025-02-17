from django.http import JsonResponse
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
        

    def get_prediction(self, input_data):
        crop_data = self.crop_data.copy()

        X = crop_data.drop(columns=['label'])
        Y = crop_data['label']

        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

        from sklearn.preprocessing import MinMaxScaler
        mx = MinMaxScaler()
        x_train = mx.fit_transform(x_train)
        x_test = mx.transform(x_test)

        model = LogisticRegression()
        model.fit(x_train, y_train)

        # Convert input_data dictionary to properly ordered numpy array
        feature_order = ['nitrogen', 'phosphorus','potassium', 'temperature','humidity', 'ph', 'rainfall']
        try:
            input_array = np.array([[input_data[feature] for feature in feature_order]], dtype=float)
        except KeyError as e:
            return {"error": f"Missing required field: {str(e)}"}


        # Scale and predict
        input_scaled = mx.transform(input_array)
        prediction = model.predict(input_scaled)
        return {"prediction": prediction[0]}
