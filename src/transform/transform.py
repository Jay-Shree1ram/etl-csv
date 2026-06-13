import pandas as pd

from extract.extract import extract_data

def transform_data(df):
    if df is None or df.empty:
        raise ValueError("Input DataFrame is empty")

    # -----------------------------
    #  Standardize column names
    # -----------------------------
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[.\-\s]+", "_", regex=True)
    )

    # -----------------------------
    # 2. Rename business columns
    # -----------------------------
    # column_mapping = {
    #     "e_mail_address": "email",
    #     "salary_npr": "salary"
    # }

    # df = df.rename(columns=column_mapping)
