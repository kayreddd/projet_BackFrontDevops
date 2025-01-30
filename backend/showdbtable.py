import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Nom de la table pour laquelle vous voulez obtenir les informations
table_name = 'historic'

# Exécuter la commande pour obtenir les informations des colonnes
cursor.execute(f"PRAGMA table_info({table_name});")

# Récupérer les résultats
columns = cursor.fetchall()

# Afficher les informations des colonnes
print(f"Colonnes de la table '{table_name}' :")
for column in columns:
    print(f"Nom de la colonne : {column[1]}, Type : {column[2]}")

# Fermer la connexion
conn.close()
