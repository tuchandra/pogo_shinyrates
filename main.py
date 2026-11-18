# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas>=3.1",
#     "requests>=2.34",
# ]
# ///

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
    data_csv = pd.DataFrame(data)
    return data_csv


if __name__ == "__main__":
    data = get_shinyrates()
    today = datetime.now().strftime(r"%Y-%m-%d %H%M")
    data.to_csv(f"data/{today}.csv")
