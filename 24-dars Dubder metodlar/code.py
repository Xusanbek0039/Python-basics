# class Oquvchi:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def __str__(self):
#         return f"O'quvchi: {self.ism}, Yosh: {self.yosh} yosh"

# o1 = Oquvchi("Ali", 14)
# print(o1)















# class Oquvchi:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def __repr__(self):
#         return f"O'quvchi: {self.ism}, Yosh: {self.yosh} yosh"

# o1 = Oquvchi("Ali", 14)
# print(repr(o1))












# class Sinf:
#     def __init__(self):
#         self.oquvchilar = ["Ali", "Laylo", "Sardor"]

#     def __getitem__(self, index):
#         return self.oquvchilar[index]

# sinf = Sinf()
# print(sinf[0])


















# class Sinf:
#     def __init__(self):
#         self.oquvchilar = ["Ali", "Laylo", "Sardor"]

#     def __setitem__(self, index, qiymat):
#         self.oquvchilar[index] = qiymat

# sinf = Sinf()
# sinf[0] = "Miraziz"
# print(sinf.oquvchilar)



















# class Oqituvchi:
#     def __init__(self, ism):
#         self.ism = ism

#     def __call__(self, oquvchi_ismi):
#         return f"{self.ism} {oquvchi_ismi}ni ro‘yxatga oldi."

# oqituvchi = Oqituvchi("Xasan aka")
# print(oqituvchi("Dilnoza"))















# class Oquvchi:
#     def __init__(self, ism):
#         self.ism = ism

#     def __add__(self, other):
#         return f"{self.ism} va {other.ism} guruh bo‘ldi."

# o1 = Oquvchi(10)
# o2 = Oquvchi(11)
# print(o1 + o2)




















# class Sinf:
#     def __init__(self):
#         self.oquvchilar = ["Ali", "Laylo", "Sardor"]

#     def __sub__(self, ism):
#         del self.oquvchilar[ism] 
#         return self.oquvchilar

# sinf = Sinf()
# print(sinf - 1)
















# class Oquvchi:
#     def __init__(self, ism, baho):
#         self.ism = ism
#         self.baho = baho

#     def __eq__(self, other):
#         return self.baho == other.baho

#     def __lt__(self, other):
#         return self.baho < other.baho

#     def __gt__(self, other):
#         return self.baho > other.baho

# o1 = Oquvchi("Ali", 4)
# o2 = Oquvchi("Sardor", 5)

# print(o1 == o2)  # False
# print(o1 < o2)   # True
# print(o1 > o2)   # False