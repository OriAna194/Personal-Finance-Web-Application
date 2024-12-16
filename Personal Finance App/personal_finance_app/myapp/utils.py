import json
from urllib.request import urlopen
from urllib.error import URLError
from django.conf import settings

import requests

def get_conversion_rate(base_currency, target_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        return data['rates'].get(target_currency, 1)  # Default to 1 if the target currency is not found
    except requests.RequestException as e:
        print(f"Error fetching conversion rate: {e}")
        return 1  # Default to 1 if there's an error (no conversion)
