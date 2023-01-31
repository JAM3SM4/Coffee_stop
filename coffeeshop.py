# Write your code here :-)
print("Welcome to James' Coffee Shop")
answer = input("Please enter your name:")


drinks = ["hot chocolate", "coffee", "decaf", "latte"]
flavors= ["caramel", "vanilla", "peppermint", "raspberry", "plain"]
toppings = ["chocolate", "cinnamon", "caramel", "no topping"]

## drinks
print("James' Coffee Shop drinks")
print("-------------------------")
i = 1
for d in drinks:
    print(i, d)
    i = i +1
drink = input("Choose your drink: ")


##flavors
print("James' Coffee Shop flavors")
print("-------------------------")
i = 1
for f in flavors:
    print(i, f)
    i = i + 1

flavor= input("Choose your flavor: ")

#toppings
print("James' Coffee Shop toppings")
print("-------------------------")
i = 1
for t in toppings:
    print(i,t )
    i = i + 1

topping = input("Choose your topping: ")

print("Here is your order:", answer)
print("Coffee: ", drinks[int(drink)-1])
print("Flavor: ", flavors[int(flavor) - 1])
print("Topping: ", toppings[int(topping) - 1])
print("Thanks for your order")




