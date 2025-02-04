import axios from "axios";

const API_URL = "http://localhost:8000"; // Port de FastAPI

// export const getTransactions = async (transactionId, userId) => {
//   try {
//     const response = await axios.get(`${API_URL}/transactions/${transactionId}/${userId}`);
//     return response.data;
//   } catch (error) {
//     console.error("Erreur lors de la récupération des transactions :", error);
//     return null;
//   }
// };

// Récupérer toutes les transactions d'un utilisateur
export const getAllTransactions = async (userId) => {
  try {
    const response = await axios.get(`${API_URL}/transactions/${userId}`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des transactions :", error);
    return [];
  }
};

// annuler une transaction 
export const cancelTransaction = async (transactionId, userId) => {
  try {
    console.log(`Annulation transaction: ID=${transactionId}, UserID=${userId}`);
    const response = await axios.put(`${API_URL}/cancel_transaction/${transactionId}/${userId}`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de l'annulation de la transaction :", error);
    throw error;
  }
};