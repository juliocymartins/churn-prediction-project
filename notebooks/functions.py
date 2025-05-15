def transform_columns_mapping(dataframe, columns, mapping):
    for column in columns:
        dataframe[column] = dataframe[column].replace(mapping)

def handle_missing_values(dataframe, column):
    median_value = dataframe[column].median()
    dataframe[column] = dataframe[column].fillna(median_value)
