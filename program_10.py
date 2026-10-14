# Inventory of two stores
store1 = {"Pen": 50, "Book": 30, "Pencil": 40}
store2 = {"Pen": 20, "Book": 15, "Eraser": 25}

print("Store 1 Inventory:", store1)
print("Store 2 Inventory:", store2)

# Check if an item exists
item = input("Enter item name: ")

if item in store1:
    print("Quantity in Store 1:", store1.get(item))
else:
    print("Item not found in Store 1")

# Merge inventories
inventory = store1.copy()

for item, quantity in store2.items():
    inventory[item] = inventory.get(item, 0) + quantity

print("Combined Inventory:", inventory)

# Dictionary comprehension
result = {item: qty for item, qty in inventory.items() if qty > 20}
print("Items with quantity greater than 20:", result)