import requests
from googletrans import Translator

def get_exchange_rate(from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        rates = data["rates"]
        if to_currency in rates:
            return rates[to_currency]
        else:
            raise ValueError("Kiritilgan valyuta kodi topilmadi!")
    else:
        raise ConnectionError("Valyuta kurslarini olishda xatolik yuz berdi!")

def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def main():
    print("🌐 Valyuta konvertori va tarjimon dasturi")
    
    try:
        from_currency = input("Qaysi valyutadan? (masalan: USD): ").upper()
        amount = float(input("Miqdor: "))
        to_currency = input("Qaysi valyutaga? (masalan: UZS): ").upper()
        lang = input("Qaysi tilga tarjima qilay? (masalan: ru, en, uz): ").lower()

        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate

        result_text = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        translated = translate_text(result_text, lang)

        print("\nNatija:")
        print(result_text)
        print(f"Tarjimasi ({lang}): {translated}")

    except ValueError as ve:
        print("❗ Xatolik:", ve)
    except Exception as e:
        print("⚠️ Umumiy xatolik:", e)

if __name__ == "__main__":
    main()
