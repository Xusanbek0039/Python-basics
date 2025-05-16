"""
Mentor: Suyunov Husan
YouTube: https://youtube.com/@it_creative
Web: https://praktikum.itc.uz
GitHub: https://github.com/xusanbek0039
Mavzu: Python xatoliklar bilan ishlash, try except
"""

# # 1-kod

# try:
#     son = int(input("Son kiriting: "))
#     print("Natija:", 10 / son)
# except:
#     print("Xatolik yuz berdi.")

















# # 2-kod
# try:
#     son = int(input("Son kiriting: "))
#     print("Natija:", 10 / son)
# except ValueError:
#     print("Faqat butun son kiriting!")



















# # 3-kod
# try:
#     f = open("data.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("Fayl topilmadi.")
# finally:
#     print("Dastur tugadi.")





















# # 4-kod
# try:
#     son = int(input("Son kiriting: "))
# except ValueError:
#     print("Xatolik: butun son kiriting!")
# else:
#     print("Siz kiritgan son:", son)
















# # 5-kod
# file_name = input("Fayl nomini kiriting: ")
# try:
#     with open(file_name, "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("Bu nomdagi fayl mavjud emas.")


















# # 6-kod
# try:
#     a = int(input("a ni kiriting: "))
#     b = int(input("b ni kiriting: "))
#     print("Natija:", a / b)
# except (ValueError, ZeroDivisionError) as e:
#     print("Xatolik:", e)




















# # 7-kod
# try:
#     lst = [1, 2, 3]
#     print(lst[5])
# except IndexError:
#     print("Index mavjud emas.")





















# # 8-kod
# try:
#     import math
#     print(math.sqrt(-10))
# except:
#     print("Manfiy sonning ildizi yo'q.")
