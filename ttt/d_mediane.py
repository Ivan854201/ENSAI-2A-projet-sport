import pandas as pd
import os
from extraire_url_zip import extract_zip_from_url

def donnees_mediane(url, extract_path, folder_path):
    # Exemple de traitement avec ces arguments
    print(f"URL : {url}")
    print(f"Extract Path : {extract_path}")
    print(f"Folder Path : {folder_path}")
    # Appel de la fonction
    extract_zip_from_url(url, extract_path)
    # Liste des fichiers chargés
    #for f in os.listdir(folder_path):
    #    print(f)
    # Charger le fichier Excel en utilisant le chemin complet
    file_path = os.path.join(folder_path, 'base-cc-filosofi-2020-geo2023.xlsx')
    donnees_mediane = pd.read_excel(file_path, sheet_name='DEP')
    donnees_mediane = donnees_mediane.iloc[5:101, [0,4,5,6,15,28]]
    donnees_mediane = donnees_mediane.rename(columns={
        donnees_mediane.columns[0]: 'code',
        donnees_mediane.columns[1]: 'Mediane_nivvie',
        donnees_mediane.columns[2]: 'Part_menages_fiscaux_imposes',
        donnees_mediane.columns[3]: 'Taux_pauvrete',
        donnees_mediane.columns[4]: 'Part_des_revenus_dactivite',
        donnees_mediane.columns[5]: 'Rapport_interdecile'})
    return donnees_mediane