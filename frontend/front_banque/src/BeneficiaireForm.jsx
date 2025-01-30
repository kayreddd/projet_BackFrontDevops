import { useState } from "react";

export default function BeneficiaireForm() {
  const [formData, setFormData] = useState({
    name_beneficiaire: "",
    id_beneficiaire: "",
    id_user: 1, // Valeur par défaut
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/add_beneficiaire", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name_beneficiaire: formData.name_beneficiaire,
          id_beneficiaire: parseInt(formData.id_beneficiaire), // Convertir en nombre
          id_user: formData.id_user, // Utiliser la valeur par défaut
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Erreur lors de la création du bénéficiaire");
      }

      const data = await response.json();
      console.log("Réponse de l'API:", data);
      alert("Bénéficiaire créé avec succès");

      // Réinitialisation du formulaire (sauf id_user)
      setFormData({
        name_beneficiaire: "",
        id_beneficiaire: "",
        id_user: 1, // Conserver la valeur par défaut
      });
    } catch (error) {
      console.error("Erreur:", error);
      setError(error.message);
      alert("Échec de la création du bénéficiaire: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4 p-4 border rounded-lg w-96 mx-auto mt-10">
      <input
        type="text"
        name="name_beneficiaire"
        placeholder="Nom du bénéficiaire"
        value={formData.name_beneficiaire}
        onChange={handleChange}
        className="border p-2 rounded"
        required
      />
      <input
        type="number"
        name="id_beneficiaire"
        placeholder="ID du bénéficiaire"
        value={formData.id_beneficiaire}
        onChange={handleChange}
        className="border p-2 rounded"
        required
      />
      <input
        type="hidden" // Champ caché
        name="id_user"
        value={formData.id_user}
      />
      {error && <p className="text-red-500 text-sm">{error}</p>}
      <button
        type="submit"
        disabled={loading}
        className="bg-blue-500 text-white p-2 rounded disabled:bg-gray-400"
      >
        {loading ? "Création en cours..." : "Créer un bénéficiaire"}
      </button>
    </form>
  );
}