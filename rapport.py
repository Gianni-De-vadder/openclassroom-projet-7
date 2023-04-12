import argparse
import pandas as pd

# Analyse des arguments en ligne de commande
parser = argparse.ArgumentParser(description="Analyse de fichiers CSV.")
parser.add_argument("fichier_csv", type=str, help="nom du fichier CSV à analyser")
args = parser.parse_args()

# Lecture du fichier CSV
df = pd.read_csv(
    args.fichier_csv, sep=",", header=None, names=["id", "cout", "benefice"]
)

# Nombre total d'actions
total_actions = df.shape[0]
print("Nombre d'actions : ", total_actions)

# Nombre d'actions avec un coût inférieur ou égal à 0
actions_cout_inf_0 = df[df["cout"] <= 0].shape[0]
print("Nombre d'actions avec un coût inférieur ou égal à 0 : ", actions_cout_inf_0)

# Nombre d'actions avec un bénéfice inférieur ou égal à 0
actions_benef_inf_0 = df[df["benefice"] <= 0].shape[0]
print("Nombre d'actions avec un bénéfice inférieur ou égal à 0 : ", actions_benef_inf_0)

# Pourcentage de données exploitables après traitement
pourcentage_donnees_exploitables = (
    (total_actions - actions_cout_inf_0 - actions_benef_inf_0) / total_actions
) * 100
print(
    "Pourcentage de données exploitables après traitement : {:.2f}%".format(
        pourcentage_donnees_exploitables
    )
)
