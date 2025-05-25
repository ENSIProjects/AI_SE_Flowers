# main.py

# --- Règles de base ---
REGLES = {
    "classification": {
        "succulente": "classe = succulente",
        "cactus": "classe = cactus",
        "tropicale": "classe = tropicale",
        "aromatique": "classe = aromatique",
        "fleur_d_interieur": "classe = fleur_d_interieur",
        "fleur_d_exterieur": "classe = fleur_d_exterieur"
    },
    "arrosage_ete": {
        "succulente": "1 fois/semaine",
        "fleur_d_interieur": "3 fois/semaine",
        "tropicale": "2 fois/semaine",
        "cactus": "1 fois/2 semaines",
        "aromatique": "Tous les 2 jours",
        "fleur_d_exterieur": "2-3 fois/semaine"
    },
    "ajustement_hiver": {
        "3 fois/semaine": "2 fois/semaine",
        "2 fois/semaine": "1 fois/semaine",
        "Tous les 2 jours": "1 fois/semaine"
    },
    "alertes": [
        lambda bfe: "Sol trop sec !" if bfe["sol"] == "drainant" and bfe["humidite"] == "faible" else None,
        lambda bfe: "Lumière insuffisante !" if bfe["lumiere"] != "directe" and bfe["type"] in ["succulente", "cactus"] else None,
        lambda bfe: "Arrosage excessif possible !" if bfe["saison"] == "hiver" and bfe["type"] == "cactus" else None
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


# --- Interface CLI ---

def demander_donnees():
    print("Entrez les caractéristiques de la plante :")
    bfe = {
        "type": input("Type (succulente, cactus, tropicale, aromatique, fleur_d_interieur, fleur_d_exterieur) : ").strip().lower(),
        "saison": input("Saison (été, hiver) : ").strip().lower(),
        "sol": input("Type de sol (drainant, argileux, etc.) : ").strip().lower(),
        "humidite": input("Humidité (faible, moyenne, élevée) : ").strip().lower(),
        "lumiere": input("Lumière (directe, indirecte, faible) : ").strip().lower()
    }
    return bfe


if __name__ == "__main__":
    BFE = demander_donnees()
    PPB = ["determiner_arrosage", "generer_alertes", "generer_precautions"]
    PLAN = []

    if resoudre(PPB, BFE, PLAN):
        print("\nSuccès !")
        print("PLAN GÉNÉRÉ :")
        for action in PLAN:
            print("-", action)
    else:
        print("\nÉchec de résolution. Vérifiez les données saisies.")
