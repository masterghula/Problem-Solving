def add_item(item, quantity):
    if item in inventory:
        inventory[item]+=quantity
    else:
        inventory[item]=quantity

def sell_item(item, quantity):
    if item in inventory and quantity<inventory[item]:
        inventory[item]-=quantity
    elif quantity>inventory[item]:
        print("Bro we dont got that much")
    else:
        print("Bro we dont sell that here")

def current_inv():
    print(inventory)
inventory={"apple":3, "banana":5, "orange":8}

current_inv()
add_item("apple", 2)
sell_item("banana", 3)
current_inv()