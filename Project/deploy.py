import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Deposit Prediction App", layout="wide", page_icon="🏦")
model=pickle.load(open('Project/bank_marketing.sav','rb'))
# this is the main function in which we define our webpage  
def main():
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Bank Marketing Prediction App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
