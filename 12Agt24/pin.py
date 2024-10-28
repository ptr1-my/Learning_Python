# verifikasi pin
pin = "nimda123"

print ("\033[1;37m-------------------------")
print ("\033[1;33mVerifikasi Login Anda")
print ("\033[1;37m-------------------------")

username = input ("\033[1;35mMasukkan Username Anda: ")
password = input("Masukkan Password Anda: ")

if password == pin:
    print (f'''\033[0;32m-------------------------
Login berhasil
-------------------------''')
else:
    print (f'''\033[1;31m-------------------------
Maaf, Password Salah
-------------------------''')