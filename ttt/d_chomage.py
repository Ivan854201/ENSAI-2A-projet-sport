import pandas as pd  # Ajout de l'importation de pandas

def donnees_chomage(url):
    donnees_chomage = pd.read_excel(url)
    donnees_chomage = donnees_chomage.iloc[3:99, [0, 2]]
    donnees_chomage = donnees_chomage.rename(columns={donnees_chomage.columns[0]: 'code', donnees_chomage.columns[1]:                             'Taux_chomage_2024'})
    return donnees_chomage