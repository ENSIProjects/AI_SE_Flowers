def arriere_ii(f, bf, rules):
    if f in bf:
        return "succes"

    conflit = [r for r in rules if r["conclusion"] == f]

    if directe(conflit, bf) == "succes":
        return "succes"

    return etape1(f, bf, conflit, rules)

def directe(les_r, bf):
    if not les_r:
        return "echec"

    for rule in les_r:
        if all(premisse in bf for premisse in rule["conditions"]):
            return "succes"

    return "echec"

def etape1(f, bf, les_r, rules):
    if not les_r:
        return "echec"

    for rule in les_r:
        if rule["conclusion"] == f:
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

    if arriere_ii(f, bf, rules) == "echec":
        return "echec"

    return conjonction(reste, bf, rules)
# Base de faits initiale
bf = ["type:cactus", "saison:hiver", "sol:drainant", "humidite:faible"]

# Règles du système expert
rules = [
    {"conditions": ["type:cactus"], "conclusion": "classe:cactus"},
    {"conditions": ["classe:cactus", "saison:hiver"], "conclusion": "alerte:arrosage_excessif"},
    {"conditions": ["sol:drainant", "humidite:faible"], "conclusion": "alerte:sol_trop_sec"},
    {"conditions": ["classe:cactus", "saison:été"], "conclusion": "arroser:1/2semaines"},
]

# Tests
objectif1 = "alerte:sol_trop_sec"
objectif2 = "arroser:1/2semaines"
objectif3 = "alerte:sol_trop_sec"

print(f"{objectif1} ->", arriere_ii(objectif1, bf.copy(), rules))  # succes
print(f"{objectif2} ->", arriere_ii(objectif2, bf.copy(), rules))  # echec
print(f"{objectif3} ->", arriere_ii(objectif3, bf.copy(), rules))  # succes
