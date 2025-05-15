import pandas as pd
import joblib
from functions import transform_columns_mapping, handle_missing_values
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, roc_auc_score

# 1. Carregamento dos dados
churn_df_clean = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv", na_values=' ')
churn_df_clean = churn_df_clean.drop(columns=['customerID', 'PhoneService', 'gender'])

# 2. Mapeamento de colunas binárias
binary_columns = ['Partner', 'Dependents', 'PaperlessBilling', 'Churn']
mapping = {'Yes': 1, 'No': 0}
transform_columns_mapping(churn_df_clean, binary_columns, mapping)

# 3. One-hot encoding nas colunas categóricas
categorical_columns = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                       'Contract', 'PaymentMethod']
churn_df_clean = pd.get_dummies(churn_df_clean, columns=categorical_columns, drop_first=True)

# 4. Conversão de booleanos para inteiros
bool_columns = churn_df_clean.select_dtypes(include='bool').columns
churn_df_clean[bool_columns] = churn_df_clean[bool_columns].astype(int)

# 5. Separação de features e target
X = churn_df_clean.drop(columns=['Churn'])
y = churn_df_clean['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# 6. Tratamento de valores ausentes
handle_missing_values(X_train, 'TotalCharges')
handle_missing_values(X_test, 'TotalCharges')

# 7. Padronização
cols_to_standardize = ['tenure', 'TotalCharges', 'MonthlyCharges']
scaler = StandardScaler()
X_train[cols_to_standardize] = scaler.fit_transform(X_train[cols_to_standardize])
X_test[cols_to_standardize] = scaler.transform(X_test[cols_to_standardize])

# 8. Undersampling para balanceamento
undersampler = RandomUnderSampler(random_state=42)
X_train_us, y_train_us = undersampler.fit_resample(X_train, y_train)

# 9. Treinamento do modelo
gbc_model = GradientBoostingClassifier(random_state=42)
gbc_model.fit(X_train_us, y_train_us)

# 10. Avaliação
y_test_pred = gbc_model.predict(X_test)
y_test_proba = gbc_model.predict_proba(X_test)[:, 1]
print("----- Test Set -----")
print(classification_report(y_test, y_test_pred))
print(f"AUC-ROC (Test): {roc_auc_score(y_test, y_test_proba)}")

# 11. Salvamento da pipeline
model_pipeline = {
    'model': gbc_model,
    'scaler': scaler,
    'cols_to_standardize': cols_to_standardize,
    'training_columns': X_train.columns.to_list()
}
joblib.dump(model_pipeline, 'churn_gbcmodel_pipeline.pkl')
