import { useEffect, useState } from "react";
// import { getTransactions } from "./api";
import { getAllTransactions } from "./api"; // import de la fonction pour recup toutes les transactions
import { FaShoppingCart, FaArrowUp, FaArrowDown, FaSearch } from "react-icons/fa";
import { useNavigate } from 'react-router-dom'; // Import du hook useNavigate
import { useLocation } from "react-router-dom";
import { cancelTransaction } from './api';
import './transaction.css';

const Transactions = () => {
  const [transactions, setTransactions] = useState([]);
  const [searchTransaction, setSearchTransaction] = useState("");
  const [filterType, setFilterType] = useState("all");
  const [cancelToast, setCancelToast] = useState(null); // Gérer l'affichage du toast
  const [tempTransaction, setTempTransaction] = useState(null); // Ajouté pour stocker temporairement l'état de la transaction avant modification
  const navigate = useNavigate(); // Hook pour la navigation
  const location = useLocation();
  const userId = location.state?.id || "Aucun ID reçu";
  console.log(userId);
  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const data = await getAllTransactions(userId);
        if (data) {
          setTransactions(Array.isArray(data) ? data : [data]); // Convertir en tableau si nécessaire
        }
      } catch (error) {
        console.error("Erreur lors de la récupération des transactions :", error);
      }
    };

    fetchTransactions();
  }, [userId]);

  // Filtrage des transactions selon l'onglet actif
  const filteredTransactions = transactions.filter((t) => {
    if (filterType === "income" && t.value <= 0) return false;
    if (filterType === "expense" && t.value >= 0) return false;
    return t.message.toLowerCase().includes(searchTransaction.toLowerCase()); // Filtrage par recherche
  });

  // Séparer les transactions en deux catégories : "en cours" et "done"
  const pendingTransactions = filteredTransactions.filter(t => t.etat === "pending");
  const doneTransactions = filteredTransactions.filter(t => t.etat === "done");

  // Fonction pour annuler une transaction (avec délai de confirmation)
  const handleCancelTransaction = async (transactionId, userId) => {

    // Sauvegarder l'état de la transaction avant tentative d'annulation
    const transactionToCancel = transactions.find(t => t.id === transactionId);
    setTempTransaction(transactionToCancel);

    try {  
      // Appel API pour mettre à jour en "cancel"
      await cancelTransaction(transactionId, userId);
  
      // ✅ Mettre à jour localement l'état de la transaction
      setTransactions(prev => prev.map(t =>
        t.id === transactionId ? { ...t, etat: "cancel" } : t
      ));
  
      // ✅ Afficher le toast
      setCancelToast({
        id: transactionId,
        timeout: setTimeout(() => {
          setCancelToast(null);
        }, 5000),
      });
    } catch (error) {
      console.error("Erreur lors de l'annulation :", error);
      // Rétablir la transaction en cas d'échec
      setTransactions(prev => prev.map(t =>
        t.id === transactionId ? tempTransaction : t  // Restaurer l'état initial de la transaction
      ));
    }
  };  

   // Annuler l'annulation (garder la transaction)
   const undoCancel = () => {
    if (cancelToast) {
      clearTimeout(cancelToast.timeout);
      setCancelToast(null);

      // Restaurer l'état de la transaction si l'utilisateur annule
      if (tempTransaction) {
        setTransactions(prev => prev.map(t =>
          t.id === tempTransaction.id ? tempTransaction : t
        ));
      }
    }
  };

  return (
    <div className="transactions-container">
      <h2>Mes Transactions</h2>
      <div className="search-bar">
        <FaSearch className="search-icon" />
        <input
          type="text"
          placeholder="Rechercher une transaction..."
          value={searchTransaction}
          onChange={(e) => setSearchTransaction(e.target.value)}
        />
      </div>

      {/* Onglets pour filtrer les transactions */}
      <div className="tabs">
        <button
          className={filterType === "all" ? "active" : ""}
          onClick={() => setFilterType("all")}
        >
          Transactions
        </button>
        <button
          className={filterType === "income" ? "active" : ""}
          onClick={() => setFilterType("income")}
        >
          Recettes <FaArrowUp className="icon-income" />
        </button>
        <button
          className={filterType === "expense" ? "active" : ""}
          onClick={() => setFilterType("expense")}
        >
          Dépenses <FaArrowDown className="icon-expense" />
        </button>
      </div>
      {/* Transactions en cours */}
      <div className="transactions-list">
        {pendingTransactions.length > 0 && (
          <div>
            <h3>Transactions en cours</h3>
            {pendingTransactions.map((t, index) => (
              <div key={index} className="transaction-item">
                <FaShoppingCart className="icon" />
                <div className="transaction-content">
                  <div className="transaction-details">
                    <div className="transaction-name">{t.message}</div>
                    <div className="transaction-type">{t.type}</div>
                  </div>
                  <div className={`transaction-value ${t.value > 0 ? "positive" : "negative"}`}>
                    {t.value} €
                  </div>
                  <button className="cancel-btn" onClick={() => handleCancelTransaction(t.id, t.id_user)}>Annuler</button>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Transactions terminées */}
        {doneTransactions.length > 0 && (
          <div>
            <h3>Transactions terminées</h3>
            {doneTransactions.map((t, index) => (
              <div key={index} className="transaction-item">
                <FaShoppingCart className="icon" />
                <div className="transaction-content">
                  <div className="transaction-details">
                    <div className="transaction-name">{t.message}</div>
                    <div className="transaction-type">{t.type}</div>
                  </div>
                  <div className={`transaction-value ${t.value > 0 ? "positive" : "negative"}`}>
                    {t.value} €
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Bouton pour créer une transaction */}
      {/* <div className="test">
        <button onClick={() => navigate('/transaction_form')}>Créer une transaction</button>
      </div> */}

      {/* Message si aucune transaction */}
      {pendingTransactions.length === 0 && doneTransactions.length === 0 && (
        <p>Aucune transaction trouvée.</p>
      )}

      {/* Toast d'annulation */}
      {cancelToast && (
        <div className="toast">
          <p>Annulation de la transaction en cours...</p>
          <button onClick={undoCancel}>Annuler l'annulation</button>
        </div>
      )}
    </div>
  );
};

export default Transactions;
