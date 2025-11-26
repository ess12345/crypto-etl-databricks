import requests
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_crypto_data(base_url, endpoint, vs_currency="usd", limit=50, retries=3, timeout=10):
    url = base_url + endpoint
    params = {
        "vs_currency": vs_currency,
        "per_page": limit
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, params=params, timeout=timeout)

            if response.status_code == 200:
                logger.info("API request successful.")
                return response.json()
            else:
                logger.warning(f"Attempt {attempt}: API returned status {response.status_code}")

        except Exception as e:
            logger.error(f"Attempt {attempt}: Error occurred → {e}")

        time.sleep(2)

    raise Exception(f"API request failed after {retries} attempts.")
