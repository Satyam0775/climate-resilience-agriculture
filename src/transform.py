import pandas as pd

def clean_dataframe(df, date_column="date"):
    # Remove extra index columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed', case=False)]

    # Fix date parsing
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")
    df = df.dropna(subset=[date_column])
    df = df.sort_values(by=date_column)
    return df
