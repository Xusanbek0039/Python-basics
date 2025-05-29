# pip install requests
# python -m pip install requests



# Kod: requests bilan API'dan ma'lumot olish
import requests

# JSON ma'lumot taqdim etuvchi bepul API (masalan: randomuser.me)
url = "https://randomuser.me/api/"
javob = requests.get(url)

# Javob holati kodi
print("Holat kodi:", javob.status_code)

# JSON ko‘rinishida javob
if javob.status_code == 200:
    data = javob.json()
    foydalanuvchi = data['results'][0]
    ism = foydalanuvchi['name']['first']
    familiya = foydalanuvchi['name']['last']
    email = foydalanuvchi['email']
    davlat = foydalanuvchi['location']['country']

    print(f"Ism: {ism}")
    print(f"Familiya: {familiya}")
    print(f"Email: {email}")
    print(f"Davlat: {davlat}")
else:
    print("So‘rovda xatolik yuz berdi.")
