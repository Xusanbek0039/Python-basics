"""Takroriy qiymatlarni o‘chirish
mevalar = ["olma", "banan", "olma", "shaftoli", "olma"]
While tsikli orqali ro‘yxatdan barcha "olma"larni o‘chiring
Natijaviy ro‘yxatni ekranga chiqaring"""

mevalar = ["olma", "banan", "olma", "shaftoli", "olma"]
while mevalar:
    if mevalar == "olma":
        mevalar.remove("olma")
    else:
        print(mevalar)