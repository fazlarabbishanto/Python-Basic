requested_toppings=['Mushrooms','Green Peppers','Extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='Green Peppers':
       print("Sorry,we are out of green papers right now")
    else:
       print(f"Adding {requested_topping}.")
print("\nFinished making your pizza")