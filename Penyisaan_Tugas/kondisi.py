k_air = input("Masukkan kondisi air: ").lower()
s = int(input("Masukkan suhu ruangan dalam derajat c: "))
m = input("Masukkan Kodisi Mobil: ").lower()
x = int(input("Masukkan bilangan : "))

if k_air == "dalam ketel mendidih":
    print(f'Matikan Kompor')
if s > 50 :
    print(f'Bunyikan alarm tanda bahaya !')
if m == "rusak":
    print(f'Naik Angkot')
if x %2 == 0:
    print(f'Angka Bilangan Genap')
