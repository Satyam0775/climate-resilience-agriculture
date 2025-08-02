import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingest import load_all_data

def test_data_loading():
    data = load_all_data()
    assert "MH_temp" in data
    assert not data["MH_temp"].empty
