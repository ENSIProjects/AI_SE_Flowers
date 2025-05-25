def arriere_i(f, bf, rules):
    if f in bf:
        return "succes"
    return etape1(f, bf, rules)

def etape1(f, bf, rules):
    if not rules:
        return "echec"

    for i, rule in enumerate(rules):
        conclusion = rule["conclusion"]
        if conclusion == f:
            if etape2(rule, bf, rules) == "succes":
                return "succes"
    return "echec"

def etape2(rule, bf, rules):
    premisses = rule["conditions"]
    return conjonction(premisses, bf, rules)

def conjonction(faits, bf, rules):
    if not faits:
        return "succes"

    f = faits[0]
    reste = faits[1:]

    if arriere_i(f, bf, rules) == "echec":
        return "echec"

    return conjonction(reste, bf, rules)
# Base de faits initiale
bf = ["type:cactus", "saison:hiver", "sol:drainant", "humidite:faible", "luminosite:faible"]

# Règles
rules = [
    {"conditions": ["type:cactus"], "conclusion": "classe:cactus"},
    {"conditions": ["classe:cactus", "saison:hiver"], "conclusion": "alerte:arrosage_excessif_possible"},
    {"conditions": ["sol:drainant", "humidite:faible"], "conclusion": "alerte:sol_trop_sec"},
    {"conditions": ["classe:cactus", "saison:été"], "conclusion": "arroser:1/2semaines"},
]

# Objectif
objectif1 = "alerte:arrosage_excessif_possible"
print(f"Objectif '{objectif1}' :", arriere_i(objectif1, bf, rules))

objectif2 = "arroser:1/2semaines"
print(f"Objectif '{objectif2}' :", arriere_i(objectif2, bf, rules))

objectif3 = "alerte:sol_trop_sec"
print(f"Objectif '{objectif3}' :", arriere_i(objectif3, bf, rules))
