import csv


def list_to_csv(liste):

    nom_fichier_csv = 'donnees.csv'

    liste.insert(0, ["Prospect", "Contact", "Adresse",
                     "Site", "Choix", "Raison"])
    with open(nom_fichier_csv, mode='w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerows(liste)
