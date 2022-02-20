import sys
# sys.path.append("E:\\workspace\\Crypto\crypo_task\\api")

import requests
import json
from urllib.error import HTTPError
from logger import logger

def http_get(url, params={}):
    try:
        resp = requests.get(url, params)
        logger.info("http GET to URL %s succes!"%url)
        logger.info("response text is %s"%resp.text)
        logger.info("response status code is %s"%resp.status_code)
    except HTTPError as e:
        logger.info("http GET failed, error message is: %s"%e)
    else:
        return resp.json()

if __name__ == "__main__":
    url = "https://pda.weather.gov.hk/locspc/data/fnd_e.xml"
    http_get(url)