import pandas as pd
import streamlit as st

names = 'dataset.csv'
names_data = pd.read_csv(names)

st.title('Streamlit and pandas')
st.dataframe(names_data)
