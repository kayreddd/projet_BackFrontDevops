import { useEffect, useState } from "react";
// import { getTransactions } from "./api";
import { getAllTransactions } from "./api"; // import de la fonction pour recup toutes les transactions
import { FaShoppingCart } from "react-icons/fa";
import './transaction.css'

const Transactions = ({ userId }) => {
  const [transactions, setTransactions] = useState([]);

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

  return (
    <div className="transactions-container">
      <h2>Mes Transactions</h2>
      <div className="transactions-list">
        {transactions.map((t, index) => (
          <div key={index} className="transaction-item">
            <FaShoppingCart className="icon" />
            <div className="transaction-content">
              <div className="transaction-details">
                <span className="transaction-type">{t.type}</span>
              </div>
              <div className="transaction-value">{t.value} €</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Transactions;
