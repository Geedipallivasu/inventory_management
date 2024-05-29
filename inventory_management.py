import json

def add_product(inventory, product_id, name, price, quantity):
    inventory[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

def update_product(inventory, product_id, **kwargs):
    if product_id in inventory:
        for key, value in kwargs.items():
            if key in inventory[product_id]:
                inventory[product_id][key] = value

def remove_product(inventory, product_id):
    if product_id in inventory:
        del inventory[product_id]

def get_product(inventory, product_id):
    return inventory.get(product_id, None)

def save_to_file(inventory, filename):
    with open(filename, 'w') as f:
        json.dump(inventory, f, indent=4)

def load_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def create_order(inventory, order_id, product_orders):
    order = {"order_id": order_id, "products": product_orders}
    for product_id, quantity in product_orders.items():
        if product_id in inventory:
            if inventory[product_id]['quantity'] >= quantity:
                inventory[product_id]['quantity'] -= quantity
            else:
                print(f"Not enough {inventory[product_id]['name']} in stock")
    return order

def restock_product(inventory, product_id, quantity):
    if product_id in inventory:
        inventory[product_id]['quantity'] += quantity

def main():
    inventory = {}
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. View Product")
        print("5. Create Order")
        print("6. Restock Product")
        print("7. Save Inventory")
        print("8. Load Inventory")
        print("9. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(inventory, product_id, name, price, quantity)
        
        elif choice == '2':
            product_id = input("Enter product ID: ")
            name = input("Enter new product name (leave blank to skip): ")
            price = input("Enter new product price (leave blank to skip): ")
            quantity = input("Enter new product quantity (leave blank to skip): ")
            kwargs = {}
            if name:
                kwargs['name'] = name
            if price:
                kwargs['price'] = float(price)
            if quantity:
                kwargs['quantity'] = int(quantity)
            update_product(inventory, product_id, **kwargs)
        
        elif choice == '3':
            product_id = input("Enter product ID: ")
            remove_product(inventory, product_id)
        
        elif choice == '4':
            product_id = input("Enter product ID: ")
            product = get_product(inventory, product_id)
            if product:
                print(product)
            else:
                print("Product not found")
        
        elif choice == '5':
            order_id = input("Enter order ID: ")
            products = input("Enter product IDs and quantities (e.g. 1:2,2:1): ")
            product_orders = {k: int(v) for k, v in (item.split(":") for item in products.split(","))}
            create_order(inventory, order_id, product_orders)
        
        elif choice == '6':
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity to restock: "))
            restock_product(inventory, product_id, quantity)
        
        elif choice == '7':
            filename = input("Enter filename to save inventory: ")
            save_to_file(inventory, filename)
        
        elif choice == '8':
            filename = input("Enter filename to load inventory: ")
            inventory = load_from_file(filename)
        
        elif choice == '9':
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()