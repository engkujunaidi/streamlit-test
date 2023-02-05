import streamlit as st
import datetime

today = datetime.date.today()

year = today.year

gender = st.radio("Pick your gender",['Male','Female'])

st.write("Your gender is " + gender)

born_year = st.number_input("Your born year: ",min_value=None, max_value=None, value=1990)
age = year - born_year
st.write("Your age is ",age)
