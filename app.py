import warnings
warnings.filterwarnings("ignore")
import os,sys
import pandas as pd
import pickle
transformer = pickle.load(open("transformer.pkl","rb"))
model = pickle.load(open("model.pkl","rb"))
import streamlit as st
import warnings
import datetime
warnings.filterwarnings('ignore')
# @st.cache_data

if __name__=="__main__":
    
    st.header("Bike Rental System")
    date = st.date_input("Enter a date",min_value=datetime.date(2011,1,1),max_value= datetime.date(2012,12,31),value=datetime.date(2011,1,1))
    if date:
        year,month,day = date.year,date.month,date.day
    
    season = st.selectbox("Season",["spring","summer","fall","winter"])
    sea = 0
    if season == "spring":
        sea+=1
    elif season == "summer":
        sea+=2
    elif season == "summer":
        sea+=3
    else:
        sea+=4
    
    hour = st.number_input("which hour",min_value=0,max_value=23,step=1)
    holiday = st.radio("holiday",{"Yes":1,"No":0})
    holi = 0
    if holiday =="yes":
        holi+=1
    else:
        holi = 0
    working  = st.number_input("weekday",min_value=0,max_value=1)
    weekday = st.slider("weekday",min_value=0,max_value=6,step=1)
    weathsit = st.selectbox("weather",[''' Clear/Few clouds/Partly cloudy/Partly cloudy''','''Mist + Cloudy/Mist + Broken clouds/Mist + Few clouds/Mist''','''Light Snow, Light Rain/Thunderstorm''',''' Heavy Rain /Ice Pallets '''])
    weather = 0
    if weathsit =='''Clear/Few clouds/Partly cloudy/Partly cloudy''':
        weather+=1
    elif weathsit =='''Mist + Cloudy/Mist + Broken clouds/Mist + Few clouds/Mist''':
        weather+=2
    elif weathsit =='''Light Snow, Light Rain/Thunderstorm''':
        weather+=3
    else:
        weather+=4
    temp = st.slider("normalized temprature",min_value=0.0,max_value=1.0,step =0.1)
    atemp = st.slider("atemp",min_value=0.0,max_value=1.0,step =0.1)
    humid = st.slider("humidity",min_value=0.0,max_value=1.0,step =0.1)
    windspeed =st.slider("windspeed",min_value=0.0,max_value=1.0,step =0.1)
    causal = st.number_input("number of non-registered user rentals initiated",min_value=0,max_value=500,step=1)
    regis = st.number_input("number of registered user rentals initiated",min_value=0,max_value=500,step=1)

    ye = 0
    if str(year)=="2011":
        ye+=0
    else:
        ye = 1
    
    k = [day,sea,ye,month,hour,holi,weekday,working,weather,temp,atemp,humid,windspeed,causal,regis]
    # Day,season,yr,mnth,hr,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed,casual,registered
    
    data = transformer.transform([k])
    outcome = model.predict(data)
    vechicle =round(outcome[0],0)
    final= st.button("predict")
    if final:
        st.write('**the avilable bike is**')
        st.write(vechicle)
    
    
# print(instance_prediction(input_list=input1
