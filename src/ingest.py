import os
import pandas as pd

def load_all_data():
    base_path = "data/raw"

    data = {
        "MH_temp": pd.read_csv(os.path.join(base_path, "MH_temperature.csv")),
        "MH_precip": pd.read_csv(os.path.join(base_path, "MH_precipitation.csv")),
        "MP_temp": pd.read_csv(os.path.join(base_path, "MP_temperature.csv")),
        "MP_precip": pd.read_csv(os.path.join(base_path, "MP_precipitation.csv")),
    }

    return data
