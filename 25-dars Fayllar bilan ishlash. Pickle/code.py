# """
# https://youtube.com/@it-creative
# www.husanbek-coder.uz

# Fayllar bilan ishlash va Pickle moduli
# """



# Faylni o‘qish rejimida ochamiz
with open('malumot.txt', 'r', encoding='utf-8') as fayl:
    matn = fayl.read()
    print(matn)











# Faylga yangi matn yozamiz (avvalgi ma'lumot o‘chib ketadi)
# with open('malumot.txt', 'w', encoding='utf-8') as fayl:
#     fayl.write("Salom, bu yangi yozuv!")












# # Faylga matn qo‘shamiz (avvalgilar o‘chmaydi)
# with open('malumot.txt', 'a', encoding='utf-8') as fayl:
#     fayl.write("\nYana bir qator qo‘shildi.")









# with open('malumot.txt', 'r+', encoding='utf-8') as fayl:
#     matn = fayl.read()
#     print("Eski matn:", matn)
#     fayl.seek(0)  # Boshlanishiga qaytamiz
#     fayl.write("Yangi boshlanish!")
















# import pickle

# talaba = {'ism': 'Ali', 'yosh': 20, 'fanlar': ['matematika', 'informatika']}

# # Ob'ektni faylga saqlaymiz
# with open('talaba.pkl', 'wb') as fayl:
#     pickle.dump(talaba, fayl)














# import pickle

# # Fayldan Python obyektini qayta tiklaymiz
# with open('talaba.pkl', 'rb') as fayl:
#     tiklangan = pickle.load(fayl)
#     print(tiklangan)









# # Diqqat! Pickle fayllarini faqat ishonchli manbadan o‘qing!
