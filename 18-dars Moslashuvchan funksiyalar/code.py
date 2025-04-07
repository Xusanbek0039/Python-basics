# Ushbu kod IT Creative jamoasi tomonidan yozilgan
# Muallif: Suyunov Husan
# Python asoslari Moslashuvchan funksiya 18-dars arguments kewords
# YouTube: https://www.youtube.com/@it_creative
# GitHub: https://github.com/Xusanbek0039



# 1-code 
# Funksiya yaratamiz
# def yigindi(*son):
#     return sum(son)

# print(yigindi(1, 2, 3, 5))      # Natija: 6
# print(yigindi(10, 20, 30, 40))  # Natija: 100







# 2-code 
# def foydalanuvchi_malumotlari(**qiymat):
#     for kalit, qiymat in qiymat.items():
#         print(f"{kalit}: {qiymat}")

# # Funksiyani chaqiramiz
# foydalanuvchi_malumotlari(ism="Ali", yosh=25, shahar="Toshkent", Familiya="O'tkirov")







# 3-code 
# def mahsulot_tavsifi(nomi, *args, **kwargs):
#     print(f"Mahsulot: {nomi}")
    
#     for xususiyat in args:
#         print(f"- {xususiyat}")
    
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit}: {qiymat}")

# # Funksiyani chaqiramiz
# mahsulot_tavsifi("Telefon", "Yuqori sifat", "Tezkor ishlash", rang="Qora", narx="500$")











# # 4-code 
# def kopaytir(*args):
#     """Berilgan sonlarni ko‘paytirib natijani qaytaradi"""
#     natija = 1
#     for son in args:
#         natija = son * natija  # Har bir sonni natijaga ko‘paytiramiz
#     return natija

# print(kopaytir(2, 3, 4))  # Natija: 24
# print(kopaytir(5, 10))    # Natija: 50
# print(kopaytir(1, 2, 3, 4, 5,5))  # Natija: 120











# # 5-code 
# def foydalanuvchi_info(**kwargs):
#     """Foydalanuvchi haqida ma'lumotlarni chiqaruvchi funksiya"""
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit.capitalize()}: {qiymat}")

# # Funksiyani chaqirish
# foydalanuvchi_info(ism="Ali", yosh=25, shahar="Toshkent")













# 6-code 
# def tanishtir(ism, *args, **kwargs):
#     """Ism, qo‘shimcha malumotlar va kalit-qiymat juftliklarini qabul qiladi"""
#     print(f"Salom, men {ism}!")
    
#     if args:
#         print("Qo‘shimcha malumotlar:")
#         for malumot in args:
#             print(f" - {malumot}")

#     if kwargs:
#         print("Shaxsiy ma'lumotlar:")
#         for kalit, qiymat in kwargs.items():
#             print(f"{kalit.capitalize()}: {qiymat}")

# # Funksiyani chaqirish
# tanishtir("Akmal", "Dasturchi", "Python mutaxassisi", yosh=30, shahar="Samarqand")














# 7-code 
# def tanishtir(ism, *args, **kwargs):
#     """Ism, qo‘shimcha malumotlar va kalit-qiymat juftliklarini qabul qiladi"""
#     print(f"Salom, men {ism}!")
    
#     if args:
#         print("Qo‘shimcha malumotlar:")
#         for malumot in args:
#             print(f"- {malumot}")

#     if kwargs:
#         print("Shaxsiy ma'lumotlar:")
#         for kalit, qiymat in kwargs.items():
#             print(f"{kalit.capitalize()}: {qiymat}")

# # Funksiyani chaqirish
# tanishtir("Akmal", "Dasturchi", "Python mutaxassisi", yosh=30, shahar="Samarqand")















# 8-code 
# def yigindi(a, b):
#     return a + b

# def ayirma(a, b):
#     return a - b

# def hisobla(funksiya, *args):
#     """Berilgan funksiyani chaqirib natijani qaytaradi"""
#     return funksiya(*args)

# print(hisobla(yigindi, 10, 5))  # Natija: 15
# print(hisobla(ayirma, 10, 5))   # Natija: 5
