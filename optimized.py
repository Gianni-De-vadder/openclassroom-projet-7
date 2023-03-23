import json


def greedy(actions, budget):
    sorted_actions = sorted(actions, key=lambda x: x["benefice"], reverse=True)
    combination = []
    for action in sorted_actions:
        if budget >= action["cout"]:
            combination.append(action)
            budget -= action["cout"]
    return combination


with open("actions.json", "r") as f:
    actions = json.load(f)

print(greedy(actions, 500))
