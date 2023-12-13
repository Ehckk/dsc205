import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

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
    
    ## Reliablity
    
    ### Mean Distance Between Failures
    
	- Metric for the aggregate distance between mechanical faliures of a train car during operation.
	- Each train car used by the MTA:
		- Recorded MDBF 
		- MDBF goal 
	- Using both of these values we can calculate the residual 
	- How well did the fleet meet its reliability goals?
    """
)

mdbf = read_csv("MDBF")
mdbf["Year"] = pd.to_datetime(mdbf["Month"]).dt.year
mdbf["Month"] = pd.to_datetime(mdbf["Month"]).dt.strftime("%m/%Y")
mdbf["MDBF Residual"]=(mdbf["MDBF Value"] - mdbf["MDBF Goal"]) / mdbf["MDBF Goal"]
mdbf = mdbf.sort_values(by=['Year', 'Month'])
mdbf[["Month", "MDBF Value", "MDBF Goal", "MDBF Residual"]].head()

fig, ax = plt.subplots(figsize=(12, 6))
mdbf_data = mdbf[mdbf["Fleet Type"] == "Fleet-wide"]
ax.axhline(0, xmin=0, xmax=1, color="black")
sns.scatterplot(x="Month", y="MDBF Residual", hue="Fleet Type", data=df, ax=ax, zorder=100)
ax.set_xlabel("Date")
fig.autofmt_xdate()
st.pyplot(fig)

# st.header("Mean Distance Between Failures")
st.markdown(
	"""
	
	"""
)
