import requests
import logging
import json

from src.shapes import shape_registry_mapping

logger = logging.getLogger(__name__)

def request_data(url: str):
    """
    Reads the data from the url
    """
    try:
        response = requests.get(url)
        response.raise_for_status() # checks for 4xx or 5xx error
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        logger.error("Error in fetching data: {e}")
        return None

def process_data_to_objs(json_value: dict):
    """
    creates a list of shape objects
    The json object is to be same as shown in the
    fake data.
    """
    list_shapes = json_value["shapeTypes"]
    shape_objs = []
    for type_params in list_shapes:
        shape_class = shape_registry_mapping[type_params["type"]]

        shape_obj = shape_class(*type_params['params'])
        shape_objs.append(shape_obj)

    return shape_objs
