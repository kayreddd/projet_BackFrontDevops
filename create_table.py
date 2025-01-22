import sqlite3

# Connexion à la base de données (crée le fichier s'il n'existe pas)
conn = sqlite3.connect("my_database.db")

# Créer un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

#Commande SQL pour créer une table
cursor.execute("""
CREATE TABLE transaction2 (
    id INTEGER PRIMARY KEY,
    id_sender INTEGER,
    id_receveur INTEGER,
    type_transaction VARCHAR,
    valeur_transaction INTEGER,
    message VARCHAR,
    date_transaction DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# cursor.execute('DROP TABLE IF EXISTS "transaction2"')


# Sauvegarder les changements et fermer la connexion
conn.commit()
conn.close()

print("Table supprimé avec succès.")
