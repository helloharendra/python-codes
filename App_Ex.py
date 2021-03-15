from os import name
import streamlit as st
st.header('welcome to streamlit')
st.subheader('by harendra')

st.sidebar.title('Cool \n Hey.. you are using streamlit')

st.text('simple text')
st.sidebar.success('Success')
st.sidebar.error('error')
st.sidebar.warning('warning')

btn=st.button('dont click')

if btn:
     st.error('what have you done')
     st.write('Its not available more')
countries=['india','pakistan','Amerika']
c=st.selectbox('select the cpuntry',countries)
st.write(f'you have selected : {c}')

name=st.text_input("what is your name",value='harendra')
st.write(f'so you are {name}')

age=st.sidebar.slider('what is you age ', min_value=10, max_value=100, step=2,value=20)
if age <15:
    st.write('you are too young for this')
elif age >50:
    st.write('you are too old for this')

else:
    st.write("you are fit for this")
