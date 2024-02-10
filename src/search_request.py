#!/usr/bin/env python

"""
search_request.py:
    This Python script sends a search request to the Google Places API using a
    text query and returns the results.
"""

import requests

from res.config import KEY

api_key = KEY
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'


def search_request(query):

    params = {
        'query': query,
        'key': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return None
