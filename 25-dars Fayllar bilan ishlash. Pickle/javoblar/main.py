with open("data.txt", "r", encoding="utf-8") as file: 
    lines = file.readlines()

name_data = {}

for line in lines:
    name, age = line.strip().split(",")
    name = name.strip()
    age = int(age.strip())

    if name in name_data:
        name_data[name].append(age)
    else:
        name_data[name] = [age]

results = []
for name in name_data:
    yoshlar = name_data[name]
    count = len(yoshlar)
    avg = sum(yoshlar) / count
    results.append(f"{name} - {count} ta - o'rtacha yosh: {round(avg)}")

with open("results.txt", "w", encoding="utf-8") as file:
    for line in results:
        file.write(line + "\n")

print("✅ Bajarildi: 'results.txt' fayliga yozildi.")
