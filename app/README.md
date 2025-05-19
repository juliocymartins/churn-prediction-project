# App Folder – Churn Prediction App

This folder contains all the necessary files to run the Fraud Detection web application built with **Streamlit**. The app loads a pre-trained machine learning model and provides a user-friendly interface for users to input transaction data or test entire files.

## Contents

- `churn_app.py`: Streamlit app script to interact with the model.
- `churn_gbcmodel_pipeline.pkl`: Saved preprocessing pipeline and trained Gradient Boosting model.
- `background_churn`.jpg: Background image used in the app interface.
- `test_churn_yes`.xlsx: Test dataset containing churned customers.
- `test_churn_no`.xlsx: Test dataset containing non-churned customers.

## How to Run Locally

From the root of the project:

```bash
streamlit run app/churn_app.py