# Customer Churn Prediction Project

<img align="center" alt="Churn App" width="400" src="https://propz.com.br/wp-content/uploads/2022/12/capa-6-jpg-1200x900.webp">

# Overview
This project focuses on predicting customer churn by analyzing behavioral, demographic, and account data. The goal is to build and deploy a machine learning model capable of identifying customers at risk of cancelling their services. The project includes a full end-to-end pipeline: data analysis, preprocessing, model training, testing, deployment via Docker, and a working web app hosted on Google Cloud Platform.

### What is Churn?
Churn refers to the rate at which customers stop doing business with a service provider. By identifying potential churners in advance, businesses can develop effective customer retention strategies.

🔗 **Live App**: [Access the Churn Prediction App](https://fraud-detection-app-855024627767.us-central1.run.app/)

**Link to Dataset**: [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

# About Dataset

### Context
"Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]

### Content
Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:

- Customers who left within the last month – the column is called Churn
- Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers – gender, age range, and if they have partners and dependents

# How to Use the App

1. **Adjust the Input Settings**  
   Use the sidebar to fill in customer data, such as **tenure**, **monthly charges**, **internet services**, and **contract type**.

2. **Predict**  
   - Click **Predict** to generate a churn prediction based on the current input values.  
   - The result will indicate whether the customer is likely to **churn** or **stay**, along with the **probability**.

3. **Test with Churn Data**  
   - Click **Test with Churn Data** to auto-fill the form with a real example of a customer who **left**.  
   - The app will automatically run a prediction using this example.

4. **Test with Non-Churn Data**  
   - Click **Test with Non-Churn Data** to auto-fill the form with a real example of a customer who **did not churn**.  
   - The app will show the prediction result accordingly.

# Repository Files

- **app/**: Contains the application files:

- **notebooks/**: Contains the Jupyter notebooks and related scripts:

- **Dockerfile**: Configuration for building the Docker container.

- **requirements.txt**: List of required Python packages.

- **.gitignore**: Git ignored files.

- **README.md**: Project documentation.

# Required Libraries
To run this project, the following Python packages are needed:

- pandas
- matplotlib
- seaborn
- numpy
- scikit-learn
- imbalanced-learn
- tensorflow
- streamlit
- openpyxl

# How to Use Locally
- Clone the repository to your local machine
- Install dependencies
- Run the Streamlit app

# GCP Deployment
This project was successfully deployed on Google Cloud Platform (GCP) using a Docker container as a study of end-to-end machine learning deployment.

# Author
Julio Cesar Yamashita Martins

# E-mail
yamashitajulio@gmail.com