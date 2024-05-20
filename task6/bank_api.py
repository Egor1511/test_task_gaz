from datetime import datetime

import requests


def get_bank_data(api_url):
    """
    Function to get data from API

    Args:
        api_url: url of API
    Returns:
        json data from API
    """
    current_datetime = datetime(2024, 5, 17)

    start_of_day = datetime(current_datetime.year, current_datetime.month,
                            current_datetime.day, 0, 0, 0)

    timestamp_start_of_day = start_of_day.timestamp()

    params = {'documents_date': {f"{timestamp_start_of_day}"}}
    response = requests.get(api_url, params=params, timeout=120)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Failed to get data from API")
        return None
