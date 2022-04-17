import streamlit as st
from multiapp import MultiApp
from apps import Food ,Data,Pima_app

app = MultiApp()

st.markdown("""
# Arar Studio AI Apps 
This multi-page apps Food Recommendation app and Data profiling App.
""")

# Add all your application here
app.add_app("Food", Food.app)
app.add_app("Data Profiling", Data.app)
app.add_app("Diabetes Prediction", Pima_app.app)
# The main app
app.run()