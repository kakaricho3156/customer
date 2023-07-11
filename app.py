from db_config import Customer


def main():
    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")

    while True:
        str = input("Your command >")
        if str == "S":
            show_customer()
        elif str == "Q":
            print("Bye!")
            break
        elif str == "A":
            add_customer()
        elif str == "F":
            search()
        elif str == "D":
            delete()
        elif str == "E":
            edit()
        else:
            print(f"Sorry, {str} is not found")


def edit():
    all_user = Customer.select()
    search_name = input("User name >")
    bool = False
    for user in all_user:
        if search_name == user.name:
            edit_name = input(f"New user name({user.name})")
            edit_age = input(f"New user age({user.age})")
            user.name = edit_name
            user.age = edit_age
            user.save()
            bool = True
            break
    if not bool:
        print(f"Sorry, {search_name} is not foundQ")


def delete():
    all_user = Customer.select()
    delete_name = input("User name >")
    found = False
    for user in all_user:
        if delete_name == user.name:
            cus = Customer.get_by_id(user.id)
            cus.delete_instance()
            found = True
            break
    if not found:
        print(f"Sorry, {delete_name} is not found")


def search():
    all_user = Customer.select()
    search_name = input("User name >")
    bool = False
    for user in all_user:
        if search_name == user.name:
            print(f"Name: {user.name} Age:{user.age}")
            bool = True
            break
    if not bool:
        print(f"Sorry, {search_name} is not found")


def add_customer():
    input_name = input("New user name >")
    input_age = input("New user age >")
    all_user = Customer.select()
    for user in all_user:
        if input_name == user.name:
            print(f"Duplicated user name {input_name}")
            return

    Customer.create(name=input_name, age=input_age)
    print(f"Add new user: {input_name}")


def show_customer():
    for cus in Customer.select():
        print(f"Name: {cus.name} Age: {cus.age}")


if __name__ == "__main__":
    main()
