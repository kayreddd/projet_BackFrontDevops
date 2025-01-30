from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Importer les fonctions nécessaires
from createAccount import create_account
from createUser import create_user
from showUser import showUser
from showAccount import showAccount
from addMoney import addMoney
from transaction import create_transaction
from transaction import updateTransaction
from showTransaction import showTransaction
from showTransaction import showAllTransaction
from closeAccount import close_account
from showBeneficiaire import addBeneficiaire
from showBeneficiaire import showBeneficiaire

app = FastAPI()

# Configuration CORS
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",  # Ajouté pour le frontend sur le port 5173
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles Pydantic pour la validation des données
class CompteCreate(BaseModel):
    id_user: int
    type_de_compte: str

class UserCreate(BaseModel):
    mail: str
    password: str

class TransactionCreate(BaseModel):
    montant: int
    id_sender: int
    id_receveur: int
    statut: str
    message: str

class BeneficiaireCreate(BaseModel):
    name_beneficiaire: str
    id_beneficiaire: str

class AccountRequest(BaseModel):
    id_user: int

class AddMoneyRequest(BaseModel):
    id_compte: int
    montant: int

# Route principale
@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.post("/create_account")
async def create_account_route(compte: CompteCreate):
    try:
        # Appeler la fonction create_account en utilisant await
        result = await create_account(compte)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour créer un utilisateur
@app.post("/create_user")
async def create_user_route(user: UserCreate):
    try:
        result = create_user(user)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour afficher les comptes d'un utilisateur
@app.post("/show_accounts")
async def show_accounts(request: AccountRequest):
    try:
        # Appeler la fonction showAccount en passant l'id utilisateur récupéré
        result = showAccount(request.id_user)
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        
        return result  # Renvoie les comptes de l'utilisateur
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erreur interne du serveur")


@app.post("/show_user")
async def get_user(id_user: int):
    try:
        result = showUser(id_user)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route pour ajouter de l'argent à un compte
@app.post("/add_money")
async def add_money_route(request: AddMoneyRequest):
    try:
        result = addMoney(request.id_compte, request.montant)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour créer une transaction
@app.post("/create_transaction")
async def create_transaction_route(transaction: TransactionCreate):
    try:
        result = create_transaction(transaction)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour mettre à jour une transaction
@app.post("/update_transaction")
async def update_transaction_route():
    try:
        result = updateTransaction()
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour afficher une transaction
@app.post("/show_transaction")
async def get_transaction(transaction_id: int, count_id: int):
    try:
        result = showTransaction(transaction_id, count_id)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour afficher toutes les transactions
@app.post("/show_all_transaction")
async def get_all_transaction(account_id: int):
    try:
        result = showAllTransaction(account_id)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour fermer un compte
@app.post("/close_account")
async def get_close_account(account_id: int):
    try:
        result = close_account(account_id)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour ajouter un bénéficiaire
@app.post("/add_beneficiaire")
async def add_beneficiaire_route(beneficiaire: BeneficiaireCreate, id_user: int):
    try:
        result = addBeneficiaire(beneficiaire.name_beneficiaire, beneficiaire.id_beneficiaire, id_user)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route pour afficher les bénéficiaires
@app.post("/show_beneficiare")
async def get_beneficiaire(id_user: int):
    try:
        result = showBeneficiaire(id_user)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Pour lancer le serveur uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

#pour que la fonction ne s'execute que toutes les 10 sec auto

# @app.on_event("startup")
# async def start_background_task():
#     asyncio.create_task(run_update_transaction_periodically())


# async def run_update_transaction_periodically():
#     while True:
#         result = await updateTransaction()  # Appelle la fonction
#         if "error" in result:
#             print(f"Erreur : {result['error']}")
#         else:
#             print("Mise à jour réussie.")
#         await asyncio.sleep(10)  # Attends 10 secondes avant de recommencer