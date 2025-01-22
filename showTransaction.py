import sqlite3

def showTransaction(account_id):
    try:
         
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT * FROM transaction2 WHERE id_sender= ? ORDER BY date_transaction",(str(account_id)))
        rows = cursor.fetchall()
        print(rows)
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "La table 'compte' est vide."}

        # Retourner les données sous forme de liste de dictionnaires
        return (rows)
    
    except Exception as e:
        return {"error": str(e)}