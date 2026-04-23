document.getElementById("btn-calculer").addEventListener("click", async () => {

    const poids = parseFloat(document.getElementById("poids").value);
    const taille = parseFloat(document.getElementById("taille").value);

    if (!poids || !taille) {
        alert("Veuillez remplir les deux champs !");
        return;
    }

    const response = await fetch("https://imc-app-ackd.onrender.com/calculer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ poids: poids, taille_cm: taille })
    });

    const data = await response.json();

    document.getElementById("imc-valeur").textContent = data.imc;
    document.getElementById("conseil").textContent = data.conseil;

    const categorieEl = document.getElementById("categorie");
    categorieEl.textContent = data.categorie;

    // Couleur dynamique selon catégorie
    categorieEl.className = "";
    if (data.categorie === "Maigreur") {
        categorieEl.classList.add("cat-maigreur");
    } else if (data.categorie === "Poids Normal") {
        categorieEl.classList.add("cat-normal");
    } else if (data.categorie === "Surpoids") {
        categorieEl.classList.add("cat-surpoids");
    } else {
        categorieEl.classList.add("cat-obesite");
    }

    document.getElementById("resultat").style.display = "block";
});