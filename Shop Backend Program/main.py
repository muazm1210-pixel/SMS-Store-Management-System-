from auth import signup, login, users
from products import add_product, view_products
from billing import add_to_bill, generate_bill

while True:
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        signup()

    elif choice == "2":
        user = login()
        if user:
            shop = users[user]["shop"]

            while True:
                print("1. Add Product")
                print("2. View Products")
                print("3. Add Item to Bill")
                print("4. Generate Bill")
                print("5. Logout")

                opt = input("Select: ")

                if opt == "1":
                    add_product()
                elif opt == "2":
                    view_products()
                elif opt == "3":
                    add_to_bill()
                elif opt == "4":
                    generate_bill(shop)
                elif opt == "5":
                    break

    elif choice == "3":
        break