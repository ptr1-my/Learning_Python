print ("\033[1;37m-------------------------")
print ("\033[1;35mVerifikasi Login Anda")
print ("\033[1;37m-------------------------")

username = str(input("\033[1;36mMasukkan Username Anda: "))
password = str(input("Masukkan Password Anda: "))

if username == "admin" and password == "nimda123":
    print (f'''\033[0;32m-------------------------
Verifikasi Berhasil
-------------------------''')

else:
    print (f'''\033[1;31m-------------------------
Verifikasi Gagal
-------------------------''')