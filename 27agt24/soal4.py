h = int(input("Masukkan Hari Proyek : "))

tahun = int(h/365)
sisa_hari = (h%365)
bulan = int(sisa_hari/30)
hari = (sisa_hari%30)

print(f'tahun {tahun}, bulan {bulan}, hari {hari}')

