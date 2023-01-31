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

f = open("orders.json", "w")
json.dump(orders, f, indent=4)
print(orders)

f = open("orders.json", "r")
saved_orders = json.load(f)
print(saved_orders)

