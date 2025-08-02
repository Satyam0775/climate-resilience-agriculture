def compute_climate_resilience(temp_df, precip_df, temp_col, precip_col):
    indicators = {}

    # Temperature metrics
    indicators["Temp_Mean"] = round(temp_df[temp_col].mean(), 2) if temp_col in temp_df else "N/A"
    indicators["Temp_Variability"] = round(temp_df[temp_col].std(), 2) if temp_col in temp_df else "N/A"

    # Rainfall metrics
    indicators["Rainfall_Total"] = round(precip_df[precip_col].sum(), 2) if precip_col in precip_df else "N/A"
    indicators["Rainfall_Variability"] = round(precip_df[precip_col].std(), 2) if precip_col in precip_df else "N/A"

    return indicators
