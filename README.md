# 🌾 Climate Resilience Assessment – Maharashtra & Madhya Pradesh

This project analyzes climate patterns in Maharashtra and Madhya Pradesh using historical temperature and rainfall data. It helps assess climate resiliency for agricultural regions by generating trend plots and key indicators like temperature variability and rainfall totals.

---

## 📁 Project Structure

CLIMATE_RESILIENCE_SATELLITE_AGRICULTURE/
│
├── data/
│ └── raw/
│ ├── MH_temperature.csv # Maharashtra temperature data
│ ├── MH_precipitation.csv # Maharashtra rainfall data
│ ├── MP_temperature.csv # Madhya Pradesh temperature data
│ └── MP_precipitation.csv # Madhya Pradesh rainfall data
│
├── Task/
│ ├── app.py # Streamlit-based interactive dashboard
│ ├── main.py # CLI-based analysis script
│ ├── analyze.py # Plotting and trend analysis functions
│ ├── indicators.py # Climate resilience indicator logic
│ ├── ingest.py # Raw data loading functions
│ ├── transform.py # Data cleaning and transformation
│ ├── utils.py # Utility/helper functions
│ └── tests/
│ └── test_pipeline.py # Basic unit tests
│
├── README.md # Project documentation and instructions
├── case_study_analysis.md # Climate resilience case study write-up
└── requirements.txt # Required Python packages


---

## 🚀 How to Run

### 🔧 Setup

1. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

Launch the interactive dashboard:
▶️ Option 1: Streamlit App
streamlit run Task/app.py
Features:

Select state (MH or MP)
Choose temperature type (mean, max, min)
View trend graphs and resilience indicators

▶️ Option 2: CLI Mode
Run from terminal:
python Task/main.py
What it does:

Loads and cleans climate data
Plots temperature and rainfall trends
Prints climate resilience indicators

📊 Climate Resilience Indicators
We calculate the following indicators:

Indicator	Description
Temp_Mean	Average temperature
Temp_Variability	Std deviation of temperature
Rainfall_Total	Sum of precipitation (mm)
Rainfall_Variability	Std deviation of rainfall (mm)

🧪 Testing
Run all tests using:

pytest Task/tests/
Includes:

Data ingestion test

Transformation logic validation

Output structure check

📚 Documentation
See case_study_analysis.md for:

Case study summary

Climate observations

Future plans (NDVI, crop yield, economic impact)

Recommendations for monitoring & policy enhancement

📽 Demo Video
▶️ Watch the full walkthrough video here: https://www.loom.com/share/23c89ee6511c4c2eb8a52755ddaf4515

The video explains:

Project structure

How to use the dashboard

Key climate insights

What can be added next

✅ Summary
This project builds a strong foundation for climate resiliency analysis using open-source tools. It can be extended with:

NDVI (satellite vegetation data)

Economic and crop yield data

Government scheme effectiveness

With these, it can support decision-making for farmers, researchers, and policymakers.
