# 🩺 Calculateur IMC — App Web

> Application web de calcul d'IMC basée sur les standards OMS.  
> Par **Emmanuel SAVI** — Infirmier & Développeur HealthTech

---

## 🗺️ Étape 0 : Avoir l'idée

Transformer un simple script Python de calcul d'IMC en une vraie application web avec une API et une interface utilisateur propre.

---

## 📐 Étape 1 : Construire le schéma du projet

```
app_imc/
├── backend/
│   ├── calculator.py   # Logique IMC pure
│   ├── models.py       # Schémas Pydantic
│   ├── main.py         # Serveur FastAPI
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

**Stack choisie :**
- Backend : FastAPI + Python
- Frontend : HTML / CSS / JS vanilla

---

## ⚙️ Étape 2 : Créer le backend

### `calculator.py` — La fonction principale
Contient la logique IMC pure, sans aucune dépendance à FastAPI.  
Testable indépendamment depuis le terminal.

```python
python -c "from calculator import calculer_imc; print(calculer_imc(70, 175))"
```

### `models.py` — Les schémas Pydantic
Définit ce que l'API **reçoit** (poids + taille) et ce qu'elle **renvoie** (imc + catégorie + conseil).

### `main.py` — Le serveur FastAPI
Branche la logique sur une route HTTP :  
`POST /calculer` → reçoit les données → appelle `calculer_imc()` → retourne le résultat en JSON.

---

## 🎨 Étape 3 : Créer le frontend

Interface utilisateur moderne inspirée des apps santé cliniques.

- Police **Inter** (Google Fonts)
- Dégradé bleu médical `#0f4c81 → #1a8fe3 → #38c9b0`
- Couleurs dynamiques selon la catégorie OMS :
  - 🟡 **Maigreur** — `#f59e0b`
  - 🟢 **Poids normal** — `#10b981`
  - 🟠 **Surpoids** — `#f97316`
  - 🔴 **Obésité** — `#ef4444`

---

## 🚀 Étape 4 : Déploiement

| Composant | Plateforme | Statut |
|---|---|---|
| Backend FastAPI | Render | ✅ |
| Frontend HTML/CSS/JS | Netlify | ✅ |

---

## 🏁 Lancer le projet en local

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
# Ouvrir index.html dans le navigateur
```

---

## 👤 Auteur

**Emmanuel SAVI**  
Infirmier Diplômé d'État | HealthTech & IA  
*"Je suis le pont entre le professionnel de santé d'aujourd'hui et celui de demain"*
