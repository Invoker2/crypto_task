import requests
import json
from http_request import http_get
from common import time_today_after_tomorrow
from logger import logger

def test_get_nine_day_forecase():
    url = "https://pda.weather.gov.hk/locspc/data/fnd_e.xml"
    ret_msg = http_get(url)
    time_tat = time_today_after_tomorrow()
    forcast_details = ret_msg["forecast_detail"]
    for forcast_detail in forcast_details:
        if forcast_detail["forecast_date"] == time_tat:
            assert "min_rh" in forcast_detail and "max_rh" in forcast_detail
            max_rh = forcast_detail["max_rh"]
            min_rh = forcast_detail["min_rh"]
            logger.info("Relative humidity for the day after tomorrow %s is from %s to %s"%(time_tat, min_rh, max_rh))