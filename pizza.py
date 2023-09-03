#stre informatiion about a pizza being oedered:
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
print(f"you ordered a {pizza['crust']}-crust pizza.""with the following toppings")
for topping in pizza['toppings']:
    print("\t"+topping)
