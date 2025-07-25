# kod_1

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n = 1 
# while True:
#     ism = input(f"{n}-do'stingiz ismini kiriting: ")
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
#     javob = javob.lower()
#     javob = javob.strip()
#     if javob =='ha':
#         n = 1 + n
#         continue
#     elif javob == "yo'q":
#         break
#     else:
#         print("Iltimos to'g'ri matindan foydalaning ha/yo'q: ")

# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())




















# kod_2


# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)\t")
#     javob = javob.lower()
#     javob = javob.strip()
#     if javob == "yo'q":
#         ishora = False
#     elif javob == "ha":
#         continue


# for ism, yosh in dostlar.items():
#     print(f"\n{ism.title()} {yosh} yoshda!")





















# kod_3
# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)

















# kod_4
talabalar = []
son  = int(input("Nechta talabangiz mavjud: "))
for i in range(son):
    name = input(f"{i+1} ning ismini kiriting: ")
    talabalar.append(name)

baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop() 
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho

for x,y in baholangan_talabalar.items():
    print(f"\n{x.title()}ning baxosi: {y}")



