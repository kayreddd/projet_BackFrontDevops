import sqlite3

def showAccount(id_user):
    try:
         
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT * FROM compte WHERE id_user = ? ORDER BY date_creation DESC" , (id_user))
        rows = cursor.fetchall()
        print(rows)
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "La table 'compte' est vide."}

        # Retourner les données sous forme de liste de dictionnaires
        return {"accounts": [{"id": row[0], "money": row[1], "id_user": row[2], "date_creation":row[3], "type_de_compte":row[4]} for row in rows]}

    
    except Exception as e:
        return {"error": str(e)}
