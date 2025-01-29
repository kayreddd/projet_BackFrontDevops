import sqlite3

# Connexion à la base de données (crée le fichier s'il n'existe pas)
conn = sqlite3.connect("my_database.db")

# Créer un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

#Commande SQL pour créer une table

# cursor.execute("""
# CREATE TABLE compte (
#     id INTEGER PRIMARY KEY,
#     money INTEGER,
#     id_user INTEGER,
#     date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
#     statut_compte VARCHAR         
# )
# """)

cursor.execute('DROP TABLE IF EXISTS "compte"')

cursor.execute("""
CREATE TABLE compte (
    id INTEGER PRIMARY KEY,
    money INTEGER,
    id_user INTEGER,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
    statut_compte VARCHAR,
    iban INTEGER
)
""")


# Sauvegarder les changements et fermer la connexion
conn.commit()
conn.close()

print("Table supprimé avec succès.")
