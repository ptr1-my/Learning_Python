# Menentukan Nama Segititga

a = int(input('Masukkan alas: '))
b = int(input('masukkan tinggi: '))
c = int(input('Masukkan Sisi miring: '))

r = a**2+b**2
c2 = c**2

if c2 == r:
    print(f'Segitiga Merupakan Siku-siku')
elif c2 < r:
    print(f'Segitiga Merupakan Lancip')
elif c2 > r:
    print(f'Segitiga Merupakan Tumpul')