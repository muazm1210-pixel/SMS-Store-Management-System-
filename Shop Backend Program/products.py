products = {}

def add_product():
    pid = int(input("Product ID: "))
    name = input("Product Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    products[pid] = {
        "name": name,
        "price": price,
        "qty": qty
    }
    print("Product added!\n")


def view_products():
    print("\n--- PRODUCT LIST ---")
    for pid, p in products.items():
        print(pid, p["name"], "Rs", p["price"], "Qty:", p["qty"])
    print()