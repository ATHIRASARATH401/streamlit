import streamlit as st
st.title("ICT")
num1 = st.slider("number 1", 0, 130, 25)
num2 = st.slider("number2",0,70)
sum=num1+num2
st.write("sum of two number", sum )