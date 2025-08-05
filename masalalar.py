users = {
    "admin":1234
}
quiz = input("Kirish uchun 'kirish', Ro'yxatdan o'tish uchun 'register' deb yozing Chiqish uchun 'exit': ").lower().strip()

def login():
    ishora = True
    while ishora:
        if quiz == "kirish":
            login = input("Login kiriting: ")
            parol = input("Parol kiriting: ")
            """Davom bor"""
        elif quiz == "register":
            login = input("Yangi login kiriting: ")
            parol = input("Yangi parol kiriting: ")
            users[login] = parol
            print(users)
        elif quiz == "exit":
            print("Ko'rishguncha xayr!")
            ishora = False
            
login()