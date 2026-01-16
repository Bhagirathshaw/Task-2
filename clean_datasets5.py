import pandas as pd
import numpy as np

house = pd.read_csv("house_prices_raw.csv")
medical = pd.read_csv("medical_appointments_raw.csv")

def clean_dataset(df):
    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(exclude=np.number).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

house_clean = clean_dataset(house)
medical_clean = clean_dataset(medical)

house_clean.to_csv("house_prices_cleaned.csv", index=False)
medical_clean.to_csv("medical_appointments_cleaned.csv", index=False)
