import pandas as pd

def clean_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Trim spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x,str) else x)

    # Fix missing values
    df = df.fillna("")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

    return df