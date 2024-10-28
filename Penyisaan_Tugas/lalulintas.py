w = input("Masukkan Warna Lampu : ").lower()
# .lower()  digunakan untuk Huruf Besar dan huruf Kecil

if w == "merah":
    print("Berhenti !")
elif w == "kuning":
    print("Bersiap !")
elif w == "hijau":
    print("Jalan !")
else:
    print("Tidak terdapat warna tersebut !")