import json

order = {
    "name": "James",
    "drink" : "coffee",
    "flavor": "caramel",
    "topping": "chocolate"
    }

order1 = {
    "name": "Catherine",
    "drink" : "coffee",
    "flavor": "caramel",
    "topping": "chocolate"
    }

orders =[]
orders.append(order)
orders.append(order1)

with open("orders.json", "w") as f:
    json.dump(orders, f, indent=4)
print(orders)

with open("orders.json", "r") as f:
    saved_orders = json.load(f)
print(saved_orders)

