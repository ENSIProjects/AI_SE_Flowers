'''def tous_les_premisses_sont_dans_bf(premisses, bf):
    return all(p in bf for p in premisses)

def un_cycle(rules, bf, bf_prime, goal):
    if not rules:
        if not bf_prime:
            return "echec"
        bf += bf_prime
        return un_cycle(all_rules.copy(), bf, [], goal)

    rule = rules[0]
    reste = rules[1:]

    if tous_les_premisses_sont_dans_bf(rule["conditions"], bf):
        conclusion = rule["conclusion"]

        if conclusion == goal:
            return "succes"

        if conclusion not in bf and conclusion not in bf_prime:
            bf_prime.append(conclusion)

        return un_cycle(reste, bf, bf_prime, goal)

    return un_cycle(reste, bf, bf_prime, goal)

def avant_ii(goal, bf, rules):
    global all_rules
    all_rules = rules.copy()  # pour redémarrer UN-CYCLE avec les règles complètes
    if goal in bf:
        return "succes"
    return un_cycle(rules.copy(), bf.copy(), [], goal)
# Base de faits initiale
bf = ["type:succulente", "saison:été", "sol:drainant", "humidite:faible", "luminosite:faible"]

# Règles
rules = [
    {"conditions": ["type:succulente"], "conclusion": "classe:succulente"},
    {"conditions": ["classe:succulente", "saison:été"], "conclusion": "arroser:1/semaine"},
    {"conditions": ["sol:drainant", "humidite:faible"], "conclusion": "alerte:sol_trop_sec"},
    {"conditions": ["luminosite:faible", "classe:succulente"], "conclusion": "alerte:lumiere_insuffisante"},
]

# Tester un objectif
objectif1 = "arroser:1/semaine"
print(f"Objectif '{objectif1}':", avant_ii(objectif1, bf, rules))

objectif2 = "alerte:sol_trop_sec"
print(f"Objectif '{objectif2}':", avant_ii(objectif2, bf, rules))

objectif3 = "classe:succulente"
print(f"Objectif '{objectif3}':", avant_ii(objectif3, bf, rules))

objectif4 = "alerte:lumiere_insuffisante"
print(f"Objectif '{objectif4}':", avant_ii(objectif4, bf, rules))'''
