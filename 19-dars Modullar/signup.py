users = {
    "admin": "1234",   # foydalanuvchi nomi: parol
    "ali": "1111",
    "vali": "2222"
}
def signup():
    while True:
        username = input("Yangi username kiriting: ")
        if username in users:
            print("⚠️ Bu username allaqachon mavjud. Boshqasini tanlang.\n")
        else:
            parol = input("Yangi parol kiriting: ")
            users[username] = parol
            print(f"✅ Foydalanuvchi '{username}' muvaffaqiyatli qo‘shildi!")
            break
