from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import random

app = FastAPI()

# Fonction pour générer un IBAN aléatoire
def generate_iban():
    country_code = "FR"
    bank_code = "30003"
    branch_code = "01234"
    account_number = "".join(str(random.randint(0, 9)) for _ in range(11))
    rib_key = str(random.randint(10, 99))
    return f"{country_code}{bank_code}{branch_code}{account_number}{rib_key}"

# Définir un modèle Pydantic pour la validation des données d'entrée
class CompteCreate(BaseModel):
    id_user: int
    type_de_compte: str

# Fonction pour créer un compte dans la base de données
def create_account_in_db(compte: CompteCreate):
    try:
        iban = generate_iban()  # Générer un IBAN
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Créer un compte dans la base de données
        cursor.execute("""
        INSERT INTO compte (money, id_user, statut_compte, iban) 
        VALUES (?, ?, ?, ?)
        """, (0, compte.id_user, compte.type_de_compte, iban))
        conn.commit()
        conn.close()

        return {"message": f"Compte créé avec succès! IBAN: {iban}", "iban": iban}

    except Exception as e:
        return {"error": str(e)}

# Route FastAPI pour créer un compte
@app.post("/create_account")
async def create_account(request: CompteCreate):
    response = create_account_in_db(request)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response