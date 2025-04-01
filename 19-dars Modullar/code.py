# Ushbu kod IT Creative jamoasi tomonidan yozilgan
# Muallif: Suyunov Husan
# Python asoslari: Modullar 19-dars
# YouTube: https://www.youtube.com/@it_creative
# GitHub: https://github.com/Xusanbek0039

# 1-code
# from salom import salom_ber
# print(salom_ber("Husan"))










# 2-code
# import salom
# print(salom_ber("Husan"))











# math – matematik amallar uchun

# random – tasodifiy sonlar yaratish uchun

# datetime – vaqt bilan ishlash uchun

# os – operatsion tizim bilan ishlash uchun

# sys – tizim parametrlariga kirish uchun










# 3-code
# import math 
# print(math.sqrt(16))  # 4.0

















# 4-code
# import math

# # Doiraning yuzasini hisoblash
# radius = 5
# yuza = math.pi * math.pow(radius, 2)
# print(f"Doira yuzasi: {yuza}")

# # Ikkita sonning EKUB'ini topish
# print(math.gcd(36, 48))  # 12

# # Sonning faktorialini hisoblash
# print(math.factorial(5))  # 120

# # Darajaga oshirish (2^3)
# print(math.pow(2, 3))  # 8.0

# # Radial burchakni gradusga aylantirish
# print(math.degrees(math.pi))  # 180.0

# # Gradusni radianlarga aylantirish
# print(math.radians(180))  # 3.141592653589793

# # Sonning butun qismini olish
# print(math.floor(3.7))  # 3
# print(math.ceil(3.1))   # 4

















# # 5-code
import random

# 1 dan 10 gacha tasodifiy butun son
# print(random.randint(1, 10))

# 0 va 1 orasida tasodifiy haqiqiy son
# print(random.random())

# # Berilgan oraliqda tasodifiy haqiqiy son (5 dan 15 gacha)
# print(random.uniform(5, 15))

# # Ro‘yxatdan tasodifiy element tanlash
# mevalar = ["olma", "banan", "uzum", "shaftoli"]
# print(random.choice(mevalar))

# # Ro‘yxat elementlarini tasodifiy aralashtirish
# raqamlar = [1, 2, 3, 4, 5]
# random.shuffle(raqamlar)
# print(raqamlar)

# # 10 dan 100 gacha 3 ta tasodifiy son olish
# print(random.sample(range(10, 100), 5))

# # 0 va 1 orasida tasodifiy son chiqarib, ehtimollikni tekshirish
# if random.random() > 0.5:
#     print("Omadingiz keldi!")
# else:
#     print("Bu safar omad yo‘q 😅")


















# 6-code
# from datetime import datetime, timedelta

# # Joriy sana va vaqt
# hozir = datetime.now()
# print("Hozirgi vaqt:", hozir)

# # Faqat sana yoki vaqtni olish
# print("Bugungi sana:", hozir.date())
# print("Joriy vaqt:", hozir.time())

# # Belgilangan formatda vaqt chiqarish
# print("Formatlangan vaqt:", hozir.strftime("%Y-%m-%d %H:%M:%S"))

# # Belgilangan sanani yaratish
# tugilgan_kun = datetime(2004, 1, 30)
# print("Tug‘ilgan kun:", tugilgan_kun)

# # Oradan 7 kun o'tkazish
# bir_hafta_keyin = hozir + timedelta(days=7)
# print("Bir hafta keyin:", bir_hafta_keyin.date())

# # Oradan 3 soat oldin
# uch_soat_oldin = hozir - timedelta(hours=3)
# print("Uch soat oldin:", uch_soat_oldin.time())

# # Ikki sana orasidagi farq
# farq = hozir - tugilgan_kun
# print("Yashagan kunlaringiz:", farq.days)

# # Yangi yilgacha qolgan vaqt
# yangi_yil = datetime(hozir.year + 1, 1, 1)
# qolgan_vaqt = yangi_yil - hozir
# print(f"Yangi yilgacha {qolgan_vaqt.days} kun qoldi!")

















# 7-code
import os

# Joriy ishchi katalogni olish
# print("Joriy katalog:", os.getcwd())

# Yangi papka yaratish
# os.mkdir("yangi_papka")
# print("Papka yaratildi!")

# # Papkani o‘chirish
# os.rmdir("yangi_papka")
# print("Papka o‘chirildi!")

# # Fayl yoki katalog mavjudligini tekshirish
# print("Fayl bormi?", os.path.exists("test.txt"))

# # Fayl hajmini olish (baytlarda)
# if os.path.exists("test.txt"):
#     print("Fayl hajmi:", os.path.getsize("test.txt"), "bayt")
# else:
#     print("Fayl mavjud emas!")

# # Joriy katalogdagi fayl va papkalarni olish
# print("Fayllar:", os.listdir())

# # Muayyan faylning to‘liq yo‘lini olish
# print("To‘liq yo‘l:", os.path.abspath("test.txt"))

# # Muhit o‘zgaruvchilarini olish
# print("Foydalanuvchi nomi:", os.getenv("USERNAME") or os.getenv("USER"))

# # Dasturdan chiqish
# os.exit(0)  # Ushbu qatorda dastur to‘xtaydi

# # Buyruq qatori komandalarini bajarish
# os.system("echo Salom, dunyo!")


# # Fayl nomini belgilang
# import os

# # Fayl yo'lini olish va tekshirish
# fayl_nomi = r"F:\Git Hub\Python-asoslar\19-dars Modullar\logo.png"

# if os.path.exists(fayl_nomi):
#     print("Fayl mavjud! Ochilmoqda...")
#     os.startfile(fayl_nomi)
# else:
#     print(f"❌ Xatolik: '{fayl_nomi}' topilmadi. Joriy katalog: {os.getcwd()}")




















# # 8-code
# # Python versiyasini aniqlash
# import sys
# print("Python versiyasi:", sys.version)






# # txt faylga malumot yozish
# import sys

# sys.stdout = open("output.txt", "w")  # Natijani faylga yozadi
# print("Bu matn faylga yoziladi!")
# sys.stdout.close()




# Qiziq code ishga tushursangiz VS Code yopiladi fayllariz saqlanganiga ishonch xosil qiling!!!
import os

os.system("taskkill /IM code.exe /F")  # VS Code-ni yopish
