from utils.data_utils import clean_address
from utils.geotag_util import call_geocode_api
import streamlit as st
import pandas as pd

DATA_FILE_NAME = "data/MHMP_dopravni_prestupky_2023.csv"

df = pd.read_csv(DATA_FILE_NAME, nrows= 100)
print(df.columns)
df = df.dropna(subset=['MISTOSK'])
df["MISTOSK"] = df["MISTOSK"].apply(clean_address)
st.dataframe(df)
