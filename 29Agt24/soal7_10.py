n = int(input("Masukkan Bilangan : "))

if n <1 or n >10:
    print("Bilangan Hanya Bisa 1 - 10")
else:
    angka_r = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", 'IX', "X"]
    print(f'Angka Romawi dari {n} adalah {angka_r[n]}')