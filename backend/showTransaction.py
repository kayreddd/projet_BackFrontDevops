import sqlite3

def showTransaction(transaction_id, user_id):
    try:
         
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT * FROM transaction2 WHERE id = ? AND (sender_id = ? OR receveur_id = ?)  ",(transaction_id, user_id, user_id))
        rows = cursor.fetchone()
        print(rows)
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "Aucune transaction trouvée pour cet utilisateur."}

        # Retourner les données sous forme de liste de dictionnaires
        return (rows)
    
    except Exception as e:
        return {"error": str(e)}