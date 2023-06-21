import streamlit as st
import pandas as pd
import numpy as np
import pickle

file1 = open('pipe.pkl', 'rb')
rf = pickle.load(file1)
file1.close()

data = pd.read_csv("Banglore_house_price_predicted.csv")

#data['location'].unique()
st.title("House Price Prediction")

location = st.selectbox('Loction', data['location'].unique())
bhk = st.selectbox('How much BHK you are looking for', data['size'].unique())
sqft = st.number_input('Total square ft.')

if st.button('Predict Price'):

    query = np.array([location, bhk, sqft])
    query = query.reshape(1, 3)

    prediction = int((rf.predict(query)[0]))

    st.title(f"Predicted price for {location} location house is {str(prediction)}Lacs ₹")