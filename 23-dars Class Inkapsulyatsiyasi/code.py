# class Oquvchi:
#     def __init__(self, ism):
#         self.ism = ism
#         self.__baho = []  # inkapsulatsiya qilingan maxfiy atribut

#     def baho_qoshish(self, ball):
#         if 1 <= ball <= 5:
#             self.__baho.append(ball)
#         else:
#             print("Xatolik: Baholar faqat 1 dan 5 gacha bo'lishi mumkin.")

#     def o_rtalama_baho(self):
#         if len(self.__baho) == 0:
#             return 0
#         return sum(self.__baho) / len(self.__baho)

#     def barcha_baholar(self):
#         return self.__baho


# ali = Oquvchi("Ali")
# ali.baho_qoshish(4)
# ali.baho_qoshish(5)
# ali.baho_qoshish(2)

# print("Barcha baholar:", ali.barcha_baholar())
# print("O‘rtacha baho:", ali.o_rtalama_baho())























# class Kutubxona:
#     def __init__(self):
#         self.__kitoblar = []  # private ro‘yxat

#     def kitob_qoshish(self, nomi):
#         self.__kitoblar.append(nomi)
#         print(f"'{nomi}' kitobi kutubxonaga qo‘shildi.")

#     def kitoblar_royxati(self):
#         for i, nom in enumerate(self.__kitoblar, start=1):
#             print(f"{i}. {nom}")

#     def kitob_soni(self):
#         return len(self.__kitoblar)


# kutubxona = Kutubxona()
# kutubxona.kitob_qoshish("Matematika 10-sinf")
# kutubxona.kitob_qoshish("Python Dasturlash")
# kutubxona.kitob_qoshish("Fizika asoslari")

# print("\n📚 Kutubxonadagi kitoblar:")
# kutubxona.kitoblar_royxati()
# print("Kitoblar soni:", kutubxona.kitob_soni())






















# class Davomat:
#     def __init__(self):
#         self.__davomat = {}  # private dict

#     def kelgan(self, ism):
#         self.__davomat[ism] = "Bor"

#     def kelmagan(self, ism):
#         self.__davomat[ism] = "Yo‘q"

#     def holat_korish(self):
#         for ism, status in self.__davomat.items():
#             print(f"{ism}: {status}")

#     def borlar_soni(self):
#         return sum(1 for status in self.__davomat.values() if status == "Bor")


# kunlik = Davomat()
# kunlik.kelgan("Ali")
# kunlik.kelgan("Gulbahor")
# kunlik.kelmagan("Kamol")

# print("📅 Bugungi davomat:")
# kunlik.holat_korish()
# print("Borlar soni:", kunlik.borlar_soni())






















# class Topshiriqlar:
#     def __init__(self, ism):
#         self.ism = ism
#         self.__topshiriqlar = []

#     def topshiriq_qoshish(self, mavzu):
#         self.__topshiriqlar.append({"mavzu": mavzu, "bajarildi": False})

#     def bajar(self, index):
#         if 0 <= index < len(self.__topshiriqlar):
#             self.__topshiriqlar[index]["bajarildi"] = True
#         else:
#             print("Xatolik: Index noto‘g‘ri.")

#     def holat(self):
#         for i, task in enumerate(self.__topshiriqlar):
#             status = "✅" if task["bajarildi"] else "❌"
#             print(f"{i+1}. {task['mavzu']} - {status}")


# jamshid = Topshiriqlar("Jamshid")
# jamshid.topshiriq_qoshish("Funksiyalar yaratish")
# jamshid.topshiriq_qoshish("Inkapsulyatsiya mavzusi")
# jamshid.topshiriq_qoshish("Python quiz")

# jamshid.bajar(1)  # ikkinchi topshiriqni bajarilgan deb belgilaymiz

# print(f"📋 {jamshid.ism}ning topshiriqlari:")
# jamshid.holat()
