import requests
import logging
import json

from src.shapes import shape_registry_mapping

logger = logging.getLogger(__name__)
print(shape_registry_mapping)
def request_data(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status() # checks for 4xx or 5xx error
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        logger.error("Error in fetching data: {e}")
        return None

def process_data_to_objs(json_value: dict):
    list_shapes = json_value["shapeTypes"]
    shape_objs = []
    for type_params in list_shapes:
        shape_class = shape_registry_mapping[type_params["type"]]

        shape_obj = shape_class(*type_params['params'])
        shape_objs.append(shape_objs)

    return shape_objs
