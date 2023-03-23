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


def greedy(actions, budget):
    sorted_actions = sorted(actions, key=lambda x: x["benefice"], reverse=True)
    combination = []
    for action in sorted_actions:
        if budget >= action["cout"]:
            combination.append(action)
            budget -= action["cout"]
    return combination


print(greedy(actions, 500))
