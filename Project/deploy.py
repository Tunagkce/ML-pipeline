
import streamlit as st
import os
import pickle
import sklearn
# Get absolute path to current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'bank_marketing.sav')

# Load the model safely
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

