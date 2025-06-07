import streamlit as st

st.title("My First Streamlit App 🎉")
st.write("Hello, this is my first web app using Streamlit!")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")
