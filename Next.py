import streamlit as st

import numpy as np

import pandas as pd

from sklearn.externals import joblib

from joblib import load


st.title('Get suggested date of next appointment')

st.header('Procedure Information')

Fluoroscopy_Time = st.number_input('Fluoroscopy Time (min)')

Total_Contrast = st.number_input('Total Contrast Used (cc)')

Lidocaine = st.number_input('Lidocaine 1% (cc)')

#Thrombolysis = int(st.number_input('Thrombolysis'))

#Prolonged_Bleeding = int(st.number_input('Prolonged_Bleeding'))


Thrombolysis = st.radio(label="Thrombolysis", options=(0, 1))

Prolonged_Bleeding = st.radio(label="Prolonged Bleeding", options=(0, 1))



