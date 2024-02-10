#!/usr/bin/env python

"""
get_ids.py:
    This Python script retrieves unique location identifiers using a search
    query and returns a list of unique identifiers.
"""

from src.search_request import search_request


def get_ids(query):

    results = search_request(query)
    unique_results = {}

    for result in results:
        place_id = result["place_id"]
        if place_id not in unique_results:
            unique_results[place_id] = place_id

    unique_results_list = list(unique_results.values())

    return unique_results_list
