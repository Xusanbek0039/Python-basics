# # 1-misol: Oddiy class va obyekt

# class Talaba:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def salom_ber(self):
#         print(f"Salom, mening ismim {self.ism}, yoshim {self.yosh}da.")

# # # # # # Obyekt yaratish
# talaba1 = Talaba("Ali", 20)
# talaba1.salom_ber()













# 2-misol: Bir nechta obyektlar

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


# doira1 = Doira(7)
# print("Doira yuzi: ", doira1.yuzani_hisobla())












# # 5-misol: Vorislik (ya'ni class boshqa classdan meros oladi)

class Inson:
    def __init__(self, ism, familiya, yosh):
        self.yosh = yosh
        self.ism = ism
        self.familiya = familiya

    def salom_ber(self):
        print(f"Salom, men {self.ism} {self.familiya} Yoshi: {self.yosh}")

class Talaba(Inson):
    def __init__(self, ism, kurs,familiya,yosh):
        super().__init__(ism)  # ota classni chaqiryapmiz
        self.kurs = kurs
        super().__init__(familiya)
        super().__init__(yosh)


    def info(self):
        print(f"{self.ism} {self.familiya} {self.kurs}-kurs talabasi\nYoshi: {self.yosh}")

class Oqituvchi(Inson):
    def __init__(self, ism, working,familiya,yosh):
        super().__init__(ism)
        super().__init__(familiya)
        super().__init__(yosh)
        self.working = working

    def info(self):
        print(f"{self.ism} {self.familiya} {self.working}-kurs o'qituvchisi. \nYoshi: {self.yosh}")



oqituvchi = Oqituvchi("Botir","Ona tili","Axmatov",45)













# # 6-misol: Obyektlar ro'yxati

# talabalar = [
#     Talaba("Ali", 20),
#     Talaba("Laylo", 19),
#     Talaba("Bekzod", 22),
# ]

# for talaba in talabalar:
#     talaba.salom_ber()
#     talaba.info()