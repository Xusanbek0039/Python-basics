# pip install googletrans==4.0.0-rc1
# google_translate.py
"""
# Envdan chiqish
deactivate

# Eskisini o'chiring (Windowsda)
rmdir /s /q .venv

# Yoki PowerShell-da
Remove-Item -Recurse -Force .venv

# Python 3.10 yangi muhit yaratish
py -3.10 -m venv .venv

# Virtual muhitni faollashtiring
.\.venv\Scripts\activate

# Pip-ni yangilang va kerakli paketlarni o'rnating
pip install --upgrade pip
pip install googletrans==4.0.0-rc1



"""
from googletrans import Translator, LANGUAGES

def show_supported_languages():
    print("🌍 Qo'llab-quvvatlanadigan tillar:")
    for code, name in LANGUAGES.items():
        print(f"{code} - {name.title()}")

def translate_text(text, dest_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"❌ Tarjima qilishda xatolik: {e}"

def main():
    print("🔤 Google Translate | Python versiyasi")
    show_supported_languages()

    text = input("\nTarjima qilinadigan matnni kiriting: ")
    dest_lang = input("Qaysi tilga tarjima qilinsin? (Masalan: en, ru, uz): ").lower()

    if dest_lang not in LANGUAGES:
        print("❗ Noto‘g‘ri til kodi!")
        return

    result = translate_text(text, dest_lang)
    print(f"\n✅ Tarjima natijasi: {result}")

if __name__ == "__main__":
    main()
