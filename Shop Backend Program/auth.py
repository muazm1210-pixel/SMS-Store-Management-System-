users = {}

def signup():
    print("\n--- SIGNUP ---")
    username = input("Username: ")
    password = input("Password: ")

    shop_name = input("Shop Name: ")
    owner = input("Owner Name: ")
    phone = input("Phone: ")

    users[username] = {
        "password": password,
        "shop": {
            "shop_name": shop_name,
            "owner": owner,
            "phone": phone
        }
    }
    print("Account created successfully!\n")


def login():
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!\n")
        return username
    else:
        print("Invalid credentials!\n")
        return None