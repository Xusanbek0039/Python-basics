"""
https://youtube.com/@it-creative
www.husanbek-coder.uz

Fayllar bilan ishlash va Pickle moduli
"""



# Faylni o‘qish rejimida ochamiz
# with open('malumot.txt', 'r', encoding='utf-8') as fayl:
#     matn = fayl.read()
#     print(matn)











# Faylga yangi matn yozamiz (avvalgi ma'lumot o‘chib ketadi)
with open('malumot.txt', 'w', encoding='utf-8') as fayl:
    fayl.write("Salom, bu yangi yozuv!")
