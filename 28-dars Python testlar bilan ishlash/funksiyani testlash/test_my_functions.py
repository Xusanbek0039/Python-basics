# test_my_functions.py

import unittest
from my_functions import toq_mi  # Test qilinadigan funksiya import qilinadi

class TestToqMi(unittest.TestCase):
    def test_toq_son(self):
        # 5 soni toq, shuning uchun True bo'lishi kerak
        self.assertTrue(toq_mi(5))

    def test_juft_son(self):
        # 4 soni juft, shuning uchun False bo'lishi kerak
        self.assertFalse(toq_mi(4))

    def test_nol(self):
        # 0 ham juft son hisoblanadi
        self.assertFalse(toq_mi(0))

    def test_manfiy_toq(self):
        # -3 toq son
        self.assertTrue(toq_mi(-3))

    def test_manfiy_juft(self):
        # -8 juft son
        self.assertFalse(toq_mi(-8))

if __name__ == '__main__':
    unittest.main()
