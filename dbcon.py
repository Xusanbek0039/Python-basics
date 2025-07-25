r = {
    "husan":["python","html","css","js"]
}

for ism, tillar in r.items():
    print(f"{ism.title()} quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(til.upper())