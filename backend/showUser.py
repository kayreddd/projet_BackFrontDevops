import sqlite3

def showUser(id_user):
    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT mail FROM user WHERE id = ?", (id_user))
        
        rows = cursor.fetchall()
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "La table 'compte' est vide."}

        # Retourner les données sous forme de liste de dictionnaires
        return {"accounts": [{"mail": row[0]} for row in rows]}
    
    except Exception as e:
        return {"error": str(e)}
