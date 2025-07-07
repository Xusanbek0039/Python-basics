a,b,c =map(int, input("3 ta son kiriting 1,2,3 ko'rinishda (1 2 3 umumkin emas!):").split())
x = (a+b+c)/3
if x <= 20:
    print("Qish")
elif x < 30:
    print("Baxor")
elif x < 40:
    print("Kuz")
elif x < 50:
    print("Yoz")
else:
    print("Xato format qaytadan urining!")