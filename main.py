from src.ingest import load_all_data
from src.transform import clean_dataframe
from src.analyze import plot_trend
from src.indicators import compute_climate_resilience

def process_state(state_name, temp_df, precip_df, temp_col, precip_col):
    print(f"\n🔍 Processing {state_name} data...")

    # Clean the data
    temp_df = clean_dataframe(temp_df)
    precip_df = clean_dataframe(precip_df)

    # Debug info
    print("   Columns in temp data:", temp_df.columns.tolist())
    print("   Columns in precip data:", precip_df.columns.tolist())

    # Plotting
    print(f"\n📈 Plotting {state_name} Temperature Trend...")
    plot_trend(temp_df, temp_col, state_name, "Temperature", show_plot=True)

    print(f"📉 Plotting {state_name} Precipitation Trend...")
    plot_trend(precip_df, precip_col, state_name, "Precipitation", show_plot=True)

    # Compute indicators
    indicators = compute_climate_resilience(temp_df, precip_df, temp_col, precip_col)
    print(f"\n✅ Climate Resilience Indicators for {state_name}:")
    for key, val in indicators.items():
        print(f"   {key}: {val:.2f}")

    print(f"\n✔️ {state_name} analysis complete. Close plots to continue...\n")


def main():
    print("\n🌾 Starting Climate Resilience Analysis...\n")

    # Load all data
    data = load_all_data()

    # Step 1: Maharashtra
    process_state(
        "Maharashtra",
        data["MH_temp"],
        data["MH_precip"],
        temp_col="mean",
        precip_col="rainfall_mm"
    )

    # Step 2: Madhya Pradesh
    process_state(
        "Madhya Pradesh",
        data["MP_temp"],
        data["MP_precip"],
        temp_col="mean",
        precip_col="rainfall_mm"
    )

    print("\n🏁 All states processed. Analysis complete.\n")


if __name__ == "__main__":
    main()
