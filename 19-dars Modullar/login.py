users = {
    "admin": "1234",   
    "ali": "1111",
    "vali": "2222"
}

def login():
    while True:
        username = input("Username kiriting: ")
        parol = input("Parol kiriting: ")

        if username in users and users[username] == parol:
            print("✅ Muvaffaqiyatli kirdingiz!")
            break
        elif username in users and users[username] != parol:
            print("Parol xato!")
        else:
            print("Login xato!")

