#!/usr/bin/env python

"""
get_list_infos.py:
    This Python script retrieves location information from the Google Places API using identifiers and an API key, 
    and returns a list of relevant information, such as name, address, contact and website.
"""

import requests

from src.get_ids import get_ids
from res.config import KEY

def get_list_infos(query):
    list_infos = []
    list_ids = get_ids(query)
    url = "https://maps.googleapis.com/maps/api/place/details/json"

    for id in list_ids:
        params = {
            'key': KEY,
            'placeid': id
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            res = data["result"]
            name = res["name"]
            address = res["formatted_address"]
            contact = res["formatted_phone_number"]
            website = None
            if "website" in res:
                website = res["website"]
            list_infos.append([name, contact, address, website])
    return list_infos