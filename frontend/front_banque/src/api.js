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