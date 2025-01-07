from datetime import datetime

print("----------------Welcome to Mahesh Supermarket----------------")
name = input("Enter your name: ")

# List of items
items = {
    'rice': 20, 
    'sugar': 30, 
    'salt': 15, 
    'oil': 80, 
    'paneer': 110, 
    'maggi': 50, 
    'boost': 90, 
    'colgate': 85
}

# Display items
print("\nAvailable Items:")
print('''
| Item     | Price       |
|----------|-------------|
| Rice     | Rs 20/kg    |
| Sugar    | Rs 30/kg    |
| Salt     | Rs 15/kg    |
| Oil      | Rs 80/liter |
| Paneer   | Rs 110/kg   |
| Maggi    | Rs 50/kg    |
| Boost    | Rs 90/kg    |
| Colgate  | Rs 85/each  |
''')

# Initialize variables
pricelist = []
totalprice = 0

# Loop to add items
while True:
    choice = input("\nDo you want to buy an item? (yes/no): ").lower()
    if choice == 'no':
        break
    elif choice == 'yes':
        item = input("Enter the item name: ").lower()
        quantity = int(input(f"Enter the quantity for {item}: "))

        if item in items:
            price = quantity * items[item]
            pricelist.append((item, quantity, price))
            totalprice += price
        else:
            print("Sorry, the item is not available.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Calculate GST and final amount
gst = (totalprice * 5) / 100
final_amount = totalprice + gst

# Print bill if items were added
if pricelist:
    print("\n------------------ Mahesh Supermarket ------------------")
    print(23*" ","uravakonda")
    print(f"Customer Name: {name}")
    print(f"Date & Time: {datetime.now()}")
    print("-" * 50)
    print(f"{'Item':<10} {'Quantity':<10} {'Price':<10}")
    for item, quantity, price in pricelist:
        print(f"{item:<10} {quantity:<10} Rs {price:<10}")
    print("-" * 50)
    print(f"{'Total Price':<20}: Rs {totalprice}")
    print(f"{'GST (5%)':<20}: Rs {gst}")
    print(f"{'Final Amount':<20}: Rs {final_amount}")
    print("-" * 50)
    print("Thank you for shopping with us!")
else:
    print("\nNo items purchased. Thank you for visiting!")
