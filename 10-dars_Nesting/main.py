# book = {
#     "title": "Dunyoning ishlari", 
#     "author": "O. Hoshimov", 
#     "pages": 352
#     }
# empty = dict()            # bo‘sh lug‘at
# pairs = dict([("a", 1), ("b", 2)])  # ro‘yxatdan

# # O‘qish va o‘zgartirish
# print(book["title"])      # "Dunyoning ishlari"
# book["pages"] += 10       # 362
# book["year"] = 1982       # yangi element

# # Xatolikdan qochish
# print(book.get("pages"))   




















# student = {"name": "Aziza", "age": 18, "lang": "Python"}

# for k in student:                 # kalitlar
#     print(k, student[k])

# for k, v in student.items():      # juftlik
#     print(f"{k:5} → {v}")












# nums = [1, 2, 3, 4, 5]
# squared = {n: n**2 for n in nums if n % 2 == 1}
# # {1: 1, 3: 9, 5: 25}
# print(squared)










# school = {
#     "1‑A": {
#         "class_teacher": "S. Karimova", 
#         "pupils": 32
#         },
#     "1‑B": {
#         "class_teacher": "N. Usmonov",
#         "pupils": 29
#         }
# }
# print(school["1‑B"]["class_teacher"])   # "N. Usmonov"
















# school = {
#     "1-A": {"teacher": "Karimova", "students": 30},
#     "1-B": {"teacher": "Usmonov",  "students": 28}
# }


# for class_name, class_info in school.items():
#     print(f"Sinf: {class_name}")
#     for key, value in class_info.items():
#         print(f"  {key.title()}: {value}")














# # Kiritilgan foydalanuvchilardan lug'at tuzish
users = {}
n = int(input("Nechta foydalanuvchi kiritasiz? "))
for _ in range(n):
    username = input("Login: ")
    age = int(input("Yosh: "))
    email = input("Email: ")
    skills = input("Ko'nikmalarni vergul bilan kiriting: ").split(",")

    users[username] = {
        "age": age,
        "email": email,
        "skills": [s.strip() for s in skills]
    }
print("\nYangi foydalanuvchilar ro'yxati:")
for u, i in users.items():
    print(f"{u} ({i['age']}): {i['email']} - {i['skills']}")
