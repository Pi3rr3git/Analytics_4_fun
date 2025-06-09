import pandas as pd

# Charger le fichier CSV
df = pd.read_csv(r"C:\perso\Moi\data_analysis\club-analyzer.csv")

# Compter le nombre de joueurs pour chaque note générale
rating_counts = df["Rating"].value_counts().sort_index()
unique_locations = df["Location"].unique()

# print(unique_locations)
# Afficher les résultats
print(rating_counts)
