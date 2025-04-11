# kutubxona.py

from mahsulotlar import mahsulotlar

def buyurtma_ber():
    narxlar = []  # Tanlangan mahsulotlarning narxlari ro'yxati
    
    while True:
        # Foydalanuvchidan mahsulot nomini so'rash
        mahsulot_nomi = input("Mahsulot nomini kiriting: ").lower()
        
        # Agar mahsulot mavjud bo'lsa narxlar ro'yxatiga qo'shiladi
        if mahsulot_nomi in mahsulotlar:
            narx = mahsulotlar[mahsulot_nomi]
            narxlar.append(narx)
            print(f"{mahsulot_nomi.capitalize()} narxi: {narx} so'm")
        else:
            print("Bunday mahsulot topilmadi!")
        
        # Yana mahsulot tanlashni sorash
        javob = input("Yana mahsulot tanlaysizmi? (ha/yo'q): ").lower()
        if javob != 'ha':
            break
    
    # Umumiy to'lov miqdorini hisoblash
    jami_summa = sum(narxlar)
    print(f"Siz uchun to'lov miqdori: {jami_summa} so'm")