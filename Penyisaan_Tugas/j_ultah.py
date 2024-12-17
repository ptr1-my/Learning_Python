def jumlah_kabisat(tl, ts):
    jumlah = 0
    for tahun in range(tl + 1, ts + 1):
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            jumlah += 1
    return jumlah

# Meminta input dari pengguna
tl = int(input("Masukkan Tahun Lahir: "))
ts = 2024

# Validasi input
if tl > ts:
    print("Tahun Lahir tidak boleh melebihi 2024")
else:
    kabisat_count = jumlah_kabisat(tl, ts)
    print(f'Jumlah ulang tahun pada tahun kabisat sejak {tl}: {kabisat_count}')
