# untuk menangani error
try:
#  meminta input dari user
    a1 = int(input("masukan angka 1 : "))
    a2 = int(input('masukan angka 2 : '))

# teks kalkulator
    hasilpertambahan = a1 + a2
    hasilpengurangan = a1 - a2
    hasilperkalian = a1 * a2
    hasilpembagian = a1 / a2
    hasilsisabagi = a1 % a2

# kalkulator
    print(f" {a1} + {a2} = {hasilpertambahan}")
    print(f" {a1} - {a2} = {hasilpengurangan}")
    print(f" {a1} * {a2} = {hasilperkalian}")
    print(f" {a1} / {a2} = {hasilpembagian}")
    print(f" {a1} % {a2} = {hasilsisabagi}")

# except tidak boleh di kosongkan, minimal print("")
except:
    print("tidak boleh mengisi selain angka")