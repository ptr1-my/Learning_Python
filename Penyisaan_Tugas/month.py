month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Menampilkan elemen ke-2 dan ke-10 dari daftar
print(month[2])  # March
print(month[9])  # October

# Mengubah elemen pada indeks tertentu
month[7] = 'Agustus'  # Mengubah 'August' menjadi 'Agustus'
month[0] = 'Januari'  # Mengubah 'January' menjadi 'Januari'

# Menambahkan elemen baru di akhir daftar
month.append('Muharam')  # Menambahkan 'Muharam'

# Looping dengan indeks menggunakan enumerate()
for index, data in enumerate(month):
    print(f'Bulan ke-{index + 1}: {data}')
