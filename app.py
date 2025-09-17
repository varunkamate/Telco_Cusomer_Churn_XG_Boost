import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: 'model.pkl' not found. Please ensure the model file is in the same directory.")

# App title
st.set_page_config(page_title="Telco Customer Churn Predictor", page_icon="📞", layout="centered")
st.title("📞 Telco Customer Churn Prediction App")
st.markdown("This app predicts whether a customer will churn based on their service usage and demographic data.")

# Sidebar for user input
st.sidebar.header("Enter Customer Information")

def user_input_features():
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    SeniorCitizen = st.sidebar.selectbox('Senior Citizen', ('Yes', 'No'))
    Partner = st.sidebar.selectbox('Partner', ('Yes', 'No'))
    Dependents = st.sidebar.selectbox('Dependents', ('Yes', 'No'))
    tenure = st.sidebar.slider('Tenure (months)', 0, 72, 1)
    PhoneService = st.sidebar.selectbox('Phone Service', ('Yes', 'No'))
    MultipleLines = st.sidebar.selectbox('Multiple Lines', ('Yes', 'No', 'No phone service'))
    InternetService = st.sidebar.selectbox('Internet Service', ('DSL', 'Fiber optic', 'No'))
    OnlineSecurity = st.sidebar.selectbox('Online Security', ('Yes', 'No', 'No internet service'))
    OnlineBackup = st.sidebar.selectbox('Online Backup', ('Yes', 'No', 'No internet service'))
    DeviceProtection = st.sidebar.selectbox('Device Protection', ('Yes', 'No', 'No internet service'))
    TechSupport = st.sidebar.selectbox('Tech Support', ('Yes', 'No', 'No internet service'))
    StreamingTV = st.sidebar.selectbox('Streaming TV', ('Yes', 'No', 'No internet service'))
    StreamingMovies = st.sidebar.selectbox('Streaming Movies', ('Yes', 'No', 'No internet service'))
    Contract = st.sidebar.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
    PaperlessBilling = st.sidebar.selectbox('Paperless Billing', ('Yes', 'No'))
    PaymentMethod = st.sidebar.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
    MonthlyCharges = st.sidebar.slider('Monthly Charges', 18.0, 120.0, 50.0)
    TotalCharges = st.sidebar.slider('Total Charges', 0.0, 9000.0, 500.0)

    # Create a dictionary of the input data
    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Define the features to match the model's training data
# This part handles one-hot encoding for the categorical variables
df_encoded = pd.DataFrame(columns=[
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling',
    'MonthlyCharges', 'TotalCharges', 'MultipleLines_No phone service', 'MultipleLines_Yes',
    'InternetService_Fiber optic', 'InternetService_No', 'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes', 'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'DeviceProtection_No internet service', 'DeviceProtection_Yes', 'TechSupport_No internet service',
    'TechSupport_Yes', 'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes', 'Contract_One year',
    'Contract_Two year', 'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
])

df_encoded.at[0, 'gender'] = 1 if input_df['gender'].iloc[0] == 'Male' else 0
df_encoded.at[0, 'SeniorCitizen'] = 1 if input_df['SeniorCitizen'].iloc[0] == 'Yes' else 0
df_encoded.at[0, 'Partner'] = 1 if input_df['Partner'].iloc[0] == 'Yes' else 0
df_encoded.at[0, 'Dependents'] = 1 if input_df['Dependents'].iloc[0] == 'Yes' else 0
df_encoded.at[0, 'tenure'] = input_df['tenure'].iloc[0]
df_encoded.at[0, 'PhoneService'] = 1 if input_df['PhoneService'].iloc[0] == 'Yes' else 0
df_encoded.at[0, 'PaperlessBilling'] = 1 if input_df['PaperlessBilling'].iloc[0] == 'Yes' else 0
df_encoded.at[0, 'MonthlyCharges'] = input_df['MonthlyCharges'].iloc[0]
df_encoded.at[0, 'TotalCharges'] = input_df['TotalCharges'].iloc[0]

# One-hot encode the categorical features
for col in ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']:
    for option in input_df[col].unique():
        if col == 'MultipleLines':
            if option == 'Yes':
                df_encoded.at[0, 'MultipleLines_Yes'] = 1
            elif option == 'No phone service':
                df_encoded.at[0, 'MultipleLines_No phone service'] = 1
        elif col == 'InternetService':
            if option == 'Fiber optic':
                df_encoded.at[0, 'InternetService_Fiber optic'] = 1
            elif option == 'No':
                df_encoded.at[0, 'InternetService_No'] = 1
        elif col == 'OnlineSecurity':
            if option == 'Yes':
                df_encoded.at[0, 'OnlineSecurity_Yes'] = 1
            elif option == 'No internet service':
                df_encoded.at[0, 'OnlineSecurity_No internet service'] = 1
        elif col == 'OnlineBackup':
            if option == 'Yes':
                df_encoded.at[0, 'OnlineBackup_Yes'] = 1
            elif option == 'No internet service':
                df_encoded.at[0, 'OnlineBackup_No internet service'] = 1
        elif col == 'DeviceProtection':
            if option == 'Yes':
                df_encoded.at[0, 'DeviceProtection_Yes'] = 1
            elif option == 'No internet service':
                df_encoded.at[0, 'DeviceProtection_No internet service'] = 1
        elif col == 'TechSupport':
            if option == 'Yes':
                df_encoded.at[0, 'TechSupport_Yes'] = 1
            elif option == 'No internet service':
                df_encoded.at[0, 'TechSupport_No internet service'] = 1
        elif col == 'StreamingTV':
            if option == 'Yes':
                df_encoded.at[0, 'StreamingTV_Yes'] = 1
            elif option == 'No internet service':
                df_encoded.at[0, 'StreamingTV_No internet service'] = 1
        elif col == 'StreamingMovies':
            if option == 'Yes':
                df_encoded.at[0, 'StreamingMovies_Yes'] = 1
            elif option == 'No internet service':
                df_encoded.at[0, 'StreamingMovies_No internet service'] = 1
        elif col == 'Contract':
            if option == 'One year':
                df_encoded.at[0, 'Contract_One year'] = 1
            elif option == 'Two year':
                df_encoded.at[0, 'Contract_Two year'] = 1
        elif col == 'PaymentMethod':
            if option == 'Credit card (automatic)':
                df_encoded.at[0, 'PaymentMethod_Credit card (automatic)'] = 1
            elif option == 'Electronic check':
                df_encoded.at[0, 'PaymentMethod_Electronic check'] = 1
            elif option == 'Mailed check':
                df_encoded.at[0, 'PaymentMethod_Mailed check'] = 1
    # Replace NaN with 0 for one-hot encoded columns
    df_encoded = df_encoded.fillna(0)

# Display user input
st.subheader("User Input Features")
st.write(input_df)

# Prediction
if st.sidebar.button("Predict Churn"):
    prediction = model.predict(df_encoded.values)
    prediction_proba = model.predict_proba(df_encoded.values)

    st.subheader("Prediction")
    churn_status = "Customer will churn 😥" if prediction[0] == 1 else "Customer will not churn 🎉"
    st.write(churn_status)

    st.subheader("Prediction Probability")
    st.write(f"Churn probability: {prediction_proba[0][1]:.2%}")
    st.write(f"No churn probability: {prediction_proba[0][0]:.2%}")