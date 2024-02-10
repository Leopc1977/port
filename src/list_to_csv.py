#!/usr/bin/env python

"""
list_to_csv.py:
    This function converts a list of prospect data into a CSV file with
    Prospect, Contact, Address, Site, Choice and Reason columns.

    Return:
        None
"""

import csv


def list_to_csv(liste):

    nom_fichier_csv = 'donnees.csv'

    liste.insert(0, ["Prospect", "Contact", "Adresse",
                     "Site", "Choix", "Raison"])
    with open(nom_fichier_csv, mode='w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerows(liste)

    return None
