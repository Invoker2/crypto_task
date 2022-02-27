import requests
import json
from http_request import http_get
from common import time_today_after_tomorrow
from logger import logger


def test_get_nine_day_forecase():
    url = "https://pda.weather.gov.hk/locspc/data/fnd_e.xml"
    status_code, ret_msg, ret_header = http_get(url)
    assert status_code == 200, f"Request failed with {status_code}"
    time_tat = time_today_after_tomorrow()
    forcast_details = ret_msg["forecast_detail"]
    for forcast_detail in forcast_details:
        if forcast_detail["forecast_date"] == time_tat:
            assert "min_rh" in forcast_detail and "max_rh" in forcast_detail
            max_rh = forcast_detail["max_rh"] if "max_rh" in forcast_detail else None
            min_rh = forcast_detail["min_rh"] if "min_rh" in forcast_detail else None
            logger.info(f"Relative humidity for the day after tomorrow {time_tat} is from {min_rh} to {max_rh}")
