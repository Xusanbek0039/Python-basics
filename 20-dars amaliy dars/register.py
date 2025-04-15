users = {}

def register_user():
    users["ism"] = input("Ismingizni kiriting: ").title()
    users["familiya"] = input("Familiyangizni kiriting: ").title()
    users["login"] = input("Login kiriting: ")
    users["parol"] = input("Parol kiriting: ")
    print(users)


