from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# ⚠️ Parolingizni quyida almashtiring
uri = f"mongodb+srv://shoirablog:7tvmi7a8ocpeATju@blog.cbbcsq1.mongodb.net/?retryWrites=true&w=majority&appName=blog"

# Klientni yaratish
client = MongoClient(uri, server_api=ServerApi('1'))

# Ping yuborish (bog‘lanishni tekshirish)
try:
    client.admin.command('ping')
    print("MongoDB bilan bog‘lanish muvaffaqiyatli!")
except Exception as e:
    print("Bog‘lanishda xatolik:", e)
