import unittest
from my_module import Talaba  # Talaba klassi joylashgan fayldan import qilamiz

class TestTalaba(unittest.TestCase):
    def setUp(self):
        """
        Har bir testdan oldin ishga tushadigan metod.
        Bu yerda Talaba obyektini yaratamiz va boshqa testlar uchun tayyorlaymiz.
        """
        self.talaba = Talaba("Ali", 20)

    def test_ism(self):
        """
        Talaba obyektining 'ism' atributi to'g'ri saqlanganligini tekshirish.
        """
        self.assertEqual(self.talaba.ism, "Ali")

    def test_yosh(self):
        """
        Talaba obyektining 'yosh' atributi to'g'ri saqlanganligini tekshirish.
        """
        self.assertEqual(self.talaba.yosh, 20)

    def test_salom_ber(self):
        """
        Talabaning salom_ber() metodining qaytargan natijasi to'g'ri ekanligini tekshirish.
        """
        natija = self.talaba.salom_ber()
        self.assertEqual(natija, "Salom, men Aliman!")

if __name__ == "__main__":
    unittest.main()
