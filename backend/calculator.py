def calculer_imc (poids: float , taille_cm : float) -> dict : 

    taille_m = taille_cm/100
    imc = poids / (taille_m **2)
    imc = round(imc, 2)
    if imc < 18.5 : 
      categorie = "Maigreur"
      conseil = "Votre Poids est insufissant. Consultez un professionnel de santé"
    elif imc < 25 : 
      categorie = "Poids Normal"
      conseil = "Votre Poids est idéal . Maintenez  vos bonnes habitudes. "
    elif imc < 30: 
      categorie = "Surpoids"
      conseil = "Un suivie nutritionnel peut ètre bénéfique "
    else : 
      categorie = "Obésité"
      conseil = "Consultez un médécin pour un accompagnement adapté "

    return {
        "imc" : imc,
        "categorie" : categorie,
        "conseil" : conseil
    }

