import streamlit as st
import os
import pickle
import pandas as pd

# Get absolute path to current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'prediction_deploy.sav')

# Load the model safely
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def make_prediction(features):
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    confidence = proba[prediction] * 100  # Get probability of the predicted class
    return prediction, confidence

def main():
    # UI banner
    html_temp = """ 
    <div style ="background-color:lightblue;padding:13px;border-radius:10px"> 
    <h1 style ="color:black;text-align:center;">Bank Marketing Prediction App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.subheader("Please fill in the customer information:")
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
    job = st.selectbox('Job', (
        'entrepreneur', 'housemaid', 'management',
        'retired', 'self-employed', 'services', 'blue-collar', 'student', 'technician', 'admin.', 'unemployed'))
    marital = st.selectbox('Marital Status', ('married', 'single', 'divorced'))
    education = st.selectbox('Education', (
        'basic.6y', 'basic.9y', 'high.school',
        'illiterate', 'professional.course', 'university.degree', 'basic.4y'))
    default = st.selectbox('Has Credit in Default?', ('no', 'yes'))
    housing = st.selectbox('Has Housing Loan?', ('no', 'yes'))
    loan = st.selectbox('Has Personal Loan?', ('no', 'yes'))
    contact = st.selectbox('Contact Communication Type', ('cellular', 'telephone'))
    month = st.selectbox('Last Contact Month', ('apr', 'aug', 'dec', 'jul', 'jun', 'mar', 'may', 'nov', 'oct', 'sep'))
    day_of_week = st.selectbox('Last Contact Day', ('mon', 'tue', 'wed', 'thu', 'fri'))
    duration = st.number_input("Last Contact Duration (seconds)", step=1)
    campaign = st.number_input("Number of Contacts Per Campaign", step=1)
    pdays = st.number_input("Days Passed Since Last Contact (-1 if never)", step=1)
    previous = st.number_input("Number of Contacts Before Campaign", step=1)
    poutcome = st.selectbox('Outcome of Previous Campaign', ('failure', 'nonexistent', 'success'))
    emp_var_rate = st.number_input("Employment Variation Rate")
    cons_price_idx = st.number_input("Consumer Price Index")
    cons_conf_idx = st.number_input("Consumer Confidence Index")
    euribor3m = st.number_input("Euribor 3 Month Rate")
    nr_employed = st.number_input("Number of Employees")
    
    was_contacted_before = 1 if (pdays != -1 and pdays != 999) else 0

    if st.button("Predict"):
        features = pd.DataFrame({
            'age': [age],
            'job': [job],
            'marital': [marital],
            'education': [education],
            'default': [default],
            'housing': [housing],
            'loan': [loan],
            'contact': [contact],
            'month': [month],
            'day_of_week': [day_of_week],
            'duration': [duration],
            'campaign': [campaign],
            'pdays': [pdays],
            'previous': [previous],
            'poutcome': [poutcome],
            'emp.var.rate': [emp_var_rate],
            'cons.price.idx': [cons_price_idx],
            'cons.conf.idx': [cons_conf_idx],
            'euribor3m': [euribor3m],
            'nr.employed': [nr_employed],
            'was_contacted_before': [was_contacted_before]
        })

        result, confidence = make_prediction(features)

        if result == 1:
            st.success(f"Prediction: YES – Customer likely to subscribe.")
        else:
            st.error(f"Prediction: NO – Customer unlikely to subscribe.")

        st.info(f"Model Confidence: {confidence:.2f}%")

     
        st.progress(min(confidence / 100, 1.0))

if __name__ == '__main__':
    main()
