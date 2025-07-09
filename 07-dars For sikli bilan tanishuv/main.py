# # Kod_1
# Mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']

# for mehmon in Mehmonlar:

#     print(f"Assalom alekum {mehmon}")

# print(Mehmonlar)

    








# # Kod_2
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")








# # Kod_3
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")








# Kod_4
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")











# # Kod_5
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
#     print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi  











# # Kod_6
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
# print(mehmonlar)












# # Kod_7
# sonlar = list(range(1,159999))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")











# Kod_8
# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar: # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
# print(sonlar)
# print(sonlar_kvadrati)






# # Kod_9
# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# for dost in dostlar:
#     print(dost)







# Foydalanuvchidan N ta son qabul qilib
# ularning yig'indisini hisoblang
# n = int(input("Nechta son kiritasiz: "))

# umumiy = 0
# for i in range(n):
#     son = int(input(f"{i + 1} sonni kiriting: "))
#     umumiy = umumiy+son
# print(umumiy)






















# Foydalanuvchi kiritgan N songacha (1 dan N gacha) quyidagi qoidalar 
# asosida sonlarni chop et:
# Agar son 3 ga bo‘linsa — "Fizz"
# Agar son 5 ga bo‘linsa — "Buzz"
# Agar son 3 ga ham, 5 ga ham bo‘linsa — "FizzBuzz"
# Aks holda — o‘sha sonni o‘zini chop et












# N = int(input("1 dan N gacha bo'lgan son kiriting: "))

# for i in range(1, N + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)












# 2-masala
# Foydalanuvchidan butun son N kiritilsin. Shu songa qarab piramida 
# shaklida yulduzlar (*) chiqarilsin.
#     *
#    ***
#   *****
#  *******
# *********
#         print(" ", end="")







# N = int(input("Piramida balandligini kiriting: "))

# for i in range(1, N + 1):
#     # Bo'sh joylar
#     for space in range(N - i):
#         print(" ", end="")
#     # Yulduzlar
#     for star in range(2 * i - 1):
#         print("*", end="")
#     print()  # Har qatordan keyin yangi qatorga o'tish

# 3-masala
# Foydalanuvchi N sonini kiritsin. Siz 1 dan N gacha bo‘lgan toq va 
# juft sonlarning:
# Jami yig‘indisini
# Sonlar sonini (nechta ekanini)
# alohida-alohida chiqarishingiz kerak.
# Misol
# Toq sonlar: 1 3 5 7 9
# Juft sonlar: 2 4 6 8 10
# Toq sonlar soni: 5
# Toq sonlar yig'indisi: 25
# Juft sonlar soni: 5
# Juft sonlar yig'indisi: 30





N = int(input("1 dan N gacha bo'lgan son kiriting: "))

if N !=0:
    juft = list(range(0,N,2))
    toq = list(range(1,N,2))

    print(f"Juftlar yig'indisi: {sum(juft)}, Umumiy {len(juft)}")
    print(f"Toqlar yig'indisi: {sum(toq)}, Umumiy {len(toq)}")
else:
    print("Siz nol sonini kiritdingiz!")

# toq_sonlar_soni = 0
# toq_yigindi = 0
# juft_sonlar_soni = 0
# juft_yigindi = 0
# if N!=0:
#     for i in range(1, N + 1):
#         if i % 2 == 0:
#             juft_sonlar_soni += 1
#             juft_yigindi += i
#         else:
#             toq_sonlar_soni += 1
#             toq_yigindi += i
#     print("Toq sonlar soni:", toq_sonlar_soni)
#     print("Toq sonlar yig'indisi:", toq_yigindi)
#     print("Juft sonlar soni:", juft_sonlar_soni)
#     print("Juft sonlar yig'indisi:", juft_yigindi)

# else:
#     print("0 son kiritdingiz")
