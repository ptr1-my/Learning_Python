# Jika Total belanja Lebih Dari Rp. 100.000, mengeluarkan Diskon, Harga yang harus di bayar

t = float(input("Masukkan Total Belanja Anda : "))

d = (t*17)/100

if t > 100000:
    print(f'Diskon Belanjaan Anda : {d} \nHarga yg harus Anda bayar : {t-d}')
else:
    print(f'Harga yang harus anda bayar : {t}')