import streamlit as st
import joblib
import pandas as pd

model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection System")

st.write("Enter transaction details to predict whether the transaction is fraudulent.")

transaction_type = st.selectbox(
    "Transaction Type",
    ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
)

step = st.number_input("Step", min_value=0)
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)
isFlaggedFraud = st.number_input("Is Flagged Fraud", min_value=0, max_value=1, step=1)

if st.button("Predict Fraud"):

    balance_change_orig = oldbalanceOrg - newbalanceOrig
    balance_change_dest = oldbalanceDest - newbalanceDest

    input_data = pd.DataFrame([{
    "step": step,
    "type": transaction_type,
    "amount": amount,
    "oldbalanceOrg": oldbalanceOrg,
    "newbalanceOrig": newbalanceOrig,
    "oldbalanceDest": oldbalanceDest,
    "newbalanceDest": newbalanceDest,
    "isFlaggedFraud": isFlaggedFraud,
    "balance_change_orig": balance_change_orig,
    "balance_change_dest": balance_change_dest
}])
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Genuine Transaction")