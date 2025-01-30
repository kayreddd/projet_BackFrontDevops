import { useState, useEffect } from "react";

export default function TransactionForm() {
  const [formData, setFormData] = useState({
    montant: "",
    id_receveur: "",
    statut: "",
    message: "",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [beneficiaires, setBeneficiaires] = useState([]);

  // Remplace par l'ID de l'utilisateur connecté (ex: stocké dans le state global)
  const id_user = 1;

  useEffect(() => {
    // Récupérer la liste des bénéficiaires de l'utilisateur
    const fetchBeneficiaires = async () => {
      try {
        const response = await fetch("http://localhost:8000/show_beneficiare", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ id_user }),
        });

        if (!response.ok) {
          throw new Error("Erreur lors de la récupération des bénéficiaires");
        }

        const data = await response.json();
        setBeneficiaires(data.accounts || []);
      } catch (error) {
        console.error("Erreur:", error);
        setError("Impossible de récupérer les bénéficiaires");
      }
    };

    fetchBeneficiaires();
  }, [id_user]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/create_transaction", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          montant: parseFloat(formData.montant),
          id_sender: id_user,
          id_receveur: parseInt(formData.id_receveur),
          statut: formData.statut,
          message: formData.message,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Erreur lors de l'envoi des données");
      }

      alert("Transaction créée avec succès");

      // Réinitialisation du formulaire
      setFormData({
        montant: "",
        id_receveur: "",
        statut: "",
        message: "",
      });
    } catch (error) {
      console.error("Erreur:", error);
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4 p-4 border rounded-lg w-96 mx-auto mt-10">
      <input type="hidden" name="id_sender" value={id_user} />
      
      <input type="number" name="montant" placeholder="Montant" value={formData.montant} onChange={handleChange} className="border p-2 rounded" required />

      {/* Sélection des bénéficiaires */}
      <select name="id_receveur" value={formData.id_receveur} onChange={handleChange} className="border p-2 rounded" required>
        <option value="">Sélectionnez un bénéficiaire</option>
        {beneficiaires.map((b) => (
          <option key={b.id} value={b.id_beneficiaire}>
            {b.name_beneficiare} (ID: {b.id_beneficiaire})
          </option>
        ))}
      </select>

      <input type="text" name="statut" placeholder="Statut" value={formData.statut} onChange={handleChange} className="border p-2 rounded" required />
      
      <textarea name="message" placeholder="Message" value={formData.message} onChange={handleChange} className="border p-2 rounded" required />

      {error && <p className="text-red-500">{error}</p>}

      <button type="submit" disabled={loading} className="bg-blue-500 text-white p-2 rounded">
        {loading ? "Envoi en cours..." : "Envoyer"}
      </button>
    </form>
  );
}
