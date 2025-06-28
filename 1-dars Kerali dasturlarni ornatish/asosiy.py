ismlar = []

# 10 ta ismni kiritamiz
for i in range(10):
    ism = input(f"Ism kiriting ({i+1}/10): ")
    ismlar.append(ism)

# Eng ko'p uchraydigan ismni topamiz
eng_kop_ism = ""
eng_kop_soni = 0

for ism in ismlar:
    takror_soni = ismlar.count(ism)
    if takror_soni > eng_kop_soni:
        eng_kop_soni = takror_soni
        eng_kop_ism = ism

print(f"Eng ko‘p kiritilgan ism: {eng_kop_ism} ({eng_kop_soni} marta)")
