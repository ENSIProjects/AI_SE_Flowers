'''def tous_les_premisses_sont_dans_bf(premisses, bf):
    return all(p in bf for p in premisses)

def un_cycle(rules, bf, goal):
    if goal in bf:
        return "succes"

    if not rules:
        return "echec"

    for i, rule in enumerate(rules):
        premisses = rule["conditions"]
        conclusion = rule["conclusion"]

        if tous_les_premisses_sont_dans_bf(premisses, bf):
            if conclusion == goal:
                return "succes"
            if conclusion not in bf:
                bf.append(conclusion)

            # Supprimer la règle appliquée
            new_rules = rules[:i] + rules[i+1:]
            return un_cycle(new_rules, bf, goal)

    return "echec"

# Base de faits initiale
bf = ["type:succulente", "saison:été", "sol:drainant", "humidite:faible", "luminosite:faible"]

# Liste de règles
regles = [
    # Classification
    {"conditions": ["type:succulente"], "conclusion": "classe:succulente"},
    {"conditions": ["type:tropicale"], "conclusion": "classe:tropicale"},
    {"conditions": ["type:cactus"], "conclusion": "classe:cactus"},

    # Arrosage
    {"conditions": ["classe:succulente", "saison:été"], "conclusion": "arroser:1/semaine"},
    {"conditions": ["classe:cactus", "saison:été"], "conclusion": "arroser:1/2semaines"},

    # Alertes
    {"conditions": ["sol:drainant", "humidite:faible"], "conclusion": "alerte:sol_trop_sec"},
    {"conditions": ["luminosite:faible", "classe:succulente"], "conclusion": "alerte:lumiere_insuffisante"}
]

# Exemple : vérifier si on peut obtenir "arroser:1/semaine"
objectif = "arroser:1/semaine"
resultat = un_cycle(regles, bf.copy(), objectif)
print("Objectif:", objectif, "=>", resultat)

# Exemple : vérifier si alerte "sol trop sec"
objectif2 = "alerte:sol_trop_sec"
resultat2 = un_cycle(regles, bf.copy(), objectif2)
print("Objectif:", objectif2, "=>", resultat2)
'''