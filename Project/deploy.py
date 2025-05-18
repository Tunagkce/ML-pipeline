import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Deposit Prediction App", layout="wide", page_icon="🏦")
with open('bank_marketing.sav', 'rb') as f:
    model = pickle.load(f)

