# 🌾 Climate Resilience Assessment – Maharashtra & Madhya Pradesh

This project analyzes climate patterns in Maharashtra and Madhya Pradesh using historical temperature and rainfall data. It helps assess climate resiliency for agricultural regions by generating trend plots and key indicators like temperature variability and rainfall totals.

## 📁 Project Structure

CLIMATE_RESILIENCE_SATELLITE_AGRICULTURE/
├── data/
│ └── raw/
│ ├── MH_temperature.csv
│ ├── MH_precipitation.csv
│ ├── MP_temperature.csv
│ └── MP_precipitation.csv
├── Task/
│ ├── app.py # Streamlit dashboard
│ ├── main.py # Console-based analysis
│ ├── analyze.py # Plotting functions
│ ├── indicators.py # Resilience indicators
│ ├── ingest.py # Data loading
│ ├── transform.py # Data cleaning
│ ├── utils.py # Helper utilities
│ └── tests/
│ └── test_pipeline.py # Basic tests
├── README.md # Project overview
├── case_study_analysis.md # Case study writeup
└── requirements.txt # Python dependencies

## 🚀 How to Run

### 🔧 Setup

1. Create virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:

pip install -r requirements.txt
▶️ Option 1: Streamlit App
Launch interactive dashboard:

streamlit run Task/app.py
Features:

Select state (MH or MP)

Choose temperature type (mean, max, min)

View trend graphs & resilience indicators

▶️ Option 2: CLI Mode
Run analysis in terminal:

python Task/main.py
It will:

Load and clean temperature & rainfall data

Plot both trends

Print resilience indicators

📊 Climate Resilience Indicators
We calculate the following metrics:

Indicator	Description
Temp_Mean	Average temperature
Temp_Variability	Std deviation of temperature
Rainfall_Total	Sum of precipitation (mm)
Rainfall_Variability	Std deviation of rainfall (mm)

🧪 Testing
Run tests with:

pytest Task/tests/
This ensures basic pipeline checks and data processing logic.

📚 Documentation
See case_study_analysis.md for:

Case study writeup (with recommendations)

Climate observations

Future enhancement plans (NDVI, policies, crop yield, economics)

📽 Demo Video
➡️ A walkthrough video of the dashboard, pipeline, and insights is attached with the submission (or hosted on the repo).


✅ This is a foundational framework for agricultural climate resiliency analysis, which can be extended with NDVI, yield data, and economic impacts.

Let me know if you want the **video script** or **GitHub-ready version** next.
