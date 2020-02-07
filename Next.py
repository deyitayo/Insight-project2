import streamlit as st

import numpy as np

import pandas as pd

from sklearn.externals import joblib

from joblib import load


st.title('Get suggested date of next appointment')

st.header('Procedure Information')

Fluoroscopy_Time = st.number_input('Fluoroscopy Time (min)')

Lidocaine = st.number_input('Lidocaine 1% (cc)')

Age = st.number_input('Patient age (years)')


#Thrombolysis = int(st.number_input('Thrombolysis'))

#Prolonged_Bleeding = int(st.number_input('Prolonged_Bleeding'))


Clotted_Access = st.radio(label="Clotted Access", options=(0, 1))

Arterial = st.radio(label="Arterial", options=(0, 1))

def get_pred(data_input):
    data_input = [Fluoroscopy_Time, Lidocaine, Age, Clotted_Access, Arterial]
    features = pd.DataFrame([data_input], columns =['Fluoroscopy_Time', 'Lidocaine', 'Age', 'Clotted_Access', 'Arterial'])
    loaded_model = joblib.load('Rf_model.joblib')
    pred1 = loaded_model.predict(features)
    pred2 = pred1[0]
    prediction = np.exp(pred2)
    return prediction


if st.button(label='Submit'):    
    data_input = [Fluoroscopy_Time, Lidocaine, Age, Clotted_Access, Arterial]
    prediction = get_pred(data_input)
    pred = str(int(prediction)) + ' ' + 'days'
    full_date = pd.datetime.now().date() + pd.DateOffset(days=int(prediction))
    year = full_date.year
    month = full_date.month
    day = full_date.day
    date = str(month) + '-' + str(day) + '-' + str(year)
    st.write(f'Estimated time till next appointment: {pred}')
    st.write(f'Estimated date of next appointment: {date}')

