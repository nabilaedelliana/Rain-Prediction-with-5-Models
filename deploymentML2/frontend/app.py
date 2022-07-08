import streamlit as st
import requests


st.title("Rain Tomorrow Predictor Online Apps")
MinTemp = st.number_input("Temperature")
Humidity3pm = st.number_input("Humidity")
Cloud9am = st.number_input("Cloud_Cover")
Rainfall = st.number_input("Rainfall")
WindGustSpeed = st.number_input("Wind_Speed")
raintoday = st.selectbox("is_today_rain", [0, 1])
month = st.selectbox("Month", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# inference
data = {'Temperature':MinTemp,
        'Humidity':Humidity3pm,
        'Cloud_Cover': Cloud9am,
        'Rainfall':Rainfall,
        'Wind_Speed':WindGustSpeed,
        'is_today_rain':raintoday,
        'Month':month}

URL = " http://127.0.0.1:5000/predict"

# komunikasi
prediction = st.button('Predict')
if prediction :
    r = requests.post(URL, json=data)
    res = r.json()

    if res['code'] == 200:
        rezz = (res['result']['description'])
        if rezz == 'Not Rain':
            st.markdown(''' <h2> Not Rain </h2>''', unsafe_allow_html=True)

        else:
            st.markdown(''' <h2> Rain </h2>''', unsafe_allow_html=True)

    else:
        st.write("There is an Error")
        st.write(f"Details : {res['result']['error_msg']}")