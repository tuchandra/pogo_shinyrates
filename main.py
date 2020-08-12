"""
main.py -- scrape shinyrates.com
"""

import json
from datetime import datetime

import pandas as pd
import requests

def get_shinyrates() -> pd.DataFrame:
    """Get shiny rates snapshot from shinyrates.com"""

    url = "https://shinyrates.com/data/rate"
    data = requests.get(url).json()
    data_csv = pd.DataFrame.from_dict(data)
    return data_csv


if __name__ == "__main__":
    data = get_shinyrates()
    today = datetime.now().strftime(r"%Y-%m-%d %H%M")
    data.to_csv(f"data/{today}.csv")
