# Inventory of different stores
store1 = {"Apple": 50, "Banana": 30, "Mango": 20}
store2 = {"Apple": 40, "Orange": 25, "Mango": 15}
store3 = {"Banana": 20, "Orange": 10, "Grapes": 35}

# Display inventories
print("Store 1:", store1)
print("Store 2:", store2)
print("Store 3:", store3)

# Merge all inventories
inventory = {}

for store in (store1, store2, store3):
    for item, quantity in store.items():
        inventory[item] = inventory.get(item, 0) + quantity

print("\nCombined Inventory:", inventory)

# Check whether an item exists
item = input("\nEnter item to search: ")

if item in inventory:
    print(item, "is available.")
    print("Total quantity:", inventory.get(item, 0))
else:
    print(item, "is not available.")

# Dictionary comprehension to find low-stock items
low_stock = {
    item: quantity
    for item, quantity in inventory.items()
    if quantity < 50
}

print("\nLow Stock Items:", low_stock)

# Add a new item using update()
inventory.update({"Pineapple": 40})

print("\nInventory after adding new item:", inventory)