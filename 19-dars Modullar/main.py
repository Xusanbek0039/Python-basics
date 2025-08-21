from login import login
from signup import signup

shart = int(input("Kirish uchun 0: Ro'yxatdan o'tish 1: "))

if shart == 0:
    login()
elif shart == 1:
    signup()
else:
    print("Nomalum birlik kiriting 0 va 1 kiriting!")






















"""
🔹Funksiya: ildiz_va_daraja(x, n)

📌 Maqsad:

Berilgan sonning kvadrat ildizini (√x) hisoblash

O‘sha sonning n-darajasini (xⁿ) hisoblash

math.sqrt(x) → kvadrat ildiz
math.pow(x, n) → daraja hisoblash

math modulidan foydalanish shart! 
"""














""" 
📝 MASALA: Talabalar baholarini hisoblash
📌 Vazifa:

Foydalanuvchidan talabalar ismi va baholarini kiritishni so‘rang.

O‘rtacha bahoni hisoblang.

Eng yuqori va eng past bahoni toping.

Natijalarni ekranga chiqaring.


🔹 Modullarga bo‘linishi:

1 - main.py
Foydalanuvchi bilan muloqot qiladi (ism, baholarni kiritadi).
Boshqa modullardan funksiyalarni chaqiradi.

2 - hisob.py
O‘rtacha bahoni hisoblaydigan funksiya yoziladi.
Eng yuqori va eng past bahoni aniqlash funksiyalari bo‘ladi.

3 - chiqar.py
Natijalarni chiroyli qilib ekranga chiqaradigan funksiya yoziladi.
"""