import React, { useState, useEffect } from 'react';
import axios from 'axios';  // Importation d'Axios
import { useNavigate } from 'react-router-dom'; // Import du hook useNavigate
import CreateAccount from './CreateAccount';
import './Accounts.css';  // Importation du CSS



function Accounts() {
  const [accounts, setAccounts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate(); // Hook pour la navigation

  useEffect(() => {
    const fetchAccounts = async () => {
      setLoading(true);
      try {
        const response = await axios.post("http://127.0.0.1:8000/show_accounts", {
          id_user: 2,  // on remplace par un ID utilisateur valide
        });

        if (response.data && response.data.accounts) {
          // Vérification de la présence des données
          console.log(response.data.accounts);
          const formattedAccounts = response.data.accounts.map((account) => ({
            id: account.id,
            money: account.money,
            id_user: account.id_user,
            type_de_compte: account.type_de_compte,
            iban: account.iban,
          }));

          setAccounts(formattedAccounts);  // Mise à jour de l'état avec les comptes formatés
        } else {
          throw new Error("Format de la réponse incorrect");
        }
      } catch (error) {
        setError(error.message || "Erreur lors de la récupération des comptes");
      } finally {
        setLoading(false);
      }
    };

    fetchAccounts();
  }, []);

  // Calcul du total des actifs
  const totalAssets = accounts.reduce((total, account) => total + account.money, 0);

  return (
    <div className="App">
      <header>
        
        <h1>Mes Comptes</h1>
        <h2 className="total-assets">Total des actifs : {totalAssets} €</h2>
      </header>
      <main>
        {loading ? (
          <p>Chargement des comptes...</p>
        ) : error ? (
          <p className="error">Erreur : {error}</p>
        ) : (
          <div className="account-container">
            {accounts.length === 0 ? (
              <p>Aucun compte trouvé.</p>
            ) : (
              accounts.map((account) => (
                <div key={account.iban} className="account-card">
                  <h2>{account.type_de_compte}</h2>
                  <p><strong>IBAN :</strong> {account.iban}</p>
                  <p><strong>Solde :</strong> {account.money} €</p>
                  <button onClick={() => navigate('/transactions', { state: { id: account.id } })}>
                    Créer une transaction
                  </button>
                  <button onClick={() => alert('Le compte va être cloturer')}>
                    Cloturer le compte
                  </button>
                </div>
              ))
            )}
          </div>
        )}
        <div className="create-account-section">
          <h2>Créer un Nouveau Compte</h2>
          <CreateAccount />
        </div>
      </main>
    </div>
    
  );
}

export default Accounts;