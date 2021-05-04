from os import name
import streamlit as st
from config import *
st.sidebar.write(PROJECT_NAME)
st.sidebar.write(AUTHOR)
st.write(""" 
# hello this is my first app
Hello *world!*""")

#set slider
age=st.slider("pick your age",0,100) #you can change numbers acording to requirement
if age<20:
    st.error("you are not able for this")
elif age>70:
    st.error("you are to old for this")
else:
    st.write("you are fit for this")
#pic date

date=st.date_input("pick a date")

#pick time

time=st.time_input("pick time input")
btn=st.button("dont click")
if btn:
    st.error("please fill properly")
    st.write("this is not available")
countries=["india","amerika","japan","russia"]
c=st.selectbox('plese select the country',countries)
st.write(f'so you are selected :{c}')
#st.sidebar.set(number)
btn1=st.button("submit")
if btn1:
    st.write(" succesfully submitted")