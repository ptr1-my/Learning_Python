USN = "putri@gmail.com"
PW = "1235678"

usn = input("Masukkan Username Anda : ")
pw = input("Masukkan Pasword Anda : ")

if usn != USN:
    print (f'Username tidak Tersedia')
elif usn == USN and pw != PW:
    print("Password salah")
else:
    print("Selamat Datang", usn)
