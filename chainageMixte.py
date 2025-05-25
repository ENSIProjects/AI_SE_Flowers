# Données initiales (faits)
BFE = {
    "type": "succulente",
    "saison": "hiver",
    "sol": "drainant",
    "humidite": "faible",
    "lumiere": "indirecte"
}

PPB = ["determiner_arrosage", "generer_alertes", "generer_precautions"]
PLAN = []

# Règles simplifiées (déclaratives)
REGLES = {
    "classification": {
        "succulente": "classe = succulente",
        "cactus": "classe = cactus",
        "tropicale": "classe = tropicale"
    },
    "arrosage_ete": {
        "succulente": "1 fois/semaine",
        "cactus": "1 fois/2 semaines"
    },
    "ajustement_hiver": {
        "1 fois/semaine": "1 fois/2 semaines",  # Supposons un ajustement
        "2 fois/semaine": "1 fois/semaine"
    },
    "alertes": [
        lambda bfe: "Sol trop sec !" if bfe["sol"] == "drainant" and bfe["humidite"] == "faible" else None,
        lambda bfe: "Lumière insuffisante !" if bfe["lumiere"] != "directe" and bfe["type"] in ["succulente", "cactus"] else None
    ]
}


def resoudre(ppb, bfe, plan):
    if not ppb:
        return True

    pb = ppb.pop(0)

    if pb == "determiner_arrosage":
        type_plante = bfe["type"]
        classe = REGLES["classification"].get(type_plante)
        if not classe:
            return False
        plan.append(f"Classification : {classe}")
        bfe["classe"] = classe.split(" = ")[1]

        frequence = REGLES["arrosage_ete"].get(bfe["classe"])
        if not frequence:
            return False
        plan.append(f"Arrosage été : {frequence}")

        if bfe["saison"] == "hiver":
            ajust = REGLES["ajustement_hiver"].get(frequence)
            if ajust:
                plan.append(f"Arrosage ajusté pour hiver : {ajust}")
            else:
                plan.append(f"Arrosage inchangé pour hiver : {frequence}")

        return resoudre(ppb, bfe, plan)

    elif pb == "generer_alertes":
        for regle in REGLES["alertes"]:
            alerte = regle(bfe)
            if alerte:
                plan.append(f"Alerte : {alerte}")
        return resoudre(ppb, bfe, plan)

    elif pb == "generer_precautions":
        if bfe.get("classe") == "tropicale":
            plan.append("Précaution : Éviter les courants d'air")
        if bfe.get("classe") == "fleur_d_exterieur" and bfe["saison"] == "hiver":
            plan.append("Précaution : Rentrer la plante en hiver")
        return resoudre(ppb, bfe, plan)

    return False


# Exécution
if resoudre(PPB, BFE, PLAN):
    print("succes !")
    print("\nPLAN GÉNÉRÉ :")
    for action in PLAN:
        print("-", action)
else:
    print("echec.")


