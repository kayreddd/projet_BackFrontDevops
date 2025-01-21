import sqlite3

# Connexion à la base de données (crée le fichier s'il n'existe pas)
conn = sqlite3.connect("my_database.db")

# Créer un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

# Commande SQL pour créer une table
cursor.execute("""
CREATE TABLE historic (
    id INTEGER PRIMARY KEY,
    id_user INTEGER,
    type_transaction VARCHAR,
    valeur_transaction INTEGER    
)
""")

# Sauvegarder les changements et fermer la connexion
conn.commit()
conn.close()

print("Table créée avec succès.")
