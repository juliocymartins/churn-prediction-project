import streamlit as st
import pandas as pd
import joblib
import base64

# ======== FUNCTION TO SET BACKGROUND WITH TRANSPARENCY ========
def set_background(image_file):
    import base64
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        position: relative;
    }}

    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 0;
    }}

    .stApp > * {{
        position: relative;
        z-index: 1;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: white !important;
    }}

    [data-testid="stSidebar"] h2 {{
        color: black !important;
    }}

    .css-1avcm0n label,
    .css-1avcm0n .st-bw {{
        color: black !important;
    }}

    /* Scrollable sidebar */
    section[data-testid="stSidebar"] > div:first-child {{
        height: 100vh;
        overflow-y: auto;
        padding-right: 10px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background
set_background("app/background_churn.jpg")

# ======== LOAD MODEL AND DATA ========
model_pipeline = joblib.load('churn_gbcmodel_pipeline.pkl')
model = model_pipeline['model']
scaler = model_pipeline['scaler']
cols_to_standardize = model_pipeline['cols_to_standardize']
training_columns = model_pipeline['training_columns']

churn_data_yes = pd.read_excel('app/test_churn_yes.xlsx')
churn_data_no = pd.read_excel('app/test_churn_no.xlsx')

# ======== FUNCTIONS ========
def make_prediction(model, scaler, df):
    df[cols_to_standardize] = scaler.transform(df[cols_to_standardize])
    prediction = model.predict(df)
    probability = model.predict_proba(df)[:, 1]
    return prediction, probability

def get_random_entry(data):
    return data.sample(n=1).iloc[0].to_dict()

# ======== SESSION STATE INITIALIZATION ========
if 'input_values' not in st.session_state:
    st.session_state.input_values = {
        'tenure': 0,
        'MonthlyCharges': 0.0,
        'MultipleLines': 'No',
        'InternetService': 'No',
        'OnlineSecurity': 'No',
        'OnlineBackup': 'No',
        'DeviceProtection': 'No',
        'TechSupport': 'No',
        'StreamingTV': 'No',
        'StreamingMovies': 'No',
        'Contract': 'Month-to-month',
        'PaymentMethod': 'Electronic check'
    }

if 'run_prediction' not in st.session_state:
    st.session_state.run_prediction = False

# ======== STREAMLIT INTERFACE ========
st.title("Customer Churn Prediction")

st.sidebar.header("Input Settings")

input_values = st.session_state.input_values
tenure = st.sidebar.number_input("Tenure", min_value=0, max_value=100, value=int(input_values['tenure']))
monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, max_value=150.0, value=float(input_values['MonthlyCharges']))
total_charges = tenure * monthly_charges

multiple_lines = st.sidebar.selectbox("Multiple Lines", ['No phone service', 'No', 'Yes'], index=['No phone service', 'No', 'Yes'].index(input_values['MultipleLines']))
internet_service = st.sidebar.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'], index=['DSL', 'Fiber optic', 'No'].index(input_values['InternetService']))

if internet_service in ['DSL', 'Fiber optic']:
    online_security = st.sidebar.selectbox("Online Security", ['No', 'Yes'], index=['No', 'Yes'].index(input_values['OnlineSecurity']))
    online_backup = st.sidebar.selectbox("Online Backup", ['No', 'Yes'], index=['No', 'Yes'].index(input_values['OnlineBackup']))
    device_protection = st.sidebar.selectbox("Device Protection", ['No', 'Yes'], index=['No', 'Yes'].index(input_values['DeviceProtection']))
    tech_support = st.sidebar.selectbox("Tech Support", ['No', 'Yes'], index=['No', 'Yes'].index(input_values['TechSupport']))
    streaming_tv = st.sidebar.selectbox("Streaming TV", ['No', 'Yes'], index=['No', 'Yes'].index(input_values['StreamingTV']))
    streaming_movies = st.sidebar.selectbox("Streaming Movies", ['No', 'Yes'], index=['No', 'Yes'].index(input_values['StreamingMovies']))
else:
    online_security = 'No internet service'
    online_backup = 'No internet service'
    device_protection = 'No internet service'
    tech_support = 'No internet service'
    streaming_tv = 'No internet service'
    streaming_movies = 'No internet service'

contract = st.sidebar.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'], index=['Month-to-month', 'One year', 'Two year'].index(input_values['Contract']))
payment_method = st.sidebar.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], index=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'].index(input_values['PaymentMethod']))

# ======== FUNCTION TO SHOW RESULT ========
def show_result():
    data_input = {
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'Dependents': [0],  # Adjust as needed
        'PaperlessBilling': [1],  # Adjust as needed
        'MultipleLines_No phone service': [int(multiple_lines == 'No phone service')],
        'MultipleLines_Yes': [int(multiple_lines == 'Yes')],
        'InternetService_Fiber optic': [int(internet_service == 'Fiber optic')],
        'InternetService_No': [int(internet_service == 'No')],
        'OnlineSecurity_Yes': [int(online_security == 'Yes')],
        'OnlineBackup_Yes': [int(online_backup == 'Yes')],
        'DeviceProtection_Yes': [int(device_protection == 'Yes')],
        'TechSupport_Yes': [int(tech_support == 'Yes')],
        'StreamingTV_Yes': [int(streaming_tv == 'Yes')],
        'StreamingMovies_Yes': [int(streaming_movies == 'Yes')],
        'Contract_One year': [int(contract == 'One year')],
        'Contract_Two year': [int(contract == 'Two year')],
        'PaymentMethod_Credit card (automatic)': [int(payment_method == 'Credit card (automatic)')],
        'PaymentMethod_Bank transfer (automatic)': [int(payment_method == 'Bank transfer (automatic)')],
        'PaymentMethod_Mailed check': [int(payment_method == 'Mailed check')]
    }

    data_input_df = pd.DataFrame(data_input)
    data_input_df = data_input_df.reindex(columns=training_columns, fill_value=0)

    prediction, probability = make_prediction(model, scaler, data_input_df)
    if prediction[0] == 1:
        st.markdown(f"<h2 style='color: red;'>🚨 Prediction: Churn </h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: red;'>Churn Probability: {probability[0] * 100:.2f}%</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='color: green;'>✅ Prediction: Not Churn </h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: green;'>Churn Probability: {probability[0] * 100:.2f}%</h3>", unsafe_allow_html=True)

# ======== TEST BUTTONS ========
if st.sidebar.button("Test with Churn Data"):
    st.session_state.input_values = get_random_entry(churn_data_yes)
    st.session_state.run_prediction = True
    st.rerun()

if st.sidebar.button("Test with Non-Churn Data"):
    st.session_state.input_values = get_random_entry(churn_data_no)
    st.session_state.run_prediction = True
    st.rerun()

if st.session_state.run_prediction:
    show_result()
    st.session_state.run_prediction = False

# ======== MANUAL PREDICTION BUTTON ========
if st.sidebar.button("Predict"):
    show_result()
