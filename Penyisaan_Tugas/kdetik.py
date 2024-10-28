j =  int(input("Masukkan Waktu Tempuh Dalam Satuan Jam: "))
m = int(input("Masukkan Waktu Tempuh Dalam Satuan Menit: "))
d = int(input("Masukkan Waktu Tempuh Dalam Satuan Detik: "))

r1 = j*3600
r2 = m*60
r3 = r1+r2+d

print(f'Jarak Tempuh Dalam Satuan Detik : {r3}')