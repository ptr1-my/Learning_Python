n = int(input("Masukkan Bilangan Bulat Positif : "))
romawi = [
    (1000, "M"), (900, "CM"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), 
    (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]
hasil = ""
for nilai, simbol in romawi:
    while n >= nilai:
        hasil += simbol
        n -= nilai

print(f'Angka romawi dari {n} ialah {hasil}')