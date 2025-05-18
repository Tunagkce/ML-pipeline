import streamlit as st
import pickle
import pandas as pd

model= pickle.load(open('ADA442 Proje/bank_marketing.sav ', 'rb'))