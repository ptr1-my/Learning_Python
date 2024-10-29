pin_atm = "122333"
saldo = 4000000

def verifikasi_pin():
    input_pin = input ("Masukkan PIN Anda: ")
    if input_pin == pin_atm:
        return True
    else:
        print("PIN salah, Cobal Lagi")
        return False
        
def tampilkan_menu():
    print("menu ATM")
    print("1. cek saldo")
    print("2. tarik tunai")
    print("3. setor tunai")
    print("4. keluar")
    
print("----------------------")
print("Selamat datang di ATM")
print("----------------------")

if verifikasi_pin():
    while True:
        tampilkan_menu()
        
        pilihan =input("Pilih Menu (1-4): ")
        
        if pilihan == "1":
            print("Saldo Anda: Rp", saldo)
        elif pilihan == "2":
            tarik_tunai = int(input("Masukkan jumlah tarik tunai: "))
            if tarik_tunai <= saldo:
                saldo -= tarik_tunai
                print("Penarikan Berhasil. Saldo anda: Rp", saldo)
            else:
                print("Saldo tidak mencukupi.")
        elif pilihan == "3":
            setor_tunai = int(input("Masukan jumlah setor tunai: "))
            saldo += setor_tunai
            print ("Setor tunai Berhasil. Saldo anda sekarang adalah: Rp", saldo)
        elif pilihan == "4":
            print ("Terimakasih Sampai Jumpa.")
            break
    else :
        print("Pilihan Tidak Valid, Silahkan Pilih 1-4")