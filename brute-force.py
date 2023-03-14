actions = [
    {"nom": "Action-1", "cout": 20, "benefice": 5},
    {"nom": "Action-2", "cout": 30, "benefice": 10},
    {"nom": "Action-3", "cout": 50, "benefice": 15},
    {"nom": "Action-4", "cout": 70, "benefice": 20},
    {"nom": "Action-5", "cout": 60, "benefice": 17},
    {"nom": "Action-6", "cout": 80, "benefice": 25},
    {"nom": "Action-7", "cout": 22, "benefice": 7},
    {"nom": "Action-8", "cout": 26, "benefice": 11},
    {"nom": "Action-9", "cout": 48, "benefice": 13},
    {"nom": "Action-10", "cout": 34, "benefice": 27},
    {"nom": "Action-11", "cout": 42, "benefice": 17},
    {"nom": "Action-12", "cout": 110, "benefice": 9},
    {"nom": "Action-13", "cout": 38, "benefice": 23},
    {"nom": "Action-14", "cout": 14, "benefice": 1},
    {"nom": "Action-15", "cout": 18, "benefice": 3},
    {"nom": "Action-16", "cout": 8, "benefice": 8},
    {"nom": "Action-17", "cout": 4, "benefice": 12},
    {"nom": "Action-18", "cout": 10, "benefice": 14},
    {"nom": "Action-19", "cout": 24, "benefice": 21},
    {"nom": "Action-20", "cout": 114, "benefice": 18},
]


def brute_force(actions, budget):
    """
    Renvoie la liste des actions qui maximisent le bénéfice
    avec le budget donné, en testant toutes les combinaisons possibles
    """
    n = len(actions)
    best_combination = None
    best_profit = 0

    for i in range(2**n):
        combination = []
        profit = 0
        total_cost = 0

        for j in range(n):
            if (i >> j) & 1:
                action = actions[j]
                combination.append(action)
                profit += action["benefice"]
                total_cost += action["cout"]

        if total_cost <= budget and profit > best_profit:
            best_profit = profit
            best_combination = combination

    return best_combination


print(brute_force(actions, 500))
