class Talaba:
    def __init__(self, ism, yosh):
        """
        Klass konstruktori (boshlovchi) — obyekt yaratishda ism va yosh
        parametrlarini qabul qiladi va ularni obyektga o'rnatadi.
        """
        self.ism = ism
        self.yosh = yosh

    def salom_ber(self):
        """
        Talabaning salom beruvchi metodi.
        Return qiymat sifatida ismni kiritib, salomni qaytaradi.
        """
        return f"Salom, men {self.ism}man!"