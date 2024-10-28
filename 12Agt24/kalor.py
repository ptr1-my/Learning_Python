# Q1 = m x c x t

# Q = BANYAK KALOR YG DI TERIMA ATAU DI LEPAS
# M = MASSA BENDA YG MENERIMA/ MELEPAS KALOR (KG)
# C =  KALOR ZENIS ZAT (J/KG'C)
# T = PPERUBAHAN SUHU ('C)

def tampilan_satu():
    print ("\033[0;31m============================")
    print ("MENGHITUNG KALOR JENIS ES")
    print ("============================")
    m = float(input("\033[0;37mMasukkan Masa Benda: ", ))
    c = float(input("Masukkan Kalor Jenis Zat (JENIS ES): ", ))
    t = float(input("Masukkan Perubahan Suhu: ", ))
    q1 = m*c*t
    print ("\033[0;34m----------------------------")
    print(f'Kalor Jenis Es : {round(q1)} (J/Kg^C)')
    print ("----------------------------")
    
def tampilan_dua():
    print ("\033[1;35m============================")
    print ("MENGHITUNG KALOR LEBUR ES")
    print ("============================")
    m = float(input("\033[0;37mMasukkan Masa Benda: ", ))
    l = float(input("Masukkan Kalor Jenis Zat (LEBUR ES): ", ))
    q2 = m*l
    print ("\033[1;33m----------------------------")
    print(f'Kalor Lebur Es : {round(q2)} (J/Kg^C)')
    print ("----------------------------")
    
def tampilan_tiga():
    print ("\033[0;32m============================")
    print ("MENGHITUNG KALOR JENIS AIR")
    print ("============================")
    m = float(input("\033[0;37mMasukkan Masa Benda: ", ))
    ca = float(input("Masukkan Kalor Jenis Zat (JENIS AIR): ", ))
    t = float(input("Masukkan Perubahan Suhu: ", ))
    q3 = m*ca*t
    print ("\033[1;31m----------------------------")
    print(f'kalor jenis air : {round(q3)}')
    print ("----------------------------")
    
def tampilan_empat():
    print ("\033[0;30m============================")
    print ("\033[0;37mMENGHITUNG 3 JENIS KALOR")
    print ("\033[0;30m============================")
    m = float(input("\033[0;31mMasukkan Masa Benda: ", ))
    c = float(input("\033[0;32mMasukkan Kalor Jenis Zat (JENIS ES): ", ))
    l = float(input("\033[0;33mMasukkan Kalor Jenis Zat (LEBUR ES): ", ))
    ca = float(input("\033[0;34mMasukkan Kalor Jenis Zat (JENIS AIR): ", ))
    t = float(input("\033[0;35mMasukkan Perubahan Suhu: ", ))
    q1 = m*c*t
    q2 = m*l
    q3 = m*ca*t
    print ("\033[1;31m----------------------------")
    print(f'kalor jenis es : {round(q1)}')
    print ("----------------------------")
    print ("\033[1;32m----------------------------")
    print(f'kalor lebur es : {round(q2)}')
    print ("----------------------------")
    print ("\033[0;35m----------------------------")
    print(f'kalor jenis air : {round(q3)}')
    print ("----------------------------")

while True:
    pilihan =float(input(
        "\033[1;37mPILLIH JENIS KALOR YANG AKAN DI HITUNG:\n1. Kalor Jenis Es\n2. Kalor Lebur Es\n3. Kalor Jenis Air\n4. Semua Pilihan Kalor\n5. Keluar\n\nPilih Menu 1-5: "))
    if (pilihan == 1):
        tampilan_satu()
    elif (pilihan == 2):
        tampilan_dua()
    elif (pilihan == 3):
        tampilan_tiga()
    elif (pilihan == 4):
        tampilan_empat()
    elif (pilihan == 5):
        print("Terimakasih, Maaf Bila Ada Kesalahan :)")
        break
    else :
        print("Tidak Valid!")