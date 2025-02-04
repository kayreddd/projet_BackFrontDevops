from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
#import asyncio
from pydantic import BaseModel
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
from fastapi.middleware.cors import CORSMiddleware
from showTransaction import router as transaction_router
from transaction import cancel_transaction


app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurer Jinja2 pour les templates
# templates = Jinja2Templates(directory="template")

# Route pour afficher une page HTML
# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request, "title": "Page d'accueil"})
# Définir un modèle Pydantic pour la validation des données d'entrée


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Autoriser Vite.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routes de transactions
app.include_router(transaction_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

class CompteCreate(BaseModel):
    id_user: int
    type_de_compte: str

class UserCreate(BaseModel):
    mail: str
    password: str

class transactionCreate(BaseModel):
    montant: int
    id_sender: int
    id_receveur: int
    statut: str
    message: str

class BeneficiaireCreate(BaseModel):
    name_beneficiaire: str
    id_beneficiaire: int
    id_user: int

class UserRequest(BaseModel):
    id_user: int

# Route pour créer un compte
@app.post("/create_account")
async def create_account_route(compte: CompteCreate):
    try:
        # Appeler la fonction create_account depuis createAccount.py
        result = create_account(compte)  # On passe l'objet CompteCreate

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route pour créer un user
@app.post("/create_user")
async def create_user_route(user: UserCreate):
    try:
        # Appeler la fonction create_user_route depuis createUser.py
        result = create_user(user)  # On passe l'objet UserCreate

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/show_accounts")
async def get_accounts(user: UserRequest):
    # Connexion à la base de données
    result = showAccount(user)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès 

@app.post("/show_user")
async def get_user(id_user):
    # Connexion à la base de données
    result = showUser(id_user)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès 

# Route pour ajouter de l'argent à un compte
@app.post("/add_money")
async def add_money_route(id_compte, montant):
    try:
        # Appeler la fonction addMoney depuis addMoney.py
        result = addMoney(id_compte, montant)  # On passe les paramètre

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/create_transaction")
async def create_transaction_route(transaction: transactionCreate):
    try:
        # Appeler la fonction create_transaction depuis transaction.py
        result = create_transaction(transaction)  # On passe l'objet transactionCreate

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/update_transaction")
async def update_transaction_route():
    # Connexion à la base de données
    result = updateTransaction()
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès


@app.post("/show_transaction")
async def get_transaction(transaction_id, count_id):
    # Connexion à la base de données
    result = showTransaction(transaction_id, count_id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès

@app.post("/show_all_transaction")
async def get_all_transaction(account_id):
    # Connexion à la base de données
    result = showAllTransaction(account_id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès

@app.put("/cancel_transaction/{transaction_id}/{id_user}")
async def update_transaction_status(transaction_id: int, id_user: int):
    result = cancel_transaction(transaction_id, id_user)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès

@app.post("/close_account")
async def get_close_account(account_id):
    # Connexion à la base de données
    result = close_account(account_id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès


@app.post("/add_beneficiaire")
async def add_beneficiaire_route(beneficiaire: BeneficiaireCreate):
    try:
        result = addBeneficiaire(beneficiaire)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/show_beneficiare")
async def get_beneficiaire(user: UserRequest):
    # Connexion à la base de données
    result = showBeneficiaire(user.id_user)
    if "error" in   result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès

