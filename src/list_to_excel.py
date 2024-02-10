#!/usr/bin/env python

"""
list_to_excel.py:
    This Python script converts a list of prospect data into an Excel file with
    Prospect, Contact, Address and Site columns.

    return:
        None
"""

from openpyxl import Workbook


def list_to_excel(tableau):
    wb = Workbook()
    ws = wb.active

    ws.append(["Prospect", "Contact", "Adresse", "Site"])

    for ligne in tableau:
        ws.append(ligne)
    wb.save("google_maps_results.xlsx")

    return None
