file = open("sample1.csv", "r")
lines = file.readlines()
file.close()
users = {}
for line in lines[1:]:
    name, password, status = line.strip().split(",")
    users[name] = {"password": password, "status": int(status)}
print("Users Dictionary:", users)
choice = int(input("\n1. Register\n2. Login\nEnter choice: "))
match choice:
    case 1:
        new_name = input("Enter username: ")
        if new_name in users:
            if users[new_name]["status"] == 1:
                print("Welcome", new_name, "! You are already active.")
            else:
                print("User exists but inactive. Please login to activate.")
        else:
            new_password = input("Enter password: ")
            if new_password == "":
                print("Invalid password! Cannot be empty.")
            else:
                users[new_name] = {"password": new_password, "status": 1}
                print("User registered successfully!")
                print("Welcome", new_name)
    case 2:
        login_name = input("Enter username: ")
        if login_name not in users:
            print("User not found!")
            print("Invalid username!")
        else:
            login_password = input("Enter password: ")
            if users[login_name]["password"] != login_password:
                print("Invalid password!")
            else:
                if users[login_name]["status"] == 0:
                    print("User is inactive. Activating now...")
                    users[login_name]["status"] = 1
                print("Welcome", login_name, "! Login successful.")
    case _:
        print("Invalid choice!")
file = open("sample1.csv", "w")
file.write("name,password,status\n")
for name in users:
    file.write(
        name + "," +
        users[name]["password"] + "," +
        str(users[name]["status"]) + "\n"
    )
file.close()
print("\nUpdated Users Dictionary:", users)
