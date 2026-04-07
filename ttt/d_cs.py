import pandas as pd
import os

def donnees_cs(url):
    donnees_cs = pd.read_excel('https://www.insee.fr/fr/statistiques/fichier/2012721/TCRD_014.xlsx')
    donnees_cs = donnees_cs.iloc[3:99, [0,2,3,4,5,6,7]]
    donnees_cs = donnees_cs.rename(columns={donnees_cs.columns[0]: 'code',
                                            donnees_cs.columns[1]: 'cs_agri',
                                            donnees_cs.columns[2]: 'cs_arti',
                                            donnees_cs.columns[3]: 'cs_cadr',
                                            donnees_cs.columns[4]: 'cs_inte',
                                            donnees_cs.columns[5]: 'cs_empl',
                                            donnees_cs.columns[6]: 'cs_ouvr'})
    return donnees_cs