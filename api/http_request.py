import sys
# sys.path.append("E:\\workspace\\Crypto\crypo_task\\api")

import requests
import json
from urllib.error import HTTPError
from logger import logger


def http_get(get_url, params=None, headers=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}
    try:
        resp = requests.get(get_url, params=params, headers=headers)
        logger.info(f"http GET to URL {get_url} succes!")
        logger.info(f"response text is {resp.text}")
        logger.info(f"response status code is {resp.status_code}")
    except HTTPError as e:
        logger.info(f"http GET failed, error message is: {e}")
    else:
        return resp.status_code, resp.json(), resp.headers


if __name__ == "__main__":
    url = "https://pda.weather.gov.hk/locspc/data/fnd_e.xml"
    http_get(url)
