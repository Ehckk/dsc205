import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(name):
	url = f"./datasets"
	filename = f"{url}/{name}.csv"
	return pd.read_csv(filename)