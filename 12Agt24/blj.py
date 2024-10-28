b1 = 20000
b2 = 50000
b3 = 40000
b4 = 120000
total = b1+b2+b3+b4
dc = total*(7.5/100)
byr = total-dc

print ("\033[1;33m============================")
print ("\033[1;34mBill Belanja")
print ("\033[1;33m============================")
print(f'''\033[1;30mBill anda :
        1. barang1 = 20000
        2. barang2 = 50000
        3. barang3 = 40000
        4. barang4 = 120000
Total Belanja Anda : {total}\nTotal Discount 7,5% : {dc}\nTotal Pembayaran Setelah Discount : {byr}''')

