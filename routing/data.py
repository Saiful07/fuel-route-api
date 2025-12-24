import pandas as pd
from pathlib import Path
from django.conf import settings
from functools import lru_cache

BASE_DIR = Path(settings.BASE_DIR)
CSV_PATH = BASE_DIR / "fuel-prices-for-be-assessment.csv"

@lru_cache(maxsize=1)
def load_fuel_prices():
    df = pd.read_csv(CSV_PATH)
    df.columns = [c.strip().lower() for c in df.columns]
    return df
