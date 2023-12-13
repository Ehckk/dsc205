import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(name):
	url = f"./datasets"
	filename = f"{url}/{name}.csv"
	return pd.read_csv(filename)
st.title('Public Transit through Data')

st.markdown(
    """
    # Questions
    
    1. How reliable are the trains?
     
    2. What causes major delays?
    
    3. Where is funding being allocated?
    
    # Reliablity
    
    ## Mean Distance Between Failures
    
    - Mean Distance Between Failures
    	- Metric for the aggregate distance between mechanical faliures of a train car during operation.
    	- Each train car used by the MTA:
     		- Recorded MDBF 
       		- MDBF goal 
        - Using both of these values we can calculate the residual 
        - How well did the fleet meet its reliability goals?
    """
)
# st.header("Mean Distance Between Failures")
st.markdown(
	"""
	
	"""
)
