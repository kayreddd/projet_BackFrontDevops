import sqlite3

def close_account(account_id):
    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Vérifier si le compte existe
        cursor.execute("SELECT * FROM compte WHERE id = ?", (account_id,))
        account = cursor.fetchone()
        if not account:
            return {"error": "Le compte n'existe pas."}

        # Vérifier si le compte est le compte principal
        cursor.execute("SELECT id FROM compte WHERE id_user = ? ORDER BY id ASC LIMIT 1", (account[2],))
        main_account = cursor.fetchone()
        if main_account and main_account[0] == account_id:
            return {"error": "Le compte principal ne peut pas être clôturé."}

        # Vérifier s'il y a des transactions en cours (hypothèse : vérifier dans la table des transactions)
        cursor.execute("""
            SELECT COUNT(*) 
            FROM transaction2 
            WHERE (id_sender = ? OR id_receveur = ?) AND type_transaction = 'en cours'
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