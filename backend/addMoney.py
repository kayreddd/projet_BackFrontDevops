import sqlite3


def addMoney(id_compte, montant):
    try:
         
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()
        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT money, statut_compte FROM compte WHERE id = ?" , (id_compte,))
        rows = cursor.fetchone()

        # Si la table est vide
        if not rows:
            return {"message": f"Compte avec id {id_compte} introuvable."}
        if rows[1] == "closed":
            return("le compte auquel vous souhaitez envoyé de l'argent est fermé")
        if (int(montant) > 0):
            money = int(rows[0]) + int(montant)

            # Mettre à jour la valeur de 'money' dans la table
            cursor.execute("UPDATE compte SET money = ? WHERE id = ?", (money, id_compte))
            cursor.execute("""
            INSERT INTO historic (id_user, type_transaction, valeur_transaction) 
            VALUES (?, ?, ?)
            """, (id_compte, "dépot", montant))
            conn.commit()
            conn.close()
            # Retourner les données sous forme de liste de dictionnaires
            return {"message": f"Montant ajouté avec succès. Nouveau solde: {money}"}
        return {"message": f"Montant négatif, impossible d'ajouter de l'argent sur votre compte"}
    
    except Exception as e:
        return {"error": str(e)}
