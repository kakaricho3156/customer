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
        else:
            print(f"{str}: command not found")


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
