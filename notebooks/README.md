# Notebooks Folder – Model Development

This folder contains the full machine learning development process for detecting churn cases. It includes exploratory data analysis, model training, evaluation, and creation of testing datasets.

## Contents

- `churn_prediction_notebook.ipynb`: Main Jupyter Notebook detailing the full ML workflow:
  - Exploratory Data Analysis (EDA)
  - Feature Engineering
  - Model comparison
  - Final pipeline creation
- `churn_predictions.py`: Script version of the notebook for faster execution and exporting the model pipeline as `churn_gbcmodel_pipeline.pkl`.
- `churn_test_datasets.ipynb`: Notebook used to filter and generate testing datasets for app evaluation:
  - `test_churn_yes.xlsx`
  - `test_churn_no.xlsx`
- `functions.py`: Python file containing helper functions for cleaning, preprocessing, and model building.

## How to Use

1. **Download the Dataset**  
   - First, download the dataset from [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
   - Place the downloaded `WA_Fn-UseC_-Telco-Customer-Churn.csv` file in the same folder as the notebooks.

2. **Run the Notebooks**  
   - Open and run the notebooks in your preferred environment (JupyterLab, VSCode, Google Colab, etc).
   - Ensure all required Python packages are installed (e.g., `pandas`, `scikit-learn`, `matplotlib`, etc).
