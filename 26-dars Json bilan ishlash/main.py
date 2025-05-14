"""
Github: https://github.com/xusanbek0039
Web app: https://husanbek-coder.uz

Mavzu: Pythonda json bilan ishlash.

Youtube: https://youtube.com/@it_creative
"""


# # 1. JSON stringni Python obyektiga aylantirish (json.loads())

# import json

# json_str = '{"name": "Husan", "age": 20, "languages": ["Python", "JavaScript"]}'
# python_obj = json.loads(json_str)

# print(python_obj)
# print(python_obj['name'])       # Natija: Husan
# print(python_obj['languages'])  # Natija: ['Python', 'JavaScript']


















# # 2. Python obyektini JSON stringga aylantirish (json.dumps())
# import json

# data = {
#     "name": "Husan",
#     "age": 20,
#     "is_student": True
# }

# json_data = json.dumps(data)
# print(json_data)















# # # 3. JSON faylga yozish (json.dump())
# import json

# user = {
#     "name": "Husan",
#     "course": "Python Dasturlash",
#     "level": "Boshlovchi"
# }

# with open("user.json", "w") as f:
#     json.dump(user, f, indent=4)



















# # 4. JSON fayldan o‘qish (json.load())
# import json

# with open("user.json", "r") as f:
#     data = json.load(f)

# print(data)
# print(data["course"])  # Natija: Python Dasturlash























# # # 5. Faylda bir nechta foydalanuvchi yozuvlari bilan ishlash
# import json

# # users = [
# #     {"name": "Ali", "score": 85},
# #     {"name": "Vali", "score": 92}
# # ]

# # with open("results.json", "w") as f:
# #     json.dump(users, f, indent=2)

# # O‘qish
# with open("results.json", "r") as f:
#     results = json.load(f)

# for user in results:
#     print(f"{user['name']} balli: {user['score']}")
























# # 6. JSON faylga yangi foydalanuvchi qo‘shish (read-modify-write)
# import json

# # Avvalgi ma'lumotni o‘qish
# with open("results.json", "r") as f:
#     users = json.load(f)

# # Yangi foydalanuvchi
# new_user = {"name": "Husanbek", "score": 99}
# users.append(new_user)

# # Yana yozib qo‘yish
# with open("results.json", "w") as f:
#     json.dump(users, f, indent=2)























# # 7. try-except bilan JSON parsing xatolarini ushlash
# import json

# invalid_json = "{name: Husan}"  # noto‘g‘ri format

# try:
#     data = json.loads(invalid_json)

    
# except json.JSONDecodeError as e:
#     print("Xato:", e)
