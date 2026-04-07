import matplotlib.pyplot as plt

def carte_ecarts_departement(base, departement_borders, candidat):
    # Si besoin, on renomme la colonne du code département
    if "CODE_DEPT" in departement_borders.columns:
        departement_borders = departement_borders.rename(columns={"CODE_DEPT": "code"})
    
    if "INSEE_DEP" in departement_borders.columns:
        departement_borders = departement_borders.rename(columns={"INSEE_DEP": "code"})             
    
    # On garde seulement le candidat choisi
    df_candidat = base[base["candidat"].str.upper().str.contains(candidat.upper(), na=False)
    ].copy()
    
    # Si aucun candidat n'est trouvé
    if len(df_candidat) == 0:
        print("Aucun candidat trouvé")
        return
    
    # Jointure entre la carte et les données
    carte = departement_borders.merge(df_candidat, on="code_departement", how="left")
    
    # Affichage de la carte
    carte.plot(
        column="surrepresentation",
        cmap="RdBu_r",                       #code couleur bleu rouge blanc 
        legend=True,
        edgecolor="black", 
        linewidth=2,
        figsize=(10, 8)
    )
    
    plt.title(f"Surreprésentation de {candidat.title()}")
    plt.axis("off")
    plt.show()