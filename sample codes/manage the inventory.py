def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print("UPDATED Item", item_name)
    else:
        inventory[item_name] = quantity
        print("ADDED Item", item_name)

def delete_item(inventory, item_name, quantity):
    if item_name not in inventory:
        print("Item", item_name, "does not exist")
    else:
        if inventory[item_name] < quantity:
            print("Item", item_name, "could not be DELETED")
        else:
            inventory[item_name] -= quantity
            print("DELETED Item", item_name)

T = int(input())

for _ in range(T):
    N = int(input())
    inventory = {}
    
    for _ in range(N):
        item_name, item_quantity = input().split()
        inventory[item_name] = int(item_quantity)

    M = int(input())
   
    for _ in range(M):
        operation, item_name, quantity = input().split()
        quantity = int(quantity)

        if operation == "ADD":
            add_item(inventory, item_name, quantity)
        elif operation == "DELETE":
            delete_item(inventory, item_name, quantity)

    total_quantity = sum(inventory.values())
    print("Total Items in Inventory:", total_quantity)