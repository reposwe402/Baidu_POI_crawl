# This module will handle API requests and responses.

import requests
import json


def fetch_poi_data(roi_key, city_str, baidu_ak, page_num):
    """
    Fetch POI data from Baidu API.
    """
    URL = "http://api.map.baidu.com/place/v2/search?query=" + roi_key + \
        "&region=" + city_str + \
        "&output=json" +  \
        "&ak=" + baidu_ak + \
        "&scope=2" + \
        "&page_size=20" + \
        "&page_num=" + str(page_num)
    resp = requests.get(URL)
    return json.loads(resp.text)
