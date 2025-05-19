# Customer Churn Prediction Project

<img align="center" alt="Churn App" width="400" src="https://propz.com.br/wp-content/uploads/2022/12/capa-6-jpg-1200x900.webp">

# Overview
This project focuses on predicting customer churn by analyzing behavioral, demographic, and account data. The goal is to build and deploy a machine learning model capable of identifying customers at risk of cancelling their services. The project includes a full end-to-end pipeline: data analysis, preprocessing, model training, testing, deployment via Docker, and a working web app hosted on Google Cloud Platform.

### What is Churn?
Churn refers to the rate at which customers stop doing business with a service provider. By identifying potential churners in advance, businesses can develop effective customer retention strategies.

Link to Dataset: [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## 🌐 Web Application
Try the deployed Churn Prediction App here:  
🔗 [https://churn-detection-app-855024627767.us-central1.run.app/](https://churn-detection-app-855024627767.us-central1.run.app/)

## Required Libraries
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

Install everything using the `requirements.txt` file:

pip install -r requirements.txt

## Repository Files
- **app/**: Contains the application files:
  - `churn_app.py`: Streamlit app to input variables and return predictions.
  - `churn_gbcmodel_pipeline.pkl`: Serialized pipeline and trained model.
  - `background_churn.jpg`: Background image used in the app.
  - `test_churn_yes.xlsx`: Sample of churn transactions for testing.
  - `test_churn_no.xlsx`: Sample of non-churn transactions for testing.

- **notebooks/**: Contains the Jupyter notebooks and related scripts:
  - `churn_prediction_notebook.ipynb`: Complete analysis and model development process.
  - `churn_predictions.py`: Script for training the model and saving the pipeline.
  - `churn_test_datasets.ipynb`: Creates testing datasets used in the app.
  - `functions.py`: Helper functions used in the project.

- **Dockerfile**: Configuration for building the Docker container.

- **requirements.txt**: List of required Python packages.

- **.gitignore**: Git ignored files.

- **README.md**: Project documentation.