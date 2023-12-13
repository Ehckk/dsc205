import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(name):
	url = f"./datasets"
	filename = f"{url}/{name}.csv"
	return pd.read_csv(filename)
st.title('# Public Transit through Data')

st.markdown(
    """
    # Public Transit through Data
    
    ## Questions
    
    1. How reliable are the trains?
     
    2. What causes major delays?
    
    3. Where is funding being allocated?
    
    """
)
st.header('')
