import os
import json

def main_menu(orders):
    while True:
        order = get_order()
        if order == {}:
                print("Exiting.....")
                return
        print("Check your order:")
        print_order(order)
        confirm = input("Confirm? Press Y to confirm, N to cancel: ")
        if confirm == "Y" or confirm == "y":
            orders.append(order)
            print("Thanks for your order:")
            print_order(order)
        elif confirm == "X" or confirm == "x":
            return
        else:
            continue

def menu(choices, title="Coffee Stop Menu", prompt="Choose your item: "):
    print(title)
    print(len(title) * '-')
    i = 1
    for c in choices:
        print(i, c)
        i = i + 1
    while True:
        choice = input(prompt)
        allowed_answers = []
        for a in range(1, len(choices)+1):
                allowed_answers.append(str(a))

        allowed_answers.append('X')
        allowed_answers.append('x')

        if choice in allowed_answers:
            if choice == 'X' or choice == 'x':
               answer = ''
               break
            else:
                answer = choices[int(choice) - 1]
                break
        else:
            print("enter number 1 to ", len(choices))
            answer = ''

    return answer

def read_menu(filename):
    with open(filename) as f:
        temp = f.readlines()
    result = []
    for item in temp:
        new_item = item.strip()
        result.append(new_item)

    return result


def get_order():
    order = {}
    name = input("Enter your name or enter 'X' to exit: ")
    if name == "X" or name == "x":
        return {}
    else:
        order["name"] = name

    drinks = read_menu("drinks.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")

    drink = menu(drinks, "Coffee Stop drinks", "Choose your drink: ")
    if drink == '':
        return {}
    order["drink"] = drink

    flavor = menu(flavors, "Coffee Stop flavors", "Choose your flavor: ")
    if flavor == '':
        return {}
    order["flavor"] = flavor

    topping = menu(toppings, "Coffee Stop toppings", "Choose your topping: ")
    if topping == '':
        return {}
    order["topping"] = topping

    return order

def print_order(order):
    print("Here is your order, ", order["name"])
    print("Main product: ", order["drink"])
    print("Flavor: ", order["flavor"])
    print("Topping: ", order["topping"])
    print("Thank-you for your order from Coffee Stop")
    return

def load_orders(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            orders = json.load(f)
        return orders
    else:
        return []

def save_orders(orders, filename):
    with open(filename, "w") as f:
        json.dump(orders, f, indent=4)
    return

orders = load_orders("orders.json")
main_menu(orders)
save_orders(orders, "orders.json")



