hb = float(input("Masukkan Total Harga Barang : "))

dc = (hb*5)/100
t = hb-dc

if hb >= 100000:
    print (f'''Anda Mendapatkan Discount 5%
Discount Yang Anda Dapat : {dc}
Total Yang Harus Anda Bayar :{t}''')
    
elif hb< 100000:
    print ("Anda Tidak mendapatkan Discount, Belanja Lebih Dari 100Rb Untuk Potongan Discount 5%")