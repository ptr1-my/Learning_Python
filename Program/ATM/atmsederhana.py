print("Selamat Datang Di ATM Saya")
print("Pilih Option : 1")
print("1. Cek uang saya")
print("2. Ambil uang saya")
print("3. Tabung uang saya")

option=int(input("Silahkan pilihan option mana: "))
if option==1:
    print("Uang kamu berjumalah Rp. 4.000.000")
elif option==2:
    print("Uang kamu berjumlah Rp. 4.000.000, Mau di ambil berapa?")
    print("1. 50.000")
    print("2. 100.000")
    
    uang_kamu=4000000
    option2=int(input("Option : "))
    if option2==1:
        hasil=uang_kamu-50000
        print("Uang kamu sekarang berjumlah :", hasil1)
    elif option2==2:
        hasil=uang_kamu-100000
        print("Uang kamu sekarang berjumlah :", hasil2)
    else:
        print ("Keyword anda salah")
        
elif option==3:
    uang_kamu=4000000
    print("Uang berjumlah Rp. 4.000.000, Mau nabung berapa?")
    option3=int(input("Masukan jumlah uang: "))
    hasil3=uang_kamu+option3
    print("Jumlah uang sekarang berjumalah :", hasil3)
else:
    print("Keyword anda salah, Mohon coba lagi :)")
    