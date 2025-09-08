""""
ism o'zgaruvchida ism qabul qilib 
classlar orqali ismni teskari qilib chiqaruvchi dastur tuzing.
"""
class Ism:
    def __init__(self, ism):
        self.ism = ism


class Teskari(Ism):
    def teskari_ism(self):
        self.ism = self.ism[::-1]
        print(f"Teskari ism: {self.ism}")

x = input("Ismingizni kiriting: ")
y = Teskari(x)
y.teskari_ism()
