angka = {1, 3, 5, 7}
cek = all(x % 2 != 0 for x in angka)
print("Semua angka ganjil:", cek)