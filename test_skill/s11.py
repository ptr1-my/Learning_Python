harga_barang = float(input('Masukkan Harga Barang : '))

discount = (harga_barang*12.5)/100
total = harga_barang - discount

if harga_barang >= 150000:
    print(f'''Harga Barang : {harga_barang}
Discount : {discount}
Harga Setelah Discount : {total}''')
elif harga_barang < 150000:
    print(f'''Total Belanja : {harga_barang}
Belanja Lebih Dari Rp.150000 Untuk Discount 12.5%''')