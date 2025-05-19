# Notebooks Folder – Model Development

This folder contains the full machine learning development process for detecting churn cases. It includes exploratory data analysis, model training, evaluation, and creation of testing datasets.

## Contents

The notebooks/ folder contains the model building pipeline and data preparation.

- `churn_prediction_notebook.ipynb`: Main Jupyter Notebook detailing the full ML workflow:
  - Exploratory Data Analysis (EDA)
  - Feature Engineering
  - Model comparison
  - Final pipeline creation
  - Exporting the model with joblib
- `churn_predictions.py`: Script version of the notebook for faster execution and exporting the model pipeline as `churn_gbcmodel_pipeline.pkl`.
- `churn_test_datasets.ipynb`: Notebook used to filter and generate testing datasets for app evaluation:
  - `test_churn_yes.xlsx`
  - `test_churn_no.xlsx`
- `functions.py`: Python file containing helper functions for cleaning, preprocessing, and model building.

## How to Use

You can open and run the notebooks in your preferred environment (JupyterLab, VSCode, Google Colab, etc). Make sure the dataset is available and the required packages are installed.
