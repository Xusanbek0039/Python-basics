import psycopg2

# PostgreSQL ma'lumotlar bazasi bilan bog'lanish uchun parametrlar
db_config = {
    'dbname': 'host6502_lms',  # Ma'lumotlar bazasining nomi
    'user': 'host6502',   # Foydalanuvchi nomi
    'password': 'Xusanbek0039',            # Parol
    'host': 'localhost',            # Host manzili (yoki server IP manzili)
    'port': 5432                    # Port raqami
}

try:
    # PostgreSQL ga ulanish
    connection = psycopg2.connect(**db_config)

    # Kursor yaratish
    cursor = connection.cursor()

    # SQL so'rovi: Barcha jadvallarni olish
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """
    cursor.execute(query)

    # Natijani olish
    tables = cursor.fetchall()

    # Jadvallarni chiqarish
    print("Ma'lumotlar bazasidagi jadvallar:")
    for table in tables:
        print(table[0])  # Jadval nomini chiqarish

except Exception as error:
    print("Xatolik yuz berdi:", error)

finally:
    # Bog'lanishni yopish
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL bilan bog'lanish yopildi.")