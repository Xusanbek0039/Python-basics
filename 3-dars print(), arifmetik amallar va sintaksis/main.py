"""

Mavzu: Python arifmetik amallar bilan ishlash
Web: https://husanbek-coder.uz
YouTube: https://youtube.com/@it_creative

"""

# Kod 1
# son1 = int(input("Snn 1 ni kiriting: "))
# son2 = int(input("Son 2 ni kiriting: "))

# print(f"Yig'indisi {son1+son2}, Ayirmasi {son1-son2}")










# Kod 2
# son1 = int(input("Snn 1 ni kiriting: "))
# son2 = int(input("Son 2 ni kiriting: "))

# print(f"Bo'linmasi {son1/son2}, Butun bo'linmasi {son1//son2}, Qoldiqli bo'lish {son1%son2}")












"""
Foydalanuvchidan quyidagi ma'lumotlar olinadi:
Kun (hafta kuni)
Yomg‘ir yog‘yaptimi? (ha yoki yo'q)
Soat nechi bo‘ldi?
Shartlar:
Agar yakshanba kuni bo‘lsa va yomg‘ir yog‘mayotgan bo‘lsa va 
soat 9:00 dan kichik bo‘lsa, "Tezroq avtobusga chiq, sayr qilamiz!" chiqadi.
Agar yakshanba bo‘lsa, lekin yomg‘ir yog‘ayotgan bo‘lsa, "Bugun uydan 
chiqma, yomg‘ir yog‘yapti." chiqadi.
Boshqa kunlarda esa "Bugun avtobus yo'q, ish qilamiz!" deb chiqariladi.

"""
kun = input("Hafta kuni: ").lower().strip()
yomgir = input("Yomg‘ir yog‘yaptimi? (ha yoki yo'q) ")
soat = int(input("Soat nechchi bo'ldi? "))

if kun == "yakshanba" and yomgir == "ha" and soat <= 9:
    print("Tezroq avtobusga chiq, sayr qilamiz!")
elif kun == "shanba":
    print("Bugun uyda dam olamiz!")
else:
    print("Bugun avtobus yo'q, ish qilamiz!")