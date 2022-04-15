import streamlit as st
from multiapp import MultiApp
from apps import Food ,Data

app = MultiApp()

st.markdown("""
# Arar Studio AI Apps 
This multi-page apps Food Recommendation app and Data profiling App.
""")

# Add all your application here
app.add_app("Food", Food.app)
app.add_app("Data Profiling", Data.app)
# The main app
app.run()