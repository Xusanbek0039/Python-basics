# # 1-misol: Oddiy class va obyekt
# class Talaba:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def salom_ber(self):
#         print(f"Salom, mening ismim {self.ism}, yoshim {self.yosh}da.")

# # Obyekt yaratish
# talaba1 = Talaba("Ali", 20)
# talaba1.salom_ber()











# # 2-misol: Bir nechta obyektlar

# talaba2 = Talaba("Laylo", 19)
# talaba3 = Talaba("Bekzod", 22)

# talaba2.salom_ber()
# talaba3.salom_ber()










# # 3-misol: Atributni o'zgartirish

# talaba1.yosh = 21
# talaba1.salom_ber()











# # 4-misol: Hisob-kitobli metod

# class Doira:
#     def __init__(self, radius):
#         self.radius = radius

#     def yuzani_hisobla(self):
#         return 3.14 * self.radius ** 2

# doira1 = Doira(5)
# print("Doira yuzi:", doira1.yuzani_hisobla())













# # 5-misol: Vorislik (ya'ni class boshqa classdan meros oladi)

# class Inson:
#     def __init__(self, ism):
#         self.ism = ism

#     def salom_ber(self):
#         print(f"Salom, men {self.ism}")

# class Talaba(Inson):
#     def __init__(self, ism, kurs):
#         super().__init__(ism)  # ota classni chaqiryapmiz
#         self.kurs = kurs

#     def info(self):
#         print(f"{self.ism} {self.kurs}-kurs talabasi")

# talaba4 = Talaba("Aziz", 3)
# talaba4.salom_ber()
# talaba4.info()













# # 6-misol: Obyektlar ro'yxati

# talabalar = [
#     Talaba("Ali", 20),
#     Talaba("Laylo", 19),
#     Talaba("Bekzod", 22),
# ]

# for talaba in talabalar:
#     talaba.salom_ber()
