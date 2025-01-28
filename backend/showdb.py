import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("my_database.db")  # Remplacez par le nom de votre base de données

# Créer un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

# Récupérer toutes les lignes de la table 'compte'
try:
    cursor.execute("SELECT * FROM transaction2")
    rows = cursor.fetchall()  # Récupérer toutes les lignes
    
    # Afficher les données
    if rows:
        print("Contenu de la table 'historic' :")
        for row in rows:
            print(row)
    else:
        print("La table 'historic' est vide.")
except sqlite3.Error as e:
    print(f"Erreur lors de l'accès à la table : {e}")

# Fermer la connexion
conn.close()
