import sqlite3

def close_account(account_id):
    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Vérifier si le compte existe
        cursor.execute("SELECT * FROM compte WHERE id = ? and statut_compte = ?", (account_id, "Secondaire"))
        account = cursor.fetchone()
        if not account:
            return {"error": "Le compte n'existe pas."}

        cursor.execute("SELECT id FROM compte WHERE id = ? and statut_compte = ?", (account_id, "Secondaire"))
        main_account = cursor.fetchone()
        # Vérifier s'il y a des transactions en cours (hypothèse : vérifier dans la table des transactions)
        cursor.execute("""
            SELECT COUNT(*) 
            FROM transaction2 
            WHERE (id_sender = ? OR id_receveur = ?) AND type_transaction = 'pending'
        """, (account_id, account_id))
        pending_transactions = cursor.fetchone()[0]
        if pending_transactions > 0:
            return {"error": "Le compte ne peut pas être clôturé car il y a des transactions en cours."}

        # Transférer le solde vers le compte principal
        current_balance = account[1]  # Solde actuel
        if current_balance > 0:
            cursor.execute("UPDATE compte SET money = money + ? WHERE id = ?", (current_balance, main_account[0]))

        # Clôturer le compte (marquer comme clôturé sans le supprimer de la base)
        cursor.execute("UPDATE compte SET money = 0, statut_compte = ? WHERE id = ?", ("closed", account_id,))

        # Sauvegarder les changements et fermer la connexion?
        conn.commit()
        conn.close()

        return {"message": f"Le compte {account_id} a été clôturé avec succès."}

    except Exception as e:
        return {"error": str(e)}