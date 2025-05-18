
import streamlit as st
import os
import pickle

# Get absolute path to current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'bank_marketing.sav')

# Load the model safely
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def make_prediction(features):
    prediction_value = model.predict(features)[0]
    return prediction_value


# main streamlit app
def main():
    # UI banner
    html_temp = """ 
    <div style ="background-color:lightblue;padding:13px;border-radius:10px"> 
    <h1 style ="color:black;text-align:center;">Bank Marketing Prediction App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields
    st.subheader("Please fill in the customer information:")
   
if __name__ == '__main__':
    main()
