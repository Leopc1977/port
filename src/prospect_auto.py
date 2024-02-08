#!/usr/bin/env python

"""
prospect_auto.py:
    This Python script automates the search for {query} and exports them to an Excel file.
"""

from src.get_list_infos import get_list_infos
from src.list_to_excel import list_to_excel

def prospect_auto(query):
    list_infos = get_list_infos(query)
    list_to_excel(list_infos)
