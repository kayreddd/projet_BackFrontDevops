import { useState } from "react";

export default function UserForm() {
  const [formData, setFormData] = useState({
    mail: "",
    password: "",
    confirmPassword: "",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [confirmPasswordError, setConfirmPasswordError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });

    if (e.target.name === "password") {
      validatePassword(e.target.value);
    }

    if (e.target.name === "confirmPassword") {
      validateConfirmPassword(e.target.value);
    }
  };

  const validatePassword = (password) => {
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!regex.test(password)) {
      setPasswordError("Le mot de passe doit contenir au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial.");
    } else {
      setPasswordError("");
    }
  };

  const validateConfirmPassword = (confirmPassword) => {
    if (confirmPassword !== formData.password) {
      setConfirmPasswordError("Les mots de passe ne correspondent pas.");
    } else {
      setConfirmPasswordError("");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    if (passwordError || confirmPasswordError) {
      alert("Veuillez corriger les erreurs dans le formulaire.");
      setLoading(false);
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/create_user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          mail: formData.mail.toLowerCase(),
          password: formData.password, // Envoi uniquement le mot de passe principal
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Erreur lors de la création de l'utilisateur");
      }

      alert("Utilisateur créé avec succès");

      setFormData({ mail: "", password: "", confirmPassword: "" });
    } catch (error) {
      setError(error.message);
      alert("Échec de la création de l'utilisateur: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4 p-4 border rounded-lg w-96 mx-auto mt-10">
      <input
        type="email"
        name="mail"
        placeholder="Adresse email"
        value={formData.mail}
        onChange={handleChange}
        className="border p-2 rounded"
        required
      />
      <input
        type="password"
        name="password"
        placeholder="Mot de passe"
        value={formData.password}
        onChange={handleChange}
        className="border p-2 rounded"
        required
      />
      {passwordError && <p className="text-red-500 text-sm">{passwordError}</p>}
      
      <input
        type="password"
        name="confirmPassword"
        placeholder="Confirmer le mot de passe"
        value={formData.confirmPassword}
        onChange={handleChange}
        className="border p-2 rounded"
        required
      />
      {confirmPasswordError && <p className="text-red-500 text-sm">{confirmPasswordError}</p>}
      
      {error && <p className="text-red-500 text-sm">{error}</p>}
      
      <button
        type="submit"
        disabled={loading || passwordError || confirmPasswordError}
        className="bg-blue-500 text-white p-2 rounded disabled:bg-gray-400"
      >
        {loading ? "Création en cours..." : "Créer un utilisateur"}
      </button>
    </form>
  );
}
