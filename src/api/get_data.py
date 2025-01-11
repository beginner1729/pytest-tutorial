import requests
import logging
import json

logger = logging.getLogger(__name__)

def request_data(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status() # checks for 4xx or 5xx error
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        logger.error("Error in fetching data: {e}")
        return None

